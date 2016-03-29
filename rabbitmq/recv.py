import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

def callback(ch,method,properties, body):
    print body

channel.basic_consume(callback, queue='hello',no_ack=True)

channel.start_consuming()
    
