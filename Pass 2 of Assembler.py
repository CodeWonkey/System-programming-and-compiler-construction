def pass2(symbol_table, object_code):
    final_object_code = []  

    for line in object_code:
        fields = line.split()  
        opcode = fields[0]

        if len(fields) > 1:
            operand = fields[1]

            if operand in symbol_table:
                operand_value = symbol_table[operand]
            else:
                try:
                    operand_value = int(operand)  
                except ValueError:
                    operand_value = 0  

            final_object_code.append(f"{opcode} {operand_value}")
        else:
            final_object_code.append(f"{opcode}")

    print("Final Object Code:")
    for obj in final_object_code:
        print(obj)

symbol_table = {
    "FIRST": 1000,
    "CBLOCK": 1012,
    "CEND": 1015,
    "SECOND": 1018,
    "THIRD": 1048,
    "BUFFER": 1051,
    "ALPHA": 1053
}

object_code = [
    "RESW 4",
    "RESW 1",
    "RESM 1",
    "RESM 1",
    "RESM 1",
    "RESW 1",
    "RESW 10",
    "WORD 5",
    "BYTE X'F1'",
    "BYTE C'EOF'",
    "BYTE 'AB'"
]

pass2(symbol_table, object_code)