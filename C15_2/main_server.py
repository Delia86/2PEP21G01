import logging
import subprocess
import time
from concurrent import futures
import grpc
import area_pb2
import area_pb2_grpc
from subprocess import Popen

class PingIP(area_pb2_grpc.PingServicer):

    def PingIP(self, request, context):
        ping = Popen(['ping', request.dst], text=True, stdout=subprocess.PIPE)
        output = ping.communicate()[0]
        for line in output.splitlines():
            time.sleep(0.5)
            print(line)
            yield area_pb2.Response(rsp=line)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
    area_pb2_grpc.add_PingServicer_to_server(PingIP(), server)
    server.add_insecure_port('[::]:30100')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()
    serve()