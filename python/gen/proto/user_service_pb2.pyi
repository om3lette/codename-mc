from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetUserRequest(_message.Message):
    __slots__ = ("tg_id",)
    TG_ID_FIELD_NUMBER: _ClassVar[int]
    tg_id: str
    def __init__(self, tg_id: _Optional[str] = ...) -> None: ...

class GetUserResponse(_message.Message):
    __slots__ = ("tg_id", "nickname")
    TG_ID_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    tg_id: str
    nickname: str
    def __init__(self, tg_id: _Optional[str] = ..., nickname: _Optional[str] = ...) -> None: ...

class ListUserRequest(_message.Message):
    __slots__ = ("limit", "offset")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class ListUserResponse(_message.Message):
    __slots__ = ("users",)
    class User(_message.Message):
        __slots__ = ("tg_id", "nickname")
        TG_ID_FIELD_NUMBER: _ClassVar[int]
        NICKNAME_FIELD_NUMBER: _ClassVar[int]
        tg_id: str
        nickname: str
        def __init__(self, tg_id: _Optional[str] = ..., nickname: _Optional[str] = ...) -> None: ...
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[ListUserResponse.User]
    def __init__(self, users: _Optional[_Iterable[_Union[ListUserResponse.User, _Mapping]]] = ...) -> None: ...

class CreateUserRequest(_message.Message):
    __slots__ = ("tg_id",)
    TG_ID_FIELD_NUMBER: _ClassVar[int]
    tg_id: str
    def __init__(self, tg_id: _Optional[str] = ...) -> None: ...

class UpdateUserRequest(_message.Message):
    __slots__ = ("tg_id", "nickname")
    TG_ID_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    tg_id: str
    nickname: str
    def __init__(self, tg_id: _Optional[str] = ..., nickname: _Optional[str] = ...) -> None: ...

class DeleteUserRequest(_message.Message):
    __slots__ = ("tg_id",)
    TG_ID_FIELD_NUMBER: _ClassVar[int]
    tg_id: str
    def __init__(self, tg_id: _Optional[str] = ...) -> None: ...
