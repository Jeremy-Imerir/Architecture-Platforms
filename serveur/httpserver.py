#!/usr/bin/python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os
 
#Create custom HTTPRequestHandler class
class KodeFunHTTPRequestHandler(BaseHTTPRequestHandler):
  
  #handle GET command
  def do_GET(self):
   
	#send code 200 response
	self.send_response(200)

	#send header first
	self.send_header('Content-type','text-html')
	self.end_headers()
	self.wfile.write('ws://172.30.0.170:8000')
	return
  
def run():
  print('http server is starting...')
  server_address = ('172.30.0.170', 8080)
  httpd = HTTPServer(server_address, KodeFunHTTPRequestHandler)
  print('http server is running...')
  httpd.serve_forever()
  
if __name__ == '__main__':
  run()