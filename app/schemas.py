from pydantic import BaseModel
from decimal import Decimal

class CriarConta(BaseModel):
    nome: str

class Operacao(BaseModel):
    valor: Decimal
