import time
from Selenium_Functions import *
from Functions import *
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.keys import Keys
import time
from Login import *
from datetime import datetime


# tenant name here
def lead_type_search_test_case(driver, name="",ref=""):
    log_success(tenant_name + " ""Login >> Opening Lead Types Page")
    try:
        elem = driver.find_element_by_xpath("//span[contains(text(),'Admin')]")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("//a[contains(text(),'Lead Types')]")
        elem.click()
        time.sleep(2)
        try:
            elem = driver.find_element_by_xpath("//h3[contains(text(),'Lead Types')]")
            if "LEAD TYPES" in elem.text:
                log_success(tenant_name + " ""Login >> Lead Types Page Opening  >> Pass")
                elem = driver.find_element_by_xpath("//span[contains(text(),'Admin')]")
                elem.click()
                try:
                    try:
                        if ref != "":
                            elem = driver.find_element_by_xpath("//input[@placeholder='Reference #']")
                            elem.click()
                            time.sleep(1)
                            elem.send_keys(ref)
                            elem.send_keys(Keys.ENTER)
                            time.sleep(2)
                            try:
                                elem = driver.find_element_by_id("cell-ref-undefined")
                                if ref in elem.text:
                                    log_success(tenant_name + " ""Login >> Lead Types Page >>  Search by Ref #  >> Pass")
                                    clearall(driver, Pagename="Lead Types", Fieldname="Ref #")
                                else:
                                    log_failure(tenant_name + " ""Login >> Lead Types Page >>  Search by Ref #  >> no data "
                                                              "matched")
                            except:
                                elem = driver.find_element_by_xpath(
                                    "//div[contains(text(), 'There are no records to display')]")
                                if 'There are no records to display' in elem.text:
                                    log_failure(
                                        tenant_name + " ""Login >> Lead Types Page >>  Search by Ref # >> Fail >>  No Data "
                                                      "Available")
                                    clearall(driver, Pagename="Lead Types", Fieldname="Ref #")
                        else:
                            log_success(tenant_name + " ""Login >> Lead Types Page >>  Search by Ref #  >> Input is Empty ")
                    except:
                        log_failure(tenant_name + " ""Login >> Lead Types Page >>  Search by Ref #  >> Unexpected Error")
                    ############################# Search by Name
                    try:
                        if name != "":
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
                                    log_success(tenant_name + " ""Login >> Lead Types Page >>  Search by Name  >> Pass")
                                    try:
                                        elem = driver.find_element_by_xpath(
                                            "//span[@class='sc-cvbbAY sc-jWBwVP hgiyph']")
                                        # total number of records
                                        total = int(elem.text[7:])
                                        # per page record
                                        length = int(elem.text[2:4])
                                        # print(length)
                                        log_success(
                                            tenant_name + " ""Login >> Lead Types Page >>  Name >> '" + name + "' >> Total Number of Records >>"" " + str(
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
                                                count += 1
                                                time.sleep(1)
                                                elem = driver.find_element_by_xpath(
                                                    "//div[@id='row-" + str(start) + "']/div[@id='cell-ref-undefined']")
                                                if elem:
                                                    elem1 = driver.find_element_by_xpath(
                                                        "//div[@id='row-" + str(
                                                            start) + "']/div[@id='cell-name-undefined']")
                                                    text = str(elem1.text)
                                                    text = text.lower()
                                                    if name.lower() in text:
                                                        log_success(
                                                            tenant_name + " ""Login >> Lead Types Page >>  Search by Name  >> Ref id >>"" " + str(
                                                                elem.text) + " "" >> Pass")
                                                        if count== length and length < total:
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
                                                                    tenant_name + " ""Login >> Lead Types Page >> Clicking on Next Page >> Unexpected issue")
                                                        if count == length and length == total:
                                                            try:
                                                                elem = driver.find_element_by_xpath(
                                                                    "//button[@id='pagination-next-page'][@aria-disabled='true']")
                                                                if elem:
                                                                    log_success(
                                                                        tenant_name + " ""Login >> Lead Types Page >>  Search by Name  >> Pass")
                                                                    clearall(driver, Pagename="Lead Types", Fieldname="Name")
                                                                    break
                                                                else:
                                                                    pass
                                                            except:
                                                                log_failure(
                                                                    tenant_name + " ""Login >> Lead Types Page >>  Search by Name  >> Unexpetced issue")
                                            except:
                                                elem = driver.find_element_by_xpath(
                                                    "//button[@id='pagination-next-page'][@aria-disabled='true']")
                                                if elem:
                                                    log_success(
                                                        tenant_name + " ""Login >> Lead Types Page >>  Search by Name  >> Pass")
                                                    clearall(driver, Pagename="Lead Types", Fieldname="Name")
                                                    break
                                                else:
                                                    pass
                                    except:
                                        log_failure(
                                            tenant_name + " ""Login >> Lead Types Page >>  Search by Name Current Page >> Element Present >> Fail")
                                        clearall(driver, Pagename="Lead Types", Fieldname="Name")
                                else:
                                    log_failure(tenant_name + " ""Login >> Lead Types Page >>  Search by Name  >> no data "
                                                              "matched")
                            except:
                                elem = driver.find_element_by_xpath(
                                    "//div[contains(text(), 'There are no records to display')]")
                                if 'There are no records to display' in elem.text:
                                    log_failure(
                                        tenant_name + " ""Login >> Lead Types Page >>  Search by Name >> Fail >>  No Data "
                                                      "Available")
                                    clearall(driver, Pagename="Lead Types", Fieldname="Name")
                        else:
                            log_success(
                                tenant_name + " ""Login >> Lead Types Page >>  Search by Name >> Input is Empty ")
                    except:
                        log_failure(tenant_name + " ""Login >> Lead Types Page >>  Search by Name >> Unexpected Error")

                except:
                    log_failure(tenant_name + " ""Login >> Opening Lead Types Page  >> Unexpected Error")
        except:
            log_failure(tenant_name + " ""Login >> Lead Types Page Opening >> Fail")
    except:
        log_failure(tenant_name + " ""Login >> Finance Menu Opening >> Fail")
