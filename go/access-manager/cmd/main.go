package main

import (
	"log"
	"net"

	ampb "github.com/om3lette/codename-mc/go/gen/proto/codenamemc.accesssmanager"
	"google.golang.org/grpc"
	"google.golang.org/grpc/reflection"
)

func main() {
	dummyServer := grpc.NewServer()

	dummyServer.RegisterService(&ampb.UserService_ServiceDesc, ampb.UnimplementedUserServiceServer{})
	dummyServer.RegisterService(&ampb.TokenService_ServiceDesc, ampb.UnimplementedTokenServiceServer{})

	reflection.Register(dummyServer)

	lis, err := net.Listen("tcp", ":8080")
	if err != nil {
		log.Fatalf("failed to run grpc server: %s\n", err.Error())
	}

	log.Printf("server is running on :8080\n")

	err = dummyServer.Serve(lis)
	if err != nil {
		log.Printf("server finished with err: %s\n", err.Error())
	}
}
