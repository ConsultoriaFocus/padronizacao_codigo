- Menu
  - [Sintaxe](#sintaxe)
    - [Nomes](#nomes)
    - [Constantes](#constantes)
  - [Comentarios](#comentarios)
    - [Tipos](#tipos-de-comentarios)
    - [Comentarios Uteis](#comentarios-uteis)
  - [Padrões de Código](#padrões-de-código)
    - [Classes](#classes)
      - [Constructors](#constructors)
      - [Private](#private)
      - [Parametros](#parametros)
      - [Get and Set](#get-and-set)
    - [Variaveis](#variaveis)
      - [Definir Array](#definir-array)
      - [Inteirar Array](#inteirar-array)
      - [Switch](#switch)
      - [Comparação](#comparação)
    - [Funções](#funções)
      - [Arrow functions](#arrow-functions)
      - [Event Handlers](#event-handlers)
    - [Import](#import)
    - [Export](#export)

# Sintaxe

## Nomes

### os nomes precisam ser claros para que novos leitores consigam entender

- <b>Exeção:</b> codigos muito curtos (maximo de 10 linhas)

| Style            | Category                                                           |
| :--------------- | :----------------------------------------------------------------- |
| `UpperCamelCase` | class / interface / type / enum / decorator / type parameters      |
| `lowerCamelCase` | variable / parameter / function / method / property / module alias |
| `CONSTANT_CASE`  | global constant values, including enum values                      |
| `snake_case`     | file name                                                          |

## Constantes

`CONSTANT_CASE` é usado para sinalizar que a variavel nao deve ser modificada

```typescript
const MY_SPECIAL_NUMBER = 5;
```

pode ser definida como `const` ou `static readonly` se for um atributo

```typescript
class Foo {
  private static readonly MY_SPECIAL_NUMBER = 5;
}
```

# comentarios

## Tipos de comentarios

existem dois tipos principais de comentarios em Typescript `//**...*/` e `//...`

- use `//**...*/` para comentarios que o usuario do codigo deva ler
- use `//...` para comentar linhas de codigo

## Comentarios Uteis

faça comentarios que adicionem informcao ao codigo.</br>
normalmente o nome da variavel ja é auto explicativa,</br>
portanto somente use `@param` e `@return` se forem adicionar informacao.

```typescript
/**
 * POST a requisicao para comecar a encher a xicara
 * @param quantosMl quantos mililitros ira encher a xicara
 */
encher(quantosMl: number, xicara: Xicara) {
  // ...
}
```

# Padrões de Código

<!--
## visibilidade
* nunca use `public` pois ja assim no default
-->

# Classes

## Constructors

chamda de Constructors devem ter parenteses mesmo que nao tenham parametros

```typescript
const x = new Cafe();
```

## private

use `private` para variaveis privadas, inves de `#`, pois é mais eficiente para Typescript

```typescript
class Xicara {
  /** nao use essa notacao */
  #volume = 250;
  /** use essa */
  private liquido = new Cafe();
}
```

### use `readonly`

use para marcar as propriedades que nunca sao redefinidas fora do constructor

## Parametros

inicialize o parametro no constructor

```typescript
class Cafe {
  constructor(private readonly grao: Grao) {}
}
```

se nao for um parametro nao precisa do constructor

```typescript
class Cafeteria {
  private readonly clientes: Cliente[] = [];
}
```

## get and set

é bom usar para controlar o uso das variaveis

```typescript
class Xicara {
  constructor(private readonly volume: number) {}

  get volume(): string {
    return this.volume;
  }

  set volume(newValue: string) {
    this.volume = newValue;
  }
}
```

# Variaveis

sempre use `cont` ou `let` para definir variaveis

```typescript
const c = valor;
let l = 0;
```

Não use `var`, porque pode causar conflitos e bugs complicados, alem de dificultar a leitura do codigo;

### Nunca use Primitive Types

```typescript
/** errado */
const s = new String("hello");
const b = new Boolean(false);
const n = new Number(5);

/** correto */
const s = "hello";
const b = false;
const n = 5;
```

## Definir Array

Não se deve inicializar um array com `Array()`, se precisar use o `from` para iniciar o Array com tamanho definido

```typescript
/** nao use */
const a = Array(2); // [undefined, undefined]
const b = Array(2, 3); //[2, 3]

/** use */
const c = [2, 3];
const d = Array.from<number>({ length: 5 }).fill(0);
// d = [0,0,0,0,0]
```

## Inteirar Array

Não use `for (__ in __)` e `forEach` para interar o array.

```typescript
for (const x of Arr) {
  // x é um valor do Arr.
}
for (let i = 0; i < Arr.length; i++) {
  // forma padrao de inteirar.
  const x = Arr[i];
  // ...
}
for (const [i, x] of Arr.entries()) {
  // mesmos valores que a padrao.
}
```

## Switch

todos os `switch` devem ter o `default`, mesmo que nao tenha codigo

```typescript
switch (x) {
  case 1:
    beberCafe();
    break;
  case 2:
  case 3:
    encherXicara();
    break;
  default:
  // nada.
}
```

## Comparação

sempre use `===` ou `!==` para comparar igualdades

```typescript
if (x === 1 && y !== "1") {
}
```

- <b>Exeção:</b> ao comparar com `null` deve usar `==` ou `!=` para tambem comparar com `undefined`

```typescript
if (x == null) {
  // Verdadeiro caso null ou undefined.
}
```

# Funções

## Arrow functions

não é recomnedado que Arrow functions sejam parametros exeto se for Event Handlers.

```typescript
/** nao use assim*/
class Xicara {
  constructor() {
    setTimeout(this.encher, 5000);
  }
  private encher = () => {
    this.cheia = true;
  };
}
```

```typescript
/** Forma recomendada*/
class Xicara {
  constructor() {
    setTimeout(() => {
      this.encher();
    }, 5000);
  }
  private encher() {
    this.cheia = true;
  }
}
```

## Event Handlers

se tiver que "desinstalar" a função depois, então use

```typescript
class Botao {
  ativar() {
    document.addEventListener("mousedown", this.enviar);
  }
  desativar() {
    document.removeEventListener("mousedown", this.enviar);
  }
  private enviar = () => {
    //...
  };
}
```

Classes normalmente não devem ter arrow functions como propriedades

sempre use arrow functions em expressões

```typescript
/** use */
minhaFuncao(() => {
  this.beberCafe();
});

/** nao use*/
minhaFuncao(function () {
  this.beberCafe();
});
```

# import

os imports para outros arquivos do projeto devem começar com `./` ou `../`
tente limitar o numero de diretorios (`../../../`) para ficar mais facil de entender

### module import

quando importar um modulo, acesse-o diretamente

```typescript
import { botao1, botao2 } from "./botoes";
```

### destructuring import

ao importar muitos modulos use esse metodo

```typescript
import * as botoes from "./botoes";
/** tendo que acessar assim */
botoes.botao9;
```

# export

use assim

```typescript
export class Cafe { ... }
```

Não use default exports:

```typescript
export default class Cafe { ... }
```

```typescript
/** perimte que ocorra esse problema com o nome dos modulos
 *  prejudicando a leitura do codigo
 */
import Cafe from "./cafe";
import Xicara from "./cafe";
```
