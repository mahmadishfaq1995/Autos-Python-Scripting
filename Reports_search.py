import time
from Selenium_Functions import *
from Functions import *
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.keys import Keys
import time
from Login import *
from datetime import datetime


# tenant name here
def report_search_test_case(driver, status="", ref="",created_date="",completed_date=""):
    log_success(tenant_name + " ""Login >> Opening Reports Page")
    elem = driver.find_element_by_xpath("//span[contains(text(),'Reports')]")
    elem.click()
    time.sleep(2)
    try:
        elem = driver.find_element_by_xpath("//h3[contains(text(),'Reports')]")
        if "REPORTS" in elem.text:
            log_success(tenant_name + " ""Login >> Reports Page Opening  >> Pass")
            try:
                ############################# Search by Ref
                try:
                    if ref != "":
                        elem = driver.find_element_by_xpath("//input[@placeholder='Ref #']")
                        elem.click()
                        time.sleep(1)
                        elem.send_keys(ref)
                        elem.send_keys(Keys.ENTER)
                        time.sleep(2)
                        try:
                            elem = driver.find_element_by_id("cell-ref-undefined")
                            if ref in elem.text:
                                log_success(tenant_name + " ""Login >> Reports Page >>  Search by Ref #  >> Pass")
                                clearall(driver, Pagename="Reports", Fieldname="Ref #")
                            else:
                                log_failure(tenant_name + " ""Login >> Reports Page >>  Search by Ref #  >> no data "
                                                          "matched")
                        except:
                            elem = driver.find_element_by_xpath(
                                "//div[contains(text(), 'There are no records to display')]")
                            if 'There are no records to display' in elem.text:
                                log_failure(
                                    tenant_name + " ""Login >> Reports Page >>  Search by Ref # >> Fail >>  No Data "
                                                  "Available")
                                clearall(driver, Pagename="Reports", Fieldname="Ref #")
                    else:
                        log_success(tenant_name + " ""Login >> Reports Page >>  Search by Ref #  >> Input is Empty ")
                except:
                    log_failure(tenant_name + " ""Login >> Reports Page >>  Search by Ref #  >> Unexpected Error")

                ###############################  Search by Status Dropdown
                try:
                    if status != "":
                        elem = driver.find_element_by_xpath(
                            "//span[@class='form-control text-truncate dropdown-toggle'][contains(text(),'Status')]")
                        elem.click()
                        time.sleep(1)
                        elem = driver.find_element_by_xpath(
                            "//button[@class='dropdown-item'][contains(text(),'" + status + "')]")
                        elem.click()
                        time.sleep(2)
                        try:
                            elem = driver.find_element_by_id("cell-status-undefined")
                            if status in elem.text:
                                try:
                                    log_success(
                                        tenant_name + " ""Login >> Reports Page >>  Search by Status  >> Element Present >> Pass")
                                    elem = driver.find_element_by_xpath("//span[@class='sc-cvbbAY sc-jWBwVP hgiyph']")
                                    #total number of records
                                    total = int(elem.text[7:])
                                    # per page record
                                    length = int(elem.text[2:4])
                                    #print(length)
                                    log_success(
                                        tenant_name + " ""Login >> Reports Page >>  Status >> '" + status + "' >> Total Number of Records >>"" " + str(
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
                                        ref = driver.find_element_by_xpath(
                                            "//div[@id='row-" + str(start) + "']/div[@id='cell-ref-undefined']")
                                        if ref:
                                            elem1 = driver.find_element_by_xpath(
                                                "//div[@id='row-" + str(start) + "']/div[@id='cell-status-undefined']")
                                            if elem1.text == status:
                                                log_success(
                                                    tenant_name + " ""Login >> Reports Page >>  Search by Status  >> Ref id >>"" " + str(
                                                        ref.text) + " "" >> Pass")
                                                start += 1
                                                count += 1
                                                try:
                                                    elem=driver.find_element_by_xpath("(//span[@class='table__action-icon'])[" + str(start) + "]")
                                                    log_success(
                                                        tenant_name + " ""Login >> Reports Page >> Ref id >>"" " + str(
                                                            ref.text) + " "">> Status >> '" + status + "' >> View Report Button Present >> Pass")

                                                except:
                                                    log_failure(
                                                        tenant_name + " ""Login >> Reports Page >> Ref id >>"" " + str(
                                                            ref.text) + " "">> Status >> '" + status + "' >> View Report Button Present >> Fail")
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
                                                            tenant_name + " ""Login >> Reports Page >> Clicking on Next Page >> Unexpected issue")
                                                if count == length and length == total:
                                                    try:
                                                        elem = driver.find_element_by_xpath(
                                                            "//button[@id='pagination-next-page'][@aria-disabled='true']")
                                                        if elem:
                                                            log_success(
                                                                tenant_name + " ""Login >> Reports Page >>  Search by Status  >> Pass")
                                                            clearall(driver, Pagename="Reports",
                                                                     Fieldname="Status")
                                                            break
                                                        else:
                                                            pass
                                                    except:
                                                        log_failure(
                                                            tenant_name + " ""Login >> Reports Page >>  Search by Status  >> Unexpetced issue")

                                except:
                                    log_success(
                                        tenant_name + " ""Login >> Reports Page >>  Search by Status Current Page >> Element Present >> Fail")
                                clearall(driver, Pagename="Reports", Fieldname="Status")
                            else:
                                log_failure(tenant_name + " ""Login >> Reports Page >>  Search by Status  >> no data "
                                                          "matched")
                        except:
                            elem = driver.find_element_by_xpath(
                                "//div[contains(text(), 'There are no records to display')]")
                            if 'There are no records to display' in elem.text:
                                log_failure(
                                    tenant_name + " ""Login >> Reports Page >>  Search by Status >> Fail >>  No Data "
                                                  "Available")
                                clearall(driver, Pagename="Reports", Fieldname="Status")
                    else:
                        log_failure(tenant_name + " ""Login >> Reports Page >>  Search by Status  >> Input is Empty")
                except:
                    log_failure(tenant_name + " ""Login >> Reports Page >>  Search by status  >> Unexpected Error")
                    clearall(driver, Pagename="Reports", Fieldname="Status")

                ###############################  Search by Created date Calendar
                try:
                    if not created_date:
                        elem = driver.find_element_by_id("exampleFormControlSelect3")
                        elem.click()
                        time.sleep(1)
                        created_date = datetime.today().strftime('%d')
                        if created_date[0] == '0':
                            date = created_date[1]
                        else:
                            date = created_date
                        elem = driver.find_element_by_xpath("//div[@aria-label][text() = '" + date + "']")
                        elem.click()
                        elem.click()
                        time.sleep(2)
                        try:
                            elem = driver.find_element_by_id("cell-created-at-undefined")
                            if date in elem.text:
                                log_success(tenant_name + " ""Login >> Reports Page >>  Search by Created date  >> Pass")
                                clearall(driver, Pagename="Reports", Fieldname="Created date")
                            else:
                                log_failure(
                                    tenant_name + " ""Login >> Reports Page >>  Search by Created date  >> No Data "
                                                  "Matched")
                        except:
                            time.sleep(2)
                            elem = driver.find_element_by_xpath(
                                "//div[contains(text(),'There are no records to display')]")
                            if 'There are no records to display' in elem.text:
                                log_failure(
                                    tenant_name + " ""Login >> Reports Page >>  Search by Created date  >> Fail >> No "
                                                  "Data Available")
                                clearall(driver, Pagename="Reports", Fieldname="Created date")
                    else:
                        log_failure(
                            tenant_name + " ""Login >> Reports Page >>  Search by Created date  >> Input is Empty")
                except:
                    log_failure(tenant_name + " ""Login >> Reports Page >>  Search by Created date  >> Unexpected "
                                              "Error")
                ###############################  Search by Completed date Calendar
                try:
                    if not completed_date:
                        #elem = driver.find_element_by_id("exampleFormControlSelect3")
                        elem = driver.find_element_by_xpath("(//input[@id='exampleFormControlSelect3'])[2]")
                        elem.click()
                        time.sleep(1)
                        completed_date = datetime.today().strftime('%d')
                        if completed_date[0] == '0':
                            date = completed_date[1]
                        else:
                            date = completed_date
                        elem = driver.find_element_by_xpath("//div[@aria-label][text() = '" + date + "']")
                        elem.click()
                        elem.click()
                        time.sleep(2)
                        try:
                            elem = driver.find_element_by_id("cell-created-at-undefined")
                            if date in elem.text:
                                log_success(
                                    tenant_name + " ""Login >> Reports Page >>  Search by Completed date  >> Pass")
                                clearall(driver, Pagename="Reports", Fieldname="Completed date")
                            else:
                                log_failure(
                                    tenant_name + " ""Login >> Reports Page >>  Search by Completed date  >> No Data "
                                                  "Matched")
                        except:
                            time.sleep(2)
                            elem = driver.find_element_by_xpath(
                                "//div[contains(text(),'There are no records to display')]")
                            if 'There are no records to display' in elem.text:
                                log_failure(
                                    tenant_name + " ""Login >> Reports Page >>  Search by Completed date  >> Fail >> No "
                                                  "Data Available")
                                clearall(driver, Pagename="Reports", Fieldname="Completed date")
                    else:
                        log_failure(
                            tenant_name + " ""Login >> Reports Page >>  Search by Completed date  >> Input is Empty")
                except:
                    log_failure(tenant_name + " ""Login >> Reports Page >>  Search by Completed date  >> Unexpected "
                                              "Error")
            except:
                log_failure(tenant_name + " ""Login >> Opening Reports Page  >> Unexpected Error")
    except:
        log_failure(tenant_name + " ""Login >> Reports Page Opening >> Fail")
