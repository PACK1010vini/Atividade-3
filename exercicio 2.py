import pandas as pd

def calcular_media(notas):
    try:
        return round(sum(map(float, notas)) / len(notas), 2)
    except ValueError:
        print(f"Erro ao converter notas: {notas}")
        return None

def classificar_aluno(nome, media):
    if media is None:
        return "Erro"
    elif media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Exame"
    else:
        return "Reprovado"

def processar_notas(arquivo_entrada, arquivo_saida):
    try:
        with open(arquivo_entrada, 'r') as arquivo:
            alunos = arquivo.readlines()

        dados = []

        for linha in alunos:
            aluno = linha.strip().split(",")
            if len(aluno) != 4:
                print(f"Formato inválido na linha: {linha}")
                continue

            nome = aluno[0].strip()
            notas = aluno[1:]

            media = calcular_media(notas)
            status = classificar_aluno(nome, media)

            dados.append([nome, media, status])

        df = pd.DataFrame(dados, columns=["Nome", "Média", "Status"])
        df.to_excel(arquivo_saida, index=False)
        print(f"Arquivo '{arquivo_saida}' gerado com sucesso!")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_entrada}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

processar_notas("notas.txt", "resultados.xlsx")

