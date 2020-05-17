'''
    A01700820
    Carlos Roman Rivera
    EZ-Pascal Parser
'''

from lexer import GetTokens
from pathlib import Path
import sys

# Helper function to validate files.
def IsFile(file_path):
    file = Path(file_path)

    if file.is_file():
        return True

    return False

# Helper function to parse actions and go-to tables.
def ParseTable(file_path):
    tableFile = open(file_path, 'r')
    table = [line.split(',') for line in tableFile.readlines()]

    parsedTable = []
    for row in table:

        # Strip line breaks.
        stripped = list(map(str.strip, row))

        '''
            Action:
            stripped[0] -> state
            stripped[1] -> input
            stripped[2] -> action (shift [s] / reduce [r])
            stripped[3] -> number of action

            In case of an action containing a comma,
            it will strip it and generate an extra list item because of that.

            Go-To:
            stripped[0] -> state
            stripped[1] -> input
            stripped[2] -> number
        '''

        # If a comma has been stripped.
        if(stripped[1] == '"'):
            # Replace stripped[1] and stripped[2] with a comma.
            stripped = [stripped[0], ',', stripped[3], stripped[4]]

        parsedTable.append(stripped)

    return parsedTable

def GetAction(stack, token, actionsTable):
    for action in actionsTable:
        # If stack and input token match an action entry.
        if stack == int(action[0]) and token == action[1]:
            # Return action and action number.
            return action[2], int(action[3])
    return -1

def GetGoto(stack, symbol, gotoTable):
    for goto in gotoTable:
        # If stack and symbol match a goto entry.
        if stack == int(goto[0]) and symbol == goto[1]:
            # Return goto number.
            return int(goto[2])

def Parser(input, actionsTable, gotoTable, grammar):
    stack = []
    symbols = []

    status = 'ERROR'

    stack.append(0)

    while True:
        try:
            # Action entry based on stack and input stream.
            action, number = GetAction(stack[-1], input[0], actionsTable)
        except:
            status = 'ERROR - ACTION NOT FOUND'
            break

        if action == 'ACCEPT':
            status = 'ACCEPTED'
            break
        elif action == 's':
            print("Shift:", number)
            stack.append(number)
            symbols.append(input[0])
            input.pop(0)
        elif action == 'r':
            print("Reduce:", number)
            action = grammar[number].split()
            # Pop as many elements as production requires.
            for i in range(len(action)-2):
                # If action is not epsilon.
                if action[i+2] != "''":
                    symbols.pop()
                    stack.pop()
                else:
                    break
            symbols.append(action[0])
            # Go-To entry based on stack and symbol stream.
            gotoAction = GetGoto(stack[-1], symbols[-1], gotoTable)
            print("Goto:", gotoAction)
            stack.append(gotoAction)

    print("---------------")
    print("Status:", status)
    print("Stack:", stack)
    print("Symbols:", symbols)
    print("Input:", input)
    print("---------------")

if __name__ == "__main__":

    grammar_path = './grammar.txt'
    actions_path = './actions_table.txt'
    goto_path = './gotos_table.txt'
    error = 0

    # Check for grammar file.
    if IsFile(grammar_path):
        grammar = open(grammar_path, 'r').readlines()
    else:
        print("Error: Grammar file not found")
        error = 1

    # Check for actions file.
    if IsFile(actions_path):
        actionsTable = ParseTable(actions_path)
    else:
        print("Error: Actions file not found.")
        error = 1

    # Check for go-to file.
    if IsFile(goto_path):
        gotoTable = ParseTable(goto_path)
    else:
        print("Error: Go-To file not found.")
        error = 1

    # Check for input file.
    input_path = input('Test file (example: ./examples/good/Example1.pas): ')
    # input_path = './examples/good/Example1.pas'
    if IsFile(input_path):
        tokenList = GetTokens(input_path)
        tokenList.append("$")
    else:
        print("Error: Input file not found.")
        error = 1

    # If all pre-requisites are met, parse.
    if not error:
        Parser(tokenList, actionsTable, gotoTable, grammar)
