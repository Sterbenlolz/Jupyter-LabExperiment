from sympy import *

a = 0
z1 = 50
z2 = 100
z3 = 150
U1 = 50
U2 = 50
U3 = 50
r1 = 10
r2 = 10
r3 = 10
r, x, U = symbols('r x U')
E1 = (U1 - U2) / (z2 - z1)
E2 = (U2 - U3) / (z3 - z2)
E0 = (-U1) / z1
E3 = U3 / z1

form1 = f'((0 - {U1}) / (0 - {z1})) * x'
form2 = f'{U1} + ({r1} / pi) * ({E0} - {E1}) * (1 - ((x - {z1}) / {r1}) * atan(-(x - {z1}) / {r1})) - 0.5 * (x - {z1}) * ({E0} + {E1})'
form3 = f'{U1} + ({r1} / pi) * ({E0} - {E1}) * (1 + ((x - {z1}) / {r1}) * atan((x - {z1}) / {r1})) - 0.5 * (x - {z1}) * ({E0} + {E1})'
form4 = f'{U2} + ({r2} / pi) * ({E1} - {E2}) * (1 - ((x - {z2}) / {r2}) * atan(-(x - {z2}) / {r2})) - 0.5 * (x - {z2}) * ({E1} + {E2})'
form5 = f'{U2} + ({r2} / pi) * ({E1} - {E2}) * (1 + ((x - {z2}) / {r2}) * atan((x - {z2}) / {r2})) - 0.5 * (x - {z2}) * ({E1} + {E2})'
form6 = f'{U3} + ({r3} / pi) * ({E2} - {E3}) * (1 - ((x - {z3}) / {r3}) * atan(-(x - {z3}) / {r3})) - 0.5 * (x - {z3}) * ({E2} + {E3})'
form7 = f'{U3} + ({r3} / pi) * ({E2} - {E3}) * (1 + ((x - {z3}) / {r3}) * atan((x - {z3}) / {r3})) - 0.5 * (x - {z3}) * ({E2} + {E3})'
form8 = f'(({U3} - 0) / (0 - {z1})) * x - ({z3} * {U3}) / (0 - {z1})'
f1 = sympify(form1)
f2 = sympify(form2)
f3 = sympify(form3)
f4 = sympify(form4)
f5 = sympify(form5)
f6 = sympify(form6)
f7 = sympify(form7)
f8 = sympify(form8)
d_f2 = diff(f2, x, 2)
d_f3 = diff(f3, x, 2)
d_f4 = diff(f4, x, 2)
d_f5 = diff(f5, x, 2)
d_f6 = diff(f6, x, 2)
d_f7 = diff(f7, x, 2)
dd_f2 = diff(f2, x, 4)
dd_f3 = diff(f3, x, 4)
dd_f4 = diff(f4, x, 4)
dd_f5 = diff(f5, x, 4)
dd_f6 = diff(f6, x, 4)
dd_f7 = diff(f7, x, 4)

file = open('potential.csv', 'w')
while abs(f1.evalf(subs={x: a}) - f2.evalf(subs={x: a})) < 0.1 and a < z1:
    values = []
    for b in range(0, 10):
        func = f1.evalf(subs={x: a})
        values.append(func)
    for i in values:
        file.write(str(i) + ', ')
    file.write('\n')
    a += 0.1

while a < z1:
    values = []
    for b in range(0, 10):
        func = f2.evalf(subs={x: a}) - ((b / 2) ** 2) * d_f2.evalf(subs={x: a}) + 0.25 * ((b / 2) ** 4) * dd_f2.evalf(subs={x: a})
        values.append(func)
    for i in values:
        file.write(str(i) + ', ')
    file.write('\n')
    a += 0.1

while abs(f3.evalf(subs={x: a}) - f4.evalf(subs={x: a})) > 1 and a < z2:
    values = []
    for b in range(0, 10):
        func = f3.evalf(subs={x: a}) - ((b / 2) ** 2) * d_f3.evalf(subs={x: a}) + 0.25 * ((b / 2) ** 4) * dd_f3.evalf(subs={x: a})
        values.append(func)
    for i in values:
        file.write(str(i) + ', ')
    file.write('\n')
    a += 0.1

while a < z2:
    values = []
    for b in range(0, 10):
        func = f4.evalf(subs={x: a}) - ((b / 2) ** 2) * d_f4.evalf(subs={x: a}) + 0.25 * ((b / 2) ** 4) * dd_f4.evalf(subs={x: a})
        values.append(func)
    for i in values:
        file.write(str(i) + ', ')
    file.write('\n')
    a += 0.1

while abs(f5.evalf(subs={x: a}) - f6.evalf(subs={x: a})) > 1 and a < z3:
    values = []
    for b in range(0, 10):
        func = f5.evalf(subs={x: a}) - ((b / 2) ** 2) * d_f5.evalf(subs={x: a}) + 0.25 * ((b / 2) ** 4) * dd_f5.evalf(subs={x: a})
        values.append(func)
    for i in values:
        file.write(str(i) + ', ')
    file.write('\n')
    a += 0.1

while a < z3:
    values = []
    for b in range(0, 10):
        func = f6.evalf(subs={x: a}) - ((b / 2) ** 2) * d_f6.evalf(subs={x: a}) + 0.25 * ((b / 2) ** 4) * dd_f6.evalf(subs={x: a})
        values.append(func)
    for i in values:
        file.write(str(i) + ', ')
    file.write('\n')
    a += 0.1

while abs(f7.evalf(subs={x: a}) - f8.evalf(subs={x: a})) > 0.1 and a < z3 + z1:
    values = []
    for b in range(0, 10):
        func = f7.evalf(subs={x: a}) - ((b / 2) ** 2) * d_f7.evalf(subs={x: a}) + 0.25 * ((b / 2) ** 4) * dd_f7.evalf(subs={x: a})
        values.append(func)
    for i in values:
        file.write(str(i) + ', ')
    file.write('\n')
    a += 0.1

while a < z3 + z1:
    values = []
    for b in range(0, 10):
        func = f8.evalf(subs={x: a})
        values.append(func)
    for i in values:
        file.write(str(i) + ', ')
    file.write('\n')
    a += 0.1
