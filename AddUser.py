import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

from Functions import log_failure
from Functions import log_success
from Functions import tenant_name
from selenium.common.exceptions import NoSuchElementException


def add_User(driver, fname="", lname="", Email="", Phone="",action=""):
    #global validations
    validations = 0
    log_success(tenant_name + " ""Login >> User Page >>  Adding User ")
    try:
        elem=driver.find_element_by_xpath("//button[@class='btn btn-primary pull-right'][contains(text(),'Add User')]")
        elem.click()
        time.sleep(2)
        try:
            elem = driver.find_element_by_xpath(
                "//h5[@class='modal-title'][contains(text(),'Add New User')]")
            if 'Add New User' in elem.text:
                log_success(tenant_name + " ""Login >> User Page >>  Adding User >> Pop up opened >> Pass")
                if fname !="":
                    try:
                        # Entering name
                        elem = driver.find_element_by_xpath("//input[@placeholder='Enter First Name']")
                        elem.click()
                        elem.send_keys(fname)
                        elem = driver.find_element_by_xpath(
                            "//h5[@class='modal-title'][contains(text(),'Add New User')]")
                        elem.click()
                        log_success(
                            tenant_name + " ""Login >> User Page >>  Adding User >> Entering First Name >> Pass ")
                        try:
                            elem = driver.find_element_by_xpath(
                                "//p[contains(text(),'Name must have less than 20 character')]")
                            print("Case >> User name Length is not valid")
                            if "Name must have less than 20 character" in elem.text:
                                log_success(
                                    tenant_name + " ""Login >> User Page >>  Adding User >> First Name Maximum Character Validation  >> Pass")
                                validations += 1
                            else:
                                log_failure(
                                    tenant_name + " ""Login >> User Page >>  Adding User >> First Name Maximum Character Validation>> Unexpected issue")
                        except:
                            pass
                    except:
                        log_failure(
                            tenant_name + " ""Login >> User Page >>  Adding User >>> Entering First Name >> Failure ")
                        elem = driver.find_element_by_xpath(
                            "//h5[@class='modal-title'][contains(text(),'Add New User')]")
                        elem.click()
                else:
                    try:
                        elem = driver.find_element_by_xpath(
                            "//p[contains(text(),'Please enter First name')]")
                        print("Case >> First name is sent empty")
                        if "Please enter First name" in elem.text:
                            log_success(tenant_name + " ""Login >> User Page >>  Adding User >> Empty First name Validation  >> Pass")
                            validations+=1
                        else:
                            log_failure(tenant_name + " ""Login >> User Page >>  Adding User >> Empty First name Validation  >> Unexpected issue")
                    except:
                        pass
                if lname !="":
                    try:
                        # Entering name
                        elem = driver.find_element_by_xpath("//input[@placeholder='Enter Last Name']")
                        elem.click()
                        elem.send_keys(lname)
                        elem = driver.find_element_by_xpath(
                            "//h5[@class='modal-title'][contains(text(),'Add New User')]")
                        elem.click()
                        log_success(
                            tenant_name + " ""Login >> User Page >>  Adding User >> Entering Last Name >> Pass ")
                        try:
                            elem = driver.find_element_by_xpath(
                                "//p[contains(text(),'Name must have less than 20 character')]")
                            print("Case >> User name Length is not valid")
                            if "Name must have less than 20 character" in elem.text:
                                log_success(
                                    tenant_name + " ""Login >> User Page >>  Adding User >> Last Name Maximum Character Validation >> Pass")
                                validations += 1
                            else:
                                log_failure(
                                    tenant_name + " ""Login >> User Page >>  Adding User >> Last Name Maximum Character Validation >> Unexpected issue")
                        except:
                            pass
                    except:
                        log_failure(
                            tenant_name + " ""Login >> User Page >>  Adding User >>> Entering Last Name >> Failure ")
                        elem = driver.find_element_by_xpath(
                            "//h5[@class='modal-title'][contains(text(),'Add New User')]")
                        elem.click()
                else:
                    try:
                        elem = driver.find_element_by_xpath(
                            "//p[contains(text(),'Please enter Last name')]")
                        print("Case >> Last name is sent empty")
                        if "Please enter Last name" in elem.text:
                            log_success(
                                tenant_name + " ""Login >> User Page >>  Adding User >> Empty Last name Validation  >> Pass")
                            validations += 1
                        else:
                            log_failure(
                                tenant_name + " ""Login >> User Page >>  Adding User >> Empty Last name Validation  >> Unexpected issue")
                    except:
                        pass
                if Email != "":
                    try:
                        #Entering Email
                        elem = driver.find_element_by_xpath("//input[@placeholder='Enter Email']")
                        elem.click()
                        elem.send_keys(Email)
                        elem = driver.find_element_by_xpath(
                            "//h5[@class='modal-title'][contains(text(),'Add New User')]")
                        elem.click()
                        log_success(
                            tenant_name + " ""Login >> Users Page >>  Adding User  >> Entering Email >> Pass ")
                        try:
                            elem = driver.find_element_by_xpath(
                                "//h5[@class='modal-title'][contains(text(),'Add New User')]")
                            elem.click()
                            #elem = driver.find_element_by_xpath("(//p[@class='invalid-error'])")
                            elem = driver.find_element_by_xpath("//p[contains(text(),'Enter a valid email address')]")
                            print("Case >> Email Entered is invalid")
                            if "Enter a valid email address" in elem.text:
                                log_success(
                                    tenant_name + " ""Login >> Users Page >>  Adding User  >> Invalid Email Validation  >> Pass")
                                validations += 1
                        except:
                            pass
                    except:
                        log_failure(
                            tenant_name + " ""Login >> Users Page >>  Adding User  >>> Entering Email >> Failure ")
                else:
                    try:
                        log_success(
                            tenant_name + " ""Login >> Users Page >>  Adding User  >> Email is Empty")
                        elem = driver.find_element_by_xpath(
                            "//h5[@class='modal-title'][contains(text(),'Add New User')]")
                        elem.click()
                        # elem = driver.find_element_by_xpath("(//p[@class='invalid-error'])")
                        elem = driver.find_element_by_xpath("//p[contains(text(),'Please type email')]")
                        print("Case >> Empty Email Validation")
                        if "Please type email" in elem.text:
                            log_success(
                                tenant_name + " ""Login >> Users Page >>  Adding User  >> Empty Email Validation  >> Pass")
                            validations += 1
                    except:
                        pass
                if Phone !="":
                    try:
                        #Entering Phone Number
                        elem = driver.find_element_by_xpath("//input[@placeholder='03XXXXXXXXX']")
                        elem.click()
                        elem.send_keys(Phone)
                        elem = driver.find_element_by_xpath(
                            "//h5[@class='modal-title'][contains(text(),'Add New User')]")
                        elem.click()
                        log_success(
                            tenant_name + " ""Login >> Users Page >>  Adding User  >> Entering Phone >> Pass ")
                        try:
                            elem = driver.find_element_by_xpath(
                                "(//p[contains(text(),'Please enter a valid phone number')]")
                            print("Case >> Phone Number is not valid")
                            if "Please enter a valid phone number" in elem.text:
                                log_success(
                                    tenant_name + " ""Login >> Users Page >>  Adding User  >> Invalid Phone Number Validation  >> Pass")
                                validations += 1
                            else:
                                log_failure(
                                    tenant_name + " ""Login >> Users Page >>  Adding User  >> Invalid Phone Number Validation  >> Fail")
                        except:
                            pass
                    except:
                        log_failure(
                            tenant_name + " ""Login >> Users Page >>  Adding User  >>> Entering Phone >> Failure ")

                else:
                    try:
                        elem = driver.find_element_by_xpath("//input[@placeholder='03XXXXXXXXX']")
                        elem.click()
                        elem = driver.find_element_by_xpath(
                            "//h5[@class='modal-title'][contains(text(),'Add New User')]")
                        elem.click()
                        elem = driver.find_element_by_xpath(
                            "(//p[contains(text(),'Please enter phone')]")
                        print("Case >> Phone Number is sent empty")
                        if "Please enter phone" in elem.text:
                            log_success(
                                tenant_name + " ""Login >> Users Page >>  Adding User  >> Empty Phone Number Validation  >> Pass")
                            validations += 1
                        else:
                            log_failure(
                                tenant_name + " ""Login >> Users Page >>  Adding User  >> Empty Phone Number Validation  >> Fail")
                    except:
                        pass

            if action == 'Create' and validations == 0:
                # Clicking on Create button
                elem = driver.find_element_by_xpath("(//button[@class='modal__cr-btn btn btn-primary'])")
                elem.click()
                log_success(tenant_name + " ""Login >> Users Page >>  Create User Button Clicked >> Pass")
                time.sleep(2)
                try:
                    elem = driver.find_element_by_xpath("//h3[contains(text(),'Users')]")
                    if elem:
                        time.sleep(2)
                        fullname =fname+' '+lname
                        try:
                            elem = driver.find_element_by_id("cell-name-undefined")
                            text = str(elem.text)
                            text = text.lower()
                            if fullname.lower() in text:
                                log_success(tenant_name + " ""Login >> Users Page >>  User Creation with '"+fullname+"' >> Pass")
                        except:
                            log_failure(
                                tenant_name + " ""Login >> Users Page >>  User Creation with '" + fullname + "' >> Fail")
                except:
                    log_failure(tenant_name + " ""Login >> Users Page Opening >> Fail")
            if action == 'Create' and validations > 0:
                # Clicking on Create button
                elem = driver.find_element_by_xpath("(//button[@class='modal__cr-btn btn btn-primary'])")
                elem.click()
                log_success(tenant_name + " ""Login >> Users Page >>  Create User Button Clicked >> Pass")
                # number of validations triggered
                log_success(
                    tenant_name + " ""Login >> Users Page >> Adding User >> Number of validations triggered >>"" " + str(validations))
                # Re Rerouting to Users Page
                elem = driver.find_element_by_xpath("(//button[@class='modal__cancel-btn btn btn-secondary'])")
                elem.click()
                log_success(
                    tenant_name + " ""Login >> Adding User  >> Action Create >> Validations Triggered >>  Pressing Cancel Button >> Pass")
                try:
                    elem = driver.find_element_by_xpath("//h3[contains(text(),'Users')]")
                    if "USERS" in elem.text:
                        log_success(
                            tenant_name + " ""Login >> Adding User  >> Action Create >> Validations Triggered >> Re Rerouting to Users Page >> Pass ")
                except:
                    log_success(
                        tenant_name + " ""Login >> Adding User  >> Action Create >> Validations Triggered  >> Re Rerouting to Users Page >> Failure ")

            if action == 'Cancel':
                # Clicking on Cancel button
                elem = driver.find_element_by_xpath("(//button[@class='modal__cancel-btn btn btn-secondary'])")
                elem.click()
                log_success(tenant_name + " ""Login >> Adding User  >> Action Cancel >> Pass ")
                try:
                    elem = driver.find_element_by_xpath("//h3[contains(text(),'Users')]")
                    if "USERS" in elem.text:
                        log_success(
                            tenant_name + " ""Login >> Adding User  >> Action Cancel >> Re Rerouting to Users Page >> Pass ")
                except:
                    log_success(
                        tenant_name + " ""Login >> Adding User  >> Action Cancel >> Re Rerouting to Users Page >> Failure ")
        except:
            log_failure(tenant_name + " ""Login >> User Page >>  Adding User >> Pop up not found")
    except:
        log_failure(tenant_name+" ""Login >> User Page >>  Adding User >> Unexpected "
                                              "Error")