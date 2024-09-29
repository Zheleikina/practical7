import random
import string

def generate():
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    
    numbers = ''.join(random.choices(string.digits, k=5))
    
    return letters + ' ' + numbers

def generate_N(N):
    plates = [generate() for _ in range(N)]
    return plates

N = int(input("Введіть кількість номерів для генерації: "))
license_plates = generate_N(N)

for plate in license_plates:
    print(plate)