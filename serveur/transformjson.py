#!/usr/bin/python
# -*- coding: utf-8 -*-

import json, re, numpy, shortestfield, math, yaml

json_string = """
{
    "areas": [
        {
            "name": "Quartier Ouest",
            "map": {
                "weight": {
                    "w": 1,
                    "h": 1
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
                        "name": "ab",
                        "path": [
                            "a",
                            "b"
                        ],
                        "oneway": false
                    },
                    {
                        "name": "bc",
                        "path": [
                            "b",
                            "c"
                        ],
                        "oneway": false
                    },
                    {
                        "name": "cd",
                        "path": [
                            "c",
                            "d"
                        ],
                        "oneway": false
                    },
                    {
                        "name": "de",
                        "path": [
                            "d",
                            "e"
                        ],
                        "oneway": false
                    },
                    {
                        "name": "ef",
                        "path": [
                            "e",
                            "f"
                        ],
                        "oneway": false
                    }
                ],
                "bridges": [
                    {
                        "from": "a",
                        "to": {
                            "area": "Quartier Est",
                            "vertex": "o"
                        },
                        "weight": 2
                    },
                    {
                        "from": "b",
                        "to": {
                            "area": "Quartier Centre",
                            "vertex": "l"
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
                        "name": "g",
                        "x": 1,
                        "y": 1
                    },
                    {
                        "name": "h",
                        "x": 0,
                        "y": 1
                    },
                    {
                        "name": "i",
                        "x": 0.5,
                        "y": 1
                    },
                    {
                        "name": "j",
                        "x": 0.5,
                        "y": 0
                    },
                    {
                        "name": "k",
                        "x": 1,
                        "y": 0
                    }
                ],
                "streets": [
                    {
                        "name": "gh",
                        "path": [
                            "g",
                            "h"
                        ],
                        "oneway": false
                    },
                    {
                        "name": "ij",
                        "path": [
                            "i",
                            "j"
                        ],
                        "oneway": false
                    },
                    {
                        "name": "jk",
                        "path": [
                            "j",
                            "k"
                        ],
                        "oneway": false
                    }
                ],
                "bridges": [
                    {
                        "from": "g",
                        "to": {
                            "area": "Quartier Ouest",
                            "vertex": "b"
                        },
                        "weight": 2
                    },
                    {
                        "from": "h",
                        "to": {
                            "area": "Quartier Est",
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
                        "name": "l",
                        "x": 0,
                        "y": 1
                    },
                    {
                        "name": "m",
                        "x": 0,
                        "y": 0.5
                    },
                    {
                        "name": "n",
                        "x": 1,
                        "y": 0.5
                    },
                    {
                        "name": "o",
                        "x": 1,
                        "y": 0
                    },
                    {
                        "name": "p",
                        "x": 0.5,
                        "y": 0
                    }
                ],
                "streets": [
                    {
                        "name": "lm",
                        "path": [
                            "l",
                            "m"
                        ],
                        "oneway": false
                    },
                    {
                        "name": "mn",
                        "path": [
                            "m",
                            "n"
                        ],
                        "oneway": false
                    },
                    {
                        "name": "no",
                        "path": [
                            "n",
                            "o"
                        ],
                        "oneway": false
                    },
                    {
                        "name": "po",
                        "path": [
                            "p",
                            "o"
                        ],
                        "oneway": false
                    }
                ],
                "bridges": [
                    {
                        "from": "l",
                        "to": {
                            "area": "Quartier Centre",
                            "vertex": "h"
                        },
                        "weight": 2
                    },
                    {
                        "from": "o",
                        "to": {
                            "area": "Quartier Ouest",
                            "vertex": "a"
                        },
                        "weight": 2
                    }
                ]
            }
        }
    ]
}"""

parsed_json = json.loads(json_string, "utf-8")
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
		
		# print "x :"+str(x)+" y :"+str(y)
		# nmap[y][x] = 0

		# Append vertexes in a two-dimensional array
		vertexList[0].append(str(areamapvertices[j]["name"]))
		vertexList[1].append(str(x)+";"+str(y))
	for l in range(len(areamapbridges)) :
		areamapbridgesfrom = areamapbridges[l]["from"]
		areamapbridgesto = areamapbridges[l]["to"]
		streetList.append(str(areamapbridgesfrom[0])+";"+str(areamapbridgesto["vertex"]))
	for k in range(len(areamapstreets)) :
		areamapstreetspath = areamapstreets[k]["path"]
		streetList.append(str(areamapstreetspath[0])+";"+str(areamapstreetspath[1]))


# Graph = "{"
Graph={}
alreadyPut = []
streetList = sorted(streetList, key=str.lower)

print streetList
print 

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
				try:
					Graph[vertexList[0][m]].update( {vertexList[0][n] : distance} )
				except:
					Graph[vertexList[0][m]] = {vertexList[0][n] : distance}
			if vertexList[0][m] == streetPoints[0] and vertexList[0][n] == streetPoints[1]:
				try:
					Graph[vertexList[0][m]].update( {vertexList[0][n] : distance} )
				except:
					Graph[vertexList[0][m]] = {vertexList[0][n] : distance}

print Graph

l4,c4 = shortestfield.dij_rec(Graph, "a", "p")
print 'Plus court chemin ex4 : ',c4, ' de longueur :',l4