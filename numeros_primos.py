import math
class Numeros_primos:

    def es_primo(self, numero):
        if numero == 1:
            return False
        else:
            valor = self._calcula_factorial(numero-1)
            valor = valor + 1
            if self._es_multiplo_de_n(valor,numero):
                return True
            else:
                return False


    def _calcula_factorial(self, numero):
        factorial = 1
        for i in range(1, numero+1):
            factorial = factorial * i
        return factorial

    def _es_multiplo_de_n(self, valor,numero):
        resto = valor % numero
        if resto == 0:
            return True
        else:
            return False

    # sea P el numero de primos menores que n se sabe que P es divisor de n#
    def cuantos_primos_antes_que_n(self, numero):
        contador = 0
        for i in range(2, numero):
            if Numeros_primos.es_primo(self, i):
                contador = contador + 1
        return contador





