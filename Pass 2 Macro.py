def pass2(source_code, macro_definitions):
    expanded_code = []

    for line in source_code:
        line = line.strip()  
        if line:  
            fields = line.split()

            if fields[0] in macro_definitions:
                macro_name = fields[0]
                macro_params, macro_body = macro_definitions[macro_name]
                macro_args = fields[1:]

                for body_line in macro_body:
                    expanded_line = body_line
                    for i, param in enumerate(macro_params):
                        expanded_line = expanded_line.replace(param, macro_args[i])
                    expanded_code.append(expanded_line)
            else:
                expanded_code.append(line)

    print("Expanded Code:")
    for line in expanded_code:
        print(line)

macro_definitions = {
    "SWAP": (["X", "Y"], ["TEMP WORD 0", "MOVE TEMP, X", "MOVE X, Y", "MOVE Y, TEMP"]),
    "INCR": (["X"], ["ADD X, =1"])
}

source_code = [
    "START WORD 10",
    "SWAP START, A",
    "INCR START"
]

pass2(source_code, macro_definitions)