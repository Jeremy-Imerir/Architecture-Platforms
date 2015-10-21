#!/usr/bin/python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os
 
#Create custom HTTPRequestHandler class
class HttpRequestHandler(BaseHTTPRequestHandler):
  
  #handle GET command
  def do_GET(self):
   
	#send code 200 response
	self.send_response(200)

	#send header first
	self.send_header('Content-type','text-html')
	self.end_headers()
	#send websocket address
	if (self.client_address[0]) == "192.168.0.2":
		self.wfile.write('{"IP":"192.168.0.1","port":8000}')
	else :
		self.wfile.write('{"IP":"172.30.0.227","port":8000}')
	return
  
def run(adress):
  print('http server is starting on :'+adress)
  server_address = (adress, 8090)
  httpd = HTTPServer(server_address, HttpRequestHandler)
  print('http server is running...')
  #Bind the socket on http and running forever
  httpd.serve_forever()
  
if __name__ == '__main__':
  run("0.0.0.0")