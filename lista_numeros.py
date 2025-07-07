# Se crea la clase "Lista_numeros" junto con sus metodos
class Lista_numeros:

# Se inicializa con unico atributo tipo Lista en donde se agregaran todos los numeros   
    def __init__(self):
       self.lista_numeros=[]

# Se guardan los datos anteriormente digitados (.append())
    def guardarDatos(self,datoNumero):
        self.lista_numeros.append(datoNumero)
        print(self.lista_numeros)
        
# Se inserta una nueva sublista para extenderla (.extend())
    def insertarLista(self,nuevaLista):
        self.lista_numeros.extend(nuevaLista)
        print("La lista extendida es: ",self.lista_numeros)

# Se insertan datos a la lista, dependiendo de la posiciónque se indique (.insert())
    def almacenarDato(self,posicion):
        lista2=["7","5"]
        self.lista_numeros.insert(posicion,lista2)
        print(self.lista_numeros)
        return lista2

# Se elimina los datos de la sublista que se encuentre en la posición que se indique (.pop())    
    def eliminarDato(self,posicion,):
        numeroEliminado=self.lista_numeros.pop(posicion)
        print(f"Lista actualizada: {self.lista_numeros}")
        print(f"El elemento {numeroEliminado} ha sido eliminado")
        return numeroEliminado

# Se muestra el elemento encontrado en el indice que se que se indique
    def verNumero(self,posicion):
        numero=self.lista_numeros[posicion]
        return numero        
    
