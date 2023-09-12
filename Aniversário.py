from datetime import datetime



data_atual = datetime.now()
data_de_aniversario = datetime.strptime(input('Qual é a data do seu aniversário? '),'%d/%m/%Y')
dias_ate_aniversario = data_de_aniversario - data_atual
dias_ate_aniversario = str(dias_ate_aniversario)

print(f'Faltam {dias_ate_aniversario[:3]} dias')