import math
import numpy as np
import matplotlib.pyplot as plt

class Optimizador:

    def __init__(self, a, b, tolerancia):
        self.a = a
        self.b = b
        self.tolerancia = tolerancia

    def calcular_n(self):
        n = int((self.b - self.a) / self.tolerancia)
        return n

    def buscar_minimo(self, funcion, mostrar_proceso=False):

        n = self.calcular_n()
        paso = (self.b - self.a) / n

        mejor_x = self.a
        mejor_valor = funcion(self.a)

        x = self.a

        for i in range(n + 1):

            valor_actual = funcion(x)

            if valor_actual < mejor_valor:
                mejor_valor = valor_actual
                mejor_x = x

            if mostrar_proceso:
                print("Iteracion:", i, "| x:", round(x, 4), "| f(x):", round(valor_actual, 4))

            x = x + paso

        return mejor_x, mejor_valor, n

def mostrar_resultados(nombre, funcion_texto, intervalo, resultado):

    x, valor, n = resultado

    print("\n====================================")
    print("Funcion:", nombre)
    print("Ecuacion:", funcion_texto)
    print("Intervalo:", intervalo)
    print("Numero de evaluaciones (n):", n)
    print("Mejor x encontrado:", round(x, 4))
    print("Valor minimo:", round(valor, 4))


#graficas
def graficar(funcion, a, b, nombre_archivo, titulo, x_min=None, y_min=None):

    x = np.linspace(a, b, 1000)
    y = funcion(x)

    plt.figure()
    plt.plot(x, y)
    
    # marcar el mínimo si se pasa
    if x_min is not None and y_min is not None:
        plt.scatter(x_min, y_min)
        plt.text(x_min, y_min, f"Min ({round(x_min,2)}, {round(y_min,2)})")

    plt.title(titulo)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()

    plt.savefig(nombre_archivo)
    plt.close()

#main
if __name__ == "__main__":

    tolerancia = 0.001

    print("====================================")
    print("OPTIMIZACION UNIDIMENSIONAL")
    print("Metodo: Busqueda Exhaustiva")
    print("Precision:", tolerancia)
    print("====================================")

#funcion1
    f1 = lambda x: x**2 - 4*x + 4
    opt1 = Optimizador(0, 5, tolerancia)

    resultado1 = opt1.buscar_minimo(f1)

    mostrar_resultados(
        "Funcion Cuadratica",
        "f(x) = x^2 - 4x + 4",
        "[0,5]",
        resultado1
    )

    graficar(f1, 0, 5, "grafica1.png", "Funcion Cuadratica")

#funcion2
    f2 = lambda x: x + np.sin(x)
    opt2 = Optimizador(0, 10, tolerancia)

    resultado2 = opt2.buscar_minimo(f2)

    mostrar_resultados(
        "Funcion Trigonometrica",
        "f(x) = x + sen(x)",
        "[0,10]",
        resultado2
    )

    graficar(f2, 0, 10, "grafica2.png", "Funcion Trigonometrica")

#funcion3
    f3 = lambda x: x**4 - 14*x**3 + 60*x**2 - 70*x
    opt3 = Optimizador(0, 5, tolerancia)

    resultado3 = opt3.buscar_minimo(f3)

    mostrar_resultados(
        "Funcion Polinomial",
        "f(x) = x^4 - 14x^3 + 60x^2 - 70x",
        "[0,5]",
        resultado3
    )

    graficar(f3, 0, 5, "grafica3.png", "Funcion Polinomial")

# resumen

    print("\n====================================")
    print("RESUMEN FINAL")
    print("====================================")

    print("Funcion 1 -> x:", round(resultado1[0],4), "| f(x):", round(resultado1[1],4))
    print("Funcion 2 -> x:", round(resultado2[0],4), "| f(x):", round(resultado2[1],4))
    print("Funcion 3 -> x:", round(resultado3[0],4), "| f(x):", round(resultado3[1],4))

    print("\nGraficas guardadas como:")
    print("grafica1.png, grafica2.png, grafica3.png")