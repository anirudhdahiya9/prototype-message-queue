import zmq
import datetime
import time
import datetime

port = '5559'
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:%s" %port)

while True:
    ts = time.time()
    socket.send(str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')))
    msg = socket.recv()
    time.sleep(1)
