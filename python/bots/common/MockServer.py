from concurrent import futures

import grpc
import python.gen.proto.token_service_pb2 as token_service_pb2
import python.gen.proto.token_service_pb2_grpc as token_service_pb2_grpc


class GreeterServicer(token_service_pb2_grpc.TokenServiceServicer):
	def create_token(self, request, context):
		return token_service_pb2.CreateTokenResponse(token="test_token")


def serve():
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	token_service_pb2_grpc.add_TokenServiceServicer_to_server(
		token_service_pb2_grpc.TokenServiceServicer(), server
	)
	server.add_insecure_port("localhost:50051")
	server.start()
	server.wait_for_termination()


if __name__ == "__main__":
	serve()
