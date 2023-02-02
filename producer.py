import pika
import time

credentials = pika.PlainCredentials('test','test')
parameters =  pika.ConnectionParameters('192.168.56.12', credentials=credentials, heartbeat=5)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.queue_declare(queue='hello')

count=0
while True:
	count +=1
	channel.basic_publish(exchange='', routing_key='hello', body='Hello Netology!')
	time.sleep(1)

connection.close()
