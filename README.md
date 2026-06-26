# Fortran 77 Compiler -> EWVM

This repository contains the project for the **Language Processing** (PL) Course Unit in the 2025/2026 academic year. The objective of this project is to develop a complete **Compiler** capable of translating code written in the *Fortran 77* language into executable machine code for the *EWVM* (EPL Web Virtual Machine).

The project was developed in **Python** and implements a modular compilation engine composed of lexical, syntactic, semantic analysis, optimization, and code generation.

## Project Structure

```text
pl2526/
├── src/
│   ├── main.py            # Compiler entry point (full pipeline)
│   ├── lexer.py           # Lexical Analyzer (tokenization and comment removal)
│   ├── parser.py          # Syntax Analyzer (AST construction)
│   ├── symbol_table.py    # Symbol Table (management of variables, arrays, and functions)
│   ├── semantic.py        # Semantic Analyzer (type and declaration checking)
│   ├── optimizer.py       # Optimizer (Constant Folding)
│   └── codegen.py         # EWVM Code Generator
├── tests/
│   ├── fortran/           # Sample Fortran 77 programs (.f)
│   ├── vm/                # EWVM code generated for each example (.vm)
│   └── run_tests.py       # Automated test script (17 tests)
├── docs/                  # Report
├── .gitignore
├── requirements.txt       # Python dependencies (PLY)
└── README.md
```

## Installation and Setup

The compiler requires **Python 3.8+** and depends only on the PLY library (Python Lex-Yacc).

```sh
pip install -r requirements.txt
```

## How to Use the Compiler

### Compile a Fortran file (full pipeline)

```sh
python src/main.py tests/fortran/conversor.f
```

The generated EWVM instructions are printed to the terminal. Copy them and run them in the [EWVM Online](https://ewvm.epl.di.uminho.pt/) simulator.

### Semantic analysis only (without generating code)

```sh
python src/main.py tests/fortran/test_type_bad.f --semantic
```

### Show the AST (syntax tree)

```sh
python src/main.py tests/fortran/hello.f --ast
```

### Run the automated tests

```sh
python tests/run_tests.py
```

## Extra Features (Bonus)

1. **Subprograms (FUNCTION):** Support for functions with argument passing through global variables, including CALL and RETURN.
2. **Optimization (Constant Folding):** Constant expressions are evaluated at compile time (e.g.: `2 + 3 * 4` generates only `PUSHI 14`).

## Developed by

* [Jorge Rafael Machado Fernandes](https://github.com/rafafernandes888)
* [Diogo Teixeira Fernandes](https://github.com/diogo7fernandes)
* [André Filipe Pereira Ribeiro](https://github.com/andreribeiro5)
