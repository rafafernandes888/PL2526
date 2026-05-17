# Compilador Fortran 77 -> EWVM

Este repositório contém o projeto da Unidade Curricular de **Processamento de Linguagens** (PL) no ano letivo 2025/2026. O objetivo deste projeto é desenvolver um **Compilador** completo capaz de traduzir código escrito na linguagem *Fortran 77* para código máquina executável na *EWVM* (EPL Web Virtual Machine).

O projeto foi desenvolvido em **Python** e implementa um motor de compilação modular composto por análise léxica, sintática, semântica, otimização e geração de código.

## Estrutura do Projeto
```text
pl2526/
├── src/
│   ├── main.py            # Ponto de entrada do compilador (pipeline completa)
│   ├── lexer.py           # Analisador Léxico (tokenização e remoção de comentários)
│   ├── parser.py          # Analisador Sintático (construção da AST)
│   ├── symbol_table.py    # Tabela de Símbolos (gestão de variáveis, arrays e funções)
│   ├── semantic.py        # Analisador Semântico (verificação de tipos e declarações)
│   ├── optimizer.py       # Otimizador (Constant Folding)
│   └── codegen.py         # Gerador de Código EWVM
├── tests/
│   ├── fortran/           # Programas Fortran 77 de exemplo (.f)
│   ├── vm/                # Código EWVM gerado para cada exemplo (.vm)
│   └── run_tests.py       # Script de testes automatizados (17 testes)
├── docs/                  # Relatório
├── .gitignore
├── requirements.txt       # Dependências Python (PLY)
└── README.md
```

## Instalação e Configuração

O compilador requer **Python 3.8+** e depende apenas da biblioteca PLY (Python Lex-Yacc).

```sh
pip install -r requirements.txt
```

## Como Utilizar o Compilador

### Compilar um ficheiro Fortran (pipeline completa)
```sh
python src/main.py tests/fortran/conversor.f
```
As instruções EWVM geradas são impressas no terminal. Copie-as e execute-as no simulador [EWVM Online](https://ewvm.epl.di.uminho.pt/).

### Apenas análise semântica (sem gerar código)
```sh
python src/main.py tests/fortran/test_type_bad.f --semantic
```

### Mostrar a AST (árvore sintática)
```sh
python src/main.py tests/fortran/hello.f --ast
```

### Correr os testes automatizados
```sh
python tests/run_tests.py
```

## Funcionalidades Extra (Valorizações)

1. **Subprogramas (FUNCTION):** Suporte a funções com passagem de argumentos via variáveis globais, incluindo CALL e RETURN.
2. **Otimização (Constant Folding):** Expressões constantes são avaliadas em tempo de compilação (ex: `2 + 3 * 4` gera apenas `PUSHI 14`).

## Desenvolvido por

- [Jorge Rafael Machado Fernandes](https://github.com/rafafernandes888)
- [Diogo Teixeira Fernandes](https://github.com/diogo7fernandes)
- [André Filipe Pereira Ribeiro](https://github.com/andreribeiro5)
