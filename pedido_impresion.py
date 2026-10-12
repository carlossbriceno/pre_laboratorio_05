PRECIO_PAGINA = 2


def calcular_subtotal(total_paginas, precio_pagina):
    """Calcula y retorna el subtotal multiplicando las páginas por el precio."""
    return total_paginas * precio_pagina


def main():
    paquetes = ["Apuntes", "Guía de ejercicios", "Material de consulta"]
    paquetes_aceptados = 0
    total_paginas = 0

    for indice in range(len(paquetes)):
        nombre_paquete = paquetes[indice]
        entrada = input(f"Ingrese la cantidad de páginas para {nombre_paquete} (1-50): ")

        try:
            paginas = int(entrada)
        except ValueError:
            print(f"Entrada inválida. Se omitirá el paquete '{nombre_paquete}'.")
            continue

        if paginas < 1 or paginas > 50:
            print(f"Páginas fuera de rango (1-50). Se omitirá el paquete '{nombre_paquete}'.")
            continue

        paquetes_aceptados += 1
        total_paginas += paginas

    subtotal = calcular_subtotal(total_paginas, PRECIO_PAGINA)

    if total_paginas > 100:
        descuento = subtotal * 0.10
    else:
        descuento = 0.0

    total = subtotal - descuento

    print("\n--- RESUMEN DEL PEDIDO ---")
    if paquetes_aceptados == 0:
        print("No se generó un pedido.")
    
    print(f"Paquetes aceptados: {paquetes_aceptados}")
    print(f"Total de páginas: {total_paginas}")
    print(f"Subtotal: {subtotal}")
    print(f"Descuento: {descuento}")
    print(f"Total a pagar: {total}")


if __name__ == "__main__":
    main()