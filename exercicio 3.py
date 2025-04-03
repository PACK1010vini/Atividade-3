import pandas as pd

def ler_arquivo(nome_arquivo):
    try:
        return pd.read_excel(nome_arquivo)
    except FileNotFoundError:
        print(f"Erro: O arquivo {nome_arquivo} não foi encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None

def calcular_media(nota1, nota2):
    return round((nota1 + nota2) / 2, 2)

def solicitar_exame(alunos):
    aprovados = []
    reprovados = []

    for _, aluno in alunos.iterrows():
        try:
            nome = aluno['Nome']
            nota = float(aluno['Nota'])
            
            exame = float(input(f"Informe a nota do exame do aluno {nome}: "))
            media = calcular_media(nota, exame)
            
            status = "Aprovado após exame" if media >= 5 else "Reprovado após exame"
            resultado = [nome, media, status]

            (aprovados if media >= 5 else reprovados).append(resultado)
        
        except ValueError:
            print(f"Erro: Nota inválida para o aluno {aluno['Nome']}. Pulando...")
        except KeyError:
            print("Erro: O arquivo deve conter colunas 'Nome' e 'Nota'.")
            return None, None

    return aprovados, reprovados

def salvar_resultados(nome_arquivo, dados):
    df = pd.DataFrame(dados, columns=['Nome', 'Média', 'Status'])
    df.to_excel(nome_arquivo, index=False)

def main():
    nome_arquivo = "exame.xlsx"
    alunos = ler_arquivo(nome_arquivo)

    if alunos is not None:
        aprovados, reprovados = solicitar_exame(alunos)

        if aprovados:
            salvar_resultados("aprovados.xlsx", aprovados)
        if reprovados:
            salvar_resultados("reprovados.xlsx", reprovados)

        print("Processo concluído! Resultados salvos em 'aprovados.xlsx' e 'reprovados.xlsx'.")

if __name__ == "__main__":
    main()

