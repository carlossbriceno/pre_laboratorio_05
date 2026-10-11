def consultar_existencia(posicion: int):
    # Cuerpo de la función con sangría (indentación)
    if posicion == 0:
     salida="Sin existencia"
    else:
     if posicion >=1 and posicion <=5:
       salida="Existencia baja"
     else:
       if posicion > 5:
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

