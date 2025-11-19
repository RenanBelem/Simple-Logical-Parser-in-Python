## Verificador de Sintaxe de Lógica Proposicional (Parser)

Este projeto em Python implementa um verificador de sintaxe para expressões de Lógica Proposicional, escritas em um formato similar ao LaTeX. O objetivo é determinar se a **forma** (gramática) de uma expressão está correta, sem avaliar sua semântica ou valor lógico.

### Linguagem Formal (Gramática)

O programa tenta validar expressões com base na seguinte Gramática Formal (dada no código):

| Componente | Regras |
| :--- | :--- |
| **`Formula`** | `Constante` | `Proposicao` | `FormulaUnaria` | `FormulaBinaria` |
| **`Constante`** | `"T"` (True) | `"F"` (False) |
| **`Proposicao`** | Sequência alfanumérica: `[a-z0-9]+` |
| **`FormulaUnaria`** | `AbreParen` `OperadorUnario` `Formula` `FechaParen` |
| **`FormulaBinaria`** | `AbreParen` `OperadorBinario` `Formula` `Formula` `FechaParen` |
| **`AbreParen`** | `(` |
| **`FechaParen`** | `)` |
| **`OperadorUnario`** | $\neg$ (Negação) |
| **`OperadorBinario`** | $\lor$ (Disjunção) | $\land$ (Conjunção) | $\to$ (Implicação) | $\leftrightarrow$ (Bimplicação) |

### Representação dos Operadores (Input)

Os operadores lógicos no arquivo de entrada são representados por sequências de caracteres (LaTeX):

| Operador Lógico | Representação em *String* (Código) |
| :--- | :--- |
| $\neg$ (Negação) | `\lnot` |
| $\lor$ (Disjunção) | `\lor` |
| $\land$ (Conjunção) | `\land` |
| $\to$ (Implicação) | `\Rightarrow` |
| $\leftrightarrow$ (Bimplicação) | `\Leftrightarrow` |

### Estrutura e Lógica do Parser (`main.py`)

O código Python executa uma análise sequencial (caractere a caractere ou por *sub-strings*) e utiliza *flags* e contadores para validar a sintaxe da expressão:

1.  **Entrada Interativa:** O programa roda em um *loop* `while True` e solicita ao usuário o nome do arquivo de entrada.
2.  **Leitura do Arquivo:** Lê todas as linhas do arquivo, tratando a primeira linha como o número de expressões, conforme o formato de entrada esperado.
3.  **Contagem de Parênteses:** Mantém a contagem de parênteses de abertura (`numParEsq`) e fechamento (`numParDir`) para garantir que:
      * O número de parênteses esquerdo seja igual ao direito (`numParEsq != numParDir`).
      * O total de parênteses seja par (`(numParEsq + numParDir) % 2 != 0`).
4.  **Verificações de Contexto (Condições de Existência):** O *parser* usa verificações de *substring* para garantir que operadores e elementos estejam no contexto gramatical correto:
      * **Operadores Unários/Binários:** Verifica se o operador está seguido por um elemento válido (como `(`, `\lnot`, ou uma proposição alfanumérica `isalnum() == True`). Se o operador for seguido por algo que não seja um novo parêntese, uma negação, ou uma proposição, ele marca a expressão como inválida (`x = False`).
      * **Proposições/Variáveis:** Verifica se as proposições alfanuméricas não estão adjacentes a outras proposições sem um operador binário entre elas (embora a lógica focada em espaços não seja estritamente gramatical).
      * **Parenteses:** Tenta verificar se o parêntese de abertura é seguido por algo que não seja um operador unário ou uma proposição.

### Formato de Entrada Esperado

O programa espera um arquivo de texto formatado da seguinte maneira:

1.  **Linha 1:** Um número inteiro indicando a quantidade de expressões lógicas no arquivo.
2.  **Linhas Seguintes:** Cada linha contém uma expressão lógica a ser validada.

### Formato de Saída

A saída do programa para cada expressão lida é enviada para o console, indicando o resultado da validação sintática:

```
válida!
```

ou

```
inválida!
```
