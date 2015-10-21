#!/usr/bin/python
# -*- coding: utf-8 -*-
 
 
 
def affiche_peres(pere,depart,extremite,trajet):
    """

	With fathers' dictionnary of each vertexes we send back the vertexes' 
	list of the shortest path.
    
    """
    if extremite == depart:
        return [depart] + trajet
    else:
        return (affiche_peres(pere, depart, pere[extremite], [extremite] + trajet))
 
def plus_court(graphe,etape,fin,visites,dist,pere,depart):
    # if we are at the end, we print the distance and fathers
    if etape == fin:
       return dist[fin], affiche_peres(pere,depart,fin,[])
    # if it's the first visit, the actual stape is the beginning: we put dist[etape] to 0
    if  len(visites) == 0 : dist[etape]=0
    # we begin to test each neighbors unvisited
    for voisin in graphe[etape]:
        if voisin not in visites:
            # this distance is the previous calculated distance or infinite
            dist_voisin = dist.get(voisin,float('inf'))
            # we calculate the new distance passing this step
            candidat_dist = dist[etape] + graphe[etape][voisin]
            # we do changes if we have the shortest path
            if candidat_dist < dist_voisin:
                dist[voisin] = candidat_dist
                pere[voisin] = etape
    # we saw all neighbors : entire node is visited
    visites.append(etape)
    # we are looking for the vertex, unvisited, closer from the begin
    non_visites = dict((s, dist.get(s,float('inf'))) for s in graphe if s not in visites)
    noeud_plus_proche = min(non_visites, key = non_visites.get)
    # we callback the function with the new infos
    return plus_court(graphe,noeud_plus_proche,fin,visites,dist,pere,depart)
 
def dij_rec(graphe,debut,fin):
    return plus_court(graphe,debut,fin,[],{},{},debut)
 
