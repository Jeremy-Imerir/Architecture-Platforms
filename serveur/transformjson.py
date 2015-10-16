#!/usr/bin/python
# -*- coding: utf-8 -*-

import json, re, numpy

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
}"""

nmap = numpy.array([
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])
	
def paintStreets(firstpoint, secondpoint) :
		print firstpoint+ " "+secondpoint
		print
		firstpoint = firstpoint.split(";")
		secondpoint = secondpoint.split(";")
		
		diffX = abs(int(firstpoint[0]) - int(secondpoint[0]))
		diffY = abs(int(firstpoint[1]) - int(secondpoint[1]))
		
		# Difference on the x axis
		if diffX != 0 and diffY == 0:
			for n in range(diffX) :
				if int(firstpoint[0]) > int(secondpoint[0]) :
					# X and Y are reversed because it's reversed too in nmap
					nmap[int(secondpoint[1])][int(secondpoint[0])+int(n)] = 0

				elif int(secondpoint[0]) > int(firstpoint[0]) :
					# X and Y are reversed because it's reversed too in nmap
					nmap[int(firstpoint[1])][int(firstpoint[0])+int(n)] = 0

		# Difference on the y axis
		if diffY != 0 and diffX == 0:
			for n in range(diffY):
				if int(firstpoint[1]) > int(secondpoint[1]) :
					# X and Y are reversed because it's reversed too in nmap
					nmap[int(secondpoint[1])+int(n)][int(secondpoint[0])] = 0

				elif int(secondpoint[1]) > int(firstpoint[1]) :
					# X and Y are reversed because it's reversed too in nmap
					nmap[int(firstpoint[1])+int(n)][int(firstpoint[0])] = 0

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
		nmap[y][x] = 0
		
		# vertexList.append(str(areamapvertices[j]["name"])+";"+str(i+1)+";"+str(areamapvertices[j]["x"])+";"+str(areamapvertices[j]["y"]))
		
		# Append vertexes in a two-dimensional array
		vertexList[0].append(str(areamapvertices[j]["name"]))
		vertexList[1].append(str(x)+";"+str(y))

	for k in range(len(areamapstreets)) :
		areamapstreetspath = areamapstreets[k]["path"]
		streetList.append(str(i+1)+";"+str(areamapstreetspath[0])+";"+str(areamapstreetspath[1])+";"+str(areamapstreets[k]["name"]+";"+str(areamapstreets[k]["oneway"])))
		firstpoint = ""
		secondpoint = ""

		for m in range(len(vertexList[0])) :
			# print vertexList[0][m] +" "+ str(areamapstreetspath[1])
			if vertexList[0][m] == str(areamapstreetspath[0]):
				firstpoint = vertexList[1][m]
			elif vertexList[0][m] == str(areamapstreetspath[1]):
				secondpoint = vertexList[1][m]
				
			# I have the 2 points of the street i can paint it
			if firstpoint!="" and secondpoint != "" :
				paintStreets(firstpoint, secondpoint)
				firstpoint = ""
				secondpoint = ""
		
	# for l in range(len(areamapbridges)) :
		# areamapbridgesto = areamapbridges[l]["to"]
		# bridgeList.append(str(i+1)+";"+str(areamapbridgesto["vertex"])+";"+str(areamapbridgesto["area"])+";"+str(areamapbridges[l]["from"]+";"+str(areamapbridges[l]["weight"])))
		# nmap[y][x] = 0
		
nmap = nmap[::-1]
print nmap

print vertexList[0]
print vertexList[1]