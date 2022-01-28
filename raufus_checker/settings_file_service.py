# -*- coding: utf-8 -*-

#  Copyright (c) 2022.
#  Created by Zhbert.
#  Licensed by GPLv3.

import os
import configparser


def check_settings_file():
    settings_path = get_home_path() + os.sep + ".raufus_checker"
    settings_file = settings_path + os.sep + "raufus_checker.conf"
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
    return get_home_path() + os.sep + ".raufus_checker" + os.sep + "raufus_checker.conf"


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
