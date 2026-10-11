def consultar_existencia(mi_lista:list,posicion: int):
    # Cuerpo de la función con sangría (indentación)
    cantidad = mi_lista[posicion]

    if cantidad == 0:
     salida="Agotado"
    else:
     if cantidad >=1 and cantidad <=5:
       salida="Existencia baja"
     else:
       if cantidad > 5:
         salida="Existencia suficiente"
       else:
         salida="Dato inválido"
    resultado = salida 
    return resultado

def retirar_articulo(mi_lista:list,posicion:int,cantidad:int):
    existencia = mi_lista[posicion]
    if  existencia <= 0:
        resultado = "no tiene existencia"
    else: 
            if existencia >= cantidad:
                        mi_lista[posicion]=existencia - cantidad
                        resultado = "producto retirado"
            else: 
                resultado = "no hay porducto disponible"
    return resultado

def reponer_existencia(mi_lista:list,posicion:int,cantidad:int):
    if cantidad <=0:
     resultado = "cantidad insuficiente"
    else:   
        existencia = mi_lista[posicion]
        mi_lista[posicion]=existencia + cantidad 
        resultado = "articulo repuesto"
    return resultado 
