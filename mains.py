import kel5_lexer
import kel5_parser
import kel5_interpreter

from sys import *

lexer = kel5_lexer.BasicLexer()
parser = kel5_parser.BasicParser()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    kel5_interpreter.BasicExecute(tree, env)
