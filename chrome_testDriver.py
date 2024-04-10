from selenium import webdriver
from selenium.webdriver.chrome.service import Service as CHService


class RunCHTests():

    def test(self):
        chservice = CHService()
        # Instantiate Browser
        driver = webdriver.Chrome(service=chservice)
        # Open the provided URL
        driver.get("https://www.letskodeit.com")



ch = RunCHTests()
ch.test()






***********Sample for branch stategy@@@@@