# Gramática

```
program -> declaration-star statement-star

declaration-star -> declaration declaration-star
declaration-star -> ''

declaration -> type Identifier

statement-star -> statement statement-star
statement-star -> ''

statement -> assignment
statement -> print
statement -> condition

type -> Int
type -> Bool

operator -> &
operator -> <
operator -> +
operator -> *

assignment -> Identifier Equals expression

print -> Print expression

condition -> If expression Then statement-star End

expression -> simple-expression expression-prime
expression-prime -> operator simple-expression expression-prime
expression-prime -> ''

simple-expression -> Identifier
simple-expression -> Integer
simple-expression -> Boolean
simple-expression -> LeftParenthesis expression RightParenthesis
simple-expression -> Minus simple-expression
```

# Conjunto First

| symbol |	set |
|---|---|
| program |	Int, Bool, Identifier, Print, If, ε |
| declaration-star |	Int, Bool, ε |
| declaration |	Int, Bool |
| statement-star |	Identifier, Print, If, ε |
| statement |	Identifier, Print, If |
| type |	Int, Bool |
| operator | &, <, +, * |
| assignment |	Identifier |
| print |	Print |
| condition |	If |
| expression |	Identifier, Integer, Boolean, LeftParenthesis, Minus |
| expression-prime |	operator, ε |
| simple-expression |	Identifier, Integer, Boolean, LeftParenthesis, Minus |

# Conjunto Follow

| symbol | set |
|---|---|
| program | $ |
| declaration-star | Identifier, Print, If, $ |
| declaration | Int, Bool, Identifier, Print, If, $ |
| statement-star | End, $ |
| statement | Identifier, Print, If, End, $ |
| type | Identifier |
| operator | Identifier |
| assignment | Identifier, Print, If, End, $ |
| print | Identifier, Print, If, End, $ |
| condition | Identifier, Print, If, End, $ |
| expression | Identifier, Print, If, Then, RightParenthesis, End, $ |
| expression-prime | Identifier, Print, If, Then, RightParenthesis, End, $ |
| simple-expression | Identifier, Print, If, Then, RightParenthesis, End, Operator, $ |

### Instrucciones

Requerimientos:

> python3

Ejecución:

> cd /your/work/directory/final
>
> python3 final.py
>
> introducir path al archivo a evaluar.
