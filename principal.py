# Codigo principal
from formulario import Calculadora
# Se crea una instancia de la clase calculadora, que es quien contiene los metodos a ejecutar
calculadora=Calculadora()

# Se hace llamado de cada uno de los metodos para que las funciones se ejecuten

num1,num2=calculadora.pedirNumero()

calculadora.almacenarDatos(num1,num2)

calculadora.agregarLista()

dato=calculadora.añadirDato()

numero=calculadora.eliminarNumero()

mostrar=calculadora.mostrarNumero()