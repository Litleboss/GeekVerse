from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import glob

# Cria a instância principal da aplicação FastAPI
app = FastAPI(title="Álbum de Figurinhas API")

# Configure o middleware CORS para aceitar requisições de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Defina caminhos absolutos para a pasta de imagens
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Lista chamada figurinhas com as 30 figurinhas
# Deixe ativas apenas as figurinhas cujas imagens existem na pasta figurinhas/ (ids 1 e 2)
# Comente as figurinhas que ainda não estão disponíveis (ids 3 a 30)
figurinhas = [
    {"id": 1, "nome": "Vegeta", "categoria": "Dragon Ball", "imagem_url": "/figurinhas/1/imagem"},
    {"id": 2, "nome": "Gohan", "categoria": "Dragon Ball", "imagem_url": "/figurinhas/2/imagem"},
    {"id": 3, "nome": "Goku", "categoria": "Dragon Ball", "imagem_url": "/figurinhas/3/imagem"},
    {"id": 4, "nome": "Piccolo", "categoria": "Dragon Ball", "imagem_url": "/figurinhas/4/imagem"},
    {"id": 5, "nome": "Freeza", "categoria": "Dragon Ball", "imagem_url": "/figurinhas/5/imagem"},

    {"id": 6, "nome": "Sasuke", "categoria": "Naruto", "imagem_url": "/figurinhas/6/imagem"},
    {"id": 7, "nome": "Kakashi", "categoria": "Naruto", "imagem_url": "/figurinhas/7/imagem"},
    {"id": 8, "nome": "Naruto", "categoria": "Naruto", "imagem_url": "/figurinhas/8/imagem"},
    {"id": 9, "nome": "Sakura", "categoria": "Naruto", "imagem_url": "/figurinhas/9/imagem"},
    {"id": 10, "nome": "Itachi", "categoria": "Naruto", "imagem_url": "/figurinhas/10/imagem"},

    {"id": 11, "nome": "Zoro", "categoria": "One Piece", "imagem_url": "/figurinhas/11/imagem"},
    {"id": 12, "nome": "Sanji", "categoria": "One Piece", "imagem_url": "/figurinhas/12/imagem"},
    {"id": 13, "nome": "Luffy", "categoria": "One Piece", "imagem_url": "/figurinhas/13/imagem"},
    {"id": 14, "nome": "Nami", "categoria": "One Piece", "imagem_url": "/figurinhas/14/imagem"},
    {"id": 15, "nome": "Shanks", "categoria": "One Piece", "imagem_url": "/figurinhas/15/imagem"},

    {"id": 16, "nome": "Nezuko", "categoria": "Demon Slayer", "imagem_url": "/figurinhas/16/imagem"},
    {"id": 17, "nome": "Zenitsu", "categoria": "Demon Slayer", "imagem_url": "/figurinhas/17/imagem"},
    {"id": 18, "nome": "Tanjiro", "categoria": "Demon Slayer", "imagem_url": "/figurinhas/18/imagem"},
    {"id": 19, "nome": "Inosuke", "categoria": "Demon Slayer", "imagem_url": "/figurinhas/19/imagem"},
    {"id": 20, "nome": "Muzan", "categoria": "Demon Slayer", "imagem_url": "/figurinhas/20/imagem"},

    {"id": 21, "nome": "Megumi", "categoria": "Jujutsu Kaisen", "imagem_url": "/figurinhas/21/imagem"},
    {"id": 22, "nome": "Yuta", "categoria": "Jujutsu Kaisen", "imagem_url": "/figurinhas/22/imagem"},
    {"id": 23, "nome": "Gojo", "categoria": "Jujutsu Kaisen", "imagem_url": "/figurinhas/23/imagem"},
    {"id": 24, "nome": "Yudi", "categoria": "Jujutsu Kaisen", "imagem_url": "/figurinhas/24/imagem"},
    {"id": 25, "nome": "Nobara", "categoria": "Jujutsu Kaisen", "imagem_url": "/figurinhas/25/imagem"},

    {"id": 26, "nome": "Rukia", "categoria": "Bleach", "imagem_url": "/figurinhas/26/imagem"},
    {"id": 27, "nome": "Byakuya", "categoria": "Bleach", "imagem_url": "/figurinhas/27/imagem"},
    {"id": 28, "nome": "Ichigo", "categoria": "Bleach", "imagem_url": "/figurinhas/28/imagem"},
    {"id": 29, "nome": "Kenpachi", "categoria": "Bleach", "imagem_url": "/figurinhas/29/imagem"},
    {"id": 30, "nome": "Aizen", "categoria": "Bleach", "imagem_url": "/figurinhas/30/imagem"},
]

# Endpoint GET "/figurinhas" que retorna a lista
@app.get("/figurinhas")
def listar_figurinhas():
    return figurinhas

# Endpoint GET "/figurinhas/{id}/imagem"
@app.get("/figurinhas/{id}/imagem")
def obter_imagem_figurinha(id: int):
    # Usa glob para encontrar o arquivo com prefixo "{id:02d}[!0-9]*" na pasta figurinhas/
    padrao = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")
    arquivos = glob.glob(padrao)
    
    # Retorna 404 se não encontrar
    if not arquivos:
        raise HTTPException(status_code=404, detail="Imagem não encontrada para a figurinha informada.")
    
    # Retorna FileResponse com o arquivo encontrado
    return FileResponse(arquivos[0])

