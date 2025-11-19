#RENAN BELEM BIAVATI

# Para obter os pontos relativos a este trabalho, você deverá fazer um programa, usando a linguagem de
# programação que desejar, que seja capaz de validar expressões de lógica propisicional escritas em latex e
# definir se são expressões gramaticalmente corretas.Você validará apenas a forma da expressão(sintaxe).
# A entrada será fornecida por um arquivo de textos que será carregado em linha de comando, com a seguinte
# formatação: 1. Na primeira linha deste arquivo existe um número inteiro que informa quantas expressões
# lógicas estão no arquivo. 2. Cada uma das linhas seguintes contém uma expressão lógica que deve servalidada.
# A saída do seu programa será no terminal padrão do sistema e constituirá de uma linha de saída para cada
# expressão lógica de entrada contendo ou a palavra valida ou a palavra inválida e nada mais.

# Gramática: Formula = Constante | Proposicao | FormulaUnaria | FormulaBinaria.
# Constante = "T" | "F".
# Proposicao = [a−z0−9]+
# FormulaUnaria = AbreParen OperadorUnario Formula FechaParen
# FormulaBinaria = AbreParen OperatorBinario Formula Formula FechaParen
# AbreParen = "("
# FechaParen = ")"
# OperatorUnario = "¬"
# OperatorBinario = "∨" | "∧" | "→" | "↔"

# Cada expressão lógica avaliada pode ter qualquer combinação das operações de negação, conjunção,
# disjunção, implicação e bi - implicação sem limites na combiação de preposições e operações. Os valores
# lógicos True e False estão representados na gramática e, como tal, podem ser usados em qualquer expressão
# de entrada. Para validar seu trabalho, você deve incluir no repl.it, no mínimo três arquivos contendo números
# diferentes de expressões proposicionais.O professor irá incluir um arquivo de testes extra para validar
# seu trabalho.Para isso, caberá ao professor incluir o arquivo no seu repl.it e rodar o seu
# programa carregando o arquivo de testes.

# \lnot = negação
# \lor = disjunção
# \land = conjunção
# \Rightarrow = implicação
# \Leftrightarrow = bimplicação

while True:
    print("----------------------------------------------------")
    opcao = input("Digite 1 para ler um arquivo  /  Digite qualquer coisa diferente de 1 para sair\n---> ")
    if opcao == "1":
        NomeArq = input("Digite o nome do arquivo que você deseja verificar a validez das expressões lógicas: ")

        arq = open(NomeArq)

        strings = arq.readlines()
        for i in strings:
            #impressão do numero de expressoes logicas
            if i[0] == str(len(strings)-1):
                print(i[0:len(i) - 1])

            else:
                #validez
                x = True
                #contadores de parenteses
                numParEsq = 0
                numParDir = 0

                for j in range(len(i)-1):
                    # condições de existencia do parenteses V
                    if i[j] == "(":
                        if i[j+2] != "(" and \
                            (len(i) <= 8 and (i[j+2]+i[j+3]+i[j+4]+i[j+5]+i[j+6])) != "\lnot" and \
                            i[j+2].isalnum() != True or \
                            (i[j - 1] != " " and i[j + 1] != " ") or \
                             i[j-2].isalnum() == True:
                            x = False

                    # condições de existencia da negação
                    if (j <= len(i) - 6 and (i[j]+i[j+1]+i[j+2]+i[j+3]+i[j+4]) == "\lnot") and \
                        i[j+6] != "(" and \
                        (j <= len(i) - 12 and (i[j+6]+i[j+7]+i[j+8]+i[j+9]+i[j+10]) != "\lnot") and \
                         i[j+6].isalnum() == False:
                        x = False

                    # condições de existencia da variavel
                    if i[j].isalnum() == True and j <= len(i)-3:
                        if i[j-2].isalnum() == True and i[j+2].isalnum() == True:
                            if i[j-1] == " " and i[j+1] == " ":
                               x = False

                    # condições de existencia da conjunçao
                    if j <= len(i) - 6:
                        if (i[j]+i[j+1]+i[j+2]+i[j+3]+i[j+4]) == "\land" and \
                            (j <= len(i) - 12 and (i[j+6]+i[j+7]+i[j+8]+i[j+9]+i[j+10])) != "\lnot" and \
                            i[j+6] != "(" and \
                             i[j+6].isalnum() == False:
                            x = False

                    # condições de existencia da disjunçao
                    if j <= len(i) - 5:
                        if (i[j]+i[j+1]+i[j+2]+i[j+3]) == "\lor" and \
                            (j <= len(i) - 12 and (i[j+5]+i[j+6]+i[j+7]+i[j+8]+i[j+9])) != "lnot" and \
                             i[j+5]!= "(" and \
                             i[j+5].isalnum() == False:
                            x = False

                    # condições de existencia da implicaçao
                    if j <= len(i) - 15:
                        if (i[j]+i[j+1]+i[j+2]+i[j+3]+i[j+4]+i[j+5]+i[j+6]+i[j+7]+i[j+8]+i[j+9]+i[j+10]+
                             i[j+11]) == "\Rightarrow" and \
                            (i[j + 13] + i[j + 14] + i[j + 15] + i[j + 16] + i[j + 17]) != "\lnot" and \
                            i[j + 13] != "(" and \
                             i[j + 13].isalnum() == False:
                            x = False

                    # condições de existencia da bimplicação
                    if j <= len(i) - 17:
                        if (i[j+1]+i[j+2]+i[j+3]+i[j+4]+i[j+5]+i[j+6]+i[j+7]+i[j+8]+i[j+9]+i[j+10]+
                             i[j+11]+i[j+12]+i[j+13]+i[j+14]+i[j+15]) == "\Leftrightarrow" and \
                            (i[j + 17] + i[j + 18] + i[j + 19] + i[j + 20] + i[j + 21]) != "\lnot" and \
                            i[j + 17] != "(" and \
                             i[j + 17].isalnum() == False:
                            x = False

                    #contador de parenteses
                    if i[j] == "(":
                        numParEsq += 1
                    if i[j] == ")":
                        numParDir += 1

                    #numero igual e par de parenteses
                    if j == len(i) - 2 and (numParEsq + numParDir) % 2 != 0 and numParEsq != numParDir:
                        x = False

                #validez com base na superação das condições
                if x is True:
                    if i == strings[len(strings)-1]:
                        print("válida!")
                    else:
                        print("válida!")

                else:
                    if i == strings[len(strings)-1]:
                        print("inválida!")
                    else:
                        print("inválida!")
    else:
        exit()