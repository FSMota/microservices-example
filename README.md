# 🛒 Micro-serviços E-commerce - Prova de Conceito

Este projeto demonstra a implementação de uma arquitetura de micro-serviços utilizando **Python** e **FastAPI**. O foco principal é exemplificar a **Orquestração de Serviços**, onde um serviço central coordena a comunicação entre funcionalidades independentes.

## 🏗️ Arquitetura do Sistema

O sistema é dividido em três componentes principais, cada um rodando em um processo isolado:

1.  **Serviço Orquestrador (Porta 8000):** Atua como o ponto de entrada único para o cliente. Ele não armazena dados; sua função é consultar o *Carrinho* e o *Catálogo* para processar o checkout.
2.  **Serviço de Catálogo (Porta 8001):** Gerencia o inventário de produtos e seus respectivos preços.
3.  **Serviço de Carrinho (Porta 8002):** Gerencia os itens temporários selecionados pelo usuário.

## 🛠️ Tecnologias Utilizadas

* **FastAPI:** Framework moderno e assíncrono para criação de APIs.
* **Uvicorn:** Servidor ASGI para execução dos serviços.
* **Httpx:** Cliente HTTP para comunicação assíncrona entre micro-serviços.
* **Pydantic:** Validação de dados e definição de esquemas.

## 🚀 Como Executar o Projeto

Com o seu ambiente virtual (`venv`) ativo no PowerShell, abra três terminais e execute:

**1. Iniciar o Catálogo:**
```powershell
python -m uvicorn catalogo:app --port 8001
```

```powershell
python -m uvicorn carrinho:app --port 8002
```

```powershell
python -m uvicorn orquestrador:app --port 8000
```

📸 Demonstração de Resultados
1. Serviço de Catálogo (Listagem)

Requisição ao serviço funcional de catálogo para listar produtos disponíveis.
2. Serviço de Carrinho (Adição)

Adição de itens via método POST, demonstrando a persistência em memória do serviço.
3. Orquestrador (Checkout Finalizado)

Aqui o Orquestrador consome as duas APIs anteriores, calcula os subtotais e o total geral, entregando uma resposta única ao cliente.
