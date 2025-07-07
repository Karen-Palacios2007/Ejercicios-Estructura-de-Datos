class lista_numeros:
    
    def __init__(self):
        self.Lista_numeros=[]
        
    def guardar_dato(self,dato_numero):
        self.Lista_numeros.append(dato_numero) 
        print("Lista actual: ",self.Lista_numeros)
 
    def incluir_listas(self,dato_numero):
        numero3=input("Numero 3: ")
        numero4=input("Numero 4: ")
        dato_numero=[[numero3,numero4]]
        self.Lista_numeros.extend(dato_numero)  
        print(f"Lista extendida: {self.Lista_numeros}")
        
    def insertar_datos(self):
        datos = input("Digite el número que desea insertar: ")
        posicion = int(input("Digite la posición donde insertarlos: "))
        self.Lista_numeros.insert(posicion, datos)
        print("Dato insertado:", self.Lista_numeros)
            
    def eliminarPorIndice(self):
        if len(self.Lista_numeros) > 0:
            try:
                while True:
                    posicion_eliminar=int(input("Digite la posición del numero a eliminar: "))            
                    if posicion_eliminar<len(self.Lista_numeros):
                        self.Lista_numeros.pop(posicion_eliminar)
                        print(f"Elemento en posición {posicion_eliminar} eliminado: {self.Lista_numeros}")  
                        break
                    else:
                        print ("Posición fuera de rango, intente nuevamente: ")
            except ValueError:
                print("Debes ingresar un número")
        else:
            ("La lista esta vacía..")
             
    def eliminarPorValor(self): 
        valor = input("Digite el valor que desea eliminar: ")
        encontrado = False
        for sublista in self.Lista_numeros:
            if isinstance(sublista, list) and valor in sublista:
                sublista.remove(valor)
                print(f"Se eliminó el valor '{valor}':", self.Lista_numeros)
                encontrado = True
                break
        if not encontrado:
            print(f"El valor '{valor}' no se encontró en la lista.")
            
    def mostrarPosicion(self):
        numero = input("Digite el valor del cual quiera conocer la posición: ")
        encontrado = False

        for i, sublista in enumerate(self.Lista_numeros):
            if isinstance(sublista, list) and numero in sublista:
                posicion = sublista.index(numero)
                print(f"El número '{numero}' se encuentra en la sublista {i}, posición {posicion}")
                encontrado = True
                break

        if not encontrado:
            print(f"El número '{numero}' no se encontró en la lista.")

    