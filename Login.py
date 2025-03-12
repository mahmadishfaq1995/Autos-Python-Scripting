import time
from Functions import tenant_name
from Functions import log_success
from Functions import log_failure
import time


def login(driver, email="", password=""):
    print(tenant_name + " ""Starting >>>>>>>>>>>>>> Login Form Validation Test Cases")
    try:
        if email != "" and password != "":
            print("Case >>Email and Password Fields are not empty")
            # email field
            elem = driver.find_element_by_name("email")
            driver.execute_script('console.log("email")')
            driver.execute_script('document.getElementsByName("email")[0].value = ""')
            elem.click()
            elem.send_keys(email)
            time.sleep(2)
            # password field
            elem = driver.find_element_by_name("password")
            driver.execute_script('console.log("password")')
            time.sleep(2)
            driver.execute_script('document.getElementsByName("password")[0].value = ""')
            elem.click()
            driver.execute_script('document.getElementsByName("password")[0].value = ""')
            elem.send_keys(password)
            time.sleep(1)
            # login Button
            elem = driver.find_element_by_xpath(
                "//span[contains(text(),'Login')]")
            elem.click()
            time.sleep(5)
            try:
                elem = driver.find_element_by_xpath(
                    "/html/body/div/div/div/div[1]/div/div[3]/div/div[1]/div/div[1]/div/h3")
                if "DASHBOARD" in elem.text:
                    log_success(tenant_name + " ""Login  >> Pass")
                    #logout(driver)
            except:
                try:
                    try:
                        elem = driver.find_element_by_xpath(
                            "/html/body/div/div/div/div/div/div[1]/div/div/div/div/div/div/form/div[1]/div/p")
                        if "Enter a valid email address" in elem.text:
                            log_success(tenant_name + " ""Login >> Invalid Email Validation  >> Pass")
                    except:
                        elem = driver.find_element_by_xpath(
                            "/html/body/div/div/div/div/div/div[1]/div/div/div/div/div/div/form/div[3]")
                        if "Invalid login credentials. Please try again." in elem.text:
                            log_success(tenant_name + " ""Login >> Invalid Password Validation  >> Pass")
                except:
                    log_failure(
                        tenant_name + " ""Login >> Email and Password Fields are not empty  >> Unexpected Error Occurred")
        else:
            # login Button
            elem = driver.find_element_by_xpath(
                "//span[contains(text(),'Login')]")
            elem.click()
            time.sleep(1)
            print("Case >> Email or Password Field is empty")
            elem = driver.find_element_by_xpath("//p[@class='invalid-error'][contains(text(),'Please type email')]")
            if "Please type email" in elem.text:
                log_success(tenant_name + " ""Login >> Empty Name Field Validation  >> Pass")
            elem = driver.find_element_by_xpath(
                "//p[@class='invalid-error'][contains(text(),'Please enter your password')]")
            if "Please enter your password" in elem.text:
                log_success(tenant_name + " ""Login >> Empty Password Field Validation  >> Pass")
    except:
        log_failure(tenant_name + " Login >> Unexpected Error Occurred")








