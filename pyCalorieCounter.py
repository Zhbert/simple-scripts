print("Please answer a few question:")
height = float(input("Your height (cm): "))
weight = float(input("Your weight (kg): "))
age = float(input("Your age (years): "))
gender = input("What gender are you (male, female)? ")


def check_data():
    if type(height) == float\
            and type(weight) == float\
            and type(age) == float\
            and gender == "male" or gender == "female":
        return True
    else:
        return False


def male_count():
    def get_male_muffin_geore():
        return 10 * weight + 6.25 * height - 5 * age + 5

    def get_male_harris_benedict():
        return 66.5 + 13.75 * weight + 5.003 * height - 6.775 * age

    return ((get_male_harris_benedict() - get_male_muffin_geore()) / 2) \
           + get_male_muffin_geore()


def female_count():
    def get_female_muffin_geore():
        return 10 * weight + 6.25 * height - 5 * age - 161

    def get_female_harris_benedict():
        return 655.1 + 9.563 * weight + 1.85 * height - 4.676 * age

    return (get_female_harris_benedict() - get_female_muffin_geore()) / 2 \
           + get_female_muffin_geore()


if check_data():
    if gender == "male":
        print(male_count())
    elif gender == "female":
        print(female_count())
else:
    print("Ошибка введенных данных!")

input()
