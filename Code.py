import matplotlib.pyplot as plt  # Se importa la librería matplotlib para poder graficar

# Se define una función que evalúa el polinomio en un valor de x
def evaluar_polinomio(coeficientes, x):
    # Se inicializa la variable resultado en 0
    resultado = 0
    # Se calcula el grado del polinomio restando 1 al tamaño de la lista
    grado = len(coeficientes) - 1
    # Se recorre la lista de coeficientes con un ciclo for
    for i in range(len(coeficientes)):
        # Se suma al resultado el coeficiente multiplicado por x elevado a la potencia correspondiente
        resultado += coeficientes[i] * (x ** (grado - i))
    # Se devuelve el resultado final
    return resultado

# Se define una función que grafica el polinomio
def graficar_polinomio(coeficientes):
    # Se crea una lista de valores de x desde -10 hasta 10 con un paso de 1
    x = list(range(-10, 11))
    # Se calcula el valor del polinomio para cada número de la lista x
    y = [evaluar_polinomio(coeficientes, xi) for xi in x]
    # Se dibuja la gráfica con los valores de x y y
    plt.plot(x, y)
    # Se dibuja la línea horizontal en y=0
    plt.axhline(0, color='black')
    # Se dibuja la línea vertical en x=0
    plt.axvline(0, color='black')
    # Se muestra la gráfica en pantalla
    plt.show()

# Se pide al usuario que ingrese el grado del polinomio
grado = int(input("Ingrese el grado del polinomio: "))
# Se crea una lista vacía para guardar los coeficientes
coeficientes = []
# Se recorre desde el grado hasta 0 para pedir cada coeficiente
for i in range(grado, -1, -1):
    # Se pide al usuario que ingrese el coeficiente correspondiente
    coef = int(input(f"Ingrese el coeficiente para x^{i}: "))
    # Se agrega el coeficiente a la lista
    coeficientes.append(coef)

# Se llama a la función para graficar el polinomio con los coeficientes ingresados
graficar_polinomio(coeficientes)
