import networkx as nx
import matplotlib.pyplot as plt

# Menu inicial

print("Para iniciar o programa, é necessário digitar o tipo de grafo que deseja criar, testar e manipular.")
print("Digite 'dir' para iniciar a criação de um grafo dirigido.")
print("Digite 'ndi' para iniciar a criação de um grafo não-dirigido.")
print("Digite 'pnd' para iniciar a criação de um grafo ponderado.")
tipo_gr = input("Qual tipo de grafo deseja criar? Digite a seguir: ")
tipo_gr = tipo_gr.lower()

if tipo_gr == 'pnd':
    # ----------------------------------------
    #           GRAFO PONDERADO
    # ----------------------------------------

    # -------------- DECLARAÇÃO DO GRAFO PONDERADO -----------

    print("Você escolheu criar um  grafo ponderado.")
    g = nx.Graph()  # Criando um grafo  vazio

    num_vertices = input("Número de vertices do seu grafo: ")  # Solicita o numero de vertices
    for x in range(int(num_vertices)):  # Cria um laco com com a quantidade de vertices
        nome_vertices = input(
            "Insira o nome do vértice de número " + str(x + 1) + " : ")  # Solicita o nome do vertice x
        g.add_node(nome_vertices)  # Cria um vertice graficamente

    num_arestas = input("Insira o número de arestas do seu grafo: ")  # Solicita o numero de ligacoes

    for x in range(int(num_arestas)):  # Cria um no com o tamanho das ligacoes
        print("Ligação de número.", x + 1)
        first = input("Insira o vértice origem: ")  # Solicita o no origem
        second = input("Insira o vértice destino: ")  # Solicita o no destino
        third = input("Insira o peso da aresta: ")
        # Exemplo: 3 vertices (A,B,C) com 2 ligacoes (B,A) e (B,C)
        g.add_edge(str(first), str(second), weight=float(third))

    # ------------ PROGRAMAÇÃO DO MENU DE ALTERAÇÕES/TESTES/PLOT ------------

    done = False
    while done == False:
        print("Como deseja proceder?")
        print("Digite 'plt' para visualizar(imprimir) o grafo criado.")
        print("Digite 'tst' para abrir o menu de testes.")
        print("Digite 'alt' para ser direcionado  ao menu de alterações.")
        print("Digite 'end' para finalizar o programa.")
        menu = input("Qual a sua opção? Digite a seguir: ")
        menu = menu.lower()
        # Programação do menu:
        if menu == "plt":
            # Visualização do grafo
            print("AVISO: Feche a janela do grafo impresso para prosseguir com o programa.")
            # Aviso ao usuário para quando esse desejar prosseguir com o programa
            input("Pressione qualquer tecla para continuar com o processo de visualização.")
            labels = nx.get_edge_attributes(g, 'weight')
            nx.draw_networkx_edge_labels(g, pos=nx.spring_layout(g), edge_labels=labels)
            nx.draw(g, with_labels=True)
            print("AVISO: Feche a janela do grafo impresso para prosseguir com o programa.")
            plt.show()
        elif menu == "tst":
            # Acesso ao menu de testes
            print("-- Menu de testes --")
            print("Digite 'tar' para testar a existencia de arestas.")
            print("Digite 'adj' para exibir os vertices adjacentes a um vertice X.")
            print("Digite 'gra' para exibir o grau de um vertice X.")
            print("Digite 'grx' para exibir o grau minimo, maximo e medio de um vertice X.")
            print("Digite 'gcx' para descobrir se o grafo e conexo.")
            print("Digite 'madj' para exibir a matriz adjacencia.")
            print("Digite 'euler' para verificar se há caminho de Euler.")
            test_menu = input("Qual a sua opção? Digite a seguir: ")
            if test_menu == "tar":
                print("Vertices disponiveis: ", g.node())
                print("Digite o nome dos vertices para saber se há uma aresta entre eles: ")
                vertice_1 = input("Primeiro vertice: ")
                vertice_2 = input("Segundo vertice: ")
                if g.number_of_edges(vertice_1, vertice_2) > 0:
                    print("Existe uma aresta entre os vertices!")
                else:
                    print("Nao existe uma aresta entre os vertices!")
            elif test_menu == "adj":
                print("Vertices disponiveis: ", g.node())
                print("Digite o nome do vertice para descobrir seus adjacentes: ")
                vertice = input("Nome do vertice: ")
                print(list(g.neighbors(vertice)))
            elif test_menu == "gra":
                print("Vertices disponiveis: ", g.node())
                print("Digite o nome do vertice para descobrir seu grau: ")
                vertice = input("Nome do vertice: ")
                print("Grau do vertice '" + str(vertice) + "' : ", g.degree(vertice))
            elif test_menu == "grx":
                print(max(g.degree()))
                print(min(g.degree()))
                print((nx.number_of_nodes(g) * 2) / nx.number_of_edges(g))
            elif test_menu == "gcx":
                if nx.is_connected(g) == True:
                    print("O grafo e conexo!")
                elif nx.is_connected(g) == False:
                    print("O grafo nao e conexo!")
            elif test_menu == "madj":
                print("Matriz adjacencia:")
                print(nx.to_numpy_matrix(g))
            elif test_menu == "euler":
                if nx.is_eulerian(g) == True:
                    print("Existe caminho de Euler!")
                else:
                    print("Nao existe caminho de Euler")
        elif menu == "alt":
            # Acesso ao menu de alterações
            print("-- Menu de alterações --")
            print("Digite 'nve' para inserir um novo vertice.")
            print("Digite 'rve' para remover um vertice.")
            print("Digite 'nar' para inserir uma aresta entre dois vertices.")
            print("Digite 'rar' para remover uma aresta entre dois vertices.")
            alt_menu = input("Qual a sua opção? Digite a seeguir: ")
            if alt_menu == "nve":
                print("Vertices disponiveis: ", g.node())
                novo_vertice = input("Insira o nome do novo vertice: ")
                g.add_node(novo_vertice)
                print("Vertices disponiveis apos adicao: ", g.node())
            elif alt_menu == "rve":
                print("Vertices disponiveis: ", g.node())
                remove_vertice = input("Insira o nome do vertice que deseja remover: ")
                g.remove_node(remove_vertice)
                print("Vertices disponiveis apos remocao: ", g.node())
            elif alt_menu == "nar":
                print("Arestas existentes: ", g.edges())
                print("Vertices disponiveis: ", g.node())
                first = input("Insira o nome do primeiro vertice que ligar: ")
                second = input("Insira o nome do segundo vertice que ligar: ")
                g.add_weighted_edges_from([(str(first), str(second), 1)])
                print("Arestas existentes apos nova ligacao: ", g.edges())
            elif alt_menu == "rar":
                print("Arestas existentes: ", g.edges())
                print("Vertices disponiveis: ", g.node())
                first = input("Insira o nome do primeiro vertice que remover ligacao: ")
                second = input("Insira o nome do segundo vertice que remover ligacao: ")
                g.remove_edges_from([(str(first), str(second), 1)])
                print("Arestas existentes apos remover ligacao: ", g.edges())
        elif menu == "end":
            # Finalização do programa
            print("Programa encerrado.")
            done = True
        else:
            # Caso padrão(default), encerra o programa
            print("Caracteres não reconhecidos.")
            print("Programa encerrado.")
            done = True

    # ----------------------------------------
    #               FIM
    #           GRAFO PONDERADO
    # ----------------------------------------

if tipo_gr == 'dir':
    # ----------------------------------------
    #           GRAFO DIRECIONAL
    # ----------------------------------------

    # -------------- DECLARAÇÃO DO GRAFO DIRECIONAL -----------

    print("Você escolheu criar um  grafo direcional.")
    g = nx.DiGraph()  # Criando um grafo  vazio

    num_vertices = input("Número de vertices do seu grafo: ")  # Solicita o numero de vertices
    for x in range(int(num_vertices)):  # Cria um laco com com a quantidade de vertices
        nome_vertices = input(
            "Insira o nome do vértice de número " + str(x + 1) + " : ")  # Solicita o nome do vertice x
        g.add_node(nome_vertices)  # Cria um vertice graficamente

    num_arestas = input("Insira o número de arestas do seu grafo: ")  # Solicita o numero de ligacoes

    for x in range(int(num_arestas)):  # Cria um no com o tamanho das ligacoes
        print("Ligação de número.", x + 1)
        first = input("Insira o vértice origem: ")  # Solicita o no origem
        second = input("Insira o vértice destino: ")  # Solicita o no destino
        # Exemplo: 3 vertices (A,B,C) com 2 ligacoes (B,A) e (B,C)
        g.add_weighted_edges_from([(str(first), str(second), 1)])  # adicionando aresta

    # -------------- PROGRAMAÇÃO MENU DE ALTERAÇÕES/TESTES/PLOT -----------

    done = False
    while done == False:
        print("Como deseja proceder?")
        print("Digite 'plt' para visualizar(imprimir) o grafo criado.")
        print("Digite 'tst' para abrir o menu de testes.")
        print("Digite 'alt' para ser direcionado  ao menu de alterações.")
        print("Digite 'end' para finalizar o programa.")
        menu = input("Qual a sua opção? Digite a seguir: ")
        menu = menu.lower()
        # Programação do menu:
        if menu == "plt":
            # Visualização do grafo
            print("AVISO: Feche a janela do grafo impresso para prosseguir com o programa.")
            # Aviso ao usuário para quando esse desejar prosseguir com o programa
            input("Pressione qualquer tecla para continuar com o processo de visualização.")
            nx.draw(g, with_labels=True)
            print("AVISO: Feche a janela do grafo impresso para prosseguir com o programa.")
            plt.show()
        elif menu == "tst":
            print("-- Menu de testes --")
            print("Digite 'tar' para testar a existencia de arestas.")
            print("Digite 'adj' para exibir os vertices adjacentes a um vertice X.")
            print("Digite 'gra' para exibir o grau de um vertice X.")
            print("Digite 'grx' para exibir o grau minimo, maximo e medio de um vertice X.")
            print("Digite 'gcx' para descobrir se o grafo e conexo.")
            print("Digite 'madj' para exibir a matriz adjacencia.")
            print("Digite 'euler' para verificar se há caminho de Euler.")
            test_menu = input("Qual a sua opção? Digite a seguir: ")
            if test_menu == "tar":
                print("Vertices disponiveis: ", g.node())
                print("Digite o nome dos vertices para saber se há uma aresta entre eles: ")
                vertice_1 = input("Primeiro vertice: ")
                vertice_2 = input("Segundo vertice: ")
                if g.number_of_edges(vertice_1, vertice_2) > 0:
                    print("Existe uma aresta entre os vertices!")
                else:
                    print("Nao existe uma aresta entre os vertices!")
            elif test_menu == "adj":
                print("Vertices disponiveis: ", g.node())
                print("Digite o nome do vertice para descobrir seus adjacentes: ")
                vertice = input("Nome do vertice: ")
                print(list(g.neighbors(vertice)))
            elif test_menu == "gra":
                print("Vertices disponiveis: ", g.node())
                print("Digite o nome do vertice para descobrir seu grau: ")
                vertice = input("Nome do vertice: ")
                print("Grau do vertice '" + str(vertice) + "' : ", g.degree(vertice))
            elif test_menu == "grx":
                print(max(list(nx.number_of_nodes(g))))
                print(min(list(nx.number_of_nodes(g))))
                print(len(g.degree()))
                print(g.size())
                print(g.size() * 2 / len(g.degree()))
            elif test_menu == "gcx":
                if nx.is_connected(g) == True:
                    print("O grafo e conexo!")
                elif nx.is_connected(g) == False:
                    print("O grafo nao e conexo!")
            elif test_menu == "madj":
                print("Matriz adjacencia:")
                print(nx.to_numpy_matrix(g))
            elif test_menu == "euler":
                if nx.is_eulerian(g) == True:
                    print("Existe caminho de Euler!")
                else:
                    print("Nao existe caminho de Euler")
        elif menu == "alt":
            # Acesso ao menu de alterações
            print("-- Menu de alterações --")
            print("Digite 'nve' para inserir um novo vertice.")
            print("Digite 'rve' para remover um vertice.")
            print("Digite 'nar' para inserir uma aresta entre dois vertices.")
            print("Digite 'rar' para remover uma aresta entre dois vertices.")
            alt_menu = input("Qual a sua opção? Digite a seeguir: ")
            if alt_menu == "nve":
                print("Vertices disponiveis: ", g.node())
                novo_vertice = input("Insira o nome do novo vertice: ")
                g.add_node(novo_vertice)
                print("Vertices disponiveis apos adicao: ", g.node())
            elif alt_menu == "rve":
                print("Vertices disponiveis: ", g.node())
                remove_vertice = input("Insira o nome do vertice que deseja remover: ")
                g.remove_node(remove_vertice)
                print("Vertices disponiveis apos remocao: ", g.node())
            elif alt_menu == "nar":
                print("Arestas existentes: ", g.edges())
                print("Vertices disponiveis: ", g.node())
                first = input("Insira o nome do primeiro vertice que ligar: ")
                second = input("Insira o nome do segundo vertice que ligar: ")
                g.add_weighted_edges_from([(str(first), str(second), 1)])
                print("Arestas existentes apos nova ligacao: ", g.edges())
            elif alt_menu == "rar":
                print("Arestas existentes: ", g.edges())
                print("Vertices disponiveis: ", g.node())
                first = input("Insira o nome do primeiro vertice que remover ligacao: ")
                second = input("Insira o nome do segundo vertice que remover ligacao: ")
                g.remove_edges_from([(str(first), str(second), 1)])
                print("Arestas existentes apos remover ligacao: ", g.edges())
        elif menu == "end":
            # Finalização do programa
            print("Programa encerrado.")
            done = True
        else:
            # Caso padrão(default), encerra o programa
            print("Caracteres não reconhecidos.")
            print("Programa encerrado.")
            done = True
    # ----------------------------------------
    #                 FIM
    #           GRAFO DIRECIONAL
    # ----------------------------------------

elif tipo_gr == 'ndi':
    print("Você escolheu criar um  grafo não-direcional.")
    # ----------------------------------------
    #           GRAFO NÃO-DIRECIONAL
    # ----------------------------------------

    # -------------- DECLARAÇÃO DO GRAFO DIRECIONAL -----------

    g = nx.Graph()  # Criando um grafo  vazio

    num_vertices = input("Número de vertices do seu grafo: ")  # Solicita o numero de vertices
    for x in range(int(num_vertices)):  # Cria um laco com com a quantidade de vertices
        nome_vertices = input(
            "Insira o nome do vértice de número " + str(x + 1) + " : ")  # Solicita o nome do vertice x
        g.add_node(nome_vertices)  # Cria um vertice graficamente

    num_arestas = input("Insira o número de arestas do seu grafo: ")  # Solicita o numero de ligacoes

    for x in range(int(num_arestas)):  # Cria um no com o tamanho das ligacoes
        print("Ligação de número.", x + 1)
        first = input("Insira o vértice origem: ")  # Solicita o no origem
        second = input("Insira o vértice destino: ")  # Solicita o no destino
        # Exemplo: 3 vertices (A,B,C) com 2 ligacoes (B,A) e (B,C)
        g.add_edge(str(first), str(second))  # adicionando aresta

    # -------------- PROGRAMAÇÃO MENU DE ALTERAÇÕES/TESTES/PLOT -----------

    done = False
    while done == False:
        print("Como deseja proceder?")
        print("Digite 'plt' para visualizar(imprimir) o grafo criado.")
        print("Digite 'tst' para abrir o menu de testes.")
        print("Digite 'alt' para ser direcionado  ao menu de alterações.")
        print("Digite 'end' para finalizar o programa.")
        menu = input("Qual a sua opção? Digite a seguir: ")
        menu = menu.lower()
        # Programação do menu:
        if menu == "plt":
            # Visualização do grafo
            print("AVISO: Feche a janela do grafo impresso para prosseguir com o programa.")
            # Aviso ao usuário para quando esse desejar prosseguir com o programa
            input("Pressione qualquer tecla para continuar com o processo de visualização.")
            nx.draw(g, with_labels=True)
            print("AVISO: Feche a janela do grafo imprimido para prosseguir com o programa.")
            plt.show()
        elif menu == "tst":
            # Acesso ao menu de testes
            print("-- Menu de testes --")
            print("Digite 'tar' para testar a existencia de arestas.")
            print("Digite 'adj' para exibir os vertices adjacentes a um vertice X.")
            print("Digite 'gra' para exibir o grau de um vertice X.")
            print("Digite 'grx' para exibir o grau minimo, maximo e medio de um vertice X.")
            print("Digite 'gcx' para descobrir se o grafo e conexo.")
            print("Digite 'madj' para exibir a matriz adjacencia.")
            print("Digite 'euler' para verificar se há caminho de Euler.")
            test_menu = input("Qual a sua opção? Digite a seguir: ")
            if test_menu == "tar":
                print("Vertices disponiveis: ", g.node())
                print("Digite o nome dos vertices para saber se há uma aresta entre eles: ")
                vertice_1 = input("Primeiro vertice: ")
                vertice_2 = input("Segundo vertice: ")
                if g.number_of_edges(vertice_1, vertice_2) > 0:
                    print("Existe uma aresta entre os vertices!")
                else:
                    print("Nao existe uma aresta entre os vertices!")
            elif test_menu == "adj":
                print("Vertices disponiveis: ", g.node())
                print("Digite o nome do vertice para descobrir seus adjacentes: ")
                vertice = input("Nome do vertice: ")
                print (list(g.neighbors(vertice)))
            elif test_menu == "gra":
                print("Vertices disponiveis: ", g.node())
                print("Digite o nome do vertice para descobrir seu grau: ")
                vertice = input("Nome do vertice: ")
                print("Grau do vertice '" + str(vertice)+"' : ", g.degree(vertice))
            elif test_menu == "grx":
                print(max(g.degree()))
                print(min(g.degree()))
                print(((nx.number_of_edges(g) * 2)) / nx.number_of_nodes(g))
            elif test_menu == "gcx":
                if nx.is_connected(g) == True:
                    print("O grafo e conexo!")
                elif nx.is_connected(g) == False:
                    print("O grafo nao e conexo!")
            elif test_menu == "madj":
                print("Matriz adjacencia:")
                print(nx.to_numpy_matrix(g))
            elif test_menu == "euler":
                if nx.is_eulerian(g) == True:
                    print("Existe caminho de Euler!")
                else:
                    print("Nao existe caminho de Euler")
        elif menu == "alt":
            # Acesso ao menu de alterações
            print("-- Menu de alterações --")
            print("Digite 'nve' para inserir um novo vertice.")
            print("Digite 'rve' para remover um vertice.")
            print("Digite 'nar' para inserir uma aresta entre dois vertices.")
            print("Digite 'rar' para remover uma aresta entre dois vertices.")
            alt_menu = input("Qual a sua opção? Digite a seeguir: ")
            if alt_menu == "nve":
                print("Vertices disponiveis: ", g.node())
                novo_vertice = input("Insira o nome do novo vertice: ")
                g.add_node(novo_vertice)
                print("Vertices disponiveis apos adicao: ", g.node())
            elif alt_menu == "rve":
                print("Vertices disponiveis: ", g.node())
                remove_vertice = input("Insira o nome do vertice que deseja remover: ")
                g.remove_node(remove_vertice)
                print("Vertices disponiveis apos remocao: ", g.node())
            elif alt_menu == "nar":
                print("Arestas existentes: ", g.edges())
                print("Vertices disponiveis: ", g.node())
                first = input("Insira o nome do primeiro vertice que ligar: ")
                second = input("Insira o nome do segundo vertice que ligar: ")
                g.add_weighted_edges_from([(str(first), str(second), 1)])
                print("Arestas existentes apos nova ligacao: ", g.edges())
            elif alt_menu == "rar":
                print("Arestas existentes: ", g.edges())
                print("Vertices disponiveis: ", g.node())
                first = input("Insira o nome do primeiro vertice que remover ligacao: ")
                second = input("Insira o nome do segundo vertice que remover ligacao: ")
                g.remove_edges_from([(str(first), str(second), 1)])
                print("Arestas existentes apos remover ligacao: ", g.edges())
        elif menu == "end":
            # Finalização do programa
            print("Programa encerrado.")
            done = True
        else:
            # Caso padrão(default), encerra o programa
            print("Caracteres não reconhecidos.")
            print("Programa encerrado.")
            done = True

    # ----------------------------------------
    #                 FIM
    #           GRAFO NÃO DIRECIONAL
    # ----------------------------------------




else:
    print("Input não reconhecido.")
    print("Encerrando o programa.")

# Adicionar print("\n \n") nos menus.
