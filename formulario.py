from lista_dato import lista_numeros

objlista=lista_numeros()

class Calculadora:
    
    def pedir_numero(self):
        numero1=input("Numero 1: ")
        numero2=input("Numero 2: ")
        return numero1,numero2
    
    def almacenarDatos(self,dato1,dato2):
        dato_numero=[[dato1,dato2]]
        objlista.incluir_listas(dato_numero)
        objlista.insertar_datos(dato_numero)
        
calculadora=Calculadora()
dato1,dato2=calculadora.pedir_numero()
calculadora.almacenarDatos(dato1,dato2)

dato1,dato2=calculadora.pedir_numero()
calculadora.almacenarDatos(dato1,dato2)

dato1,dato2=calculadora.pedir_numero()
calculadora.almacenarDatos(dato1,dato2)

dato1,dato2=calculadora.pedir_numero()
calculadora.almacenarDatos(dato1,dato2)

        
    
        
    
    