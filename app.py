def add_numbers(a, b):
<<<<<<< HEAD
    return a+b
def subtract_numbers(a , b):
    return a - b
def multiply_numbers(a,b):
    return a* b
def divide_numbers(a, b):
    if b== 0:
        raise ValueError("Dzielenie przez zero jest niedozwolone.")
    return a /b

if __name__ == "__main__":
    num1 = 10
    num2 = 5
    print(f"Dodawanie: {add_numbers(num1, num2)}")
    print(f"Odejmowanie: {subtract_numbers(num1, num2)}")
    print(f"Mnożenie: {multiply_numbers(num1, num2)}")
    print(f"Dzielenie: {divide_numbers(num1, num2)}")

=======
    return a + b
def subtract_numbers(a, b):
    return a - b
def multiply_numbers(a, b):
    return a * b
def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Dzielenie przez zero jest niedozwolone.")
    return a / b
if __name__ == "__main__":
 num1 = 10
 num2 = 5
 print(f"Dodawanie: {add_numbers(num1, num2)}")
 print(f"Odejmowanie: {subtract_numbers(num1, num2)}")
 print(f"Mnożenie: {multiply_numbers(num1, num2)}")
 print(f"Dzielenie: {divide_numbers(num1, num2)}")
>>>>>>> e533da87127c19d41a472b19c04e96ceefcd44c9
