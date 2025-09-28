import re

production_regex = re.compile(r"^[A-Z]\s*→\s*([A-Za-z0-9ϵ]+(\s*\|\s*[A-Za-z0-9ϵ]+)*)$")

def load_grammar(path: str):
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines

def validate_grammar(lines: list[str]):
    for i, line in enumerate(lines, 1):
        if not production_regex.match(line):
            raise ValueError(f"Error en línea {i}: {line}")
