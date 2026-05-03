from fastapi import FastAPI

app = FastAPI(title="Serviço de Catálogo")

# Banco de dados em memória
produtos_db = {
    1: {"id": 1, "nome": "Notebook High Performance", "preco": 8500.00},
    2: {"id": 2, "nome": "Teclado Mecânico", "preco": 350.00},
    3: {"id": 3, "nome": "Monitor 27''", "preco": 1200.00}
}

@app.get("/produtos")
def listar_produtos():
    return list(produtos_db.values())

@app.get("/produtos/{produto_id}")
def buscar_produto(produto_id: int):
    return produtos_db.get(produto_id, {"erro": "Produto não encontrado"})