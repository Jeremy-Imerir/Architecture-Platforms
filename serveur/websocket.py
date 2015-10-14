#!/usr/bin/python

import signal, sys, json
from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer

listOfClients = []
adresse = '172.30.0.170'
port = 8000

class WebsocketServer(WebSocket):

	rejected = 0
	
	def handleMessage(self):
		str = '{"areas": [{"name": "Quartier Nord","map": {"weight": {"w": 1,"h": 1},"vertices": [{"name": "m","x": 0.5,"y": 0.5},{"name": "b","x": 0.5,"y": 1}],"streets": [{"name": "mb","path": ["m","b"],"oneway": false}],"bridges": [{"from": "b","to": {"area": "Quartier Sud","vertex": "h"},"weight": 2}]}}]}'
		self.sendMessage(unicode(str))
		print self.data, 'sent'
	
	def handleConnected(self):
		if len(listOfClients)<4:
			listOfClients.append(self)
			print self.address, 'connected'
		else:
			self.rejected = 1
			handleClose(self)
	
	def handleClose(self):
		if self.rejected == 0:
			listOfClients.remove(self)
			# self.rejected = 0
			print self.address, 'closed'
			
		else:
			print self.address, 'rejected. Full'
	
server = SimpleWebSocketServer(adresse, port, WebsocketServer)
print "Serveur en ecoute sur l'adresse : "+adresse+" et sur le port : "+str(port)
server.serveforever()