from utils import load_grammar, validate_grammar
from grammar import Grammar

def run(file_path):
    lines = load_grammar(file_path)
    print(f"\nArchivo cargado: {file_path}")
    for line in lines:
        print("  ", line)

    validate_grammar(lines)
    print("\n Gramática válida")

    g = Grammar.from_lines(lines)
    g.display("Gramática Original")

    g.remove_epsilon()
    g.display("Gramática sin producciones-ϵ")

if __name__ == "__main__":
    run("Ejercicio1/grammars/g1.txt")
    run("Ejercicio1/grammars/g2.txt")
