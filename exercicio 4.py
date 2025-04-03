import pandas as pd

def ler_alunos(arquivo):
    try:
        with open(arquivo, 'r') as f:
            alunos = [linha.strip().split(',') for linha in f.readlines()]
        return alunos
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
        return []
    except Exception as e:
        print(f"Erro ao ler '{arquivo}': {e}")
        return []

def exibir_alunos(tipo, alunos):
    print(f"\nAlunos {tipo}:")
    for nome, nota in alunos:
        print(f"Aluno: {nome} | NF: {float(nota):.2f}")

def salvar_em_xlsx(aprovados, reprovados):
    try:
        df_aprovados = pd.DataFrame(aprovados, columns=["Nome", "Nota"])
        df_reprovados = pd.DataFrame(reprovados, columns=["Nome", "Nota"])
        
        with pd.ExcelWriter("resultados.xlsx") as writer:
            df_aprovados.to_excel(writer, sheet_name="Aprovados", index=False)
            df_reprovados.to_excel(writer, sheet_name="Reprovados", index=False)

        print("\nDados salvos em 'resultados.xlsx'!")
    except Exception as e:
        print(f"Erro ao salvar em Excel: {e}")

aprovados = ler_alunos("aprovados.txt")
reprovados = ler_alunos("reprovados.txt")

exibir_alunos("Aprovados", aprovados)
exibir_alunos("Reprovados", reprovados)

salvar_em_xlsx(aprovados, reprovados)
