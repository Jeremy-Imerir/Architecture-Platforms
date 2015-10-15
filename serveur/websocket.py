#!/usr/bin/python

import signal, sys, json, re
from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer
import time
from threading import Thread
import numpy
from heapq import *

listOfClients = []
adresse = '172.30.0.170'
port = 8000
thread = None


def heuristic(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

def astar(array, start, goal):

    neighbors = [(0,1),(0,-1),(1,0),(-1,0)]

    close_set = set()
    came_from = {}
    gscore = {start:0}
    fscore = {start:heuristic(start, goal)}
    oheap = []

    heappush(oheap, (fscore[start], start))
    
    while oheap:

        current = heappop(oheap)[1]

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j            
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:                
                    if array[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue
                
            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue
                
            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heappush(oheap, (fscore[neighbor], neighbor))
                
    return False

# nmap = numpy.array([
    # [0,0,0,0,0,0,0,0,0,0 ,0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0],
    # [1,1,1,1,1,1,1,1,1,0 ,1,1,1,1,1,1,1,1,1,0, 1,1,1,1,1,1,1,1,1,0],
    # [0,0,0,0,0,0,0,0,0,0 ,0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0],
    # [1,0,1,1,1,1,1,1,1,1 ,1,0,1,1,1,1,1,1,1,1, 1,0,1,1,1,1,1,1,1,1],
    # [0,0,0,0,0,0,0,0,0,0 ,0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0],
    # [1,1,1,1,1,1,1,1,1,0 ,1,1,1,1,1,1,1,1,1,0, 1,1,1,1,1,1,1,1,1,0],
    # [0,0,0,0,0,0,0,0,0,0 ,0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0],
    # [1,0,1,1,1,1,1,1,1,1 ,1,0,1,1,1,1,1,1,1,1, 1,0,1,1,1,1,1,1,1,1],
    # [0,0,0,0,0,0,0,0,0,0 ,0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0],
    # [1,1,1,1,1,1,1,1,1,0 ,1,1,1,1,1,1,1,1,1,0, 1,1,1,1,1,1,1,1,1,0]])
    
# print astar(nmap, (0,0), (10,13))


# Creer le tableau via le json avant
# Gerer la position du cab

json_string = """
{
    "areas": [
        {
            "name": "Quartier Ouest",
            "map": {
                "weight": {
                    "w": 1,
                    "h": 2
                },
                "vertices": [
                    {
                        "name": "a",
                        "x": 0,
                        "y": 1
                    },
                    {
                        "name": "b",
                        "x": 1,
                        "y": 1
                    },
                    {
                        "name": "c",
                        "x": 1,
                        "y": 0.5
                    },
                    {
                        "name": "d",
                        "x": 0.5,
                        "y": 0.5
                    },
                    {
                        "name": "e",
                        "x": 0.5,
                        "y": 0
                    },
                    {
                        "name": "f",
                        "x": 1,
                        "y": 0
                    }
                ],
                "streets": [
                    {
                        "name": "mb",
                        "path": [
                            "a",
                            "b"
                        ],
                        "oneway": false
                    },
                    {
                        "name": "mb",
                        "path": [
                            "b",
                            "c"
                        ],
                        "oneway": false
                    },
                    {
                        "name": "mb",
                        "path": [
                            "c",
                            "d"
                        ],
                        "oneway": false
                    },
                    {
                        "name": "mb",
                        "path": [
                            "d",
                            "e"
                        ],
                        "oneway": false
                    },
                    {
                        "name": "mb",
                        "path": [
                            "e",
                            "f"
                        ],
                        "oneway": false
                    }
                ],
                "bridges": [
                    {
                        "from": "b",
                        "to": {
                            "area": "Quartier Sud",
                            "vertex": "h"
                        },
                        "weight": 2
                    }
                ]
            }
        },
        {
            "name": "Quartier Centre",
            "map": {
                "weight": {
                    "w": 1,
                    "h": 1
                },
                "vertices": [
                    {
                        "name": "a",
                        "x": 1,
                        "y": 1
                    },
                    {
                        "name": "m",
                        "x": 0,
                        "y": 1
                    },
                    {
                        "name": "h",
                        "x": 0.5,
                        "y": 0
                    }
                ],
                "streets": [
                    {
                        "name": "ah",
                        "path": [
                            "a",
                            "h"
                        ],
                        "oneway": false
                    },
                    {
                        "name": "mh",
                        "path": [
                            "m",
                            "h"
                        ],
                        "oneway": false
                    }
                ],
                "bridges": [
                    {
                        "from": "h",
                        "to": {
                            "area": "Quartier Nord",
                            "vertex": "b"
                        },
                        "weight": 2
                    }
                ]
            }
        },
        {
            "name": "Quartier Est",
            "map": {
                "weight": {
                    "w": 1,
                    "h": 1
                },
                "vertices": [
                    {
                        "name": "a",
                        "x": 1,
                        "y": 1
                    },
                    {
                        "name": "m",
                        "x": 0,
                        "y": 1
                    },
                    {
                        "name": "h",
                        "x": 0.5,
                        "y": 0
                    }
                ],
                "streets": [
                    {
                        "name": "ah",
                        "path": [
                            "a",
                            "h"
                        ],
                        "oneway": false
                    },
                    {
                        "name": "mh",
                        "path": [
                            "m",
                            "h"
                        ],
                        "oneway": false
                    }
                ],
                "bridges": [
                    {
                        "from": "h",
                        "to": {
                            "area": "Quartier Nord",
                            "vertex": "b"
                        },
                        "weight": 2
                    }
                ]
            }
        }
    ]
}
"""
json_string = json_string.replace('\n', ' ')
json_string = re.sub(' +', ' ', json_string)

class WebsocketServer(WebSocket):

	rejected = 0

	def handleMessage(self):
		print self.data, 'sent'
	
	def handleConnected(self):
		if len(listOfClients)<4:
			listOfClients.append(self)
			self.sendMessage(unicode(json_string))
			print self.address, 'connected'
	#		global thread
	#		if thread is None:
	#			thread = Thread(target=send_cab_pos)
	#			thread.start()
		else:
			self.rejected = 1
			handleClose(self)
	
	def handleClose(self):
		if self.rejected == 0:
			listOfClients.remove(self)
			# self.rejected = 0
			print self.address, 'closed'
			
		else:
			self.sendMessage(unicode("Server full, client rejected"))
			print self.address, 'rejected. Full'

	# def send_map(self):
		# while True:
			# if len(listOfClients)==4:
				# time.sleep(1)
				# str = ''
				# self.sendMessage(unicode(str))
			# else:
				# time.sleep(10)
				# self.sendMessage(unicode("En attente d'autres utilisateurs"))


	
server = SimpleWebSocketServer(adresse, port, WebsocketServer)
print "Serveur en ecoute sur l'adresse : "+adresse+" et sur le port : "+str(port)
server.serveforever()