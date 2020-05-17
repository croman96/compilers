'''
    A01700820
    Carlos Roman Rivera
    EZ-Pascal Lexer
'''

import tokenize

def TokenInKeyList(token, keyList):
    if token in keyList:
        return True
    return False

def AddToken(tokenList, tokenStringLower):

    reserved = [
        "program",
        "begin",
        "end",
        "function",
        "constant",
        "if",
        "else",
        "then",
        "var",
        "const"
        "do",
        "while",
        "repeat",
        "for",
        "until",
        "to",
        "downto",
        "writeln",
        "readln",
    ]

    types = [
        "integer",
        "string",
        "boolean",
        "real",
    ]

    operators = [
        "and",
        "or",
        "not",
        "mod",
        "div"
    ]

    '''
        I think we are missing in the grammar a production where we assign a
        variable to a boolean expression.
    '''

    if TokenInKeyList(tokenStringLower, reserved) or TokenInKeyList(tokenStringLower, types) or TokenInKeyList(tokenStringLower, operators):
        tokenList.append(tokenStringLower)
    else:
        tokenList.append('identifier')

    return tokenList

def GetTokens(filePath):

    dict = {
        'system': 1,
        'number': 2,
        'string': 3,
        'operator': 53
    }

    tokenList = []

    with tokenize.open(filePath) as file:
        tokens = tokenize.generate_tokens(file.readline)
        for index, token in enumerate(tokens):

            tokenType = token.type
            tokenString = token.string
            tokenStringLower = token.string.lower()

            if tokenType == dict.get('system'):
                tokenList = AddToken(tokenList, tokenStringLower)
            elif tokenType ==  dict.get('number'):
                tokenList.append('number')
            elif tokenType ==  dict.get('string'):
                tokenList.append('string')
            elif tokenType ==  dict.get('operator'):
                if(tokenStringLower == ':' or tokenStringLower == '>' or tokenStringLower == '<' or tokenStringLower == '='):
                    nextToken = next(tokens)
                    if(nextToken.string == '=' or nextToken.string == '<' or nextToken.string == '>'):
                        tokenList.append(tokenStringLower + nextToken.string.lower())
                    else:
                        tokenList.append(tokenStringLower)
                        if nextToken.type == dict.get('system'):
                            tokenList = AddToken(tokenList, nextToken.string.lower())
                        else:
                            tokenList.append(nextToken.string.lower())
                else:
                    tokenList.append(tokenStringLower)

    return tokenList
