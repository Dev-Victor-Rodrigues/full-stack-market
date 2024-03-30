"""
 Systema de adicionamento de produtos
"""

"""
 tempo = obter a qtd de protudos
 sacola = todos os produtos em sua array
"""
tempo = int(input("Digite quantos produtos serão adicionados"))
sacola_de_produtos = []

"""
um lop que adiciona os produtos no array, vai so ate a qtd que foi adicionada
"""
for Prod in range(1,tempo +1):
  nomes_dos_produtos = input("Digite nome dos  produtos :")
  sacola_de_produtos.append(nomes_dos_produtos)

 
"""
imprime a qtd de produtos, 
e nomes dos produtos na array
"""
print(f"Total de produtos adicionados {len(sacola_de_produtos)}")
print(f"produtos adicionados :{sacola_de_produtos} \n" )

"""
array para armazenar os preços
"""
preco_cada = []

"""
lop para adicionar os preço ao array
"""
for Prod in range(1,tempo +1):
  preco_produto = float(input("\nDigite Valor dos produtos :"))
  preco_cada.append(preco_produto)

"""
valores = a soma de todos os preço
"""
valores = sum(preco_cada)
print(f"Preço total {valores:.2f}")
