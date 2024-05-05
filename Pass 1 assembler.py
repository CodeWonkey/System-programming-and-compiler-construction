symbol_table = {}

object_code = []

def pass1(source_code):
    locctr = 0  
    for line in source_code:
        line = line.strip()  
        if line:  
            fields = line.split()  
            label = fields[0]
            opcode = fields[1]

            if label.endswith(':'):
                label = label[:-1]  
                symbol_table[label] = locctr  

            if opcode == 'WORD':
                locctr += 3 
                object_code.append(f"{opcode} {fields[2]}")  
            elif opcode == 'RESW':
                locctr += 3 * int(fields[2])  
                object_code.append(f"{opcode} {fields[2]}")  
            elif opcode == 'RESB':
                locctr += int(fields[2])  
                object_code.append(f"{opcode} {fields[2]}")  
            elif opcode == 'BYTE':
                if fields[2].startswith('X'):
                    locctr += len(fields[2]) // 2  
                    object_code.append(f"{opcode} {fields[2]}")  
                else:
                    locctr += len(fields[2]) - 3  
                    object_code.append(f"{opcode} {fields[2]}")  
            else:
                locctr += 3  
                object_code.append(f"{opcode}")  

    print("Symbol Table:")
    if symbol_table:
        for symbol, address in symbol_table.items():
            print(f"{symbol}: {address}")
    else:
        print("No symbols found.")

    print("\nObject Code:")
    if object_code:
        for obj in object_code:
            print(obj)
    else:
        print("No object code generated.")

source_code = [
    "COPY START 1000",
    "FIRST RESW 4",
    "CBLOCK RESW 1",
    "FIELD1 RESM 1",
    "FIELD2 RESM 1",
    "FIELD3 RESM 1",
    "CEND RESW 1",
    "SECOND RESW 10",
    "THIRD WORD 5",
    "BUFFER BYTE X'F1'",
    "BUFFER BYTE C'EOF'",
    "ALPHA BYTE 'AB'",
    "END COPY"
]
pass1(source_code)