import pika

from tasks import analyze

__author__ = "grao-swe"

class Receiver(object):
    
    connection = None
    channel = None
    
    def __init__(self, host):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.channel = self.connection.channel()


    def callback(self, channel, method, properties, body):
        # (TODO) log info of the received
        result = analyze(body)       

    def start_consuming(self, queue, no_ack=True):        
        self.channel.basic_consume(self.callback, queue=queue, no_ack=no_ack)
        print (' [*] Waiting for messages.')
        self.channel.start_consuming()        


if __name__ == "__main__":
    
    queue = "geo-tweet"
    host = "localhost"
    
    receiver = Receiver(host)
    receiver.start_consuming(queue, no_ack=True)
    