# Se importa la Clase "Lista_numeros" de "lista_numeros.py"
from base_datos import Base_Datos

# Creación de una instancia de la clase importada
lista=Base_Datos()

# Se crea la Clase "Calculadora" junto con sus metodos
class Calculadora():
    
# Se obtienen los numeros a insertar inicialmente en la lista
    def pedirNumero(self):
        num1=input("Numero 1: ")
        num2=input("Numero 2: ")
        return num1,num2

# Se almacenan los datos proporcionados
    def almacenarDatos(self,dato1,dato2):
        datoNumero=[dato1,dato2]
        lista.guardarDatos(datoNumero)
        
# Se obtiene los nuevos datos para extender la lista
    def agregarLista(self):
        print ("\nDigite dos nuevo datos para extender la lista: ")
        num1,num2=self.pedirNumero()
        nuevaLista=[num1,num2]
        lista.insertarLista([nuevaLista])
    
# Se obtiene la posición en donde se desea insertar el dato ya determinado  
    def añadirDato(self):
        Dato1=int(input("\nDato 1:"))
        Dato2=int(input("Dato 2:"))
        sublista=([Dato1,Dato2])
        posicion=int(input(f"\nDigite la posición en que desea insertar la sublista: ")) 
        lista.almacenarDato(posicion,sublista)          
        return posicion,sublista

# Se obtiene la posición del dato que se desea eliminar
    def eliminarNumero(self):
        while True:
            try:
                posicion=int(input("Digite la posición (entre 0-{}) del dato a eliminar: ".format(len(lista.lista_numeros)-1)))
                if posicion<len(lista.lista_numeros):
                    numeroEliminado=lista.eliminarDato(posicion)     
                    return numeroEliminado
                else: 
                    print("\ningrese una valor dentro del rango e intente nuevamente...")
            except ValueError:
                print("\ningrese una numero entero valido e intente nuevamente...")
            
# Se obtiene la posición del dato que desea conocer
    def mostrarNumero(self):
        while True:
            try:        
                posicion=int(input("Digite una posición (entre 0-{}) para conocer el numero que almacena: ".format(len(lista.lista_numeros)-1)))
                if posicion<len(lista.lista_numeros):
                    numero=lista.lista_numeros[posicion]
                    print(f"Dato en posición {posicion}: {numero}")
                    return posicion
                else: 
                    print("\ningrese una valor dentro del rango e intente nuevamente...")
            except ValueError:
                print("\ningrese una numero entero valido e intente nuevamente...")

# Codigo principal

# Se crea una instancia de la clase calculadora, que es quien contiene los metodos a ejecutar
calculadora=Calculadora()

aux=True
# Se hace la creación del Menu
while aux:    
    try:
        print("\nMENÚ")
        print("Digite el número de la acción que desea realizar:\n")
        print("\n1. Agregar un par de números a la lista")
        print("2. Eliminar un par de datos ya existente dependiendo de su posición")
        print("3. Insertar un nuevo par de datos")
        print("4. Remover un par de datos de acuerdo a su valores")
        print("5. Salir del sistema ")
        print("Seleccione una opción: ")
        opc=input(" ")
        match opc:
            case "1":
        #if opc=="1":
                num1,num2=calculadora.pedirNumero()
                calculadora.almacenarDatos(num1,num2)
                
            case "2":
                numero=calculadora.eliminarNumero()
                
            case "3":
                dato=calculadora.añadirDato()
                
            case "5":
                print("Saliendo del sistema...")
                aux = False
            case _:
                print("Opción inválida, por favor ingrese un número válido del menú.")
            

    except ValueError:
            print("Opción invalida, ingrese un número de acuerdo al menu")

    

    

# Se hace llamado de cada uno de los metodos para que las funciones se ejecuten

#calculadora.agregarLista()
#mostrar=calculadora.mostrarNumero()