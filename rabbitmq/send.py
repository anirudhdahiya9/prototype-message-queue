import pika
import sys
import datetime
import time

connnection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connnection.channel()
serv = sys.argv[1]
print serv
channel.queue_declare(queue="hello")
while True:
    bdy = 'Server ' + serv + str(datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S'))
    print 'SEND' + bdy
    channel.basic_publish(exchange='',routing_key='hello',body=bdy)
    time.sleep(1)
    
