#!/usr/bin/env python
import pika

credentials = pika.credentials.PlainCredentials('ksl-ubl', 'ksl-ubl', erase_on_connect=False)
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', credentials=credentials, socket_timeout=2))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received {}".format(str(body,"utf-8")))

channel.basic_consume(callback, queue='hello', no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
