from collections import defaultdict

class Grammar:
    def __init__(self, productions: dict[str, list[str]]):
        self.productions = productions 

    @staticmethod
    def from_lines(lines: list[str]):
        grammar = defaultdict(list)
        for line in lines:
            left, right = line.split("→")
            left = left.strip()
            prods = [p.strip() for p in right.split("|")]
            grammar[left].extend(prods)
        return Grammar(dict(grammar))

    def display(self, title="Gramática"):
        print(f"\n--- {title} ---")
        for nt, prods in self.productions.items():
            print(f"{nt} → {' | '.join(prods)}")

    def find_nullable(self):
        nullable = set()
        changed = True

        while changed:
            changed = False
            for A, prods in self.productions.items():
                for p in prods:
                    if p == "ϵ":
                        if A not in nullable:
                            nullable.add(A)
                            changed = True

                    else:
                        if all((sym in nullable) if sym.isupper() else False for sym in p):
                            if A not in nullable:
                                nullable.add(A)
                                changed = True

        return nullable



    def remove_epsilon(self):
        nullable = self.find_nullable()
        print("\nSímbolos anulables:", nullable)

        new_productions = defaultdict(set)

        for A, prods in self.productions.items():
            for p in prods:
                if p == "ϵ":
                    continue  

                combinations = {p}
                for i, sym in enumerate(p):
                    if sym in nullable:
                        combos = set()
                        for c in combinations:
                            # quitar el símbolo i
                            new = c[:i] + c[i+1:]
                            if new == "":
                                new = "ϵ"
                            combos.add(new)
                        combinations |= combos

                new_productions[A].update(combinations)

        self.productions = {A: sorted(list(ps)) for A, ps in new_productions.items()}
