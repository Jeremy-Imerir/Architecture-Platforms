#!/usr/bin/python

from gevent import monkey
monkey.patch_all()

import time
from threading import Thread
from flask import Flask, render_template, session, request
from flask.ext.socketio import SocketIO, emit, join_room, leave_room, \
    close_room, disconnect

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
thread = None
disconnected = True
maxclients = 4
nbofclients = 0
hostip = "172.30.0.170"
port = 5001



def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    global disconnected
    while disconnected == True:
        time.sleep(1)
        #count += 1
        #socketio.emit('my response',
        #              {'data': 'Server generated event', 'count': count},
        #              namespace='/test')
    print "Sorti du Thread"

@app.route('/')
def index():
    global maxclients
    global nbofclients
    if nbofclients<maxclients:
    	global thread
    	if thread is None:
        	thread = Thread(target=background_thread)
        	thread.start()
    	nbofclients += 1
    	print 'Client '+str(nbofclients)+' connected'
		
    	return render_template('index.html')
    	#return "ws://"+str(hostip)+ ":" +str(port)+"/test"
    else:       
	
    	#return render_template('indexfull.html')
    	return "C'est pas bon"


@socketio.on('my event', namespace='/test')
def test_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    print message['data']+" // received"
    emit('my response',
         {'data': message['data'], 'count': session['receive_count']})


@socketio.on('my broadcast event', namespace='/test')
def test_broadcast_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    print message['data']+" // broadcast received"
    emit('my response',
         {'data': message['data'], 'count': session['receive_count']},
         broadcast=True)

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected', 'count': 0})


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': 'Disconnected!', 'count': session['receive_count']})
    

    global disconnected 
    disconnected = False
    print('Client disconnected')
    disconnect()


if __name__ == '__main__':
    socketio.run(app, host=hostip, port=port)
