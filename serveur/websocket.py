#!/usr/bin/python
# -*- coding: utf-8 -*-

import signal, sys, json, re
from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer
import time
import threading
import shortestfield, math, yaml
from transformjson import Transformer

listOfClients = []
maxOfClients = 1
adresse = '0.0.0.0'
port = 8001
clientThread = None
Taxi = None
disconnected = 0

# Creer le tableau via le json avant
# Gerer la position du cab

with open('map.json', 'r') as content_file:
    content = content_file.read()

json_string = content
json_string = content.replace('\r\n', ' ')
json_string = re.sub(' +', ' ', json_string)
parsed_json = json.loads(json_string, "utf-8")

Graphique = Transformer()
Graph = Graphique.transform(parsed_json)
VertexList = Graphique.VertexList

print Graph

class Taxi(threading.Thread):
	def __init__(self):
		super(Taxi, self).__init__()
		self.x = 0
		self.y = 1
		self.status = "Free"
		self.destination = ""
		self.distanceToEnd = ""
		self.listOfPoints = []

	def run (self):
		global listOfClients
		global maxOfClients
		global VertexList
		
		while True :
			if len(listOfClients) == maxOfClients:
				if len(self.listOfPoints)==0:
					self.status = "Free"
					time.sleep(1)
				else:
					for i in range(len(self.listOfPoints)):

						self.status = "Busy"
						firstPoint = VertexList[0].index(str(self.listOfPoints[0]))
						try:
							secondPoint = VertexList[0].index(str(self.listOfPoints[1]))
							
							firstPoint = VertexList[1][firstPoint]
							secondPoint = VertexList[1][secondPoint]
							firstPoint = firstPoint.split(";")
							secondPoint = secondPoint.split(";")
							
							# Directement sur les points
							self.x = secondPoint[0]
							self.y = secondPoint[1]
							time.sleep(1)
							
							xdistance = abs(float(firstPoint[0]) - float(secondPoint[0]))
							ydistance = abs(float(firstPoint[1]) - float(secondPoint[1]))
							distance = math.sqrt((xdistance ** 2) + (ydistance ** 2))

							#On y va avec un pas
							
							# if xdistance <= 0 :
								# negativeX = -1
							# else :
								# negativeX = 1

							# if ydistance <= 0 :
								# negativeY = -1
							# else :
								# negativeY = 1
							
							

							# temps = 9
							# kmhX = xdistance/temps
							# kmhY = ydistance/temps
							# for j in range(temps):
								# self.x = self.x + (kmhX*-1)
								# self.y = self.y + (kmhY*-1)
								# time.sleep(0.5)
								
							self.distanceToEnd = self.distanceToEnd - distance
							del self.listOfPoints[0]
						except:
							self.distanceToEnd = 0
							self.goTo = ""
							del self.listOfPoints[:]
							break


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
			time.sleep(1)
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
				# if self.address[0] == "192.168.0.2":
				if Taxi.status == "Free":
					self.sendMessage(unicode('{"status":"free"}'))
					distance, points = shortestfield.dij_rec(Graph, cabRequest["from"], cabRequest["to"])
		
					Taxi.listOfPoints.extend(points)
					Taxi.distanceToEnd = distance
					Taxi.destination = cabRequest["to"]
				else :
					self.sendMessage(unicode('{"status":"busy"}'))
				# else:
					# for i in range(len(listOfClients)):
						# currentClient = listOfClients[i]
						# if currentClient.address[0] == "192.168.0.2":
							# currentClient.sendMessage(unicode(self.data))
							
			
			
	
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