# EditorConfig

estensao que facilita a padronizacao, definindo espaco do t

# Como configurar

ao criar o projeto com
`npx create-react-app my-app --template typescript`

instale a extensao do ESLint no VScode
| foto |

apos isso digite `CTRL+SHIFT+P` e `Open Settings (JSON)` abrindo um arquivo de configuracao do VSCode
entao adicione

```JSON
"editor.formatOnSave": true,
"editor.codeActionsOnSave": {
  "source.fixAll": true,
},
```

essas configiracoes sao recomendadas para salvar automaticamente o codigo, sem ter que usar o `Format Document` padrao do VSCode.

apos isso voce tera que adicionar o eslint
<br>`npm add eslint -D`<br>
e apos isso inicia-lo:
<br>`npm eslint --init`<br>
e iniciara uma serie de perguntas, segue o gabarito:

```
How would you like do use Eslint?
>To check syntax, find problems and enforce code style

Which framework does your project use?
>JavaScript modules (import/export)

Which framework does your project use?
>React

Does your project use TypeScript?
>Yes

Where does your code run?
>Browser

How would you like to define a style for your project?
>Use a popular style guide

Which style guide do you want to follow?
>Standard

What format do you want your config file to be in?
>JSON

Would you like to install them now with npm?
>Yes
```

apos isso ira criar o arquivo `.eslintrc.json` , e nele
