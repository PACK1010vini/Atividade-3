import pandas as pd
import os

arquivo_excel = "notas.xlsx"

def obter_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem).replace(",", ".")) 
            if 0 <= nota <= 10:
                return round(nota, 2)
            else:
                print("Erro: A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Erro: Entrada inválida. Digite um número.")

def salvar_em_excel(nome, notas):
    df_novo = pd.DataFrame([[nome] + notas], columns=["Nome", "N1", "N2", "N3"])
    
    if os.path.exists(arquivo_excel):
        df_existente = pd.read_excel(arquivo_excel)
        df_final = pd.concat([df_existente, df_novo], ignore_index=True)
    else:
        df_final = df_novo

    df_final.to_excel(arquivo_excel, index=False)
    print(f"Dados salvos em '{arquivo_excel}' com sucesso!")

def main():
    nome = input("Informe seu nome: ").strip()
    notas = [obter_nota(f"Informe a N{i+1}: ") for i in range(3)]
    salvar_em_excel(nome, notas)

if __name__ == "__main__":
    main()

