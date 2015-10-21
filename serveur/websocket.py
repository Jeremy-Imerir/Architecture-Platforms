#!/usr/bin/python
# -*- coding: utf-8 -*-

import signal, sys, json, re
from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer
import time
import threading
import shortestfield, math, yaml
from transformjson import Transformer

listOfClients = []
maxOfClients = 3
adresse = '0.0.0.0'
port = 8000
clientThread = None
Taxi = None
disconnected = 0
rejected = 0

#Get json from file
with open('map.json', 'r') as content_file:
    content = content_file.read()

#Delete returns and multiple spaces
json_string = content.replace('\r\n', ' ')
json_string = re.sub(' +', ' ', json_string)
parsed_json = json.loads(json_string, "utf-8")

#Transformer object for creating a graph
Graphique = Transformer()
Graph = Graphique.transform(parsed_json)
VertexList = Graphique.VertexList

print Graph

#Class of the taxi
class Taxi(threading.Thread):
	def __init__(self):
		#Intialize variables
		super(Taxi, self).__init__()
		self.x = 0
		self.y = 1
		self.status = "Free"
		self.destination = "None"
		self.distanceToEnd = 0
		self.listOfPoints = []

	def run (self):
		global listOfClients
		global maxOfClients
		global VertexList
		
		while True :
			#If everyone is here
			if len(listOfClients) == maxOfClients:
				if len(self.listOfPoints)==0:
					self.status = "Free"
					time.sleep(1)
				else:
					#If taxi has some points to go
					for i in range(len(self.listOfPoints)):
						
						#Taxi is busy
						self.status = "Busy"
						firstPoint = VertexList[0].index(str(self.listOfPoints[0]))
						try:
							secondPoint = VertexList[0].index(str(self.listOfPoints[1]))
							
							firstPoint = VertexList[1][firstPoint]
							secondPoint = VertexList[1][secondPoint]
							firstPoint = firstPoint.split(";")
							secondPoint = secondPoint.split(";")
							
							# Jump on vertexes
							self.x = secondPoint[0]
							self.y = secondPoint[1]
							time.sleep(1)
							
							xdistance = abs(float(firstPoint[0]) - float(secondPoint[0]))
							ydistance = abs(float(firstPoint[1]) - float(secondPoint[1]))
							distance = math.sqrt((xdistance ** 2) + (ydistance ** 2))

							# Walk to vertexes
							
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
							self.destination = " "
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
				#Send cab infos to everyone
				string = '{"cab":{"x":'+str(Taxi.x)+',"y":'+str(Taxi.y)+',"goTo":"'+Taxi.destination+'","status":"'+Taxi.status+'","distanceToEnd":'+str(Taxi.distanceToEnd)+'}}'
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

	def handleMessage(self):
		global listOfClients
		print str(self.data) + ' sent from :'+str(self.address)
		#If i receive json
		try:
			json_object = json.loads(self.data)
		except ValueError, e:
			json_object = None
			self.sendMessage(unicode('{"error":"not json"}'))
		#If everyone here
		if len(listOfClients)==maxOfClients:
			if json_object!=None:
				# Get cab request
				cabRequest = json_object["cabRequest"]
				#If it's a request from arduino
				if self.address[0] == "192.168.0.2":
					if Taxi.status == "Free":
						#I send the points to Dijkstra algorithm for getting all points
						distance, points = shortestfield.dij_rec(Graph, cabRequest["from"], cabRequest["to"])
			
						#Update cab infos
						Taxi.listOfPoints.extend(points)
						Taxi.distanceToEnd = distance
						Taxi.destination = cabRequest["to"]
				# If it's another client
				else:
					for i in range(len(listOfClients)):
						currentClient = listOfClients[i]
						#I send it back to the arduino
						if currentClient.address[0] == "192.168.0.2":
							currentClient.sendMessage(unicode(self.data))
							
			
			
	
	def handleConnected(self):
		global listOfClients
		# Accept connection
		if len(listOfClients)<maxOfClients:
			listOfClients.append(self)
			#If it's arduino
			if self.address[0] == "192.168.0.2":
				self.sendMessage(unicode("salut arduino"))
			#If it's another client
			else :
				self.sendMessage(unicode('{"clientNumber":'+str(len(listOfClients))+","+json_string[2:]))
			print self.address, 'connected'
			
			global clientThread
			clientThread = SendTaxiInfos(self)
			clientThread.start()
		#Reject connection
		else:
			global rejected
			rejected = 1
			handleClose(self)
	
	def handleClose(self):
		global clientThread
		global rejected
		clientThread.stop()
		# Connection closed by client
		if rejected == 0:
			listOfClients.remove(self)
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