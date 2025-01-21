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
		panic("failed to run server")
	}

	log.Println("listening on :8080")

	dummyServer.Serve(lis)
}
