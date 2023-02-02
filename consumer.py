import pika
import time

credentials = pika.PlainCredentials('test','test')
parameters =  pika.ConnectionParameters('192.168.56.11', credentials=credentials, heartbeat=5)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
	print(" [x] Received %r" % body)
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=False)

channel.start_consuming()
