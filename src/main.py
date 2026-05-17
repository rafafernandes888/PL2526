"""
Compilador Fortran 77 -> EWVM
Ponto de entrada principal.

"""

import sys
import lexer as lexer_module
import parser as parser_module
from lexer import preprocess
from semantic import SemanticAnalyzer
from codegen import CodeGenerator


def compile_file(path, mode='codegen'):
    with open(path, 'r', encoding='utf-8') as f:
        source = f.read()

    # Pré-processamento e parsing
    source = preprocess(source)


    lex = lexer_module.lex.lex(module=lexer_module)
    tree = parser_module.parser.parse(source, lexer=lex)

    if tree is None:
        print("Erro: Falha no parsing do ficheiro.")
        sys.exit(1)

    # Modo AST: mostrar a árvore e sair
    if mode == 'ast':
        import json
        print(json.dumps(tree, indent=2, default=str))
        return

    # Análise semântica
    analyzer = SemanticAnalyzer()
    analyzer.analyze(tree)

    if analyzer.errors:
        sys.exit(1)


    if mode == 'semantic':
        return

    # Geração de código
    gen = CodeGenerator()
    gen.generate(tree)
    print(gen.get_code())


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Compilador Fortran 77 -> EWVM")
        print()
        print("Uso:")
        print("  python src/main.py <ficheiro.f>              Compilar e gerar código EWVM")
        print("  python src/main.py <ficheiro.f> --semantic   Apenas análise semântica")
        print("  python src/main.py <ficheiro.f> --ast        Mostrar a AST")
        sys.exit(1)

    path = sys.argv[1]
    mode = 'codegen'

    if len(sys.argv) > 2:
        flag = sys.argv[2]
        if flag == '--semantic':
            mode = 'semantic'
        elif flag == '--ast':
            mode = 'ast'

    compile_file(path, mode)
