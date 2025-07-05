from formulario import Calculadora
class lista_numeros:
    
    def __init__(self):
        self.Lista_numeros=[]
        
    def guardar_dato(self,dato_numero):
        self.Lista_numeros.append(dato_numero)  
    
    def incluir_listas(self,dato_numero):      
        self.Lista_numeros.extend(dato_numero)  
        print(self.Lista_numeros)
    def insertar_datos(self):
        self.Lista_numeros.insert(0,2)  
    def eliminar_datos(self):
        self.Lista_numeros.pop(2)  
    def ver_numero(self):
        pass   

    