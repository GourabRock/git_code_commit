from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as Newservice
import time


class D_T_Element():
    def Table_element(self):
        newservice = Newservice()
        baseURL = "https://demo.opencart.com/admin/"
        DriverNew= webdriver.Firefox(service = newservice)
        DriverNew.get(baseURL)
        DriverNew.implicitly_wait(10)
        DriverNew.maximize_window()
        #DriverNew.refresh()

        DriverNew.find_element(By.ID,"input-username").send_keys("demo")
        DriverNew.find_element(By.ID, "input-password").send_keys("demo")
        time.sleep(5)
        DriverNew.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
        time.sleep(5)
        DriverNew.find_element(By.CLASS_NAME,"btn-close").click()
        DriverNew.find_element(By.XPATH,"//a[@href='#collapse-4']").click()
        DriverNew.find_element(By.XPATH,"//a[text()='Orders']").click()

        #Expected_name= "Dilshad Nilakhe"

        # Customer_names= DriverNew.find_elements(By.XPATH,"//table//td[4]")
        # i=0
        # for ECustomer in Customer_names:
        #     SampleCust = ECustomer.text

        #     if SampleCust.__eq__(Expected_name):
        #below are the action for checkbox selection :-
        #        CheckSample= "//table//tr["+str(i)+"]//td[1]"
        #        DriverNew.find_element(By.XPATH,CheckSample).click()
        #     i= i+10
        DriverNew.execute_script("window.scrollBy(0,1000);")
        time.sleep(3)
        # below are the action for Xpath AXES :-
        Expected_name = 'Dilshad Nilakhe'
        CheckSample = "//table//td[text()='"+Expected_name+"']"
        DriverNew.find_element(By.XPATH,CheckSample+"//preceding-sibling::td[3]").click()
        #DriverNew.execute_script("argument[0].scrollIntoView(true);",DriverCheck).click()

        #time.sleep(2)

D_T_new= D_T_Element()
D_T_new.Table_element()




