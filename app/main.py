from fastapi import FastAPI, HTTPException
from uuid import UUID
from app.models import Conta
from app.schemas import CriarConta, Operacao
from app.database import db

app = FastAPI()

@app.post("/contas", response_model=Conta)
async def criar_conta(dados: CriarConta):
    conta = Conta(nome=dados.nome)
    db[conta.id] = conta
    return conta

@app.get("/contas/{conta_id}", response_model=Conta)
async def obter_conta(conta_id: UUID):
    conta = db.get(conta_id)
    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    return conta

@app.post("/contas/{conta_id}/depositar")
async def depositar(conta_id: UUID, op: Operacao):
    conta = db.get(conta_id)
    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    conta.saldo += op.valor
    return {"saldo": conta.saldo}

@app.post("/contas/{conta_id}/sacar")
async def sacar(conta_id: UUID, op: Operacao):
    conta = db.get(conta_id)
    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    if conta.saldo < op.valor:
        raise HTTPException(status_code=400, detail="Saldo insuficiente")
    conta.saldo -= op.valor
    return {"saldo": conta.saldo}

@app.post("/transferir")
async def transferir(origem_id: UUID, destino_id: UUID, op: Operacao):
    origem = db.get(origem_id)
    destino = db.get(destino_id)
    if not origem or not destino:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    if origem.saldo < op.valor:
        raise HTTPException(status_code=400, detail="Saldo insuficiente")
    origem.saldo -= op.valor
    destino.saldo += op.valor
    return {"mensagem": "Transferência realizada com sucesso"}
