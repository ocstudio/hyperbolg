#reto de la calse python presupuesto trimestre 

budget_enero = int(input('¿Cual es el presupuesto de enero? '))
budget_febrero = int(input('¿Cual es el presupuesto de febrero? '))
budget_marzo = int(input('¿Cual es el presupuesto de marzo? '))
 
suma_budget = (budget_enero+ budget_febrero+ budget_marzo)

promedio = (suma_budget) / 3

print('Total trimestre ', suma_budget)

print('Promedio ingreso ', promedio)


