from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from decimal import Decimal

class Conta(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    nome: str
    saldo: Decimal = Field(default=0)