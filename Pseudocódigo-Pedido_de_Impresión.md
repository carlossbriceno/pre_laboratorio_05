# Pseudocódigo: Pedido de Impresión

INICIO
    DEFINIR CONSTANTE PRECIO_PAGINA = 2
    DEFINIR LISTA paquetes = ["Apuntes", "Guía de ejercicios", "Material de consulta"]
    
    DEFINIR paquetes_aceptados = 0
    DEFINIR total_paginas = 0

    PARA indice DESDE 0 HASTA LONGITUD(paquetes) - 1 HACER
        MOSTRAR "Ingrese cantidad de páginas para " + paquetes[indice]
        LEER entrada_texto
        
        INTENTAR
            CONVERTIR entrada_texto A ENTERO num_paginas
            
            SI num_paginas >= 1 Y num_paginas <= 50 ENTONCES
                INCREMENTAR paquetes_aceptados EN 1
                INCREMENTAR total_paginas EN num_paginas
            SINO
                MOSTRAR "Páginas fuera de rango (1 a 50). Paquete omitido."
                CONTINUAR
            FIN SI
            
        EN CASO DE ERROR DE CONVERSIÓN
            MOSTRAR "Entrada inválida. Debe ser un número entero. Paquete omitido."
            CONTINUAR
        FIN INTENTAR
    FIN PARA

    SI paquetes_aceptados > 0 ENTONCES
        LLAMAR A calcular_subtotal(total_paginas, PRECIO_PAGINA) Y GUARDAR EN subtotal
        
        SI total_paginas > 100 ENTONCES
            descuento = subtotal * 0.10
        SINO
            descuento = 0
        FIN SI
        
        total_pagar = subtotal - descuento
        
        MOSTRAR "Paquetes aceptados:", paquetes_aceptados
        MOSTRAR "Total de páginas:", total_paginas
        MOSTRAR "Subtotal:", subtotal
        MOSTRAR "Descuento:", descuento
        MOSTRAR "Total a pagar:", total_pagar
    SINO
        MOSTRAR "No se generó un pedido."
        MOSTRAR "Paquetes aceptados: 0"
        MOSTRAR "Total de páginas: 0"
        MOSTRAR "Subtotal: 0, Descuento: 0, Total: 0"
    FIN SI
FIN