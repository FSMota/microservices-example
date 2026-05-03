from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Serviço de Carrinho")

# Memória do carrinho
carrinho_db = []

class ItemCarrinho(BaseModel):
    produto_id: int
    quantidade: int

@app.get("/carrinho")
def ver_carrinho():
    return {"itens": carrinho_db}

@app.post("/carrinho")
def adicionar_item(item: ItemCarrinho):
    carrinho_db.append(item.model_dump())
    return {"mensagem": "Item adicionado com sucesso!", "carrinho": carrinho_db}