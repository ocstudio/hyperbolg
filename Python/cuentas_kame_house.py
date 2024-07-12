#input para la contabilida de kame-house

fecha = input('¿cual es la fecha de factura?')
print (fecha)
#fecha = True

mes = input('¿Cual es el mes ?')
print (mes)

descripcion = input('Descripcion de la compra ')
print (descripcion)

categoria = input('¿Cual es la categoria de gasto o ingreso? ')
print (categoria)

ingreso = input('¿Valor del ingreso? ')
print (ingreso)

gasto = input('¿Valor del gasto? ') 
print (gasto)

full_line = fecha + "|" + mes + "|" + descripcion + "|" + categoria + "|" + ingreso + "|" + gasto + "|"
print(full_line)
