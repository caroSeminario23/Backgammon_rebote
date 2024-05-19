# FUNCION PARA CONVERTIR UN COLOR EN FORMATO HEXADECIMAL A RGB
def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

# DEFINICION DE COLORES
NEGRO = hex_to_rgb("#000000")
VERDE = hex_to_rgb("#a8c99e")
PLOMO = hex_to_rgb("#D9D9D9")
AMARILLO = hex_to_rgb("#efd8a4")
MELON_CLARO = hex_to_rgb("#e8ae96")
MELON_OSCURO = hex_to_rgb("#e49d89")
ROJO = hex_to_rgb("#e47f83")
MELON_TRASLUCIDO = hex_to_rgb("D9D9D9") # Agregar 60% de opacidad "superficie_transparente.set_alpha(255 * 0.6)
BEIGE = hex_to_rgb("#FEFAE4")
PLOMO2 = hex_to_rgb("#FCFCFC")