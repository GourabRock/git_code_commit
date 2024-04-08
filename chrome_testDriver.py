from selenium import webdriver
from selenium.webdriver.chrome.service import Service as CHService
from selenium.webdriver.common.by import By

class RunCHTests():

    def test(self):
        chservice = CHService()
        # Instantiate Browser
        driver = webdriver.Chrome(service=chservice)
        # Open the provided URL
        driver.get("https://www.letskodeit.com")



ch = RunCHTests()
ch.test()
