#!/bin/bash

root_relative_path=.

proto_folder_path=$root_relative_path/api/access-manager/v1
proto_files="$proto_folder_path/*.proto"

save_path=$root_relative_path/python/gen/proto
mkdir $save_path
rm -f $save_path/*pb2*
touch $save_path/__init__.py

for proto_file_path in $proto_files; do
  python3 -m grpc_tools.protoc -I$proto_folder_path --python_out=$save_path --pyi_out=$save_path --grpc_python_out=$save_path "$proto_file_path"

  # Patch generated files to support module import
  service_grpc_filename=$(basename "$proto_file_path" | cut -d. -f1)_pb2_grpc.py
  # https://stackoverflow.com/questions/62818183/protobuf-grpc-relative-import-path-discrepancy-in-python/
  sed -i 's/^import .*_pb2 as/from . \0/' "$save_path/$service_grpc_filename"
done
