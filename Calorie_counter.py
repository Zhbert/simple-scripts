def check_data(height, weight, age, gender):
    if height.isdigit() and weight.isdigit() and age.isdigit() and gender == "male" or gender == "female":
        return True
    else:
        return False


def male_count(height, weight, age):
    return 100


def female_count(height, weight, age):
    return 100


print("Please answer a few question:")
height = input("Your height (cm): ")
weight = input("Your weight (kg): ")
age = input("Your age (years): ")
gender = input("What gender are you (male, female)? ")

if check_data(height, weight, age, gender):
    print("Считаем!")
else:
    print("Ошибка введенных данных!")

input()
