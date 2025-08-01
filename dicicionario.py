# Se crea la estructura del diccionario
mi_diccionario={"Nombre":"Juan","Edad":30,"Ciudad":"Madrid"}
mi_diccionario2={"Nombre":"Maria","Edad":22,"Ciudad":"Medellin"}

# Acceder a los valores a través de las claves
print(mi_diccionario["Nombre"])
print(mi_diccionario["Edad"])
print(mi_diccionario["Ciudad"])

# Agregar un nuevo elemento al diccionario
mi_diccionario["Profesion"]="Ingeniero"
print(mi_diccionario)

# Modificar un valor existente en el diccionario
mi_diccionario["Edad"]=35
print(mi_diccionario)

# Eliminar un elemento del diccionario
del mi_diccionario["Profesion"]
print(mi_diccionario)

# Recorrido por tamaño de lista
for clave  in range(len(mi_diccionario.keys())):
    print("posición index diccionario: "+str(clave))
    
# Recorrido por tamaño de la lista
for i in range(len(mi_diccionario.items())):
    clave=list(mi_diccionario.keys())[i]
    mi_diccionario[clave]="Cúcuta"
    print("La posición que se actualiza: "+str(clave))
    print("Se actualiza datos: "+str(mi_diccionario))
    
#Recorrido por la clave del diccionario
for clave in mi_diccionario.keys():
    mi_diccionario["Nombre"]="Diego"
    print("Nombre actualizado: "+str(clave))
    
# Recorrido y asignación por items
for clave, valor in mi_diccionario.items():
    mi_diccionario["Edad"]=40
    print("El diccionario actualizado: "+clave, valor)
 
#--------------------CREACIÓN DE MENÚ-------------------------   
while True:
    print ("\nMENU:")
    print ("1. Mostrar diccionario")
    print ("2. Obtener la longitud del diccionario")
    print ("3. Obtener el valor de acuerdo a su clave")    
    print ("4. Realizar una copia del diccionario")
    print ("5. Obtener keys del diccionario")
    print ("6. Obtener valores almacenados")
    print ("7. Eliminar item especíifco")    
    print ("8. Eliminar último item")    
    print ("9. Actualizar key")    
    print ("10. Actualizar items de diccionario a otro")    
    print ("11. Eliminar todos los items del diccionario")
    print ("0. Salir")
# Variable que almacenara lo que digite la persona    
    opc=input("\n Digite su opción: \n ")
    
    try:
# Se inicializa "match case" para ejecutar las acciones
        match opc:
            case "1":
                dato=mi_diccionario.items()
                print(dato)
            case "2":
                long=len(mi_diccionario)
                print(long)
            case "3":
                op=input("Digite la posición del valor que desea conocer: ")
                match op:
                    case "1":
                        valor=mi_diccionario.get("Nombre")
                        print(valor)
                    case "2":
                        valor=mi_diccionario.get("Edad")
                        print(valor)
                    case "3":
                        valor=mi_diccionario.get("Ciudad")
                        print(valor)
                    
            case "4":
                copia=mi_diccionario.copy()
                print(copia)
            case "5":
                keys=mi_diccionario.keys()
                print(keys)
            case "6":
                valores=mi_diccionario.values()
                print(valores)
            case "7":
                clave=input("Digite la llave que desea eliminar: ").lower()
                match clave:
                    case "nombre":
                        eliminar=mi_diccionario.pop("Nombre")
                        print(eliminar)
                    case "edad":
                        eliminar=mi_diccionario.pop("Edad")
                        print(eliminar)
                    case "ciudad":
                        eliminar=mi_diccionario.pop("Ciudad")
                        print(eliminar)
            case "8":
                eliminar=mi_diccionario.popitem()
                print(eliminar)
            case "9":
                default=mi_diccionario.setdefault("Clase","Python")
                print(default)
            case "10":
                mi_diccionario.update(mi_diccionario2)
                print(mi_diccionario)                
            case "11":
                limpiar=mi_diccionario.clear()
                print(limpiar)
            case "0":
                print("\nSaliendo del sistema...")
                break
            
        
    except ValueError:
        print ("Digite una opción valida")




