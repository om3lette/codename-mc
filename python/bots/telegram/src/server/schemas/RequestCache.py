from pydantic import BaseModel
from datetime import datetime


class RequestCacheSchema(BaseModel):
	data: any
	timestamp: datetime

	def has_expired(self, expire_time: datetime.timestamp) -> bool:
		return (datetime.now() - self.timestamp) > expire_time

	class Config:
		arbitrary_types_allowed = True
