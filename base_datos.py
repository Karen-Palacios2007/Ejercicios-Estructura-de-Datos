# Se crea la clase "Base_Datos" junto con sus metodos
class Base_Datos:

# Se inicializa con unico atributo tipo Lista en donde se agregaran todos los numeros   
    def __init__(self):
        self.lista_numeros=[]
        self.tupla_pares = []
        self.tupla_impares = []    

# Se guardan los datos anteriormente digitados (.append())
    def guardarDatos(self,datoNumero):
        self.lista_numeros.append(datoNumero)
        print(f"\nLista con datos agregados: {self.lista_numeros}")
        
# Se inserta una nueva sublista para extenderla (.extend())
    def insertarLista(self,nuevaLista):
        self.lista_numeros.extend(nuevaLista)
        print("\nLa lista extendida es: ",self.lista_numeros)

# Se insertan datos a la lista, dependiendo de la posiciónque se indique (.insert())
    def almacenarDato(self,posicion,sublista):
        self.lista_numeros.insert(posicion,sublista)
        print(f"\nLista con los nuevos datos insertados: {self.lista_numeros}")

# Se elimina los datos de la sublista que se encuentre en la posición que se indique (.pop())    
    def eliminarDato(self,posicion,):
        numeroEliminado=self.lista_numeros.pop(posicion)
        print(f"\nEl dato {numeroEliminado} ha sido eliminado")
        print(f"Lista actualizada: {self.lista_numeros}")
           
# Se elimina la sublista que contenga los números ingresados (.remove())
    def remover(self,datos):
        self.lista_numeros.remove(datos)
        print("\nLista actualizada con datos removidos: ",self.lista_numeros)
        
# Muestra la posición de la sublista que contenga los números ingresados (.index())        
    def mostrarPosicion(self,datos):
        print(f"\nLos datos {datos} se encuentran en posición ", {self.lista_numeros.index(datos)})
        
# Muestra la posición de la sublista que contenga los números ingresados (.index())        
    def mostrarContador(self,datos):
        print(f"\nLos datos {datos} se repiten {self.lista_numeros.count(datos)} veces")

# Ordena las sublistas ingresadas de forma ascendente (.sort())        
    def ordenAscendente(self):
        self.lista_numeros.sort()
        print ("\nLa lista ordenada ascendentemente es: ", self.lista_numeros)

# Ordena las sublistas ingresadas de forma descendente (.reverse())        
    def ordenDescendente(self):
        self.lista_numeros.reverse()
        print ("\nLa lista ordenada descendentemente es: ", self.lista_numeros)

# Muestra la tupla de números pares
    def mostarPares(self, numero):
        self.tupla_pares.append(numero)

# Muestra la tupla de números impares
    def mostarImares(self, numero):
        self.tupla_impares.append(numero) 
                
# Se muestra el elemento encontrado en el indice que se que se indique
    def verNumero(self,posicion):
        numero=self.lista_numeros.index(posicion)
        return numero

