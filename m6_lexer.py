
tokens = []


t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'

tokens.extend([
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
])


def t_TRUE(t):
    r'True'
    t.value = True
    return t


def t_FALSE(t):
    r'False'
    t.value = False
    return t

tokens.extend([
    'TRUE',
    'FALSE',
])

t_MINUS = r'-'
t_DOLLAR = r'\$'
t_BARUNDERSCBAR = r'\|_\|'
t_DOTSLASH = r'\./'
t_SLASHELLIPSES = r'/\.\.\.'
t_UNDERSCMINUS = r'_-'
t_MINUSUNDERSC = r'-_'
t_UNDERSCSLASH = r'_/'
t_SLASHUNDERSC = r'/_'
t_UNDERSCPLUS = r'_\+'
t_PLUSUNDERSC = r'\+_'
t_PLUS = r'\+'
t_STAR = r'\*'
t_DSLASH = r'//'
t_SLASH = r'/'
t_PERCENT = r'%'
t_CARET = r'\^'
t_BSLASH = r'\\'
t_TILDE = r'~'
t_PIPE = r'\|'
t_GT = r'>'

tokens.extend([
    'MINUS', 'DOLLAR', 'BARUNDERSCBAR', 'DOTSLASH',
    'SLASHELLIPSES', 'UNDERSCMINUS', 'MINUSUNDERSC',
    'UNDERSCSLASH', 'SLASHUNDERSC', 'UNDERSCPLUS',
    'PLUSUNDERSC', 'PLUS', 'STAR', 'DSLASH', 'SLASH',
    'PERCENT', 'CARET', 'BSLASH', 'TILDE', 'PIPE', 'GT',
])

reserved = {
    'diff': 'DIFF',
    'not': 'NOT',
    'strip': 'STRIP',
    'regex': 'REGEX',
    'len': 'LEN',
    'card': 'CARD',
    'head': 'HEAD',
    'tail': 'TAIL',
    'lstrip': 'LSTRIP',
    'rstrip': 'RSTRIP',
    'lsplit': 'LSPLIT',
    'rsplit': 'RSPLIT',
    'lpad': 'LPAD',
    'rpad': 'RPAD',
    'sum': 'SUM',
    'or': 'OR',
    'concat': 'CONCAT',
    'union': 'UNION',
    'mult': 'MULT',
    'and': 'AND',
    'intersect': 'INTERSECT',
    'fdiv': 'FDIV',
    'quot': 'QUOT',
    'split': 'SPLIT',
    'mod': 'MOD',
    'pow': 'POW',
    'perm': 'PERM',
    'del': 'DEL',
    'setdiff': 'SETDIFF',
    'fold': 'FOLD',
    'filter': 'FILTER',
    'greater': 'GREATER',
}

tokens.extend(list(reserved.values()))


def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_\-]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_NUMBER(t):
    r'\d+(\.\d+)?'
    try:
        t.value = int(t.value)
    except ValueError:
        t.value = float(t.value)
    return t

tokens.extend([
    'NUMBER',
])


def t_LITERAL(t):
    r'`([^`]*\r?\n?)*`'
    t.value = t.value.strip('`')
    return t


def t_LITERAL_ALT(t):
    r',,([^"]*\r?\n?)*;;'
    t.value = t.value.lstrip(',').rstrip(";")
    return t

tokens.extend([
    'LITERAL',
    'LITERAL_ALT',
    'ID',
])

t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    try:
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
    except:
        pass


tokens = list(set(tokens))
