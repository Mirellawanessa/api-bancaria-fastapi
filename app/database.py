from typing import Dict
from uuid import UUID
from app.models import Conta

db: Dict[UUID, Conta] = {}