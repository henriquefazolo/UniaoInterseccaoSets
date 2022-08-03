'''
Crie dois sets contendo as habilidades de duas pessoas, por exemplo:
pessoa1 = {“Python”, “Java”, “C++”}.
Mostre a união e a intersecção desses dois sets.
'''

pessoa1 = "Python", "Java", "C++"
pessoa2 = "Python", "Cobol", "C#"

print(set(pessoa1).union(pessoa2))
print(set(pessoa1).intersection(pessoa2))