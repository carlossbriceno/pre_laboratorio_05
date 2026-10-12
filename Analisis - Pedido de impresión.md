Analisis - Pedido de impresión
•Entradas y salidas, especificando los tipos de datos esperados.
Entradas : 
cantidad de paginas de cada de apuntes (numero)
cantidad de paginas de cada de  Guía de ejercicios (numero)
cantidad de paginas de cada de Material de consulta (numero)

Salidas :
total de paquetes aceptados (numero)
total de paginas  (numero)
sub total (numero)
descuento (numero)
total a pagar (decimal)
• Restricciones explícitas e implícitas.
Explícitas :
cada paquete debe tener entre 1 y 50 paginas 
Se permite un solo intento por paquete 
El paquete omitido se excluye 
Si no se acepto ningun paquete no se genera ningun Pedido
implícitas :
Las entradas deben ser un numero
• Ambigüedades. Si no identifican ninguna, justifiquen la respuesta.
El enunciado no especifica si los importes deben redondearse .
 Dado que cada página cuesta 2 unidades monetarias, el subtotal siempre
  será un número par. Sin embargo, al aplicar un descuento del 10% sobre
   un subtotal impar (por ejemplo, si el total de páginas es 51, el subtotal 
   es 102, y el 10% de descuento es 10.2), el resultado incluye decimales.
• Precondiciones y postcondiciones del programa y de calcular_subtotal.
percondiciones :
Las paginas de cada paquete deben tener entre 1 y 50
Cada paquete se usara una sola vez 
postcondiciones :
Si la cantidad es mayor a 100 se le aplica un descuento 
