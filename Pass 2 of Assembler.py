class AssemblerPass2:
    def __init__(self, assembly_code, symbol_table, opcode_table, literals_table):
        self.assembly_code = assembly_code
        self.symbol_table = symbol_table
        self.opcode_table = opcode_table
        self.literals_table = literals_table
        self.object_code = []

    def process_assembly(self):
        for line in self.assembly_code.split('\n'):
            tokens = line.split()
            if not tokens:
                continue
            mnemonic = tokens[0]
            if mnemonic == 'LTORG':
                for literal, address in self.literals_table.items():
                    if address is None:
                        self.object_code.append(literal)
                        self.literals_table[literal] = len(self.object_code) - 1
            elif mnemonic != 'START':
                operand = tokens[1].split(',')[0]
                if operand in self.symbol_table:
                    self.object_code.append(self.opcode_table[mnemonic] + str(self.symbol_table[operand]))
                elif operand in self.literals_table:
                    self.object_code.append(self.opcode_table[mnemonic] + str(self.literals_table[operand]))
                else:
                    self.object_code.append(self.opcode_table[mnemonic])

    def generate_object_code(self):
        return '\n'.join(self.object_code)


if __name__ == "__main__":
    symbol_table = {'LOOP': 1000, 'MOV': 1001, 'DS': 1002, 'LTORG': 1003}
    opcode_table = {'START': '1000', 'LOOP': 'ADD,AREG', 'MOV': 'MOV,BREG', 'DS': 'DS,C'}
    literals_table = {"'5'": 1003, "'2'": 1004}

    assembly_code = """
    START 1000
    LOOP ADD, AREG
    MOV MOV, BREG
    DS DS, C
    LTORG
    """

    assembler_pass2 = AssemblerPass2(assembly_code, symbol_table, opcode_table, literals_table)
    assembler_pass2.process_assembly()
    object_code = assembler_pass2.generate_object_code()

    print("Object Code:")
    print(object_code)
