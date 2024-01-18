from CalculatorFunc import (
get_user_numbers,
get_wanted_operation,
sum_numbers,
subtract_numbers,
divide_numbers,
multiply_numbers,
show_user_result
)

def Calculadora():

	# PEDIR NUMEROS AL USUARIO
	numero1, numero2 = get_user_numbers()

	# PEDIR OPEARACIÓN AL USUARIO
	operacion = get_wanted_operation()

	# SI LA OPERACIÓN ES "+"
	if operacion == "+":

		resultado = sum_numbers(numero1, numero2)

		show_user_result(resultado)


	# SI LA OPERACIÓN ES "-"
	if operacion == "-":

		resultado = subtract_numbers(numero1, numero2)

		show_user_result(resultado)


	# SI LA OPERACIÓN ES "/"
	if operacion == "/":

		resultado = divide_numbers(numero1, numero2)
		show_user_result(resultado)


	# SI LA OPERACIÓN ES "*"
	if operacion == "*":

		resultado = multiply_numbers(numero1, numero2)
		show_user_result(resultado)



if __name__ == '__main__':
	
	Calculadora()