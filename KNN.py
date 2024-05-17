def classify(Clasificar_x, Clasificar_y):
    x = [150, 170, 50, 20, 150, 30]
    y = [60, 80, 3, 7, 70, 10]
    z = ["A", "A", "B", "B", "A", "B"]

    # Calcular las diferencias entre los números a clasificar y los números en las listas x e y
    diferencias_x = [Clasificar_x - num for num in x]
    diferencias_y = [Clasificar_y - num for num in y]

    # Imprimir las diferencias
    print("Diferencias para 'x':", diferencias_x)
    print("Diferencias para 'y':", diferencias_y)

    # Calcular las potencias de 2 de las diferencias
    potencia_diferencias_x = [dif ** 2 for dif in diferencias_x]
    potencia_diferencias_y = [dif ** 2 for dif in diferencias_y]

    # Imprimir las potencias de 2 de las diferencias
    print("Potencias de 2 para 'x':", potencia_diferencias_x)
    print("Potencias de 2 para 'y':", potencia_diferencias_y)

    # Suma de potencias de 2
    suma_potencias = [px + py for px, py in zip(potencia_diferencias_x, potencia_diferencias_y)]

    # Imprimir la suma de las potencias de 2
    print("Suma de potencias de x^2 + y^2:", suma_potencias)

    # Calcular la raíz cuadrada de la suma de potencias
    raiz_suma_potencias = [suma ** 0.5 for suma in suma_potencias]

    # Imprimir la raíz cuadrada de la suma de potencias
    print("Raíz cuadrada de la suma de potencias:", raiz_suma_potencias)

    # Relacionar las distancias con las etiquetas z
    distancias_con_etiquetas = list(zip(raiz_suma_potencias, z))

    # Ordenar las distancias de menor a mayor
    distancias_con_etiquetas.sort(key=lambda x: x[0])

    # Imprimir las distancias ordenadas con sus etiquetas
    print("Distancias ordenadas con etiquetas:", distancias_con_etiquetas)

    # Tomar las tres distancias más cortas
    tres_mas_cortas = distancias_con_etiquetas[:3]

    # Contar las etiquetas 'A' y 'B' entre las tres distancias más cortas
    conteo_A = sum(1 for _, etiqueta in tres_mas_cortas if etiqueta == 'A')
    conteo_B = sum(1 for _, etiqueta in tres_mas_cortas if etiqueta == 'B')

    # Determinar la etiqueta predominante
    resultado = 'A' if conteo_A > conteo_B else 'B'

    return resultado

# Código para probar la función manualmente
if __name__ == "__main__":
    Clasificar_x = int(input('Ingresar número a clasificar x: '))
    Clasificar_y = int(input('Ingresar número a clasificar y: '))
    resultado = classify(Clasificar_x, Clasificar_y)
    print("Resultado de la clasificación:", resultado)
