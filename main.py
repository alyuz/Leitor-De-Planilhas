from csv import reader


def ler_planilha_alunos(arquivo):
    alunos = list()
    with open(arquivo, 'r', encoding='utf') as arquivo:
        leitor = reader(arquivo)
        for linha in leitor:
            if not linha:
                continue
            alunos.append(linha)
    return alunos


if __name__ == '__main__':
    alunos_lista = ler_planilha_alunos('alunos.csv')
    print(alunos_lista)
