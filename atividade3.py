#receber 4 notas e mostrar a média no final

primeiro_Semestre = int(input('Digite a nota do primeiro semestre)'))
segundo_Semestre = int(input('Digite a nota do segundo semestre)'))
terceiro_Semestre = int(input('Digite a nota do terceiro semestre)'))
quarto_Semestre = int(input('Digite a nota do quarto semestre)'))
media = (primeiro_Semestre+segundo_Semestre+terceiro_Semestre+quarto_Semestre) /4
print(f'A média é: {media}')
