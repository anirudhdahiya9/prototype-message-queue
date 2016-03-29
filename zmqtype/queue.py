import zmq

context = zmq.Context(1)
frontend = context.socket(zmq.XREP)
frontend.bind("tcp://*:5559")

backend = context.socket(zmq.XREQ)
backend.bind("tcp://*:5560")

zmq.device(zmq.QUEUE, frontend, backend)
