# Se importa la Clase "Lista_numeros" de "lista_numeros.py"
from lista_numeros import Lista_numeros

# Creación de una instancia de la clase importada
lista=Lista_numeros()

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
        posicion=int(input(f"\nDigite la posición en que desea insertar la sublista: ")) 
        lista.almacenarDato(posicion)          
        return posicion

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