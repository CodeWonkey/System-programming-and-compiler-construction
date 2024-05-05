macro_definitions = {}

def pass1(source_code):
    macro_name = ""
    macro_body = []
    macro_params = []
    collecting_macro = False

    for line in source_code:
        line = line.strip()  
        if line:  
            fields = line.split()

            if fields[0] == "MACRO":
                macro_name = fields[1]
                macro_params = fields[2:]
                collecting_macro = True
                continue

            if fields[0] == "MEND":
                macro_definitions[macro_name] = (macro_params, macro_body)
                macro_name = ""
                macro_body = []
                macro_params = []
                collecting_macro = False
                continue

            if collecting_macro:
                macro_body.append(line)
            else:
                pass

    print("Macro Definitions:")
    for name, (params, body) in macro_definitions.items():
        print(f"MACRO {name} {' '.join(params)}")
        for line in body:
            print(line)
        print("MEND")
        print()

source_code = [
    "MACRO SWAP X, Y",
    "TEMP WORD 0",
    "MOVE TEMP, X",
    "MOVE X, Y",
    "MOVE Y, TEMP",
    "MEND",
    "MACRO INCR X",
    "ADD X, =1",
    "MEND",
    "START WORD 10",
    "SWAP START, A",
    "INCR START"
]

pass1(source_code)