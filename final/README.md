# Producciones

| id | production |
|---|---|
| 1 | program -> declaration-star statement-star |
| 2 | declaration-star -> declaration declaration-star |
| 3 | declaration-star -> '' |
| 4 | declaration -> type Identifier |
| 5 | statement-star -> statement statement-star |
| 6 | statement-star -> '' |
| 7 | statement -> assignment |
| 8 | statement -> print |
| 9 | statement -> condition |
| 10 | type -> Int |
| 11 | type -> Bool |
| 12 | assignment -> Identifier Equals expression |
| 13 | print -> Print expression |
| 14 | condition -> If expression Then statement-star End |
| 15 | expression -> simple-expression expression-prime |
| 16 | expression-prime -> Operator simple-expression expression-prime |
| 17 | expression-prime -> '' |
| 18 | simple-expression -> Identifier |
| 19 | simple-expression -> Integer |
| 20 | simple-expression -> Boolean |
| 21 | simple-expression -> LParen expression RParen |
| 22 | simple-expression -> Minus simple-expression |

# Tabla

| simbol/terminal |	Identifier | Int | Bool | Equals | Print | If | Then | End | Operator | Integer | Boolean | LParen | RParen | Minus | $ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| program | 1 | 1 | 1 | | 1 | 1 | | | | | | | |	| 1 |
| declaration-star | 3 | 2 | 2 | | 3 | 3 | | | | | | | | | 3 |
| declaration | | 4 | 4 | | | | | | | | | | |	| 6 |
| statement-star  | 5 | | | | 5 | 5 | | 6 | | | | | |	| |
| statement | 7 | | | | 8 | 9 | | | | | | | |	| |
| type | | 10 | 11 | | | | | | | | | | | | |
| assignment | 12 | | | | | | | | | | | | | | |
| print | | | | | 13 | | | | | | | | |	| |
| condition | | | | | | 14 | | | | | | | |	| |
| expression | 15 | | | | | | | | | 15 | 15 | 15 | | 15 | |
| expression-prime | 17 | | | | 17 | 17 | 17 | 17 | 16 | | | | 17 | | 17 |
| simple-expression | 18 | | | | | | | | | 19 | 20 | 21 | | 22 | |

# Instrucciones

Requerimientos:

> python3

Ejecución:

> cd /your/work/directory/final
>
> python3 final.py
>
> introducir path al archivo a evaluar.
