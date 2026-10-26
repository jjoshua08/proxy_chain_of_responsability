# Atividade — Proxy e Chain of Responsibility

Requer Python 3.9 ou superior. Utiliza somente a biblioteca padrão.
Execute os comandos na raiz do repositório (diretório que contém `atividade_padroes`).

## Questão 1 — Proxy

```bash
python3 -m atividade_padroes.questao_1_proxy.principal
```

`Usuario` e `UsuarioProxy` implementam o contrato abstrato `DadosUsuario`.
O Proxy mantém uma referência privada ao usuário real, permite ler o nome,
mascara os três primeiros e os dois últimos dígitos do CPF e bloqueia a leitura
de `endereco` com `PermissionError`. A pontuação do CPF é preservada:
`123.456.789-01` resulta em `***.456.789-**`.
Os dados originais não são alterados. O bloqueio se aplica à interface pública
do Proxy; atributos privados de Python não constituem proteção contra introspecção.

O diagrama UML está em [diagrama_proxy.md](questao_1_proxy/diagrama_proxy.md).

## Questão 2 — Chain of Responsibility

```bash
python3 -m atividade_padroes.questao_2_chain.principal
```

Cada validador verifica uma regra e delega ao próximo somente se ela for aprovada:
saldo → limite do tipo de conta → bloqueio judicial.
Uma rejeição interrompe a cadeia; a aprovação ocorre ao final de todas as regras.
Valores monetários são `Decimal`, construídos a partir de strings.
Os tipos de conta utilizados são `Comum` e `Premium`.
O sistema apenas autoriza a transação, sem debitar o saldo.

A demonstração exibe uma aprovação e quatro rejeições: saldo insuficiente,
limite de R$ 1.000,00 da conta Comum, limite de R$ 10.000,00 da conta Premium
e bloqueio judicial, sempre informando o motivo.
