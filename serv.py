import zmq
import datetime
import time
import sys

port = '5560'
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:%s" %port )
print sys.argv
while True:
    msg = socket.recv()
    print 'RECERIVED',msg
    ts = time.time()
    print 'NOW',datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    socket.send('received')
    time.sleep(1)
