# -*- coding: utf-8 -*-

#  Copyright (c) 2022.
#  Created by Zhbert.
#  Licensed by GPLv3.

import os
import configparser


doctors_names = {
    'Аллерголог-иммунолог': 0,
    'Гастроэнтеролог': 1,
    'Детский кардиолог': 2,
    'Детский хирург': 3,
    'Детский эндокринолог': 4,
    'Невролог': 5,
    'Нейрохирург': 6,
    'Нефролог': 7,
    'Оториноларинголог': 8,
    'Офтальмолог': 9,
    'Педиатр': 10,
    'Пульмонолог': 11,
    'Травматолог-ортопед': 12,
    'Функциональная диагностика': 13,
    'Челюстно-лицевой хирург': 14
}


def check_settings_file():
    settings_path = get_home_path() + os.sep + ".rauhfus_checker"
    settings_file = settings_path + os.sep + "rauhfus_checker.conf"
    if os.path.exists(settings_path):
        print("The settings directory was found. Checking the parameters file...")
        if os.path.exists(settings_file):
            print("The settings file was found.")
        else:
            print("Creating a new settings file...")
            create_new_settings_file(settings_file)
            print("A new settings file has been created")
    else:
        print("The settings directory was not found: " + settings_path)
        print("Creating a settings directory:" + settings_path)
        os.mkdir(settings_path)
        create_new_settings_file(settings_file)


def create_new_settings_file(settings_file):
    print("The settings file was not found. Creating...")
    config = configparser.ConfigParser()
    config.add_section("CHILD")
    config.set("CHILD", "Surname", "NONE")
    config.set("CHILD", "Name", "NONE")
    config.set("CHILD", "Middle_name", "NONE")
    config.set("CHILD", "Birthday", "DD.MM.YYYY")
    config.add_section("EMAIL")
    config.set("EMAIL", "Host", "smtp.gmail.com")
    config.set("EMAIL", "Port", "587")
    config.set("EMAIL", "Username", "USERNAME")
    config.set("EMAIL", "Password", "PASSWORD")
    config.set("EMAIL", "Address", "your@email.addr")
    config.add_section("DOCTOR")
    config.set("DOCTOR", "Type", "Невролог")
    if os.path.exists(settings_file):
        with open(settings_file, "w") as config_file:
            config.write(config_file)
            config_file.close()
    else:
        with open(settings_file, "x") as config_file:
            config.write(config_file)
            config_file.close()


def get_home_path():
    home_path = (os.getenv('HOME'))
    if home_path == "None":
        home_path = os.getenv('USERPROFILE')
    return home_path


def get_settings_file_path():
    return get_home_path() + os.sep + ".rauhfus_checker" + os.sep + "rauhfus_checker.conf"


def get_surname():
    config = configparser.ConfigParser()
    config.read(get_settings_file_path())
    return config.get("CHILD", "Surname")


def get_name():
    config = configparser.ConfigParser()
    config.read(get_settings_file_path())
    return config.get("CHILD", "Name")


def get_middle_name():
    config = configparser.ConfigParser()
    config.read(get_settings_file_path())
    return config.get("CHILD", "Middle_name")


def get_birthday():
    config = configparser.ConfigParser()
    config.read(get_settings_file_path())
    return config.get("CHILD", "Birthday")


def get_email_host():
    config = configparser.ConfigParser()
    config.read(get_settings_file_path())
    return config.get("EMAIL", "Host")


def get_email_port():
    config = configparser.ConfigParser()
    config.read(get_settings_file_path())
    return config.get("EMAIL", "Port")


def get_email_username():
    config = configparser.ConfigParser()
    config.read(get_settings_file_path())
    return config.get("EMAIL", "Username")


def get_email_password():
    config = configparser.ConfigParser()
    config.read(get_settings_file_path())
    return config.get("EMAIL", "Password")


def get_email_address():
    config = configparser.ConfigParser()
    config.read(get_settings_file_path())
    return config.get("EMAIL", "Address")


def get_doctor_name():
    config = configparser.ConfigParser()
    config.read(get_settings_file_path())
    return config.get("DOCTOR", "Type")


def get_doctor_type():
    return doctors_names[get_doctor_name()]
