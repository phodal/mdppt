from configparser import ConfigParser

cfg = ConfigParser()
configs = cfg.read("config.ini")
slide_key = cfg.get("default", "slide")


def get_config(key):
    return cfg.get(slide_key, key)
