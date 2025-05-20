int_var = 10
float_var = 10.5
str = "hello"
bool_var = True

print(int_var, type(int_var))
print(float_var, type(float_var))
print(str, type(str))
print(bool_var, type(bool_var))

#2
num1, num2, num3 = 7, 3, 5
print("Додавання:", num1 + num2)
print("Віднімання:", num1 - num2)
print("Множення:", num1 * num2)
print("Ділення:", num1 / num2)
print("Піднесення до степеня:", num1 ** num2)


print("Округлення:", round(5.678, 2))
print("Модуль числа:", abs(-15))
print("Остача від ділення:", num1 % num2)

average = (num1 + num2 + num3) / 3
print("Середнє арифметичне:", average)

#3
name = "Максим"
age = 17

print(name + " - це ваше ім'я.")
print(name.upper())
print(f"Моє ім'я {name}, мені {age} років.")

# 4
number = int(input("Введіть число: "))
if number % 2 == 0:
    print("Число парне.")
else:
    print("Число непарне.")

if 10 <= number <= 50:
    print("Число входить у діапазон від 10 до 50.")
else:
    print("Число не входить у діапазон від 10 до 50.")

# 5
for i in range(1, 11):
    print(i)


sum_numbers = 0
i = 1
while i <= 100:
    sum_numbers += i
    i += 1
print("Сума чисел від 1 до 100:", sum_numbers)

# 6
def add_numbers(a, b):
    return a + b

print("Сума чисел 3 і 7:", add_numbers(3, 7))

def reverse_string(s):
    return s[::-1]

print(reverse_string("1234567890"))

# 7
numbers = [2, 4, 6, 8, 10]

for num in numbers:
    print(num)

numbers.append(12)
print("Список після додавання елемента:", numbers)

numbers.pop()
print("Список після видалення останнього елемента:", numbers)

# 8
student = {
    "ім'я": "Максим",
    "вік": 17,
    "факультет": "ІПЗ"
}


print("Ім'я студента:", student["ім'я"])


student["рік навчання"] = 2
print("Оновлений словник:", student)

# 9
while True:
    try:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
        result = a / b
        print("Результат ділення:", result)
        break
    except ZeroDivisionError:
        print("Помилка: ділення на нуль.")
    except ValueError:
        print("Помилка: введіть числове значення.")
