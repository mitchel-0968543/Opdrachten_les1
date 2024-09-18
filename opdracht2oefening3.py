from math import sqrt

a = 0.87
b = 22.7
c = 5.03

term1 = 4 * a * c
term2 = b ** 2 - term1
term3 = sqrt(term2) 
term4 = -b + term3
term5 = 2 * a
term6 = term4 / term5
print(f'De waarde van y = {term6} als a = {a}, b = {b} en c = {c}')