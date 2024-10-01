from csv import reader

def multiplicacao(n1,n2):
    return n1 * n2

def ler_arquivo_csv(arquivo):
    dados = list()
    with open(arquivo, 'r', encoding='utf') as arquivo:
        leitor = reader(arquivo)
        for linha in leitor:
            if not linha:
                continue
            dados.append(linha)
    return dados


if __name__ == '__main__':
    dados_arquivo = ler_arquivo_csv('cidades.csv')
    print(dados_arquivo)
