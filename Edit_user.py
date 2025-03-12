import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

from Functions import log_failure
from Functions import log_success
from Functions import tenant_name
from selenium.common.exceptions import NoSuchElementException


def edit_user(driver, fname="", lname="", Email="", Phone="",action="",start=""):
    #global validations
    validations = 0
    log_success(tenant_name + " ""Login >> User Page >>  Edit User ")
    if start !="" and start != 0:
        try:
            elem = driver.find_element_by_xpath(
                "(//div[@data-tag='allowRowEvents']//span[2][@class='table__action-icon']/*[name()='svg'])[" + str(
                    start) + "]")
            elem.click()
            time.sleep(2)
            try:
                elem = driver.find_element_by_xpath(
                    "//h5[@class='modal-title'][contains(text(),'Update User')]")
                if 'Update User' in elem.text:
                    log_success(tenant_name + " ""Login >> User Page >>  Update User >> Pop up opened >> Pass")
                    if fname !="":
                        try:
                            # Entering name
                            elem = driver.find_element_by_xpath("//input[@placeholder='Enter First Name']")
                            elem.click()
                            elem.clear()
                            elem.send_keys(fname)
                            elem = driver.find_element_by_xpath(
                                "//h5[@class='modal-title'][contains(text(),'Update User')]")
                            elem.click()
                            log_success(
                                tenant_name + " ""Login >> User Page >>  Update User >> Entering First Name >> Pass ")
                            try:
                                elem = driver.find_element_by_xpath(
                                    "//p[contains(text(),'Name must have less than 20 character')]")
                                print("Case >> User name Length is not valid")
                                if "Name must have less than 20 character" in elem.text:
                                    log_success(
                                        tenant_name + " ""Login >> User Page >>  Update User >> First Name Maximum Character Validation  >> Pass")
                                    validations += 1
                                else:
                                    log_failure(
                                        tenant_name + " ""Login >> User Page >>  Update User >> First Name Maximum Character Validation>> Unexpected issue")
                            except:
                                pass
                        except:
                            log_failure(
                                tenant_name + " ""Login >> User Page >>  Update User >>> Entering First Name >> Failure ")
                            elem = driver.find_element_by_xpath(
                                "//h5[@class='modal-title'][contains(text(),'Update User')]")
                            elem.click()
                    else:
                        elem = driver.find_element_by_xpath(
                            "//p[contains(text(),'Please enter First name')]")
                        print("Case >> First name is sent empty")
                        if "Please enter First name" in elem.text:
                            log_success(tenant_name + " ""Login >> User Page >>  Update User >> Empty First name Validation  >> Pass")
                            validations+=1
                        else:
                            log_failure(tenant_name + " ""Login >> User Page >>  Update User >> Empty First name Validation  >> Unexpected issue")
                    if lname !="":
                        try:
                            # Entering name
                            elem = driver.find_element_by_xpath("//input[@placeholder='Enter Last Name']")
                            elem.click()
                            elem.send_keys(lname)
                            elem = driver.find_element_by_xpath(
                                "//h5[@class='modal-title'][contains(text(),'Update User')]")
                            elem.click()
                            log_success(
                                tenant_name + " ""Login >> User Page >>  Update User >> Entering Last Name >> Pass ")
                            try:
                                elem = driver.find_element_by_xpath(
                                    "//p[contains(text(),'Name must have less than 20 character')]")
                                print("Case >> User name Length is not valid")
                                if "Name must have less than 20 character" in elem.text:
                                    log_success(
                                        tenant_name + " ""Login >> User Page >>  Update User >> Last Name Maximum Character Validation >> Pass")
                                    validations += 1
                                else:
                                    log_failure(
                                        tenant_name + " ""Login >> User Page >>  Update User >> Last Name Maximum Character Validation >> Unexpected issue")
                            except:
                                pass
                        except:
                            log_failure(
                                tenant_name + " ""Login >> User Page >>  Update User >>> Entering Last Name >> Failure ")
                            elem = driver.find_element_by_xpath(
                                "//h5[@class='modal-title'][contains(text(),'Update User')]")
                            elem.click()
                    else:
                        try:
                            elem = driver.find_element_by_xpath(
                                "//p[contains(text(),'Please enter Last name')]")
                            print("Case >> Last name is sent empty")
                            if "Please enter Last name" in elem.text:
                                log_success(
                                    tenant_name + " ""Login >> User Page >>  Update User >> Empty Last name Validation  >> Pass")
                                validations += 1
                            else:
                                log_failure(
                                    tenant_name + " ""Login >> User Page >>  Update User >> Empty Last name Validation  >> Unexpected issue")
                        except:
                            pass
                    if Email != "":
                        try:
                            #Entering Email
                            elem = driver.find_element_by_xpath("//input[@placeholder='Enter Email']")
                            elem.click()
                            elem.send_keys(Email)
                            elem = driver.find_element_by_xpath(
                                "//h5[@class='modal-title'][contains(text(),'Update User')]")
                            elem.click()
                            log_success(
                                tenant_name + " ""Login >> Users Page >>  Update User >> Entering Email >> Pass ")
                            try:
                                elem = driver.find_element_by_xpath(
                                    "//h5[@class='modal-title'][contains(text(),'Update User')]")
                                elem.click()
                                #elem = driver.find_element_by_xpath("(//p[@class='invalid-error'])")
                                elem = driver.find_element_by_xpath("//p[contains(text(),'Enter a valid email address')]")
                                print("Case >> Email Entered is invalid")
                                if "Enter a valid email address" in elem.text:
                                    log_success(
                                        tenant_name + " ""Login >> Users Page >>  Update User >> Invalid Email Validation  >> Pass")
                                    validations += 1
                            except:
                                pass
                        except:
                            log_failure(
                                tenant_name + " ""Login >> Users Page >>  Update User  >>> Entering Email >> Failure ")
                    else:
                        try:
                            log_success(
                                tenant_name + " ""Login >> Users Page >>  Update User >> Email is Empty")
                            elem = driver.find_element_by_xpath(
                                "//h5[@class='modal-title'][contains(text(),'Update User')]")
                            elem.click()
                            # elem = driver.find_element_by_xpath("(//p[@class='invalid-error'])")
                            elem = driver.find_element_by_xpath("//p[contains(text(),'Please type email')]")
                            print("Case >> Empty Email Validation")
                            if "Please type email" in elem.text:
                                log_success(
                                    tenant_name + " ""Login >> Users Page >>  Update User >> Empty Email Validation  >> Pass")
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
                                "//h5[@class='modal-title'][contains(text(),'Update User')]")
                            elem.click()
                            log_success(
                                tenant_name + " ""Login >> Users Page >>  Update User >> Entering Phone >> Pass ")
                            try:
                                elem = driver.find_element_by_xpath(
                                    "(//p[contains(text(),'Please enter a valid phone number')]")
                                print("Case >> Phone Number is not valid")
                                if "Please enter a valid phone number" in elem.text:
                                    log_success(
                                        tenant_name + " ""Login >> Users Page >>  Update User >> Invalid Phone Number Validation  >> Pass")
                                    validations += 1
                                else:
                                    log_failure(
                                        tenant_name + " ""Login >> Users Page >>  Update User >> Invalid Phone Number Validation  >> Fail")
                            except:
                                pass
                        except:
                            log_failure(
                                tenant_name + " ""Login >> Users Page >>  Update User  >>> Entering Phone >> Failure ")

                    else:
                        try:
                            elem = driver.find_element_by_xpath("//input[@placeholder='03XXXXXXXXX']")
                            elem.click()
                            elem = driver.find_element_by_xpath(
                                "//h5[@class='modal-title'][contains(text(),'Update User')]")
                            elem.click()
                            elem = driver.find_element_by_xpath(
                                "(//p[contains(text(),'Please enter phone')]")
                            print("Case >> Phone Number is sent empty")
                            if "Please enter phone" in elem.text:
                                log_success(
                                    tenant_name + " ""Login >> Users Page >>  Update User >> Empty Phone Number Validation  >> Pass")
                                validations += 1
                            else:
                                log_failure(
                                    tenant_name + " ""Login >> Users Page >>  Update User >> Empty Phone Number Validation  >> Fail")
                        except:
                            pass

                if action == 'Update' and validations == 0:
                    # Clicking on Update   button
                    elem = driver.find_element_by_xpath("(//button[@class='modal__cr-btn btn btn-primary'])")
                    elem.click()
                    log_success(tenant_name + " ""Login >> Users Page >> Update User Button Clicked >> Pass")
                    time.sleep(2)
                    try:
                        elem = driver.find_element_by_xpath("//h3[contains(text(),'Users')]")
                        if elem:
                            time.sleep(2)
                            fullname =fname+' '+lname
                            if fullname != "":
                                try:
                                    elem = driver.find_element_by_xpath("(//div[@id='cell-name-undefined'])[" + str(start) + "]")
                                    text = str(elem.text)
                                    text = text.lower()
                                    if fullname.lower() in text:
                                        log_success(tenant_name + " ""Login >> Users Page >>  User Name Updated to '"+fullname+"' >> Pass")
                                except:
                                    log_failure(
                                        tenant_name + " ""Login >> Users Page >>  User Name Updated to '" + fullname + "' >> Fail")
                            if Email != "":
                                try:
                                    elem = driver.find_element_by_xpath("(//div[@id='cell-email-undefined'])[" + str(start) + "]")
                                    text = str(elem.text)
                                    text = text.lower()
                                    if Email.lower() in text:
                                        log_success(tenant_name + " ""Login >> Users Page >> User Email Updated to '"+Email+"' >> Pass")
                                except:
                                    log_failure(
                                        tenant_name + " ""Login >> Users Page >>  User Email Updated to '" + Email + "' >> Fail")
                            if Phone != "":
                                try:
                                    elem = driver.find_element_by_xpath("(//div[@id='cell-phone-undefined'])[" + str(start) + "]")
                                    text = str(elem.text)
                                    text = text.lower()
                                    if Phone.lower() in text:
                                        log_success(tenant_name + " ""Login >> Users Page >> User Phone Updated to '"+Phone+"' >> Pass")
                                except:
                                    log_failure(
                                        tenant_name + " ""Login >> Users Page >>  User Phone Updated to '" + Phone + "' >> Fail")
                    except:
                        log_failure(tenant_name + " ""Login >> Users Page Opening >> Fail")
                if action == 'Update' and validations > 0:
                    # Clicking on Update button
                    elem = driver.find_element_by_xpath("(//button[@class='modal__cr-btn btn btn-primary'])")
                    elem.click()
                    log_success(tenant_name + " ""Login >> Users Page >>  Update User Button Clicked >> Pass")
                    # number of validations triggered
                    log_success(
                        tenant_name + " ""Login >> Users Page >> Update User >> Number of validations triggered >>"" " + str(validations))
                    # Re Rerouting to Users Page
                    elem = driver.find_element_by_xpath("(//button[@class='modal__cancel-btn btn btn-secondary'])")
                    elem.click()
                    log_success(
                        tenant_name + " ""Login >> Update User >> Action Update >> Validations Triggered >>  Pressing Cancel Button >> Pass")
                    try:
                        elem = driver.find_element_by_xpath("//h3[contains(text(),'Users')]")
                        if "USERS" in elem.text:
                            log_success(
                                tenant_name + " ""Login >> Update User >> Action Update >> Validations Triggered >> Re Rerouting to Users Page >> Pass ")
                    except:
                        log_success(
                            tenant_name + " ""Login >> Update User >> Action Update >> Validations Triggered  >> Re Rerouting to Users Page >> Failure ")

                if action == 'Cancel':
                    # Clicking on Cancel button
                    elem = driver.find_element_by_xpath("(//button[@class='modal__cancel-btn btn btn-secondary'])")
                    elem.click()
                    log_success(tenant_name + " ""Login >> Update User >> Action Cancel >> Pass ")
                    try:
                        elem = driver.find_element_by_xpath("//h3[contains(text(),'Users')]")
                        if "USERS" in elem.text:
                            log_success(
                                tenant_name + " ""Login >> Update User >> Action Cancel >> Re Rerouting to Users Page >> Pass ")
                    except:
                        log_success(
                            tenant_name + " ""Login >> Update User >> Action Cancel >> Re Rerouting to Users Page >> Failure ")
            except:
                log_failure(tenant_name + " ""Login >> User Page >>  Update User >> Pop up not found")
        except:
            log_failure(tenant_name+" ""Login >> User Page >>  Update User >> Unexpected "
                                                  "Error")