from sly import Lexer
class BasicLexer(Lexer):
    tokens = { NAME, NUMBER, STRING, IF, PRINT, THEN, ELSE, FOR, FUN, TO, ARROW, EQEQ }
    ignore = '\t '

    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';' }

    # Define tokens
    IF = r'KALAU'
    PRINT = r'CETAK'
    THEN = r'KEMUDIAN'
    ELSE = r'LAIN'
    FOR = r'UNTUK'
    FUN = r'FUN'
    TO = r'OT'
    ARROW = r'->'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'

    EQEQ = r'=='

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'#.*')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def newline(self,t ):
        self.lineno = t.value.count('\n')


if __name__ == '__main__':
    lexer = BasicLexer()
    env = {}
    while True:
        try:
            text = input('yoga > ')
        except EOFError:
            break
        if text:
            lex = lexer.tokenize(text)
            for token in lex:
                print(token)