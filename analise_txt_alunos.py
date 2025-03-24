import os
from dotenv import load_dotenv

# Carregar variáveis do ambiente
load_dotenv()
caminho_alunos = os.getenv('alunos')

# Verificar se o caminho do arquivo foi carregado corretamente
if not caminho_alunos or not os.path.exists(caminho_alunos):
    raise FileNotFoundError(f"Arquivo não encontrado: {caminho_alunos}")

# Ler o arquivo e as linhas
with open(caminho_alunos, 'r') as bd_alunos:
    linhas = bd_alunos.readlines()

# Remover as 4 primeiras linhas, pois não são úteis
del linhas[:4]

# Inicializar variáveis de contagem
qtde_org = 0
qtde_site_org = 0
qtde_yt_org = 0
qtde_igfb_org = 0
qtde_anuncio = 0

# Processar cada linha do arquivo
for linha in linhas:
    email, origem = linha.strip().split(',')  # strip() remove espaços extras e quebras de linha

    if "_org" in origem:  
        qtde_org += 1
        if "hashtag_site_org" in origem:
            qtde_site_org += 1
        elif "hashtag_yt_org" in origem:
            qtde_yt_org += 1
        elif "hashtag_ig_org" in origem or "hashtag_igfb_org" in origem:
            qtde_igfb_org += 1
    else:
        qtde_anuncio += 1

# Exibir os resultados
print("\n===== RESULTADOS =====")
print(f'Quantidade Total Anúncio: {qtde_anuncio}')
print(f'Quantidade Total Orgânico: {qtde_org}')
print(f'  ↳ Site: {qtde_site_org}')
print(f'  ↳ Youtube: {qtde_yt_org}')
print(f'  ↳ Instagram/Facebook: {qtde_igfb_org}')
print("=======================\n")

# Teste com diretório temporário
caminho_analise = r"C:\Users\SAMSUNG\Downloads\Analise_de_Alunos.txt"

# Criar o diretório se não existir
diretorio = os.path.dirname(caminho_analise)
if not os.path.exists(diretorio):
    print(f"Criando diretório: {diretorio}")
    os.makedirs(diretorio, exist_ok=True)

# Escrever a análise no arquivo com codificação UTF-8
with open(caminho_analise, "w", encoding="utf-8") as analise_alunos:
    analise_alunos.write(
        "ANÁLISE DOS DADOS ADQUIRIDOS\n"
        "-------------------------------------------\n\n"
        f"Quantidade Total Anúncio: {qtde_anuncio}\n"
        f"Quantidade Total Orgânico: {qtde_org}\n"
        f"  ↳ Site: {qtde_site_org}\n"
        f"  ↳ Youtube: {qtde_yt_org}\n"
        f"  ↳ Instagram/Facebook: {qtde_igfb_org}\n"
    )

print(f"Análise salva em: {caminho_analise}")
