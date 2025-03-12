import time
from Selenium_Functions import *
from Functions import *
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.keys import Keys
import time
from Login import *
from datetime import datetime


# tenant name here
def users_search_test_case(driver, email="", phone="", role=""):
    log_success(tenant_name + " ""Login >> Opening Users Page")
    try:
        elem = driver.find_element_by_xpath("//span[contains(text(),'Admin')]")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("//a[contains(text(),'Users')]")
        elem.click()
        time.sleep(2)
        try:
            elem = driver.find_element_by_xpath("//h3[contains(text(),'Users')]")
            if "USERS" in elem.text:
                log_success(tenant_name + " ""Login >> Users Page Opening  >> Pass")
                elem = driver.find_element_by_xpath("//span[contains(text(),'Admin')]")
                elem.click()
                try:
                    ############################# Search by email
                    try:
                        if email != "":
                            elem = driver.find_element_by_xpath("//input[@placeholder='Email']")
                            elem.click()
                            time.sleep(1)
                            elem.send_keys(email)
                            elem.send_keys(Keys.ENTER)
                            time.sleep(2)
                            try:
                                elem = driver.find_element_by_id("cell-email-undefined")
                                if email in elem.text:
                                    log_success(tenant_name + " ""Login >> Users Page >>  Search by Email >> Pass")
                                    clearall(driver, Pagename="Users", Fieldname="Email")
                                else:
                                    log_failure(
                                        tenant_name + " ""Login >> Users Page >>  Search by Email >> no data "
                                                      "matched")
                            except:
                                elem = driver.find_element_by_xpath(
                                    "//div[contains(text(), 'There are no records to display')]")
                                if 'There are no records to display' in elem.text:
                                    log_failure(
                                        tenant_name + " ""Login >> Users Page >>  Search by Email>> Fail >>  No Data "
                                                      "Available")
                                    clearall(driver, Pagename="Users", Fieldname="Email")
                        else:
                            log_success(
                                tenant_name + " ""Login >> Users Page >>  Search by Email >> Input is Empty ")
                    except:
                        log_failure(tenant_name + " ""Login >> Users Page >>  Search by Email >> Unexpected Error")

                        ############################# Search by Phone Number
                    try:
                        if phone != "":
                            elem = driver.find_element_by_xpath("//input[@placeholder='Phone']")
                            elem.click()
                            time.sleep(1)
                            elem.send_keys(phone)
                            elem.send_keys(Keys.ENTER)
                            time.sleep(2)
                            try:
                                elem = driver.find_element_by_id("cell-phone-undefined")
                                if phone in elem.text:
                                    log_success(
                                        tenant_name + " ""Login >> Users Page >>  Search by Phone  >> Pass")
                                    clearall(driver, Pagename="Users", Fieldname="Phone")
                                else:
                                    log_failure(
                                        tenant_name + " ""Login >> Users Page >>  Search by Phone  >> no data "
                                                      "matched")
                            except:
                                elem = driver.find_element_by_xpath(
                                    "//div[contains(text(), 'There are no records to display')]")
                                if 'There are no records to display' in elem.text:
                                    log_failure(
                                        tenant_name + " ""Login >> Users Page >>  Search by Phone >> Fail >>  No Data "
                                                      "Available")
                                    clearall(driver, Pagename="Users", Fieldname="Phone")
                        else:
                            log_success(
                                tenant_name + " ""Login >> Users Page >>  Search by Phone >> Input is Empty ")
                    except:
                        log_failure(
                            tenant_name + " ""Login >> Users Page >>  Search by Phone >> Unexpected Error")

                    ###############################  Search by Role
                    try:
                        if role != "":
                            try:
                                elem = driver.find_element_by_xpath("//input[@placeholder='Role']")
                                elem.click()
                                time.sleep(1)
                                elem.send_keys(role)
                                elem.send_keys(Keys.ENTER)
                                time.sleep(2)
                                log_success(tenant_name + " ""Login >> Users Page >>  Role Entered >> Pass")
                                try:
                                    elem = driver.find_element_by_id("cell-roles-undefined")
                                    text = str(elem.text)
                                    text = text.lower()
                                    if role in text:
                                        try:
                                            elem = driver.find_element_by_xpath(
                                                "//span[@class='sc-cvbbAY sc-jWBwVP hgiyph']")
                                            # total number of records
                                            total = int(elem.text[7:])
                                            # per page record
                                            length = int(elem.text[2:4])
                                            # print(length)
                                            log_success(
                                                tenant_name + " ""Login >> Roles Page >>  Role >> '" + role + "' >> Total Number of Records >>"" '" + str(
                                                    total) + " "" >> Pass")
                                            global start
                                            start = 0
                                            global count
                                            count = 0

                                            class myRange(object):

                                                def restartFrom(self, start):
                                                    self.start = start

                                                def get(self, start, end):
                                                    self.start = start
                                                    while self.start != end:
                                                        yield self.start
                                                        self.start += 1

                                            myRange = myRange()
                                            for start in myRange.get(start, total):
                                                try:
                                                    ref = driver.find_element_by_xpath(
                                                        "//div[@id='row-" + str(
                                                            start) + "']/div[@id='cell-ref-undefined']")
                                                    if ref:
                                                        elem1 = driver.find_element_by_xpath(
                                                            "//div[@id='row-" + str(
                                                                start) + "']/div[@id='cell-roles-undefined']")
                                                        text = str(elem1.text)
                                                        text = text.lower()
                                                        if role.lower() in text:
                                                            log_success(tenant_name + " ""Login >> Roles Page >> Ref id >>"" '" + str(ref.text) + " "" >>  Search by Role  >>"" '" + str(
                                                                    role) + "' "">> Pass")
                                                            try:
                                                                start += 1
                                                                count += 1
                                                                try:
                                                                    elem = driver.find_element_by_xpath("(//div[@class='table__icon_opt dropdown'])["+str(start)+"]")
                                                                    log_success(tenant_name + " ""Login >> Roles Page >> Ref id >>"" '" + str(ref.text) + " "" >>  Search by Role  >>"" '" + str(
                                                                                role) + "' "">> Change Password Ellipse Present >> Pass")
                                                                except:
                                                                    log_failure(tenant_name + " ""Login >> Roles Page >> Ref id >>"" '" + str(ref.text) + " "" >>  Search by Role  >>"" '" + str(
                                                                                role) + "' "">> Change Password Ellipse Present >> Fail")
                                                                try:
                                                                    elem = driver.find_element_by_xpath(
                                                                        "(//div[@data-tag='allowRowEvents']//span[@class='table__action-icon']/*[name()='svg'])[" + str(
                                                                            start) + "]")
                                                                    log_success(tenant_name + " ""Login >> Roles Page >> Ref id >>"" '" + str(ref.text) + " "" >>  Search by Role  >>"" '" + str(
                                                                                role) + "' "">> Change Status Button Available >> Pass")
                                                                except:
                                                                    log_failure(tenant_name + " ""Login >> Roles Page >> Ref id >>"" '" + str(ref.text) + " "" >>  Search by Role  >>"" '" + str(
                                                                                role) + "' "">> Change Status Button Available >> Fail")
                                                                try:
                                                                    elem = driver.find_element_by_xpath(
                                                                        "(//div[@data-tag='allowRowEvents']//span[2][@class='table__action-icon']/*[name()='svg'])[" + str(
                                                                            start) + "]")
                                                                    log_success(tenant_name + " ""Login >> Roles Page >> Ref id >>"" '" + str(ref.text) + " "" >>  Search by Role  >>"" '" + str(
                                                                                role) + "' "">> Edit User Button Available >> Pass")
                                                                except:
                                                                    log_failure(tenant_name + " ""Login >> Roles Page >> Ref id >>"" '" + str(ref.text) + " "" >>  Search by Role  >>"" '" + str(
                                                                                role) + "' "">> Edit User Button Available >> Fail")
                                                                try:
                                                                    elem = driver.find_element_by_xpath(
                                                                        "(//div[@data-tag='allowRowEvents']//span[3][@class='table__action-icon']/*[name()='svg'])[" + str(
                                                                            start) + "]")
                                                                    log_success(tenant_name + " ""Login >> Roles Page >> Ref id >>"" '" + str(ref.text) + " "" >>  Search by Role  >>"" '" + str(
                                                                                role) + "' "">> Assign Role Button Available >> Pass")
                                                                except:
                                                                    log_failure(tenant_name + " ""Login >> Roles Page >> Ref id >>"" '" + str(ref.text) + " "" >>  Search by Role  >>"" '" + str(
                                                                                role) + "' "">> Assign Role Button Available >> Fail")

                                                                start -= 1

                                                            except:
                                                                start -= 1

                                                        if count == length and length < total:
                                                            try:
                                                                elem = driver.find_element_by_xpath(
                                                                    "//button[@id='pagination-next-page'][@aria-disabled='false']")
                                                                elem.click()
                                                                time.sleep(1)
                                                                elem = driver.find_element_by_xpath(
                                                                    "//span[@class='sc-cvbbAY sc-jWBwVP hgiyph']")
                                                                # per page record
                                                                text = elem.text
                                                                text = text.partition('-')
                                                                lengtht = text[2]
                                                                lengtht = lengtht.partition(' ')
                                                                length = int(lengtht[0])
                                                                myRange.restartFrom(-1)
                                                                time.sleep(2)
                                                            except:
                                                                log_failure(
                                                                    tenant_name + " ""Login >> Users Page >> Clicking on Next Page >> Unexpected issue")
                                                        if count == length and length == total:
                                                            try:
                                                                elem = driver.find_element_by_xpath(
                                                                    "//button[@id='pagination-next-page'][@aria-disabled='true']")
                                                                if elem:
                                                                    log_success(
                                                                        tenant_name + " ""Login >> Users Page >>  Search by Role  >> Pass")
                                                                    clearall(driver, Pagename="Users",
                                                                             Fieldname="Role")
                                                                    break
                                                                else:
                                                                    pass
                                                            except:
                                                                log_failure(
                                                                    tenant_name + " ""Login >> Users Page >>  Search by Role  >> Unexpetced issue")
                                                except:
                                                    elem = driver.find_element_by_xpath(
                                                        "//button[@id='pagination-next-page'][@aria-disabled='true']")
                                                    if elem:
                                                        log_success(
                                                            tenant_name + " ""Login >> Roles Page >>  Search by Role  >> Pass")
                                                        clearall(driver, Pagename="Roles", Fieldname="Role")
                                                        break
                                                    else:
                                                        pass
                                        except:
                                            log_failure(
                                                tenant_name + " ""Login >> Roles Page >>  Search by Role Current Page >> Element Present >> Fail")
                                            clearall(driver, Pagename="Roles", Fieldname="Role")
                                    else:
                                        log_failure(
                                            tenant_name + " ""Login >> Users Page >>  Search by Role  >> no data "
                                                          "matched")
                                except:
                                    elem = driver.find_element_by_xpath(
                                        "//div[contains(text(), 'There are no records to display')]")
                                    if 'There are no records to display' in elem.text:
                                        log_failure(
                                            tenant_name + " ""Login >> Users Page >>  Search by Role >> Fail >>  No Data "
                                                          "Available")
                                        clearall(driver, Pagename="Users", Fieldname="Role")
                            except:
                                log_failure(tenant_name + " ""Login >> Users Page >>  Role Entered  >> Fail")
                        else:
                            log_failure(
                                tenant_name + " ""Login >> Users Page >>  Search by Role  >> Input is Empty")
                    except:
                        log_failure(tenant_name + " ""Login >> Users Page >>  Search by Role  >> Unexpected Error")
                        clearall(driver, Pagename="Users", Fieldname="Role")

                except:
                    log_failure(tenant_name + " ""Login >> Opening Users Page  >> Unexpected Error")
        except:
            log_failure(tenant_name + " ""Login >> Users Page Opening >> Fail")
    except:
        log_failure(tenant_name + " ""Login >> Finance Menu Opening >> Fail")
