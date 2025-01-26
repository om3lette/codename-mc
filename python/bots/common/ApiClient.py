import grpc
import python.gen.proto.token_service_pb2 as token_service_pb2
import python.gen.proto.token_service_pb2_grpc as token_service_pb2_grpc


def run():
	with grpc.insecure_channel("localhost:50051") as channel:
		stub = token_service_pb2_grpc.TokenServiceStub(channel)
		try:
			r = stub.Create(token_service_pb2.CreateTokenRequest(tg_id="your_great_id"))
			print(r)
		except grpc.RpcError:
			return


if __name__ == "__main__":
	run()
