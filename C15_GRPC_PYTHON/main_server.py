from concurrent import futures

import grpc

import hello_pb2
import hello_pb2_grpc
import logging

class Greeter(hello_pb2_grpc.GreeterServicer):

    def SayHello(self,request,context):
        return hello_pb2.HelloReply(message=f'Hi there {request.name}')

def serve():

    server=grpc.server(futures.ThreadPoolExecutor(max_workers=3))
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(),server)
    server.add_insecure_port('[::]:30100')
    server.start()
    server.wait_for_termination()

if __name__== '__main__':
    logging.basicConfig()
    serve()