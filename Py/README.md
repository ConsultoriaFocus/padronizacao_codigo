- Menu
  - [Nome](#nome)
  - [Limite de char](#limite-de-char)
  - [Parenteses](#parenteses)
  - [Identação](#identação)
  - [Expaços](#expaços)
  - [Comentarios](#comentarios)
  - [Import](#import)
  - [Venv](#venv)

## Nome

| Type                       | Public               | Internal              |
| :------------------------- | :------------------- | :-------------------- |
| Packages                   | `lower_with_under`   |                       |
| Modules                    | `lower_with_under`   | `_lower_with_under`   |
| Classes                    | `CapWords`           | `_CapWords`           |
| Exceptions                 | `CapWords`           |                       |
| Functions                  | `lower_with_under()` | `_lower_with_under()` |
| Global/Class Constants     | `CAPS_WITH_UNDER`    | `_CAPS_WITH_UNDER`    |
| Global/Class Variables     | `lower_with_under`   | `_lower_with_under`   |
| Instance Variables         | `lower_with_under`   | `_lower_with_under`   |
| Method Names               | `lower_with_under()` | `_lower_with_under()` |
| Function/Method Parameters | `lower_with_under`   |                       |
| Local Variables            | `lower_with_under `  |                       |

## Limite de char

evite linhas com mais de 80 caracteres

## Parenteses

use com moderação

nao use parenteses em return e condicionais
anao ser que estaja retornando uma tupla

```py
    #Sim
    if foo:
        bar()
    while x:
        x = bar()
    if x and y:
        bar()
    return foo
    return spam, beans
    return (spam, beans)
```

```py
    #Nao
    if(x):
      bar()
    if not(x):
      bar()
    return (foo)
```

## Identação

use 4 espaços para identar
<br/>
Nao use Tab, pois pode perder facilmente a identação ao mudar de editor

```py
    # se precisar quebrar a linha
    # defina a variavel na linha de baixo
    # e use 4 espaços
    foo = long_function_name(
        var_one, var_two, var_three,
        var_four
    )
    meal = (
        spam,
        beans,
    )
    foo = {
        'long_dictionary_key':
            long_dictionary_value
    }
```

não use `,` no ultimo elemento de alguma lista, dicionario ou tupla

```py
    lista1 = ["valor1", "valor2"]
    lista2 = [
        "valor1",
        "valor2"
    ]
    dicionario = {
        "key1": 1,
        "key2": 2
    }
    tupla = (
        "valor1",
        "valor2"
    )
```

## Expaços

Não use dentro de `[]`, `{}`, `()`

```py
    #Sim
    spam(ham[1], {'eggs': 2}, [])
    #Nao
    spam( ham[ 1 ], { 'eggs': 2 }, [ ] )
```

Não use antes de `()` ou `[]`

```py
    #Sim
    spam(1)
    lista[0]
    #Nao
    spam (1)
    lista [ 0 ]
```

Não use ao redor de operadores

```py
    #Sim
    if x <= 1:
        pass
    #Nao
    if x<=1:
        pass
```

Não use espaço em `=` ao passar um argumento

```py
    #Sim
    def num_imaginario(real, imag=0): return Imag(r=real, i=imag)
    #Nao
    def num_imaginario(real, imag = 0): return Imag(r = real, i = imag)
```

não use espaço para alinhar `=`, `:`, `#`, no codigo

```py
  idade = 10  # comentario
  nome_completo = "Pedro"  # comentario nao alinhado

  dicionario = {
      'idade': 12,
      'nome_completo': "Ana",
  }
  # Nao alinhe
  idade         = 10      # comentario
  nome_completo = "Pedro" # comentario alinhado
```

## Comentarios

No inicio do arquivo use `""" """` para fazer o docstring descrevendo as funcionalidades

```py
"""
Descricao da funcionalidade da aplicacao,
se achar necessario, adicione descricao ou exemplos
das classes exportadas ou funcoes
"""
```

## String

Não use `+` para formatar strings, tente usar outros metodos

```py
    x = f'nome: {nome}; score: {n}'
    x = '%s, %s!' % (primeiro, segundo)
    x = '{}, {}'.format(primeiro, segundo)
    x = 'nome: %s; score: %d' % (nome, n)
    x = 'nome: {}; score: {}'.format(nome, n)
    x = a + b
```

evite usar `+=` pois aumenta a complexidade do codigo, use como uma lista e depois junte com o `join`

```py
    items = ['<table>']
    for last_name, first_name in employee_list:
        items.append('<tr><td>%s, %s</td></tr>' % (last_name, first_name))
    items.append('</table>')
    employee_table = ''.join(items)
```
# Venv
Para editar o código, é recomendado criar uma virtual machine de python(caso não tenha feito para este repositório), para maior gestão dos pacotes utilizando os comandos:

bash
## Criar a máquina virtual
python -m venv .venv

Para "Entrar" na máquina virtual deve-se usar:
bash
source .venv/Scripts/activate.ps1 # No Windows
## Vale ressaltar que no Windows deve usar o git-bash e não o PowerShell

source .venv/bin/activate # No Linux

## Baixando Pacotes do Projeto
Logo em seguida deve-se baixar os pacotes referentes à este projeto utilizando:
bash
pip install -r requirements.txt

## Adicionando Pacotes ao requirements.txt
Caso você esteja desenvolvendo cada vez mais este projeto e precise adicionar dependências de pacotes, você pode apenas instalar, e após finalizar pode adicioná-los ao requirements.txt utilizando o comando:

bash
pip freeze > requirements.txt

*Não se esqueça de commitar seu código com as alterações devidas.*