TOKEN_TYPES = {
    'KEYWORD': ['if', 'else', 'while', 'for', 'int', 'float', 'char', 'double'],
    'OPERATOR': ['+', '-', '*', '/', '=', '==', '!=', '<', '>', '<=', '>='],
    'DELIMITER': [',', ';', '(', ')', '{', '}', '[', ']'],
    'IDENTIFIER': 'IDENTIFIER',
    'NUMBER': 'NUMBER'
}

import re
PATTERN_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
PATTERN_NUMBER = r'\d+(\.\d+)?'

def tokenize(input_string):
    tokens = []
    i = 0
    while i < len(input_string):
        if input_string[i].isspace():
            i += 1
            continue

        for keyword in TOKEN_TYPES['KEYWORD']:
            if input_string[i:].startswith(keyword):
                tokens.append(('KEYWORD', keyword))
                i += len(keyword)
                break
        else:
            for operator in TOKEN_TYPES['OPERATOR']:
                if input_string[i:].startswith(operator):
                    tokens.append(('OPERATOR', operator))
                    i += len(operator)
                    break
            else:
                for delimiter in TOKEN_TYPES['DELIMITER']:
                    if input_string[i:].startswith(delimiter):
                        tokens.append(('DELIMITER', delimiter))
                        i += len(delimiter)
                        break
                else:
                    match = re.match(PATTERN_IDENTIFIER, input_string[i:])
                    if match:
                        identifier = match.group()
                        tokens.append(('IDENTIFIER', identifier))
                        i += len(identifier)
                    else:
                        match = re.match(PATTERN_NUMBER, input_string[i:])
                        if match:
                            number = match.group()
                            tokens.append(('NUMBER', number))
                            i += len(number)
                        else:
                            raise ValueError(f"Invalid character at position {i}: {input_string[i]}")

    return tokens

input_string = "int x = 10; if (x > 5) { x = x + 1; } else { x = x - 1; }"
tokens = tokenize(input_string)
print("Tokens:")
for token in tokens:
    print(token)