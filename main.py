import numeros_primos as np
if __name__=='__main__':

    # recuperar una variable desde el teclado
    # print("Ingrese los coeficientes de la ecuacion (a,b y c): ")
    # a = float(input("a: "))
    # b = float(input("b: "))
    # c = float(input("c: "))
    # ecuacion_cuadratica =  Ecuacion_cuadratica()
    # raices = calcular_raices(a, b, c)
    # print(raices)
    # expresion = input("Ingresa una operación: ")
    # resultado = resolver_operacion(expresion)
    # print("El resultado es:", resultado)

    es_primo = np.Numeros_primos()
    numero = int(input("Ingresa un número: "))
    valor = es_primo.es_primo(numero)
    print("es_primo = " + str(valor))