nome_empresa = input("Informe o nome da Empresa: ")
contacao = float(input("Digite a cotação da empresa: "))

valor_dobrado = contacao * 2
caiu_50 = contacao/2
print(f"O nome da empresa é: {nome_empresa}")
print(f"Caso a empresa suba 100% a cotação será de {valor_dobrado}")
print(f"Caso a empresa caia 50%, o valor da cotação fica: {caiu_50}")
print(type(nome_empresa))
print("Aprendendo a enviar para o git")