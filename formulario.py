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
        Dato1=input("\nDato 1:")
        Dato2=input("Dato 2:")
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
                
# Se remueve la sublista que contenga los datos digitados      
    def removerDato(self):
        while True:
            try:
                print("\nDigite los datos exactos de la sublista a eliminar ")
                dato1=input("Dato 1:")
                dato2=input("Dato 2:")
                datos=([dato1,dato2])
                lista.remover(datos)
            except ValueError:
                print("Los números no se han encontrado en una sublista, intente nuevamente:\n")

# Se obtiene la posición de la sublista que contenga los datos digitados                 
    def buscarIndice(self):
        while True:
            try:
                print("\nDigite los datos exactos de la sublista que desea conocer la posición ")
                dato1=input("Dato 1:")
                dato2=input("Dato 2:")
                datos=([dato1,dato2])
                lista.mostrarPosicion(datos)
            except ValueError:
                print("Los números no se han encontrado en una sublista, intente nuevamente:\n")

# Se obtiene la cantidad de veces que se repiten los datos de una sublista en otra              
    def contador(self):
        while True:
            try:
                print("\nDigite los datos exactos de la sublista que desea conocer la posición ")
                dato1=input("Dato 1:")
                dato2=input("Dato 2:")
                datos=([dato1,dato2])
                lista.mostrarContador(datos)
            except ValueError:
                print("Los números no se han encontrado en una sublista, intente nuevamente:\n")
       
    
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

#Se recibe la lista ordenada ascendentemente              
    def mostrarAscendencia(self):
        lista.ordenAscendente()
        
#Se recibe la lista ordenada descendentemente                      
    def mostrarDescendencia(self):
        lista.ordenDescendente()
        
        
#***************************************CODIGO PRINCIPAL**************************************************

# Se crea una instancia de la clase calculadora, que es quien contiene los metodos a ejecutar
calculadora=Calculadora()

# Se hace la creación del Menu
while True:    
    try:
        print("\nMENÚ")
        print("Digite el número de la acción que desea realizar:\n")
        print("\n1. Agregar un par de números a la lista")
        print("2. Eliminar un par de datos ya existente dependiendo de su posición")
        print("3. Insertar un nuevo par de datos")
        print("4. Remover un par de datos de acuerdo a su valores")
        print("5. Conocer la posición de una sublista")
        print("6. Contar y mostrar las veces que una sublista se repite")
        print("7. Ordenar las sublistas ingresadas de forma ascendente")
        print("8. Ordenar las sublistas ingresadas de forma descendente")
        print("9. Salir del sistema ")
        print("Seleccione una opción: ")
        opc=input(" ")

#Se hace uso de "match case" para verificar que la opción dígita sea valida para ejercutar una acción
        match opc:
            case "1":
                num1,num2=calculadora.pedirNumero()
                calculadora.almacenarDatos(num1,num2)                
            case "2":
                numero=calculadora.eliminarNumero()                
            case "3":
                dato=calculadora.añadirDato()                
            case "4":
                calculadora.removerDato()               
            case "5":
                calculadora.buscarIndice()
            case "6":
                calculadora.contador()            
            case "7":
                calculadora.mostrarAscendencia()            
            case "8":
                calculadora.mostrarDescendencia()            
            case "9":
                print("Saliendo del sistema...")
                break
            case _:
                print("Opción inválida, por favor ingrese un número válido del menú.")    
    except ValueError:
            print("Opción invalida, ingrese un número de acuerdo al menu")

