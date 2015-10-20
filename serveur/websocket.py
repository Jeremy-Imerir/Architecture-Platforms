#!/usr/bin/python
# -*- coding: utf-8 -*-

import signal, sys, json, re
from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer
import time
import threading
import shortestfield, math, yaml
from transformjson import Transformer

listOfClients = []
maxOfClients = 2
adresse = '0.0.0.0'
port = 8000
clientThread = None
Taxi = None
disconnected = 0

# Creer le tableau via le json avant
# Gerer la position du cab

with open('map.json', 'r') as content_file:
    content = content_file.read()

json_string = content
json_string = json_string.replace('\r\n', ' ')
json_string = re.sub(' +', ' ', json_string)
parsed_json = json.loads(json_string, "utf-8")

Graphique = Transformer()
Graph = Graphique.transform(parsed_json)

print Graph

class Taxi(threading.Thread):
	def __init__(self):
		super(Taxi, self).__init__()
		self.x = 0
		self.y = 0
		self.status = "Free"
		self.destination = ""
		self.distanceToEnd = ""
		self.listOfPoints = []
	def run (self):
		# VertexList = Graphique.VertexList
		# self.status = "Busy"
		# for i in range(len(VertexList[0])) :
			# if vertexBegin == VertexList[0][i]:
				# vertexBegin = VertexList[1][i]

			# elif vertexEnd == VertexList[0][i]:
				# vertexEnd = VertexList[1][i]

		# vertexBegin = vertexBegin.split(";")
		# vertexEnd = vertexEnd.split(";")
		# if vertexBegin[0] > vertexEnd[0]:
			# negativex = 1
		# else:
			# negativex = -1

		# if vertexBegin[1] > vertexEnd[1]:
			# negativey = 1
		# else:
			# negativey = -1

		global listOfClients
		global maxOfClients
		while True :
			if len(listOfClients) == maxOfClients:
				if len(self.listOfPoints)==0:
					print "je suis libre"
					self.status = "Free"
				else:
					print str(self.listOfPoints[0])+" "+str(self.listOfPoints[1])
					self.status = "Busy"
			else:
				print "il manque des gens !"
			time.sleep(1)
		# self.stop()

	def stop(self):
		self._stopevent.set() 
		global disconnected
		disconnected = 1
		print "Client thread stopped"
			

class SendTaxiInfos(threading.Thread): 
    def __init__(self, clientSocket): 
		threading.Thread.__init__(self) 
		self.client = clientSocket 
		self._stopevent = threading.Event( ) 
		global disconnected
		disconnected = 0
    def run(self):
		string = " "
		global disconnected
		while disconnected == 0:
			time.sleep(5)
			if len(listOfClients)==maxOfClients:
				string = '{"cab":{"position":{"x":'+str(Taxi.x)+',"y":'+str(Taxi.y)+'},"goTo":"'+Taxi.destination+'","status":"'+Taxi.status+'","distanceToEnd":'+str(Taxi.distanceToEnd)+'}}'
				print string
				self.client.sendMessage(unicode(string))
			else:
				string = "En attente d'autres utilisateurs"
				print string
				self.client.sendMessage(unicode(string))
    def stop(self):
		self._stopevent.set() 
		global disconnected
		disconnected = 1
		print "Client thread stopped"
  

class WebsocketServer(WebSocket):

	rejected = 0

	def handleMessage(self):
		print self.data, 'sent'
		try:
			json_object = json.loads(self.data)
		except ValueError, e:
			json_object = None
			self.sendMessage(unicode('{"error":"not json"}'))
		if len(listOfClients)==maxOfClients:
			if json_object!=None:
				cabRequest = json_object["cabRequest"]
				if Taxi.status == "Free":
					self.sendMessage(unicode('{"status":"free"}'))
					distance, points = shortestfield.dij_rec(Graph, cabRequest["from"], cabRequest["to"])
					Taxi.listOfPoints.extend(points)
					Taxi.distanceToEnd = distance
					Taxi.destination = cabRequest["to"]
				else :
					self.sendMessage(unicode('{"status":"busy"}'))
			
			
	
	def handleConnected(self):
		# Accept connection
		if len(listOfClients)<maxOfClients:
			listOfClients.append(self)
			if self.address[0] == "192.168.0.2":
				self.sendMessage(unicode("salut arduino"))
			else :
				self.sendMessage(unicode('{"clientNumber":'+str(len(listOfClients))+","+json_string[2:]))
			print self.address, 'connected'
			
			global clientThread
			clientThread = SendTaxiInfos(self)
			clientThread.start()
		#Reject connection
		else:
			self.rejected = 1
			handleClose(self)
	
	def handleClose(self):
		global clientThread
		clientThread.stop()
		# Connection closed by client
		if self.rejected == 0:
			listOfClients.remove(self)
			# self.rejected = 0
			print self.address, 'closed'
			
		# Connection closed by server
		else:
			self.sendMessage(unicode("Server full, client rejected"))
			print self.address, 'rejected. Full'


#Create websocket
server = SimpleWebSocketServer(adresse, port, WebsocketServer)
print "Serveur en ecoute sur l'adresse : "+adresse+" et sur le port : "+str(port)

Taxi = Taxi()
Taxi.start()
server.serveforever()