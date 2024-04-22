import unittest
import time
import sys
sys.path.append("..")
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Funciones.funcion import funciones

class datos():

    def __init__(self):
        driver = webdriver.Chrome()

    def login_details(self, url, username, password, segundos):
        driver = webdriver.Chrome()
        f = funciones()
        f.navegador(url, 2)
        f.validacion("//input[contains(@id,'user-name')]", username, 2)
        f.validacion("//input[contains(@id,'password')]", password, 2)
        f.cliquear("//input[contains(@id,'login-button')]", 2)