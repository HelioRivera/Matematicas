import math
class Numeros_primos:
    def es_primo(self, numero):
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





