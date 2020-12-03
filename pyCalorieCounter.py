print("Please answer a few question:")
height = float(input("Your height (cm): "))
weight = float(input("Your weight (kg): "))
age = float(input("Your age (years): "))
gender = input("What gender are you (male, female)? ")
print("Select your physical activity coefficient, where:")
print("1 - No or minimal load")
print("2 - 1-3 times a week")
print("3 - 4-5 times a week")
print("4 - Intensively 4-5 times a week")
print("5 - Every day")
print("6 - Every day is intense")
print("7 - Heavy physical work")
physical = float(input("Your physical activity: "))


def check_data():
    if type(height) == float \
            and type(weight) == float \
            and type(age) == float \
            and type(physical) == float \
            and gender == "male" or gender == "female":
        return True
    else:
        return False


def get_coefficient():
    if physical == 1:
        return 1.2
    elif physical == 2:
        return 1.375
    elif physical == 3:
        return 1.4625
    elif physical == 4:
        return 1.550
    elif physical == 5:
        return 1.6375
    elif physical == 6:
        return 1.725
    elif physical == 7:
        return 1.9


def male_count():
    def get_male_muffin_geore():
        return 10 * weight + 6.25 * height - 5 * age + 5

    def get_male_harris_benedict():
        return 66.5 + 13.75 * weight + 5.003 * height - 6.775 * age

    return (((get_male_harris_benedict() - get_male_muffin_geore()) / 2)
            + get_male_muffin_geore()) * 1.1 * get_coefficient()


def female_count():
    def get_female_muffin_geore():
        return 10 * weight + 6.25 * height - 5 * age - 161

    def get_female_harris_benedict():
        return 655.1 + 9.563 * weight + 1.85 * height - 4.676 * age

    return (get_female_harris_benedict() - get_female_muffin_geore()) / 2 \
           + get_female_muffin_geore() * 1.1 * get_coefficient()


if check_data():
    if gender == "male":
        print("You daily rate of kcal: " "%.0f" % male_count())
    elif gender == "female":
        print("You daily rate of kcal: " "%.0f" % female_count())
else:
    print("Ошибка введенных данных!")

input()
