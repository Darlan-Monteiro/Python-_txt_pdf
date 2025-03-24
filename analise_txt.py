# bloco para ler o arquivo e as linhas
bd_alunos = open('Alunos.txt', 'r')
linhas = bd_alunos.readlines()
# precisei aplicar del até o índice 4, pq eles não serviam pra nada
del linhas[:4]

# declarei as variaveis para fazer calculo
qtde_org = 0
qtde_site_org = 0
qtde_yt_org = 0
qtde_igfb_org = 0
qtde_anuncio = 0

# for para percorrer o meu arquivo txt
for linha in linhas:
    email, origem = linha.split(',') # split separa que vem antes e depois da vírgula

    if "_org" in origem: # if pra verificar se o nome está contido na var origem
        qtde_org += 1
        # bloco de if's para calcular valores caso true
        if "hashtag_site_org" in origem:
            qtde_site_org +=1
        if "hashtag_yt_org" in origem:
            qtde_yt_org += 1
        if "hashtag_ig_org" in origem or "hashtag_igfb_org" in origem:
            qtde_igfb_org += 1
        # caso os if's sejam false, o else aparece e soma
        else:
            qtde_anuncio += 1

bd_alunos.close() # close para fechar o arquivo e salvar após o loop for

# bloco de print para eu ver os valores antes de levar para o arquivo
print(f'Quantidade Total Anuncio: {qtde_anuncio}')
print(f'Quantidade Total Orgânico: {qtde_org}')
print(f'Quantidade Total Site: {qtde_site_org}')
print(f'Quantidade Total Youtube: {qtde_yt_org}')
print(f'Quantidade Total Instagram/Facebook: {qtde_igfb_org}')

# usando with para criar um arquivo novo(ou modificar um existente). armazenei as informações na var 'analise_alunos'
with open('Análise de Alunos.txt', 'w') as analise_alunos: # como estou usando with, não preciso de close no final
    # aqui estou adicionando os dados no arquivo que criei (ou modifiquei)
    analise_alunos.write('ANÁLISE DOS DADOS ADQUIRIDOS\n''\n-------------------------------------------\n\n'
        f'Quantidade Total Anuncio: {qtde_anuncio}\nQuantidade Total Orgânico: {qtde_org}\n'
        f'Quantidade Total Site: {qtde_site_org}\nQuantidade Total Youtube: {qtde_yt_org}\nQuantidade Total Instagram/Facebook: {qtde_igfb_org}')
    