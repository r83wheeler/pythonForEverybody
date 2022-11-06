import math
import random

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('en'), 'Glenn')
print(greet('es'), 'Sally')
print(greet('fr'), 'Michael')

print(math)

def thing():
    print('Hello')

print('There')

def func(x): 
    print(x)

func(10)
func(20)

def stuff():
    print('Hello')
    return
    print('World')

stuff()