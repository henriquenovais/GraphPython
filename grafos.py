import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()  # Criando um grafo vazio

num_vertices = input("Número de vertices: ") #Solicita o numero de vertices
for x in range(int(num_vertices)): #Cria um laco com com a quantidade de vertices
    nome_vertices = input("Insira o nome do vértice de número " + str(x + 1) +" : ") #Solicita o nome do vertice x
    g.add_node(nome_vertices) #Cria um vertice graficamente

num_arestas = input("Insira o número de arestas: ") #Solicita o numero de ligacoes
for x in range(int(num_arestas)): #Cria um no com o tamanho das ligacoes
    print ("Ligação de número.", x + 1)
    first = input("Insira o vértice origem: ") #Solicita o no origem
    second = input("Insira o vértice destino: ")#Solicita o no destino
    #Exemplo: 3 vertices (A,B,C) com 2 ligacoes (B,A) e (B,C)
    g.add_edge(str(first), str(second))  # adicionando aresta

print("Feche a janela do grafo imprimido para prosseguir com o programa.") #Aviso ao usuário para quando esse desejar prosseguir com o programa
nx.draw(g, with_labels = True)
plt.show()

'''
O trecho de código a seguir será para a criação do menu através do qual o usuário
será capaz de realizar alterações no grafo ou realizar testes no grafo o qual gerou.
'''

print("Você deseja realizar testes e/ou alterações no grafo gerado?")
print("Digite 'tst' para abrir o menu de testes ou digite 'alt' para ser direcionado  ao menu de alterações.")
print("Digite 'end' para finalizar o programa.")
menu = input("Insira sua opção: ")

#Programação do menu:
if menu == "tst":
    #Acesso ao menu de testes
    print("Menu de testes")
elif menu == "alt":
    #Acesso ao menu de alterações
    print("Menu de alterações")
elif menu == "end":
    #Finalização do programa
    print("Programa encerrado.")
else:
    #Caso padrão(default), encerra o programa
    print("Caracteres não reconhecidos.")
    print("Programa encerrado.")
