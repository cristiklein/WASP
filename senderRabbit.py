#!/usr/bin/env python
import pika
import ConfigParser
config = ConfigParser.RawConfigParser()
config.read('credentials.properties')
rabbitUser=config.get('user1', 'username');
rabbitPassword=config.get('user1', 'password');
credentials = pika.PlainCredentials(rabbitUser, rabbitPassword)
connection = pika.BlockingConnection(pika.ConnectionParameters('beredo.cs.umu.se',5672,'/',credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
