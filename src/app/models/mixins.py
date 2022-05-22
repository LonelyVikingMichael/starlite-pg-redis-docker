import datetime

from sqlalchemy import Column, DateTime
from sqlalchemy.orm import declarative_mixin


@declarative_mixin
class DateFieldsMixins:
    created_date: datetime.datetime = Column(DateTime, default=datetime.datetime.now)
    updated_date: datetime.datetime = Column(DateTime, default=datetime.datetime.now)
