'''
    A01700820
    Carlos Roman Rivera
    EZ-Pascal Lexer
'''

from pathlib import Path
import tokenize

pascal_tokens = {
    'symbols': [
        '.',
        ';',
        '(',
        ')',
        ',',
        ':',
    ],
    'operators': [
        ':=',
        '+',
        '-',
        '/',
        '*',
        '<',
        '>',
        '<=',
        '>=',
        '==',
        '='
    ],
    'keywords' : [
        'readln',
        'writeln',
        'program',
        'var',
        'true',
        'false',
        'procedure',
        'function'
    ],
    'statements': [
        'if',
        'else',
        'then',
        'and',
        'or',
        'repeat',
        'until',
        'begin',
        'end',
    ],
    'data_types': [
        'real',
        'integer',
        'string',
        'bool',
    ],
    'omit': [
        '\t',
        '\n',
    ]
}

file_path = input('Test file (example: ./examples/Example8.pas): ')
my_file = Path(file_path)

if my_file.is_file():
    with tokenize.open(file_path) as f:
        tokens = tokenize.generate_tokens(f.readline)
        response = {}
        for idx, token in enumerate(tokens):
            response[idx] = []
            token_content = token.string.lower()
            found = False
            for key, value in pascal_tokens.items():
                if token_content in value:
                    response[idx] = [token_content, key]
                    found = True
                    break
            if not found:
                response[idx] = [token_content, "other"]

    for key, value in response.items():
        print("Key: " + str(key) + " Value: " + str(value))
else:
    print("File not found.")