import networkx as nx
import matplotlib.pyplot as plt

#Menu inicial

print("Para iniciar o programa, é necessário digitar o tipo de grafo que deseja criar, testar e manipular.")
print("Digite 'dir' para iniciar a criação de um grafo dirigido.")
print("Digite 'ndi' para iniciar a criação de um grafo não-dirigido.")
tipo_gr = input("Qual tipo de grafo deseja criar? Digite a seguir: ")
tipo_gr = tipo_gr.lower()
if tipo_gr == 'dir':
    #----------------------------------------
    #           GRAFO DIRECIONAL
    #----------------------------------------
    print("Você escolheu criar um  grafo direcional.")
    g = nx.DiGraph()  # Criando um grafo  vazio

    num_vertices = input("Número de vertices do seu grafo: ") #Solicita o numero de vertices
    for x in range(int(num_vertices)): #Cria um laco com com a quantidade de vertices
        nome_vertices = input("Insira o nome do vértice de número " + str(x + 1) +" : ") #Solicita o nome do vertice x
        g.add_node(nome_vertices) #Cria um vertice graficamente

    num_arestas = input("Insira o número de arestas do seu grafo: ") #Solicita o numero de ligacoes

    for x in range(int(num_arestas)): #Cria um no com o tamanho das ligacoes
        print ("Ligação de número.", x + 1)
        first = input("Insira o vértice origem: ") #Solicita o no origem
        second = input("Insira o vértice destino: ")#Solicita o no destino
        #Exemplo: 3 vertices (A,B,C) com 2 ligacoes (B,A) e (B,C)
        g.add_weighted_edges_from(str(first), str(second),1)  # adicionando aresta
    
    
    print("Como deseja proceder?")
    print("Digite 'plt' para visualizar(imprimir) o grafo criado.")
    print("Digite 'tst' para abrir o menu de testes.")
    print("Digite 'alt' para ser direcionado  ao menu de alterações.")
    print("Digite 'end' para finalizar o programa.")
    menu = input("Qual a sua opção? Digite a seguir: ")
    menu = menu.lower()
    #Programação do menu:
    if menu == "plt":
        #Visualização do grafo
        print("AVISO: Feche a janela do grafo imprimido para prosseguir com o programa.")
        #Aviso ao usuário para quando esse desejar prosseguir com o programa
        input("Pressione qualquer tecla para continuar com o processo de visualização.") 
        nx.draw(g, with_labels = True)
        print("AVISO: Feche a janela do grafo imprimido para prosseguir com o programa.")
        plt.show()
    elif menu == "tst":
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
    #----------------------------------------
    #                 FIM
    #           GRAFO DIRECIONAL
    #----------------------------------------

elif tipo_gr == 'ndi':
    print("Você escolheu criar um  grafo não-direcional.")
    #----------------------------------------
    #           GRAFO NÃO DIRECIONAL
    #----------------------------------------
    g = nx.Graph()  # Criando um grafo  vazio

    num_vertices = input("Número de vertices do seu grafo: ") #Solicita o numero de vertices
    for x in range(int(num_vertices)): #Cria um laco com com a quantidade de vertices
        nome_vertices = input("Insira o nome do vértice de número " + str(x + 1) +" : ") #Solicita o nome do vertice x
        g.add_node(nome_vertices) #Cria um vertice graficamente

    num_arestas = input("Insira o número de arestas do seu grafo: ") #Solicita o numero de ligacoes

    for x in range(int(num_arestas)): #Cria um no com o tamanho das ligacoes
        print ("Ligação de número.", x + 1)
        first = input("Insira o vértice origem: ") #Solicita o no origem
        second = input("Insira o vértice destino: ")#Solicita o no destino
        #Exemplo: 3 vertices (A,B,C) com 2 ligacoes (B,A) e (B,C)
        g.weighted_add_edge(str(first), str(second))  # adicionando aresta
    
    
    print("Como deseja proceder?")
    print("Digite 'plt' para visualizar(imprimir) o grafo criado.")
    print("Digite 'tst' para abrir o menu de testes.")
    print("Digite 'alt' para ser direcionado  ao menu de alterações.")
    print("Digite 'end' para finalizar o programa.")
    menu = input("Qual a sua opção? Digite a seguir: ")
    menu = menu.lower()
    #Programação do menu:
    if menu == "plt":
        #Visualização do grafo
        print("AVISO: Feche a janela do grafo imprimido para prosseguir com o programa.")
        #Aviso ao usuário para quando esse desejar prosseguir com o programa
        input("Pressione qualquer tecla para continuar com o processo de visualização.") 
        nx.draw(g, with_labels = True)
        print("AVISO: Feche a janela do grafo imprimido para prosseguir com o programa.")
        plt.show()
    elif menu == "tst":
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

    #----------------------------------------
    #                 FIM
    #           GRAFO NÃO DIRECIONAL
    #----------------------------------------
    



else:
    print("Input não reconhecido.")
    print("Encerrando o programa.")
'''
print("Feche a janela do grafo imprimido para prosseguir com o programa.") #Aviso ao usuário para quando esse desejar prosseguir com o programa
nx.draw(g, with_labels = True)
plt.show()
'''

'''
O trecho de código a seguir será para a criação do menu através do qual o usuário
será capaz de realizar alterações no grafo ou realizar testes no grafo o qual gerou.
'''
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
'''
'''
g = nx.DiGraph()
g.add_weighted_edges_from([(1,2,0.5), (3,1,0.75)])


nx.draw(g, with_labels = True)
plt.show()
'''