# Validador de CPF em Python
Um validador de CPF funcional feito na linguagem Python

## Como Validar um CPF?

A validação de CPF é baseada na verificação dos nove primeiros dígitos do CPF, e comparada com os dois últimos dígitos.

Ela é segmentada em duas partes, na qual vou explicar a seguir:

Primeira Validação: Multiplicamos os nove primeiros dígitos do CPF um a um pelos valores decrescentes de 10 até 2, conforme o exemplo a seguir para o CPF 123.456.789-10, onde multiplicamos:

1 X 10 = 10 - 2 X 9 = 18 - 3 X 8 = 24

e assim sucessivamente, ao final pegamos o total da soma destes nove resultados e dividimos por 11.

Se o resto desta soma for menor ou igual a 1 e o penúltimo dígito do CPF deve ser igual ao numeral zero... Entretanto se o resto for maior de 2, então o penúltimo dígito do CPF deve ser igual a diferença entre o numero 11 menos o valor do resto obtido.

Segunda Validação: Faremos da mesma forma da primeira validação, sendo que a multiplicação será a partir do número 11 conforme mostrado a seguir no CPF do exemplo 123.456.789-10:

1 X 11 = 11 - 2 X 10 = 20 - 3 X 9 = 27

e assim sucessivamente... contudo desta vez adicionaremos na soma o primeiro digito verificador, sendo assim teremos a multiplicação dos dez primeiros dígitos do CPF.

Se o resto da divisão for menor ou igual a 1 então o ultimo digito verificador deve ser igual a zero... Entretanto se o resto da divisão for maior ou igual a dois, faremos a diferença entre o o numeral 11 e o resto da divisão, onde este deve ser igual o último dígito do CPF para que este seja válido.
