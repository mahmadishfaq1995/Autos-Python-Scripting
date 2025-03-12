import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

from Functions import log_failure
from Functions import log_success
from Functions import tenant_name
from selenium.common.exceptions import NoSuchElementException

def assign_role(driver,start="",Rolename=""):
    try:
        elem = driver.find_element_by_xpath(
            "(//div[@data-tag='allowRowEvents']//span[3][@class='table__action-icon']/*[name()='svg'])[" + str(
                start) + "]")
        elem.click()
        try:
            elem = driver.find_element_by_xpath(
                "//h5[@class='modal-title'][contains(text(),'Assign User Role')]")
            if 'Assign User Role' in elem.text:
                log_success(tenant_name + " ""Login >> Users Page >>  Assign Role  >> Pop up opened")
                if Rolename !="":
                    try:
                        # Entering name
                        elem = driver.find_element_by_xpath("//input[@placeholder='Select Role']")
                        elem.click()
                        try:
                            elem = driver.find_element_by_xpath(
                                "//a[@class='dropdown-item']/span[contains(text(),'" + Rolename + "')]")
                            elem.click()
                            log_success(
                                tenant_name + " ""Login >> Users Page >>  Assign Role >> Selecting Role >> Pass")
                        except:
                            log_failure(
                                tenant_name + " ""Login >> Users Page >>  Assign Role >> Selecting Role >> Fail")
                    except:
                        log_failure(
                            tenant_name + " ""Login >> Users Page >>  Assign Role  >> Selecting Role Dropdown >> Failure ")
        except:
            log_failure(
                tenant_name + " ""Login >> Users Page >>  Assign Role  >> Pop up opened >> Failure")
    except:
        log_failure(tenant_name + " ""Login >> Users Page >>  Assign Role  >> Pop up not found")
