#!/usr/bin/python

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

# json_string = json_string.replace('\n', ' ')
# json_string = re.sub(' +', ' ', json_string)
parsed_json = json.loads(json_string, "utf-8")
areas = parsed_json["areas"]

vertexList = []
streetList = []
bridgeList = []

for i in range(len(areas)) :
	areaname = json.dumps(areas[i]["name"])
	areamap = areas[i]["map"]
	
	areamapvertices = areamap["vertices"]
	areamapstreets = areamap["streets"]
	areamapbridges = areamap["bridges"]
	
	for j in range(len(areamapvertices)) :
	
		x = areamapvertices[j]["x"]*9+(i*10)
		y = ((areamapvertices[j]["y"])*9)
		
		print "x :"+str(x)+" y :"+str(y)+ " nb :"+str(j+4+i)
		nmap[y][x] = 0
		
		vertexList.append(str(areamapvertices[j]["name"])+";"+str(i+1)+";"+str(areamapvertices[j]["x"])+";"+str(areamapvertices[j]["y"]))
	
	for k in range(len(areamapstreets)) :
		areamapstreetspath = areamapstreets[k]["path"]
		streetList.append(str(i+1)+";"+str(areamapstreetspath[0])+";"+str(areamapstreetspath[1])+";"+str(areamapstreets[k]["name"]+";"+str(areamapstreets[k]["oneway"])))
			
	
	for l in range(len(areamapbridges)) :
		areamapbridgesto = areamapbridges[l]["to"]
		bridgeList.append(str(i+1)+";"+str(areamapbridgesto["vertex"])+";"+str(areamapbridgesto["area"])+";"+str(areamapbridges[l]["from"]+";"+str(areamapbridges[l]["weight"])))

nmap = nmap[::-1]
print nmap
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