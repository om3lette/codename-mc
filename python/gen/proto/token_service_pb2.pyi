from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateTokenRequest(_message.Message):
    __slots__ = ("tg_id",)
    TG_ID_FIELD_NUMBER: _ClassVar[int]
    tg_id: str
    def __init__(self, tg_id: _Optional[str] = ...) -> None: ...

class CreateTokenResponse(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class DeleteTokenRequest(_message.Message):
    __slots__ = ("tg_id",)
    TG_ID_FIELD_NUMBER: _ClassVar[int]
    tg_id: str
    def __init__(self, tg_id: _Optional[str] = ...) -> None: ...

class AuthenticateRequest(_message.Message):
    __slots__ = ("nickname", "token")
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    nickname: str
    token: str
    def __init__(self, nickname: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...
