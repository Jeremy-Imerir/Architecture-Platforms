#!/usr/bin/python
# -*- coding: utf-8 -*-

import json, re, shortestfield, math, yaml

class Transformer():
	VertexList = None
	def transform(self, parsed_json): 
		areas = parsed_json["areas"]

		vertexList = [[],[]]
		streetList = []
		bridgeList = []

		for i in range(len(areas)) :
			#Get name and map from area
			areaname = json.dumps(areas[i]["name"])
			areamap = areas[i]["map"]
			
			# Get different elements from the current area
			areamapvertices = areamap["vertices"]
			areamapstreets = areamap["streets"]
			areamapbridges = areamap["bridges"]
			
			for j in range(len(areamapvertices)) :
				
				#Get x and y of the Vertex
				x = int(round(areamapvertices[j]["x"]*9+(i*10)))
				y = int(round((areamapvertices[j]["y"])*9))

				# Append vertexes in a two-dimensional array
				vertexList[0].append(str(areamapvertices[j]["name"]))
				vertexList[1].append(str(x)+";"+str(y))
			for l in range(len(areamapbridges)) :
				#Get vertexes from the bridges
				areamapbridgesfrom = areamapbridges[l]["from"]
				areamapbridgesto = areamapbridges[l]["to"]
				streetList.append(str(areamapbridgesfrom[0])+";"+str(areamapbridgesto["vertex"]))
			for k in range(len(areamapstreets)) :
				#Get vertexes from the streets
				areamapstreetspath = areamapstreets[k]["path"]
				streetList.append(str(areamapstreetspath[0])+";"+str(areamapstreetspath[1]))

		Graph={}
		alreadyPut = []
		streetList = sorted(streetList, key=str.lower)

		#Creating the graph
		for k in range(len(streetList)) :
			streetPoints = streetList[k].split(";")
			for m in range(len(vertexList[0])) :
				for n in range(len(vertexList[0])) :
					npoint = vertexList[1][n].split(";")
					mpoint = vertexList[1][m].split(";")
					xdistance = (int(npoint[0]) - int(mpoint[0])) ** 2
					ydistance = (int(npoint[1]) - int(mpoint[1])) ** 2
					distance = int(math.sqrt(xdistance + ydistance))
					if vertexList[0][m] == streetPoints[1] and vertexList[0][n] == streetPoints[0]:
						#Try if i can add to the graph
						try:
							Graph[vertexList[0][m]].update( {vertexList[0][n] : distance} )
						#Or i create the entry
						except:
							Graph[vertexList[0][m]] = {vertexList[0][n] : distance}
					if vertexList[0][m] == streetPoints[0] and vertexList[0][n] == streetPoints[1]:
						#Try if i can add to the graph
						try:
							Graph[vertexList[0][m]].update( {vertexList[0][n] : distance} )
						#Or i create the entry
						except:
							Graph[vertexList[0][m]] = {vertexList[0][n] : distance}
		self.VertexList = vertexList
		return Graph