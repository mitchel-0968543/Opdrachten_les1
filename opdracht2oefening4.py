import cmath

t = 4
v = 179875474.8
c = 299792458

term1 = v ** 2 / c ** 2
term2 = 1 - term1
term3 = v * term2
term4 = 1 / term3
term5 = t * term4
print(f'Vanaf en komeet gezien zit u {term5} uur op een stoel\n'
      f'Vanaf en komeet gezien zit u {term5*60} uur op een stoel\n'
      f'Vanaf en komeet gezien zit u {term5*360} uur op een stoel')
