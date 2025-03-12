import time
from Selenium_Functions import *
from Functions import *
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.keys import Keys
import time
from Login import *
from datetime import datetime


# tenant name here
def deposit_search_test_case(driver, status="", ref="", inspector="", Created_Date="",Action=""):
    log_success(tenant_name + " ""Login >> Opening Deposit Page")
    try:
        elem = driver.find_element_by_xpath("//span[contains(text(),'Finance')]")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("//a[contains(text(),'Deposits')]")
        elem.click()
        time.sleep(2)
        try:
            elem = driver.find_element_by_xpath("//h3[contains(text(),'Deposits')]")
            if "DEPOSITS" in elem.text:
                log_success(tenant_name + " ""Login >> Deposit Page Opening  >> Pass")
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
                                    log_success(tenant_name + " ""Login >> Deposit Page >>  Search by Ref #  >> Pass")
                                    clearall(driver, Pagename="Deposit", Fieldname="Ref #")
                                else:
                                    log_failure(
                                        tenant_name + " ""Login >> Deposit Page >>  Search by Ref #  >> no data "
                                                      "matched")
                            except:
                                elem = driver.find_element_by_xpath(
                                    "//div[contains(text(), 'There are no records to display')]")
                                if 'There are no records to display' in elem.text:
                                    log_failure(
                                        tenant_name + " ""Login >> Deposit Page >>  Search by Ref # >> Fail >>  No Data "
                                                      "Available")
                                    clearall(driver, Pagename="Deposit", Fieldname="Ref #")
                        else:
                            log_success(
                                tenant_name + " ""Login >> Deposit Page >>  Search by Ref #  >> Input is Empty ")
                    except:
                        log_failure(tenant_name + " ""Login >> Deposit Page >>  Search by Ref #  >> Unexpected Error")

                        ############################# Search by Inspector Name
                    try:
                        if inspector != "":
                            elem = driver.find_element_by_xpath("//input[@placeholder='Inspector']")
                            elem.click()
                            time.sleep(1)
                            elem.send_keys(inspector)
                            elem.send_keys(Keys.ENTER)
                            time.sleep(2)
                            try:
                                elem = driver.find_element_by_id("cell-inspector-undefined")
                                if inspector in elem.text:
                                    log_success(
                                        tenant_name + " ""Login >> Deposit Page >>  Search by Inspector  >> Pass")
                                    clearall(driver, Pagename="Deposit", Fieldname="Inspector")
                                else:
                                    log_failure(
                                        tenant_name + " ""Login >> Deposit Page >>  Search by Inspector  >> no data "
                                                      "matched")
                            except:
                                elem = driver.find_element_by_xpath(
                                    "//div[contains(text(), 'There are no records to display')]")
                                if 'There are no records to display' in elem.text:
                                    log_failure(
                                        tenant_name + " ""Login >> Deposit Page >>  Search by Inspector >> Fail >>  No Data "
                                                      "Available")
                                    clearall(driver, Pagename="Deposit", Fieldname="Inspector")
                        else:
                            log_success(
                                tenant_name + " ""Login >> Deposit Page >>  Search by Ref #  >> Input is Empty ")
                    except:
                        log_failure(
                            tenant_name + " ""Login >> Deposit Page >>  Search by Ref #  >> Unexpected Error")

                    ###############################  Search by Status Dropdown
                    try:
                        if status != "":
                            elem = driver.find_element_by_xpath(
                                "//span[@class='form-control text-truncate dropdown-toggle'][contains(text(),'Verified')]")
                            elem.click()
                            time.sleep(1)
                            try:
                                elem = driver.find_element_by_xpath(
                                    "//button[@class='dropdown-item'][contains(text(),'" + status + "')]")
                                elem.click()
                                log_success(tenant_name + " ""Login >> Deposit Page >>  Status Selection  >> Pass")
                                time.sleep(2)
                                try:
                                    if status == 'Verified' and not Action:
                                        try:
                                            elem = driver.find_element_by_xpath(
                                                "//span[@class='sc-cvbbAY sc-jWBwVP hgiyph']")
                                            # total number of records
                                            total = int(elem.text[7:])
                                            # per page record
                                            length = int(elem.text[2:4])
                                            # print(length)
                                            log_success(
                                                tenant_name + " ""Login >> Deposit Page >>  Status >> '" + status + "' >> Total Number of Records >>"" " + str(
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
                                                    time.sleep(1)
                                                    ref = driver.find_element_by_xpath(
                                                        "//div[@id='row-" + str(
                                                            start) + "']/div[@id='cell-ref-undefined']")
                                                    if ref:
                                                        try:
                                                            start += 1
                                                            count += 1
                                                            elem1 = driver.find_element_by_xpath(
                                                                "(//div[@id='cell-verified-at-undefined'])[" + str(
                                                                    start) + "]")
                                                            elem2 = driver.find_element_by_xpath(
                                                                "(//div[@id='cell-verified-undefined'])[" + str(
                                                                    start) + "]")
                                                            if elem1.text != '-' and elem2.text != '-':
                                                                log_success(
                                                                    tenant_name + " ""Login >> Deposit Page >> Ref id >>"" " + str(
                                                                        ref.text) + " >>"" Status >> '" + status + "' >> Verified field value >> '" + str(
                                                                        elem2.text) + "' Verified at field value >> '" + str(
                                                                        elem1.text) + "' >> Pass")
                                                                try:
                                                                    elem = driver.find_element_by_xpath(
                                                                        "(//div[@data-tag='allowRowEvents']//span[@class='table__action-icon']/*[name()='svg'])[" + str(
                                                                            start) + "]")
                                                                    if elem:
                                                                        elem.click()
                                                                        time.sleep(1)
                                                                        try:
                                                                            elem1 = driver.find_element_by_xpath(
                                                                                "//button[text()='Mark Verified']")
                                                                            if elem1:
                                                                                log_failure(
                                                                                    tenant_name + " ""Login >> Deposit Page >> Ref id >>"" " + str(
                                                                                        ref.text) + " >>"" Status >> '" + status + "'  >> Marked as Verified Button not Present >> Fail")
                                                                        except:
                                                                            log_success(
                                                                                tenant_name + " ""Login >> Deposit Page >> Ref id >>"" " + str(
                                                                                    ref.text) + " >>"" Status >> '" + status + "'  >> Marked as Verified Button not Present >> Pass")
                                                                            try:
                                                                                elem1 = driver.find_element_by_xpath(
                                                                                    "//button[text()='Cancel']")
                                                                                elem1.click()
                                                                                log_success(
                                                                                    tenant_name + " ""Login >> Deposit Page >> Ref id >>"" " + str(
                                                                                        ref.text) + " >>"" Status >> '" + status + "'  >> Cancel Button Present >> Pass")
                                                                            except:
                                                                                log_failure(
                                                                                    tenant_name + " ""Login >> Deposit Page >> Ref id >>"" " + str(
                                                                                        ref.text) + " >>"" Status >> '" + status + "'  >> Cancel Button Present >> Fail")

                                                                except:
                                                                    log_failure(
                                                                        tenant_name + " ""Login >> Deposit Page >> Ref id >>"" " + str(
                                                                            ref.text) + " "" >> Marked as Verified  >> Unexpected issue occurred")
                                                            start -= 1
                                                            if count == length and length < total:
                                                                try:
                                                                    elem = driver.find_element_by_xpath(
                                                                        "//button[@id='pagination-next-page'][@aria-disabled='false']")
                                                                    time.sleep(1)
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
                                                                        tenant_name + " ""Login >> Deposit Page >> Clicking on Next Page >> Unexpected issue")
                                                            if count == length and length == total:
                                                                try:
                                                                    elem = driver.find_element_by_xpath(
                                                                        "//button[@id='pagination-next-page'][@aria-disabled='true']")
                                                                    if elem:
                                                                        log_success(
                                                                            tenant_name + " ""Login >> Deposit Page >>  Search by Status  >> Pass")
                                                                        clearall(driver, Pagename="Deposits",
                                                                                 Fieldname="Status")
                                                                        break
                                                                    else:
                                                                        pass
                                                                except:
                                                                    log_failure(
                                                                        tenant_name + " ""Login >> Deposit Page >>  Search by Status  >> Unexpetced issue")
                                                        except:
                                                            start -= 1
                                                            log_failure(
                                                                tenant_name + " ""Login >> Reports Page >> Ref id >>"" " + str(
                                                                    ref.text) + " "" Status >> '" + status + "' >> Verified at Field Data available >> Fail")

                                                except:
                                                    elem = driver.find_element_by_xpath(
                                                        "//button[@id='pagination-next-page'][@aria-disabled='true']")
                                                    if elem:
                                                        log_success(
                                                            tenant_name + " ""Login >> Leads Page >>  Search by Status  >> Pass")
                                                        clearall(driver, Pagename="Leads", Fieldname="Status")
                                                        break
                                                    else:
                                                        pass
                                        except:
                                            log_failure(
                                                tenant_name + " ""Login >> Deposit Page >>  Search by Status Current Page >> Element Present >> Fail")
                                            clearall(driver, Pagename="Deposit", Fieldname="Status")
                                    else:
                                        log_failure(
                                            tenant_name + " ""Login >> Deposit Page >>  Search by Status  >> no data "
                                                          "matched")
                                    if Action == 'MarkVerified' and status == 'Not Verified':
                                        # log_success(
                                        #     tenant_name + " ""Login >> Deposit Page >>  Search by Status >>'" + status + "'>> Pass")
                                        try:
                                            elem = driver.find_element_by_xpath(
                                                "//span[@class='sc-cvbbAY sc-jWBwVP hgiyph']")
                                            # total number of records
                                            total = int(elem.text[7:])
                                            # per page record
                                            length = int(elem.text[2:4])
                                            # print(length)
                                            log_success(
                                                tenant_name + " ""Login >> Deposit Page >>  Status >> '" + status + "' >> Total Number of Records >>"" " + str(
                                                    total) + " "" >> Pass")

                                            global start1
                                            start1 = 0
                                            global count1
                                            count1 = 0

                                            class myRange(object):

                                                def restartFrom(self, start1):
                                                    self.start1 = start1

                                                def get(self, start1, end):
                                                    self.start1 = start1
                                                    while self.start1 != end:
                                                        yield self.start1
                                                        self.start1 += 1

                                            myRange = myRange()
                                            for start1 in myRange.get(start1, total):
                                                try:
                                                    time.sleep(1)
                                                    ref = driver.find_element_by_xpath(
                                                        "//div[@id='row-" + str(
                                                            start1) + "']/div[@id='cell-ref-undefined']")
                                                    if ref:
                                                        try:
                                                            start1 += 1
                                                            count1 += 1
                                                            elem1 = driver.find_element_by_xpath(
                                                                "(//div[@id='cell-verified-at-undefined'])[" + str(
                                                                    start1) + "]")
                                                            elem2 = driver.find_element_by_xpath(
                                                                "(//div[@id='cell-verified-undefined'])[" + str(
                                                                    start1) + "]")
                                                            if '-' in elem1.text and '-' in elem2.text:
                                                                log_success(
                                                                    tenant_name + " ""Login >> Deposit Page >> Ref id >>"" " + str(
                                                                        ref.text) + " >>"" Status >> '" + status + "' >> Verified field value >> '" + str(
                                                                        elem2.text) + "' Verified at field value >> '" + str(
                                                                        elem1.text) + "' >> Pass")
                                                                try:
                                                                    elem = driver.find_element_by_xpath(
                                                                        "(//div[@data-tag='allowRowEvents']//span[@class='table__action-icon']/*[name()='svg'])[" + str(
                                                                            start) + "]")
                                                                    if elem:
                                                                        elem.click()
                                                                        time.sleep(1)
                                                                        elem1 = driver.find_element_by_xpath(
                                                                            "//button[text()='Mark Verified']")
                                                                        if elem1:
                                                                            elem1.click()
                                                                            time.sleep(1)
                                                                            log_success(
                                                                                tenant_name + " ""Login >> Deposit Page >> Ref id >>"" " + str(
                                                                                    ref.text) + " "" >> Marked as Verified  >> Pass")
                                                                except:
                                                                    log_failure(
                                                                        tenant_name + " ""Login >> Deposit Page >> Ref id >>"" " + str(
                                                                            ref.text) + " "" >> Marked as Verified  >> Unexpected issue occurred")
                                                            start1 -= 1
                                                            if count1 == length and length < total:
                                                                try:
                                                                    elem = driver.find_element_by_xpath(
                                                                        "//button[@id='pagination-next-page'][@aria-disabled='false']")
                                                                    time.sleep(1)
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
                                                                        tenant_name + " ""Login >> Deposit Page >> Clicking on Next Page >> Unexpected issue")
                                                            if count1 == length and length == total:
                                                                try:
                                                                    elem = driver.find_element_by_xpath(
                                                                        "//button[@id='pagination-next-page'][@aria-disabled='true']")
                                                                    if elem:
                                                                        log_success(
                                                                            tenant_name + " ""Login >> Deposit Page >>  Search by Status  >> Pass")
                                                                        clearall(driver, Pagename="Deposits",
                                                                                 Fieldname="Status")
                                                                        break
                                                                    else:
                                                                        pass
                                                                except:
                                                                    log_failure(
                                                                        tenant_name + " ""Login >> Deposit Page >>  Search by Status  >> Unexpetced issue")
                                                        except:
                                                            start1 -= 1
                                                            log_failure(
                                                                tenant_name + " ""Login >> Reports Page >> Ref id >>"" " + str(
                                                                    ref.text) + " "" Status >> '" + status + "' >> Verified at Field Data available >> Fail")

                                                except:
                                                    elem = driver.find_element_by_xpath(
                                                        "//button[@id='pagination-next-page'][@aria-disabled='true']")
                                                    if elem:
                                                        log_success(
                                                            tenant_name + " ""Login >> Leads Page >>  Search by Status  >> Pass")
                                                        clearall(driver, Pagename="Leads", Fieldname="Status")
                                                        break
                                                    else:
                                                        pass
                                        except:
                                            log_failure(
                                                tenant_name + " ""Login >> Deposit Page >>  Search by Status Current Page >> Element Present >> Fail")
                                            clearall(driver, Pagename="Deposit", Fieldname="Status")
                                    else:
                                        log_failure(
                                            tenant_name + " ""Login >> Deposit Page >>  Search by Status  >> no data "
                                                          "matched")
                                except:
                                    elem = driver.find_element_by_xpath(
                                        "//div[contains(text(), 'There are no records to display')]")
                                    if 'There are no records to display' in elem.text:
                                        log_failure(
                                            tenant_name + " ""Login >> Deposit Page >>  Search by Status >> Fail >>  No Data "
                                                          "Available")
                                        clearall(driver, Pagename="Deposit", Fieldname="Status")
                            except:
                                log_failure(tenant_name + " ""Login >> Deposit Page >>  Status Selection  >> Fail")
                        else:
                            log_failure(
                                tenant_name + " ""Login >> Deposit Page >>  Search by Status  >> Input is Empty")
                    except:
                        log_failure(tenant_name + " ""Login >> Deposit Page >>  Search by status  >> Unexpected Error")
                        try:
                            time.sleep(2)
                            elem = driver.find_element_by_xpath(
                                '//span[@class][contains(text(),"Clear All Filters")]')
                            elem.click()
                            log_success(tenant_name + " ""Login >> Deposit Page >>  Search by Status >> Clear "
                                                      "Filter >> Pass")
                        except:
                            log_failure(
                                tenant_name + " ""Login >> Deposit Page >>  Search by Status  >> Clear Filter "
                                              ">> Unexpected issue")

                    ###############################  Search by Created Date Calendar
                    try:
                        if not Created_Date:
                            # elem = driver.find_element_by_id("exampleFormControlSelect3")
                            elem = driver.find_element_by_xpath("(//input[@id='exampleFormControlSelect3'])")
                            elem.click()
                            time.sleep(1)
                            Created_Date = datetime.today().strftime('%d')
                            if Created_Date[0] == '0':
                                date = Created_Date[1]
                            else:
                                date = Created_Date
                            elem = driver.find_element_by_xpath("//div[@aria-label][text() = '" + date + "']")
                            elem.click()
                            elem.click()
                            time.sleep(2)
                            try:
                                elem = driver.find_element_by_id("cell-created-at-undefined")
                                if date in elem.text:
                                    log_success(
                                        tenant_name + " ""Login >> Deposit Page >>  Search by Created date >> Pass")
                                    clearall(driver, Pagename="Deposit", Fieldname="Created date")
                                else:
                                    log_failure(
                                        tenant_name + " ""Login >> Deposit Page >>  Search by Created date >> No Data "
                                                      "Matched")
                            except:
                                time.sleep(2)
                                elem = driver.find_element_by_xpath(
                                    "//div[contains(text(),'There are no records to display')]")
                                if 'There are no records to display' in elem.text:
                                    log_failure(
                                        tenant_name + " ""Login >> Deposit Page >>  Search by Created date >> Fail >> No "
                                                      "Data Available")
                                    clearall(driver, Pagename="Deposit", Fieldname="Created date")
                        else:
                            log_failure(
                                tenant_name + " ""Login >> Deposit Page >>  Search by Created date >> Input is Empty")
                    except:
                        log_failure(
                            tenant_name + " ""Login >> Deposit Page >>  Search by Created date >> Unexpected "
                                          "Error")
                except:
                    log_failure(tenant_name + " ""Login >> Opening Deposit Page  >> Unexpected Error")
        except:
            log_failure(tenant_name + " ""Login >> Deposit Page Opening >> Fail")
    except:
        log_failure(tenant_name + " ""Login >> Finance Menu Opening >> Fail")
