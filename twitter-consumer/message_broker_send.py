__author__ = "grao-swe"

import pika


class Sender(object):
    
    connection = None
    channel = None
    queue = None
    
    def __init__(self,  queue):
        self.queue = queue
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()                      
        self.channel.queue_declare(queue=self.queue)
        
    def send(self, data):
        # (TODO): log info of the data
        self.channel.basic_publish(exchange='', routing_key=self.queue, body=data)        
        
    def close(self):
        self.connection.close()