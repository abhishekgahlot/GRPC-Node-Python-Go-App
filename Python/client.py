import app

import grpc

def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = app.App(channel)
  #response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
  #print("Greeter client received: " + response.message)


if __name__ == '__main__':
  run()