import time
from Selenium_Functions import *
from Functions import *
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.keys import Keys
import time
from Login import *
from datetime import datetime


# tenant name here
def payments_search_test_case(driver, status="", ref="", reportno="",collected_date="",Deposited_Date=""):
    log_success(tenant_name + " ""Login >> Opening Payments Page")
    try:
        elem = driver.find_element_by_xpath("//span[contains(text(),'Finance')]")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("//a[contains(text(),'Payments')]")
        elem.click()
        time.sleep(2)
        try:
            elem = driver.find_element_by_xpath("//h3[contains(text(),'Payments')]")
            if "PAYMENTS" in elem.text:
                log_success(tenant_name + " ""Login >> Payments Page Opening  >> Pass")
                elem = driver.find_element_by_xpath("//span[contains(text(),'Finance')]")
                elem.click()
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
                                    log_success(tenant_name + " ""Login >> Payments Page >>  Search by Ref #  >> Pass")
                                    clearall(driver, Pagename="Payments", Fieldname="Ref #")
                                else:
                                    log_failure(tenant_name + " ""Login >> Payments Page >>  Search by Ref #  >> no data "
                                                              "matched")
                            except:
                                elem = driver.find_element_by_xpath(
                                    "//div[contains(text(), 'There are no records to display')]")
                                if 'There are no records to display' in elem.text:
                                    log_failure(
                                        tenant_name + " ""Login >> Payments Page >>  Search by Ref # >> Fail >>  No Data "
                                                      "Available")
                                    clearall(driver, Pagename="Payments", Fieldname="Ref #")
                        else:
                            log_success(tenant_name + " ""Login >> Payments Page >>  Search by Ref #  >> Input is Empty ")
                    except:
                        log_failure(tenant_name + " ""Login >> Payments Page >>  Search by Ref #  >> Unexpected Error")

                        ############################# Search by Report #
                    try:
                        if reportno != "":
                            elem = driver.find_element_by_xpath("//input[@placeholder='Report #']")
                            elem.click()
                            time.sleep(1)
                            elem.send_keys(reportno)
                            elem.send_keys(Keys.ENTER)
                            time.sleep(2)
                            try:
                                elem = driver.find_element_by_id("cell-report-undefined")
                                if reportno in elem.text:
                                    log_success(
                                        tenant_name + " ""Login >> Payments Page >>  Search by Report #  >> Pass")
                                    clearall(driver, Pagename="Payments", Fieldname="Report #")
                                else:
                                    log_failure(
                                        tenant_name + " ""Login >> Payments Page >>  Search by Report #  >> no data "
                                                      "matched")
                            except:
                                elem = driver.find_element_by_xpath(
                                    "//div[contains(text(), 'There are no records to display')]")
                                if 'There are no records to display' in elem.text:
                                    log_failure(
                                        tenant_name + " ""Login >> Payments Page >>  Search by Report # >> Fail >>  No Data "
                                                      "Available")
                                    clearall(driver, Pagename="Payments", Fieldname="Report #")
                        else:
                            log_success(
                                tenant_name + " ""Login >> Payments Page >>  Search by Ref #  >> Input is Empty ")
                    except:
                        log_failure(
                            tenant_name + " ""Login >> Payments Page >>  Search by Ref #  >> Unexpected Error")
    
                    ###############################  Search by Status Dropdown
                    try:
                        if status != "":
                            elem = driver.find_element_by_xpath(
                                "//span[@class='form-control text-truncate dropdown-toggle'][contains(text(),'Status')]")
                            elem.click()
                            time.sleep(1)
                            try:
                                elem = driver.find_element_by_xpath(
                                    "//button[@class='dropdown-item'][contains(text(),'" + status + "')]")
                                log_success(tenant_name + " ""Login >> Payments Page >>  Status Selection  >> Pass")
                                elem.click()
                                time.sleep(2)
                                try:
                                    elem = driver.find_element_by_id("cell-status-undefined")
                                    if status in elem.text:
                                        log_success(tenant_name + " ""Login >> Payments Page >>  Search by Status  >> Pass")
                                        try:
                                            log_success(
                                                tenant_name + " ""Login >> Payments Page >>  Search by Status  >> Element Present >> Pass")
                                            elem = driver.find_element_by_xpath("//span[@class='sc-cvbbAY sc-jWBwVP hgiyph']")
                                            #total number of records
                                            total = int(elem.text[7:])
                                            # per page record
                                            length = int(elem.text[2:4])
                                            #print(length)
                                            log_success(
                                                tenant_name + " ""Login >> Payments Page >>  Status >> '" + status + "' >> Total Number of Records >>"" " + str(
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
                                                    text = str(elem1.text)
                                                    text = text.lower()
                                                    if status.lower() == text:
                                                        log_success(
                                                            tenant_name + " ""Login >> Payments Page >>  Search by Status Current Page >> Ref id >>"" " + str(
                                                                ref.text) + " "" >> Pass")
                                                        if status in ('Collected','Deposited'):
                                                            try:
                                                                try:
                                                                    start += 1
                                                                    count += 1
                                                                    elem=driver.find_element_by_xpath("(//span[@class='table__action-icon']/*[name()='svg']/*[name()='circle'])[" + str(start) + "]")
                                                                    log_success(
                                                                        tenant_name + " ""Login >> Payments Page >> Ref id >>"" " + str(
                                                                            ref.text) + " "" Status >> '" + status + "' >> View Lead Button Present >> Pass")
                                                                    start -= 1 
                                                                except:
                                                                    start -= 1 
                                                                    log_failure(
                                                                        tenant_name + " ""Login >> Payments Page >> Ref id >>"" " + str(
                                                                            ref.text) + " "" Status >> '" + status + "' >> View Lead Button Present >> Fail")
                                                                try:
                                                                    start += 1
                                                                    elem = driver.find_element_by_xpath(
                                                                        "(//span[@class='table__action-icon']/*[name()='svg']/*[name()='polyline'])[" + str(
                                                                            start) + "]")
                                                                    log_success(
                                                                        tenant_name + " ""Login >> Payments Page >> Ref id >>"" " + str(
                                                                            ref.text) + " "" Status >> '" + status + "' >> View Report Button Present >> Pass")
                                                                    start -= 1 
                                                                except:
                                                                    start -= 1 
                                                                    log_failure(
                                                                        tenant_name + " ""Login >> Payments Page >> Ref id >>"" " + str(
                                                                            ref.text) + " "" Status >> '" + status + "' >> View Report Button Present >> Fail")
                                                            except:
                                                                log_failure(
                                                                    tenant_name + " ""Login >> Payments Page >> Ref id >>"" " + str(
                                                                        ref.text) + " "" Status >> '" + status + "' >> View Report Button Present >> Fail")
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
                                                                        tenant_name + " ""Login >> Payments Page >> Clicking on Next Page >> Unexpected issue")
                                                            if count == length and length == total:
                                                                try:
                                                                    elem = driver.find_element_by_xpath(
                                                                        "//button[@id='pagination-next-page'][@aria-disabled='true']")
                                                                    if elem:
                                                                        log_success(
                                                                            tenant_name + " ""Login >> Payments Page >>  Search by Status  >> Pass")
                                                                        clearall(driver, Pagename="Deposits",
                                                                                 Fieldname="Status")
                                                                        break
                                                                    else:
                                                                        pass
                                                                except:
                                                                    log_failure(
                                                                        tenant_name + " ""Login >> Payments Page >>  Search by Status  >> Unexpetced issue")
                                        except:
                                            log_success(
                                                tenant_name + " ""Login >> Payments Page >>  Search by Status Current Page >> Element Present >> Fail")
                                        clearall(driver, Pagename="Payments", Fieldname="Status")
                                    else:
                                        log_failure(tenant_name + " ""Login >> Payments Page >>  Search by Status  >> no data "
                                                                  "matched")
                                except:
                                    elem = driver.find_element_by_xpath(
                                        "//div[contains(text(), 'There are no records to display')]")
                                    if 'There are no records to display' in elem.text:
                                        log_failure(
                                            tenant_name + " ""Login >> Payments Page >>  Search by Status >> Fail >>  No Data "
                                                          "Available")
                                        clearall(driver, Pagename="Payments", Fieldname="Status")
                            except:
                                log_failure(tenant_name + " ""Login >> Payments Page >>  Status Selection  >> Fail")
                        else:
                            log_failure(tenant_name + " ""Login >> Payments Page >>  Search by Status  >> Input is Empty")
                    except:
                        log_failure(tenant_name + " ""Login >> Payments Page >>  Search by status  >> Unexpected Error")
                        clearall(driver, Pagename="Payments", Fieldname="Status")
    
                    ###############################  Search by Collected Date Calendar
                    try:
                        if not collected_date:
                            elem = driver.find_element_by_id("exampleFormControlSelect3")
                            elem.click()
                            time.sleep(1)
                            collected_date = datetime.today().strftime('%d')
                            if collected_date[0] == '0':
                                date = collected_date[1]
                            else:
                                date = collected_date
                            elem = driver.find_element_by_xpath("//div[@aria-label][text() = '" + date + "']")
                            elem.click()
                            elem.click()
                            time.sleep(2)
                            try:
                                elem = driver.find_element_by_id("cell-collected-at-undefined")
                                if date in elem.text:
                                    log_success(tenant_name + " ""Login >> Payments Page >>  Search by Collected Date  >> Pass")
                                    clearall(driver, Pagename="Payments", Fieldname="Collected Date")
                                else:
                                    log_failure(
                                        tenant_name + " ""Login >> Payments Page >>  Search by Collected Date  >> No Data "
                                                      "Matched")
                            except:
                                time.sleep(2)
                                elem = driver.find_element_by_xpath(
                                    "//div[contains(text(),'There are no records to display')]")
                                if 'There are no records to display' in elem.text:
                                    log_failure(
                                        tenant_name + " ""Login >> Payments Page >>  Search by Collected Date  >> Fail >> No "
                                                      "Data Available")
                                    clearall(driver, Pagename="Payments", Fieldname="Collected Date")
                        else:
                            log_failure(
                                tenant_name + " ""Login >> Payments Page >>  Search by Collected Date  >> Input is Empty")
                    except:
                        log_failure(tenant_name + " ""Login >> Payments Page >>  Search by Collected Date  >> Unexpected "
                                                  "Error")
                    ###############################  Search by Deposited date Calendar
                    try:
                        if not Deposited_Date:
                            #elem = driver.find_element_by_id("exampleFormControlSelect3")
                            elem = driver.find_element_by_xpath("(//input[@id='exampleFormControlSelect3'])[2]")
                            elem.click()
                            time.sleep(1)
                            Deposited_Date = datetime.today().strftime('%d')
                            if Deposited_Date[0] == '0':
                                date = Deposited_Date[1]
                            else:
                                date = Deposited_Date
                            elem = driver.find_element_by_xpath("//div[@aria-label][text() = '" + date + "']")
                            elem.click()
                            elem.click()
                            time.sleep(2)
                            try:
                                elem = driver.find_element_by_id("cell-deposited-at-undefined")
                                if date in elem.text:
                                    log_success(
                                        tenant_name + " ""Login >> Payments Page >>  Search by Deposited date  >> Pass")
                                    clearall(driver, Pagename="Payments", Fieldname="Deposited Date")
                                else:
                                    log_failure(
                                        tenant_name + " ""Login >> Payments Page >>  Search by Deposited date  >> No Data "
                                                      "Matched")
                            except:
                                time.sleep(2)
                                elem = driver.find_element_by_xpath(
                                    "//div[contains(text(),'There are no records to display')]")
                                if 'There are no records to display' in elem.text:
                                    log_failure(
                                        tenant_name + " ""Login >> Payments Page >>  Search by Deposited date  >> Fail >> No "
                                                      "Data Available")
                                    clearall(driver, Pagename="Payments", Fieldname="Deposited Date")
                        else:
                            log_failure(
                                tenant_name + " ""Login >> Payments Page >>  Search by Deposited date  >> Input is Empty")
                    except:
                        log_failure(tenant_name + " ""Login >> Payments Page >>  Search by Deposited date  >> Unexpected "
                                                  "Error")
                except:
                    log_failure(tenant_name + " ""Login >> Opening Payments Page  >> Unexpected Error")
        except:
            log_failure(tenant_name + " ""Login >> Payments Page Opening >> Fail")
    except:
        log_failure(tenant_name + " ""Login >> Finance Menu Opening >> Fail")
