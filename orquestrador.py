from fastapi import FastAPI
import httpx

app = FastAPI(title="Serviço Orquestrador")

URL_CATALOGO = "http://127.0.0.1:8001"
URL_CARRINHO = "http://127.0.0.1:8002"

@app.get("/checkout")
async def realizar_checkout():
    async with httpx.AsyncClient() as client:
        # 1. Pede os itens do carrinho ao Serviço de Carrinho
        resp_carrinho = await client.get(f"{URL_CARRINHO}/carrinho")
        itens = resp_carrinho.json().get("itens", [])

        if not itens:
            return {"mensagem": "O carrinho está vazio."}

        resumo_compra = []
        total_pedido = 0.0

        # 2. Para cada item, busca os detalhes no Serviço de Catálogo
        for item in itens:
            resp_produto = await client.get(f"{URL_CATALOGO}/produtos/{item['produto_id']}")
            dados_produto = resp_produto.json()

            if "erro" not in dados_produto:
                subtotal = dados_produto["preco"] * item["quantidade"]
                total_pedido += subtotal
                
                resumo_compra.append({
                    "produto": dados_produto["nome"],
                    "quantidade": item["quantidade"],
                    "preco_unitario": dados_produto["preco"],
                    "subtotal": subtotal
                })

        # 3. Retorna os dados agregados para o cliente (Front-end)
        return {
            "resumo": resumo_compra,
            "total_pedido": total_pedido
        }