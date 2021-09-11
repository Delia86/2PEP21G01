from __future__ import print_function
import grpc
import area_pb2_grpc
import area_pb2
import logging

def run(dst):
    with grpc.insecure_channel("localhost:30100") as channel:
        stub = area_pb2_grpc.PingStub(channel)
        response = stub.PingIP(area_pb2.Destination(dst=dst))
        for rsp in response:
            print(rsp.rsp)

if __name__ == "__main__":
    logging.basicConfig()
    run('8.8.8.8')