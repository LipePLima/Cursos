'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

exp = str(input('Digite uma expressão matemática: '))
pilha = []

for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
    if simb == '[':
        pilha.append('[')
    elif simb == ']':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(']')
            break
    if simb == '{':
        pilha.append('{')
    elif simb == '}':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append('}')
            break
print('='*40)        
if len(pilha) == 0:
    print('Sua expressão é válida')
else:
    print('Sua expressão é inválida')
