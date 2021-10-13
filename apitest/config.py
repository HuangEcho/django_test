
import configparser
import os


def getConfig(section, key):
    config = configparser.ConfigParser()
    path = os.path.join(os.getcwd(), "settings.conf")
    config.read(path)
    return config.get(section, key)
