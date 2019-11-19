import sqlparse

raw = 'select * from foo; select * from bar;'

statements = sqlparse.split(raw)

print(statements)

first = statements[0]

print(sqlparse.format(first, reindent=True, keyword_case='upper'))

parsed_all = sqlparse.parse('select *')


for token in parsed_all[0].tokens:
    print(token.normalized)
    print(token.is_keyword)
    print(token.ttype)


