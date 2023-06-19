import math
class Ecuacion_cuadratica:

    def calcular_raices_ecuacion_cuadratica(self, a, b, c):

        discriminante = b**2 - 4*a*c
        if discriminante > 0:
            print("Calculando raíces...")
            print("Raíces reales y diferentes")
            raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
            raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
            return raiz1, raiz2
        elif discriminante == 0:
            print("Raíces reales e iguales")
            print("Calculando raíces...")
            raiz = -b / (2*a)
            return raiz
        else:
            return "No existen raíces reales"