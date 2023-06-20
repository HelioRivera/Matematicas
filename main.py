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

    primo = np.Numeros_primos()
    # flag = primo.es_primo(1)
    # print(flag)
    numero = int(input("Ingresa un número: "))
    cuantos_primos = primo.cuantos_primos_antes_que_n(numero)
    resto= numero % cuantos_primos
    if resto == 0:
        print(cuantos_primos , "es divisor de ", numero)
    else:
        print(cuantos_primos , "no es divisor de ", numero)