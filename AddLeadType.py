import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

from Functions import log_failure
from Functions import log_success
from Functions import tenant_name
from selenium.common.exceptions import NoSuchElementException


def add_leadtype(driver, name="", inspcncat="", desc="", price="",action=""):
    #global validations
    validations = 0
    log_success(tenant_name + " ""Login >> Lead Type Page >>  Adding Lead Type ")
    try:
        elem=driver.find_element_by_xpath("//button[@class='btn btn-primary pull-right'][contains(text(),'Add New')]")
        elem.click()
        time.sleep(2)
        try:
            elem = driver.find_element_by_xpath(
                "//h3[contains(text(),'New')]")
            if 'NEW' in elem.text:
                log_success(tenant_name + " ""Login >> Lead Type Page >>  Adding Lead TypeType >> Pop up opened >> Pass")
                if name !="":
                    try:
                        # Entering name
                        elem = driver.find_element_by_xpath("//input[@placeholder='Enter Name']")
                        elem.click()
                        elem.send_keys(name)
                        elem = driver.find_element_by_xpath(
                            "//h3[contains(text(),'New')]")
                        elem.click()
                        log_success(
                            tenant_name + " ""Login >> Lead Type Page >>  Adding Lead Type >> Entering Name >> Pass ")
                        try:
                            elem = driver.find_element_by_xpath(
                                "//p[contains(text(),'Name must have less than 30 character')]")
                            print("Case >> Lead Type name Length is not valid")
                            if "Name must have less than 30 character" in elem.text:
                                log_success(
                                    tenant_name + " ""Login >> Lead Type Page >>  Adding Lead Type >> Lead Type Name Maximum Character Validation >> Pass")
                                validations += 1
                            else:
                                log_failure(
                                    tenant_name + " ""Login >> Lead Type Page >>  Adding Lead Type >> Lead Type Name Maximum Character Validation >> Unexpected issue")
                        except:
                            pass
                    except:
                        log_failure(
                            tenant_name + " ""Login >> Lead Type Page >>  Adding Lead Type >>> Entering Name >> Failure ")
                        elem = driver.find_element_by_xpath(
                            "//h3[contains(text(),'New')]")
                        elem.click()
                else:
                    try:
                        elem = driver.find_element_by_xpath(
                            "//p[contains(text(),'Please enter lead type name')]")
                        print("Case >> Lead Type name is sent empty")
                        if "Please enter lead type name" in elem.text:
                            log_success(tenant_name + " ""Login >> Lead Type Page >>  Adding Lead Type >> Empty Lead Type name Validation  >> Pass")
                            validations+=1
                        else:
                            log_failure(tenant_name + " ""Login >> Lead Type Page >>  Adding Lead Type >> Empty Lead Type name Validation  >> Unexpected issue")
                    except:
                        pass
                if desc != "":
                    try:
                        #Entering Email
                        elem = driver.find_element_by_xpath("//textarea[@placeholder='Enter Description']")
                        elem.click()
                        elem.send_keys(desc)
                        elem = driver.find_element_by_xpath(
                            "//h3[contains(text(),'New')]")
                        elem.click()
                        log_success(
                            tenant_name + " ""Login >> Lead Type Page >>  Adding Lead Type >> Entering Description >> Pass ")
                    except:
                        log_failure(
                            tenant_name + " ""Login >> Lead Type Page >>  Adding Lead Type >>> Entering Description >> Failure ")
                else:
                    log_success(
                        tenant_name + " ""Login >> Lead Type Page >>  Adding Lead Type >> Description is Empty")

                if inspcncat !="":
                    try:
                        #Selecting city
                        elem = driver.find_element_by_xpath("(//select[@id='Inspection Category'])")
                        elem.click()
                        select = Select(elem)
                        select.select_by_visible_text(inspcncat)
                        log_success(tenant_name + " ""Login >> Lead Type Page >>  Adding Lead Type >> Selecting City >> Pass")
                    except:
                        log_failure(tenant_name + " ""Login >> Lead Type Page >>  Adding Lead Type >> Selecting City >> Failure")
                        try:
                            elem = driver.find_element_by_xpath(
                                "//h3[contains(text(),'New')]")
                            elem.click()
                            elem = driver.find_element_by_xpath(
                                "//p[@class='invalid-error'][text()='Please select inspection category']")
                            print("Case >> inspection category is sent empty")
                            if "Please select inspection category" in elem.text:
                                log_success(
                                    tenant_name + " ""Login >> Lead Type Page >>  Adding Lead Type >> inspection category Validation  >> Given inspection category value not available >> Pass")
                                validations += 1
                            else:
                                log_failure(
                                    tenant_name + " ""Login >> Lead Type Page >>  Adding Lead Type >> inspection category Validation >> Given inspection category value not available >> Fail")
                        except:
                            pass

                else:
                    try:
                        elem = driver.find_element_by_xpath("(//select[@id='Inspection Category'])")
                        elem.click()
                        elem = driver.find_element_by_xpath(
                            "//h3[contains(text(),'New')]")
                        elem.click()
                        elem = driver.find_element_by_xpath(
                            "//p[@class='invalid-error'][text()='Please select inspection category']")
                        print("Case >> inspection category is sent empty")
                        if "Please select inspection category" in elem.text:
                            log_success(
                                tenant_name + " ""Login >> Lead Type Page >>  Adding Lead Type >> Empty inspection category Validation >> Pass")
                            validations += 1
                        else:
                            log_failure(
                                tenant_name + " ""Login >> Lead Type Page >>  Adding Lead Type >> Empty inspection category Validation >> Fail")
                    except:
                        pass
                if price !="":
                    try:
                        #Entering Phone Number
                        elem = driver.find_element_by_xpath("//input[@placeholder='Enter Price']")
                        elem.click()
                        elem.send_keys(price)
                        elem = driver.find_element_by_xpath(
                            "//h3[contains(text(),'New')]")
                        elem.click()
                        log_success(
                            tenant_name + " ""Login >> Lead Type Page >>  Adding Lead Type >> Entering Price >> Pass ")
                        try:
                            elem = driver.find_element_by_xpath(
                                "//p[@class='invalid-error'][text()='Please enter a number']")
                            print("Case >> Price is invalid")
                            if "Please enter a number" in elem.text:
                                log_success(
                                    tenant_name + " ""Login >> Lead Type Page >>  Adding Lead Type >> Invalid Price Validation  >> Pass")
                                validations += 1
                            else:
                                log_failure(
                                    tenant_name + " ""Login >> Lead Type Page >>  Adding Lead Type >> Invalid Price Validation  >> Fail")
                        except:
                            pass
                    except:
                        log_failure(
                            tenant_name + " ""Login >> Lead Type Page >>  Adding Lead Type >>> Entering Price >> Failure ")

                else:
                    try:
                        elem = driver.find_element_by_xpath("//input[@placeholder='Enter Price']")
                        elem.click()
                        elem = driver.find_element_by_xpath(
                            "//h3[contains(text(),'New')]")
                        elem.click()
                        elem = driver.find_element_by_xpath(
                            "//p[@class='invalid-error'][text()='Please enter price']")
                        print("Case >> Price is sent empty")
                        if "Please enter price" in elem.text:
                            log_success(
                                tenant_name + " ""Login >> Lead Type Page >>  Adding Lead Type >> Empty Price Validation  >> Pass")
                            validations += 1
                        else:
                            log_failure(
                                tenant_name + " ""Login >> Lead Type Page >>  Adding Lead Type >> Empty Price Validation  >> Fail")
                    except:
                        pass

            if action == 'Save' and validations == 0:
                # Clicking on Save button
                elem = driver.find_element_by_xpath("//button/span[text()='Save']")
                elem.click()
                log_success(tenant_name + " ""Login >> Lead Type Page >>  Save Button Clicked >> Pass")
                time.sleep(2)
                try:
                    elem = driver.find_element_by_xpath("//span[contains(text(),'Admin')]")
                    elem.click()
                    time.sleep(2)
                    elem = driver.find_element_by_xpath("//a[contains(text(),'Lead Types')]")
                    elem.click()
                    elem = driver.find_element_by_xpath("//h3[contains(text(),'Lead Types')]")
                    if elem:
                        try:
                            elem = driver.find_element_by_xpath("//input[@placeholder='Name']")
                            elem.click()
                            time.sleep(1)
                            elem.send_keys(name)
                            elem.send_keys(Keys.ENTER)
                            time.sleep(2)
                            try:
                                elem = driver.find_element_by_id("cell-name-undefined")
                                text = str(elem.text)
                                text = text.lower()
                                if name.lower() in text:
                                    log_success(tenant_name + " ""Login >> Lead Types Page >>  Lead Type Creation with '"+name+"' >> Pass")
                            except:
                                log_failure(
                                    tenant_name + " ""Login >> Lead Types Page >>  Lead Type Creation with '" + name + "' >> Fail")
                        except:
                            log_success(
                                tenant_name + " ""Login >> Lead Types Page >>  Search by Name >> Input is Empty ")
                except:
                    log_failure(tenant_name + " ""Login >> Lead Type Page Opening >> Fail")
            if action == 'Save' and validations > 0:
                # Clicking on Save button
                elem = driver.find_element_by_xpath("//button/span[text()='Save']")
                elem.click()
                log_success(tenant_name + " ""Login >> Lead Type Page >>  Save Button Clicked >> Pass")
                # number of validations triggered
                log_success(tenant_name + " ""Login >> Lead Type Page >>  Number of validations triggered >>"" "+ str(validations))
                # Re Rerouting to Lead Type Page
                try:
                    elem = driver.find_element_by_xpath("//span[contains(text(),'Admin')]")
                    elem.click()
                    time.sleep(2)
                    elem = driver.find_element_by_xpath("//a[contains(text(),'Lead Types')]")
                    elem.click()
                    elem = driver.find_element_by_xpath("//h3[contains(text(),'Lead Types')]")
                    if "LEAD TYPES" in elem.text:
                        log_success(tenant_name + " ""Login >> Action '"+action+"' >> Re Routing to Lead Type Page >> Pass")
                        time.sleep(2)
                except:
                    log_success(
                        tenant_name + " ""Login >> Action '" + action + "' >> Re Routing to Lead Type Page >> Fail")

            if action == 'Cancel':
                # Clicking on Cancel button
                elem = driver.find_element_by_xpath("(//button[@class='modal__cancel-btn btn btn-secondary'])")
                elem.click()
                log_success(tenant_name + " ""Login >> Adding Lead Type >> Action Cancel >> Pass ")
                try:
                    elem = driver.find_element_by_xpath("//h3[contains(text(),'Lead Types')]")
                    if "LEAD TYPES" in elem.text:
                        log_success(
                            tenant_name + " ""Login >> Adding Lead Type >> Action Cancel >> Re Rerouting to Lead Type Page >> Pass ")
                except:
                    log_success(
                        tenant_name + " ""Login >> Adding Lead Type >> Action Cancel >> Re Rerouting to Lead Type Page >> Failure ")
        except:
            log_failure(tenant_name + " ""Login >> Lead Type Page >>  Adding Lead Type >> Pop up not found")
    except:
        log_failure(tenant_name+" ""Login >> Lead Type Page >>  Adding Lead Type >> Unexpected "
                                              "Error")