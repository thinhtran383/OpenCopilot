import datetime
import uuid

from opencopilot_db.database_setup import Base, engine
from sqlalchemy import Column, String, DateTime, JSON, Text


class Flow(Base):
    __tablename__ = 'actions'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(255), nullable=True, default="")
    description = Column(Text, nullable=True, default="")
    payload = Column(JSON, nullable=False, default={})
    status = Column(String(255), default='live')
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)


Base.metadata.create_all(engine)
