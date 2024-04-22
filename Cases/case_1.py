import unittest
import time
import sys
sys.path.append("..")
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Funciones.funcion import funciones
from Funciones.datos import datos

class base_test(unittest.TestCase):

    def SetUp(self):
        driver = webdriver.Chrome()

    def testCase1(self): 
        driver = webdriver.Chrome()
        f = funciones()
        f.navegador("https://the-internet.herokuapp.com/checkboxes", 2)
        for i in range (1, 3 ):
            f.multiple_checkbox_by_Xpath(2, "(//input[contains(@type,'checkbox')])[" + str(i) + "]")

        
        
        

    def tearDown(self):
        driver = webdriver.Chrome()
        driver.close()

    

if __name__ == '__main__':
    unittest.main()