class AssemblerPass1:
    def __init__(self):
        self.symbol_table = {}
        self.opcode_table = {}
        self.literals_table = {}

    def process_assembly(self, assembly_code):
        assembly_lines = assembly_code.split('\n')
        location_counter = 0

        for line in assembly_lines:
            tokens = line.split()
            if len(tokens) == 0:
                continue

            # Check for symbol
            if len(tokens) >= 2 and tokens[1] == 'DS':
                self.symbol_table[tokens[0]] = location_counter
                if len(tokens) == 3:
                    location_counter += int(tokens[2])
                else:
                    location_counter += 1
            else:
                if tokens[0] not in ['START', 'END']:
                    self.symbol_table[tokens[0]] = location_counter
                if tokens[0] == 'LTORG':
                    for literal, addr in self.literals_table.items():
                        if addr == None:
                            self.literals_table[literal] = location_counter
                            location_counter += 1
                elif tokens[0] == 'START':
                    location_counter = int(tokens[1])
                elif tokens[0] == 'END':
                    for literal, addr in self.literals_table.items():
                        if addr == None:
                            self.literals_table[literal] = location_counter
                            location_counter += 1
                    break
                else:
                    location_counter += 1

                # Check for opcode
                if len(tokens) >= 2:
                    self.opcode_table[tokens[0]] = tokens[1]

                # Check for literals
                for i in range(len(tokens)):
                    if '=' in tokens[i]:
                        literal = tokens[i].split('=')[1]
                        if literal not in self.literals_table:
                            self.literals_table[literal] = None

    def display_tables(self):
        print("Symbol Table:")
        print("{:<10} {:<10}".format("Symbol", "Address"))
        for symbol, address in self.symbol_table.items():
            print("{:<10} {:<10}".format(symbol, address))
        
        print("\nOpcode Table:")
        print("{:<10} {:<10}".format("Opcode", "Value"))
        for opcode, value in self.opcode_table.items():
            print("{:<10} {:<10}".format(opcode, value))
        
        print("\nLiterals Table:")
        print("{:<10} {:<10}".format("Literal", "Address"))
        for literal, address in self.literals_table.items():
            print("{:<10} {:<10}".format(literal, address))


if __name__ == "__main__":
    assembler = AssemblerPass1()
    assembly_code = """
    START 1000
    LOOP ADD AREG, ='5'
    MOV BREG, ='2'
    DS C, 1
    LTORG
    END
    """
    assembler.process_assembly(assembly_code)
    assembler.display_tables()
