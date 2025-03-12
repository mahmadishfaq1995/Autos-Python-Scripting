import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

from Functions import log_failure
from Functions import log_success
from Functions import tenant_name
from selenium.common.exceptions import NoSuchElementException


def add_lead(driver, Leadtype="", Name="", Email="", Phone="", City="", leadaction=""):
    elem = driver.find_element_by_xpath(
        "//h3[contains(text(),'Dashboard')]")
    if "DASHBOARD" in elem.text:
        elem = driver.find_element_by_xpath("//span[contains(text(),'Leads')]")
        elem.click()
    time.sleep(2)
    #global validations
    validations = 0
    log_success(tenant_name + " ""Login >> Leads Page >>  Adding Lead ")
    try:
        elem=driver.find_element_by_xpath("//button[@class='btn btn-primary pull-right'][contains(text(),'Add Lead')]")
        elem.click()
        time.sleep(2)
        try:
            elem = driver.find_element_by_xpath(
                "//h5[@class='modal-title'][contains(text(),'Add New Lead')]")
            if 'Add New Lead' in elem.text:
                log_success(tenant_name + " ""Login >> Leads Page >>  Adding Lead  >> Pop up opened")
                if Leadtype !="":
                    try:
                        # Selecting Inspection Type
                        elem = driver.find_element_by_xpath('(//select[@id="Lead Type"])')
                        elem.click()
                        select = Select(elem)
                        select.select_by_visible_text(Leadtype)
                        log_success(
                            tenant_name + " ""Login >> Leads Page >>  Adding Lead  >> Inspection Type Selection >> Pass ")
                    except:
                        log_failure(tenant_name + " ""Login >> Leads Page >>  Adding Lead  >> Inspection Type Selection >> Failure ")
                        elem = driver.find_element_by_xpath(
                            "//h5[@class='modal-title'][contains(text(),'Add New Lead')]")
                        elem.click()
                        elem = driver.find_element_by_xpath(
                            "//p[contains(text(),'Please select inspection type')]")
                        print("Case >> Lead Type is sent empty")
                        if "Please select inspection type" in elem.text:
                            log_success(
                                tenant_name + " ""Login >> Leads Page >>  Adding Lead  >> Given Lead Type is not available  >> Pass")
                            validations += 1
                        else:
                            log_failure(
                                tenant_name + " ""Login >> Leads Page >>  Adding Lead  >> Given Lead Type is not available  >> Fail")
                else:
                    try:
                        elem = driver.find_element_by_xpath('(//select[@id="Lead Type"])')
                        elem.click()
                        elem = driver.find_element_by_xpath(
                            "//h5[@class='modal-title'][contains(text(),'Add New Lead')]")
                        elem.click()
                        elem = driver.find_element_by_xpath(
                            "//p[contains(text(),'Please select inspection type')]")
                        print("Case >> Lead Type is sent empty")
                        if "Please select inspection type" in elem.text:
                            log_failure(
                                tenant_name + " ""Login >> Leads Page >>  Adding Lead  >> Lead Type optional >> Fail")
                            validations += 1
                    except:
                        log_success(
                            tenant_name + " ""Login >> Leads Page >>  Adding Lead  >> Lead Type optional >> Pass")
                if Name !="":
                    try:
                        # Entering name
                        elem = driver.find_element_by_xpath("//input[@placeholder='Enter Name']")
                        elem.click()
                        elem.send_keys(Name)
                        elem = driver.find_element_by_xpath(
                            "//h5[@class='modal-title'][contains(text(),'Add New Lead')]")
                        elem.click()
                        log_success(
                            tenant_name + " ""Login >> Leads Page >>  Adding Lead  >> Entering Name >> Pass ")
                        try:
                            elem = driver.find_element_by_xpath(
                                "//p[contains(text(),'Name must have less than 30 character')]")
                            print("Case >> Lead name Length is not valid")
                            if "Name must have less than 30 character" in elem.text:
                                log_success(
                                    tenant_name + " ""Login >> Leads Page >>  Adding Lead  >>  Lead Name Maximum Character Validation  >> Pass")
                                validations += 1
                            else:
                                log_failure(
                                    tenant_name + " ""Login >> Leads Page >>  Adding Lead  >>  Lead Name Maximum Character  >> Unexpected Error")
                        except:
                            elem = driver.find_element_by_xpath(
                                "//p[contains(text(),'lead name must only contain alphabets')]")
                            print("Case >> Lead name Length is not valid")
                            if "lead name must only contain alphabets" in elem.text:
                                log_success(
                                    tenant_name + " ""Login >> Leads Page >>  Adding Lead  >> Lead Name Should Contain Alphabets Validation  >> Pass")
                                validations += 1
                            else:
                                log_failure(
                                    tenant_name + " ""Login >> Leads Page >>  Adding Lead  >> Lead Name Should Contain Alphabets Validation >> Unexpected Error")
                    except:
                        log_failure(
                            tenant_name + " ""Login >> Leads Page >>  Adding Lead  >>> Entering Name >> Failure ")
                        elem = driver.find_element_by_xpath(
                            "//h5[@class='modal-title'][contains(text(),'Add New Lead')]")
                        elem.click()
                else:
                    try:
                        elem = driver.find_element_by_xpath(
                            "//p[contains(text(),'Please enter lead name')]")
                        print("Case >> Lead name is sent empty")
                        if "Please enter lead name" in elem.text:
                            log_success(tenant_name + " ""Login >> Leads Page >>  Adding Lead  >> Empty Lead name Validation  >> Pass")
                            validations+=1
                        else:
                            log_failure(tenant_name + " ""Login >> Leads Page >>  Adding Lead  >> Empty Lead name Validation  >> Unexpected Error")
                    except:
                        pass


                if Email != "":
                    try:
                        #Entering Email
                        elem = driver.find_element_by_xpath("//input[@placeholder='Enter Email']")
                        elem.click()
                        elem.send_keys(Email)
                        elem = driver.find_element_by_xpath(
                            "//h5[@class='modal-title'][contains(text(),'Add New Lead')]")
                        elem.click()
                        log_success(
                            tenant_name + " ""Login >> Leads Page >>  Adding Lead  >> Entering Email >> Pass ")
                        try:
                            elem = driver.find_element_by_xpath(
                                "//h5[@class='modal-title'][contains(text(),'Add New Lead')]")
                            elem.click()
                            #elem = driver.find_element_by_xpath("(//p[@class='invalid-error'])")
                            elem = driver.find_element_by_xpath("//p[contains(text(),'Enter a valid email address')]")
                            print("Case >> Email Entered is invalid")
                            if "Enter a valid email address" in elem.text:
                                log_success(
                                    tenant_name + " ""Login >> Leads Page >>  Adding Lead  >> Invalid Email Validation  >> Pass")
                                validations += 1
                        except:
                            pass
                    except:
                        log_failure(
                            tenant_name + " ""Login >> Leads Page >>  Adding Lead  >>> Entering Email >> Failure ")
                else:
                    log_success(
                        tenant_name + " ""Login >> Leads Page >>  Adding Lead  >> Email is Empty")
                if Phone !="":
                    try:
                        #Entering Phone Number
                        elem = driver.find_element_by_xpath("//input[@placeholder='03XXXXXXXXX']")
                        elem.click()
                        elem.send_keys(Phone)
                        elem = driver.find_element_by_xpath(
                            "//h5[@class='modal-title'][contains(text(),'Add New Lead')]")
                        elem.click()
                        log_success(
                            tenant_name + " ""Login >> Leads Page >>  Adding Lead  >> Entering Phone >> Pass ")
                        try:
                            elem = driver.find_element_by_xpath(
                                "(//p[contains(text(),'Please enter a valid phone number')]")
                            print("Case >> Phone Number is not valid")
                            if "Please enter a valid phone number" in elem.text:
                                log_success(
                                    tenant_name + " ""Login >> Leads Page >>  Adding Lead  >> Invalid Phone Number Validation  >> Pass")
                                validations += 1
                            else:
                                log_failure(
                                    tenant_name + " ""Login >> Leads Page >>  Adding Lead  >> Invalid Phone Number Validation  >> Fail")
                        except:
                            pass
                    except:
                        log_failure(
                            tenant_name + " ""Login >> Leads Page >>  Adding Lead  >>> Entering Phone >> Failure ")

                else:
                    try:
                        elem = driver.find_element_by_xpath("//input[@placeholder='03XXXXXXXXX']")
                        elem.click()
                        elem = driver.find_element_by_xpath(
                            "//h5[@class='modal-title'][contains(text(),'Add New Lead')]")
                        elem.click()
                        elem = driver.find_element_by_xpath(
                            "(//p[contains(text(),'Please enter phone')]")
                        print("Case >> Phone Number is sent empty")
                        if "Please enter phone" in elem.text:
                            log_success(
                                tenant_name + " ""Login >> Leads Page >>  Adding Lead  >> Empty Phone Number Validation  >> Pass")
                            validations += 1
                        else:
                            log_failure(
                                tenant_name + " ""Login >> Leads Page >>  Adding Lead  >> Empty Phone Number Validation  >> Fail")
                    except:
                        pass
                if City !="":
                    try:
                        #Selecting city
                        elem = driver.find_element_by_xpath("(//select[@id='City'])")
                        elem.click()
                        select = Select(elem)
                        select.select_by_visible_text(City)
                        log_success(tenant_name + " ""Login >> Leads Page >>  Adding Lead  >> Selecting City >> Pass")
                    except:
                        log_failure(tenant_name + " ""Login >> Leads Page >>  Adding Lead  >> Selecting City >> Failure")
                        elem = driver.find_element_by_xpath( "(//p[contains(text(),'Please select city')]")
                        print("Case >> City is sent empty")
                        if "Please select city" in elem.text:
                            log_success(
                                tenant_name + " ""Login >> Leads Page >>  Adding Lead  >> City Validation  >> Given City value not available >> Pass")
                            validations += 1
                        else:
                            log_failure(
                                tenant_name + " ""Login >> Leads Page >>  Adding Lead  >> City Validation >> Given City value not available >> Fail")

                else:
                    try:
                        elem = driver.find_element_by_xpath("(//select[@id='City'])")
                        elem.click()
                        elem = driver.find_element_by_xpath(
                            "//h5[@class='modal-title'][contains(text(),'Add New Lead')]")
                        elem.click()
                        elem = driver.find_element_by_xpath("(//p[contains(text(),'Please select city')]")
                        print("Case >> City is sent empty")
                        if "Please select city" in elem.text:
                            log_success(
                                tenant_name + " ""Login >> Leads Page >>  Adding Lead  >> Empty City Validation  >> Pass")
                            validations += 1
                        else:
                            log_failure(
                                tenant_name + " ""Login >> Leads Page >>  Adding Lead  >> Empty City Validation  >> Fail")
                    except:
                        pass
            if leadaction == 'Create' and validations == 0:
                # Clicking on Create button
                elem = driver.find_element_by_xpath("(//button[@class='modal__cr-btn btn btn-primary'])")
                elem.click()
                log_success(tenant_name + " ""Login >> Leads Page >>  Create Lead Button Clicked >> Pass")
                time.sleep(2)
            if leadaction == 'Create' and validations > 0:
                # Clicking on Create button
                elem = driver.find_element_by_xpath("(//button[@class='modal__cr-btn btn btn-primary'])")
                elem.click()
                log_success(tenant_name + " ""Login >> Leads Page >>  Create Lead Button Clicked >> Pass")
                # number of validations triggered
                log_success(tenant_name + " ""Login >> Leads Page >>  Number of validations triggered >>"" "+ str(validations))
                # Re Rerouting to Leads Page
                elem = driver.find_element_by_xpath("(//button[@class='modal__cancel-btn btn btn-secondary'])")
                elem.click()
                log_success(tenant_name + " ""Login >> Adding Lead  >> Action Create >> Validations Triggered >>  Pressing Cancel Button >> Pass ")
                try:
                    elem = driver.find_element_by_xpath("//h3[contains(text(),'Leads')]")
                    if "LEADS" in elem.text:
                        log_success(
                            tenant_name + " ""Login >> Adding Lead  >> Action Create >> Validations Triggered >> Re Rerouting to Leads Page >> Pass ")
                except:
                    log_success(
                        tenant_name + " ""Login >> Adding Lead  >> Action Create >> Validations Triggered  >> Re Rerouting to Leads Page >> Failure ")

            if leadaction == 'Cancel':
                # Clicking on Cancel button
                elem = driver.find_element_by_xpath("(//button[@class='modal__cancel-btn btn btn-secondary'])")
                elem.click()
                log_success(tenant_name + " ""Login >> Adding Lead  >> Action Cancel >> Pass ")
                try:
                    elem = driver.find_element_by_xpath("//h3[contains(text(),'Leads')]")
                    if "LEADS" in elem.text:
                        log_success(
                            tenant_name + " ""Login >> Adding Lead  >> Action Cancel >> Re Rerouting to Leads Page >> Pass ")
                except:
                    log_success(
                        tenant_name + " ""Login >> Adding Lead  >> Action Cancel >> Re Rerouting to Leads Page >> Failure ")
        except:
            log_failure(tenant_name + " ""Login >> Leads Page >>  Adding Lead  >> Pop up not found")
    except:
        log_failure(tenant_name+" ""Login >> Leads Page >>  Adding Lead  >> Unexpected "
                                              "Error")