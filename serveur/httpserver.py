#!/usr/bin/python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os,sys
 
#Create custom HTTPRequestHandler class
class KodeFunHTTPRequestHandler(BaseHTTPRequestHandler):
  
  #handle GET command
  def do_GET(self):
   
	#send code 200 response
	self.send_response(200)

	#send header first
	self.send_header('Content-type','text-html')
	self.end_headers()
	#send websocket address
	self.wfile.write('{"IP":"172.30.0.227","port":8000}')
	return
  
def run():
  print('http server is starting on :'+sys.argv[1])
  server_address = (sys.argv[1], 8080)
  httpd = HTTPServer(server_address, KodeFunHTTPRequestHandler)
  print('http server is running...')
  httpd.serve_forever()
  
if __name__ == '__main__':
  run()