#python3


'''
    A01700820
    Carlos Roman Rivera
    Parser - Examen Parte 2
'''


from pathlib import Path
import tokenize


def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    token_categories = {
        'type': [
            'int',
            'bool',
        ],
        'reserved': [
            'if',
            'then',
            'end',
            'print',
        ],
        'operator': [
            '=',
            '&',
            '<',
            '+',
            '*',
        ],
        'boolean': [
            '#t',
            '#f',
        ]
    }

    file_path = input('Test file (example: ./v2/examples/good.txt): ')
    my_file = Path(file_path)

    if my_file.is_file():
        with tokenize.open(file_path) as f:
            tokens = tokenize.generate_tokens(f.readline)
            response = {}
            for idx, token in enumerate(tokens):
                token_content = token.string
                found = False
                for key, value in token_categories.items():
                    if token_content in value:
                        response[idx] = [token_content, key]
                        found = True
                        break
                if not found and token_content != '\n' and token_content != '\t\t' and token_content != '':
                    if  RepresentsInt(token_content):
                        response[idx] = [int(token_content), "integer"]
                    else:
                        response[idx] = [token_content, "identifier"]

        for key, value in response.items():
            print("Value: " + str(value))
    else:
        print("File not found.")
