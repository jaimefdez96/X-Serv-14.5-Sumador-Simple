#!/usr/bin/python3
#Jaime Fernández Sánchez
#Calculadora 2.0
import sys



def suma(Operando_1,Operando_2):
    return Operando_1 + Operando_2

def resta(Operando_1,Operando_2):
    return Operando_1 - Operando_2

def multiplicacion(Operando_1,Operando_2):
    return Operando_1 * Operando_2

def division(Operando_1,Operando_2):
    try:
        return Operando_1 / Operando_2
    except ZeroDivisionError:
        return("Error: Intento de division entre 0")
def potencia(Operando_1,Operando_2):
    return Operando_1 ** Operando_2

Operaciones = {
    "suma": suma,
    "resta": resta,
    "multiplicacion": multiplicacion,
    "division": division,
    "potencia": potencia
}

        
if __name__ == '__main__':

    MAX_ARGS = 4

    if len(sys.argv) != MAX_ARGS:
        sys.exit("Error de uso: [Operador][Operando1][Operando2] ")

    try:
        Operador = sys.argv[1]
        Operando_1 = float(sys.argv[2])
        Operando_2 = float(sys.argv[3])

    except IndexError:
        sys.exit("Error de uso: [Operador][Operando1][Operando2] ")
    except ValueError:
        sys.exit("Por favor, introduzca solamente números como operandos (argumentos 2 y 3). Gracias")

    try:
        resultado = Operaciones[Operador](Operando_1,Operando_2)
    except KeyError:
        sys.exit("No existe la funcion" + Operador)