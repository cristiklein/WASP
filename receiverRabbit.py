#!/usr/bin/env python
import pika
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('credentials.properties')
rabbitUser=config.get('user1', 'username');
rabbitPassword=config.get('user1', 'password');
rabbitServer=config.get('rabbit', 'server');
rabbitPort=config.get('rabbit', 'port');
credentials = pika.PlainCredentials(rabbitUser, rabbitPassword)

connection = pika.BlockingConnection(pika.ConnectionParameters(rabbitServer,rabbitPort,'/',credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
