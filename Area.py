v = input().split()
a = float(v[0])
b = float(v[1])
c = float(v[2])

triangulo = (a * c) / 2
circulo = (3.14159 * c**2)
trapezio = ((a + b) * c) /2
quadrado = b**2
retangulo = a * b

print("Triangulo {:.3f}" .format(triangulo))
print("Circulo {:.3f}" .format(circulo))
print("Trapezio {:.3f}" .format(trapezio))
print("Quadrado {:.3f}" .format(quadrado))
print("Retangulo {:.3f}" .format(retangulo))