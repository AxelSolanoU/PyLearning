def get_user_numbers() -> int:

	TEST1 = int(input("Dame el número 1: "))
	TEST2 = int(input("Dame el número 2: "))

	return TEST1, TEST2


def get_wanted_operation():
	
	operacion = input("Qué operación? (+, -, /, *)")

	if operacion in ["+", "-", "/", "*"]:
		return operacion

	else:

		print(f"{operacion} no es una operación valida.")
		get_wanted_operation()


def sum_numbers(numero1, numero2):

	return numero1 + numero2

def subtract_numbers(numero1, numero2):
	
	return numero1 - numero2

def divide_numbers(numero1, numero2):
	
	return numero1 / numero2

def multiply_numbers(numero1, numero2):
	
	return numero1 * numero2

def show_user_result(para_imprimir):
	
	print(para_imprimir)
