import kel5_lexer
import kel5_parser
import kel5_interpreter

from sys import *


if __name__ == '__main__':
    lexer = kel5_lexer.BasicLexer()
    parser = kel5_parser.BasicParser()
    env = {}
    while True:
        try:
            text = input('BHS KELOMPOK 5 > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            kel5_interpreter.BasicExecute(tree, env)
