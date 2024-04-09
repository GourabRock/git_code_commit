from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as Newservice
import time



class HiddenElement():


    def hidden_test(self):
        newservice = Newservice()
        baseurl = "https://www.letskodeit.com/practice"

        driverNew = webdriver.Firefox(service=newservice)
        driverNew.get(baseurl)
        driverNew.minimize_window()
        driverNew.implicitly_wait(10)

        # Find the state of the text box
        textBoxElement = driverNew.find_element(By.ID, "displayed-text")
        textBoxState = textBoxElement.is_displayed()  # True if visible, False if hidden
        # Exception if not present in the DOM
        print("Text is visible? " + str(textBoxState))
        time.sleep(2)

        # Click the Hide button
        driverNew.find_element(By.ID,"hide-textbox").click()
        # Find the state of the text box
        textBoxState = textBoxElement.is_displayed()
        print("Text is visible? " + str(textBoxState))
        time.sleep(2)

        # Added code to scroll up because the element was hiding behind the top navigation menu
        # You will learn about scrolling in future lecture
        driverNew.execute_script("window.scrollBy(0, -150);")
        # Click the Show button
        driverNew.find_element(By.ID,"show-textbox").click()
        # Find the state of the text box
        textBoxState = textBoxElement.is_displayed()
        print("Text is visible? " + str(textBoxState))
        time.sleep(2)
        # Browser Close
        driverNew.quit()


HE_test= HiddenElement()
HE_test.hidden_test()



