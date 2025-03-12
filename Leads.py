import time
from Selenium_Functions import *
from Functions import *
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.keys import Keys
import time
from Login import *
from datetime import datetime



# tenant name here
def Lead_search_test_case(driver, ref="", name="", phone="", city="", status="", leadtype="", inspectiontype="",
                          created_date=""):
    time.sleep(2)
    log_success(tenant_name + " ""Login >> Opening Leads Page")
    elem = driver.find_element_by_xpath("//span[contains(text(),'Leads')]")
    elem.click()
    time.sleep(2)
    try:
        elem = driver.find_element_by_xpath("//h3[contains(text(),'Leads')]")
        if "LEADS" in elem.text:
            log_success(tenant_name + " ""Login >> Leads Page Opening  >> Pass")
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
                                log_success(tenant_name + " ""Login >> Leads Page >>  Search by Ref #  >> Pass")
                                clearall(driver, Pagename="Leads", Fieldname="Ref #")
                            else:
                                log_failure(tenant_name + " ""Login >> Leads Page >>  Search by Ref #  >> no data "
                                                          "matched")
                        except:
                            elem = driver.find_element_by_xpath(
                                "//div[contains(text(), 'There are no records to display')]")
                            if 'There are no records to display' in elem.text:
                                log_failure(
                                    tenant_name + " ""Login >> Leads Page >>  Search by Ref # >> Fail >>  No Data "
                                                  "Available")
                                clearall(driver, Pagename="Leads", Fieldname="Ref #")
                    else:
                        log_success(tenant_name + " ""Login >> Leads Page >>  Search by Ref #  >> Input is Empty ")
                except:
                    log_failure(tenant_name + " ""Login >> Leads Page >>  Search by Ref #  >> Unexpected Error")
                ############################## Search by Name
                try:
                    if name != "":
                        elem = driver.find_element_by_xpath("//input[@placeholder='Name']")
                        elem.click()
                        time.sleep(1)
                        elem.send_keys(name)
                        elem.send_keys(Keys.ENTER)
                        time.sleep(2)
                        elem = driver.find_element_by_xpath(
                            "//li[@class='breadcrumb-item active'][contains(text(),'Leads')]")
                        elem.click()
                        time.sleep(1)
                        try:
                            elem = driver.find_element_by_id("cell-name-undefined")
                            stripped_name = elem.text
                            stripped_name = (stripped_name.splitlines())
                            y = [x.lower() for x in stripped_name]
                            for i in y:
                                try:
                                    if name in i:
                                        log_success(tenant_name + " ""Login >> Leads Page >>  Search by Name  >> Pass")
                                        clearall(driver, Pagename="Leads", Fieldname="Name")
                                        break
                                    else:
                                        continue
                                except:
                                    log_failure(
                                        tenant_name + " ""Login >> Leads Page >>  Search by Name  >> no data matched")
                        except:
                            elem = driver.find_element_by_xpath(
                                "//div[contains(text(), 'There are no records to display')]")
                            if 'There are no records to display' in elem.text:
                                log_failure(
                                    tenant_name + " ""Login >> Leads Page >>  Search by Name >> Fail >>  No Data "
                                                  "Available")
                                clearall(driver, Pagename="Leads", Fieldname="Name")
                    else:
                        log_success(tenant_name + " ""Login >> Leads Page >>  Search by Name  >> Input is Empty")
                except:
                    log_failure(tenant_name + " ""Login >> Leads Page >>  Search by Name  >> Unexpected Error")

                ###############################  Search by Phone
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
                                log_success(tenant_name + " ""Login >> Leads Page >>  Search by Phone  >> Pass")
                                clearall(driver, Pagename="Leads", Fieldname="Phone")
                            else:
                                log_failure(tenant_name + " ""Login >> Leads Page >>  Search by Phone  >> no data "
                                                          "matched")
                        except:
                            elem = driver.find_element_by_xpath(
                                "//div[contains(text(), 'There are no records to display')]")
                            if 'There are no records to display' in elem.text:
                                log_failure(
                                    tenant_name + " ""Login >> Leads Page >>  Search by Phone >> Fail >>  No Data "
                                                  "Available")
                                clearall(driver, Pagename="Leads", Fieldname="Phone")
                    else:
                        log_success(tenant_name + " ""Login >> Leads Page >>  Search by Phone  >> Input is Empty")
                except:
                    log_failure(tenant_name + " ""Login >> Leads Page >>  Search by Phone  >> Unexpected Error")
                ###############################  Search by City Dropdown
                try:
                    if city != "":
                        elem = driver.find_element_by_xpath(
                            "//span[@class='form-control text-truncate dropdown-toggle'][contains(text(),'City')]")
                        elem.click()
                        time.sleep(2)
                        elem = driver.find_element_by_xpath(
                            "//button[@class='dropdown-item'][contains(text(),'" + city + "')]")
                        # elem = driver.find_element_by_xpath("//button[contains(text(),'"+city+"')]")
                        # print("//button[contains(text(),'"+city+"')]")
                        elem.click()
                        time.sleep(2)
                        try:
                            elem = driver.find_element_by_id("cell-location-undefined")
                            if city in elem.text:
                                log_success(tenant_name + " ""Login >> Leads Page >>  Search by City  >> Pass")
                                clearall(driver, Pagename="Leads", Fieldname="City")
                            else:
                                log_failure(
                                    tenant_name + " ""Login >> Leads Page >> Search by City  >> no data matched")
                        except:
                            elem = driver.find_element_by_xpath(
                                "//div[contains(text(), 'There are no records to display')]")
                            if 'There are no records to display' in elem.text:
                                log_failure(
                                    tenant_name + " ""Login >> Leads Page >>  Search by City >> Fail >>  No Data "
                                                  "Available")
                                clearall(driver, Pagename="Leads", Fieldname="City")
                    else:
                        log_success(tenant_name + " ""Login >> Leads Page >> Search by City  >> Input is Empty")
                except:
                    log_failure(tenant_name + " ""Login >> Leads Page >> Search by city  >> Unexpected Error")

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
                                log_success(tenant_name + " ""Login >> Leads Page >>  Search by Status  >> Pass")
                                try:
                                    log_success(
                                        tenant_name + " ""Login >> Leads Page >>  Search by Status  >> Element Present >> Pass")
                                    elem = driver.find_element_by_xpath("//span[@class='sc-cvbbAY sc-jWBwVP hgiyph']")
                                    # total number of records
                                    total = int(elem.text[7:])
                                    # per page record
                                    length = int(elem.text[2:4])
                                    # print(length)
                                    log_success(
                                        tenant_name + " ""Login >> Leads Page >>  Status >> '" + status + "' >> Total Number of Records >>"" " + str(
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
                                                        start) + "']/div[@id='cell-status-undefined']")
                                                text = str(elem1.text)
                                                text = text.lower()
                                                if status.lower() == text:
                                                    log_success(
                                                        tenant_name + " ""Login >> Leads Page >>  Search by Status  >> Ref id >>"" " + str(
                                                            elem.text) + " "" >> Pass")
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
                                                                tenant_name + " ""Login >> Leads Page >> Clicking on Next Page>> Unexpected issue")
                                                    if count == length and length == total:
                                                        try:
                                                            elem = driver.find_element_by_xpath(
                                                                "//button[@id='pagination-next-page'][@aria-disabled='true']")
                                                            if elem:
                                                                log_success(
                                                                    tenant_name + " ""Login >> Leads Page >>  Search by Status  >> Pass")
                                                                clearall(driver, Pagename="Leads",
                                                                         Fieldname="Status")
                                                                break
                                                            else:
                                                                pass
                                                        except:
                                                            log_failure(
                                                                tenant_name + " ""Login >> Leads Page >>  Search by Status  >> Unexpetced issue")
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
                                    log_failure(tenant_name + " ""Login >> Leads Page >>  Search by Status Current Page >> Element Present >> Fail")
                                    clearall(driver, Pagename="Leads", Fieldname="Status")
                            else:
                                log_failure(tenant_name + " ""Login >> Leads Page >>  Search by Status  >> no data "
                                                          "matched")
                        except:
                            elem = driver.find_element_by_xpath(
                                "//div[contains(text(), 'There are no records to display')]")
                            if 'There are no records to display' in elem.text:
                                log_failure(
                                    tenant_name + " ""Login >> Leads Page >>  Search by Status >> Fail >>  No Data "
                                                  "Available")
                                clearall(driver, Pagename="Leads", Fieldname="Status")
                    else:
                        log_failure(tenant_name + " ""Login >> Leads Page >>  Search by Status  >> Input is Empty")
                except:
                    log_failure(tenant_name + " ""Login >> Leads Page >>  Search by status  >> Unexpected Error")
                ###############################  Search by leadtype Dropdown
                try:
                    if leadtype != "":
                        elem = driver.find_element_by_xpath(
                            "//span[@class='form-control text-truncate dropdown-toggle'][contains(text(),'Lead Type')]")
                        elem.click()
                        time.sleep(1)
                        elem = driver.find_element_by_xpath(
                            "//button[@class='dropdown-item'][contains(text(),'" + leadtype + "')]")
                        elem.click()
                        time.sleep(2)
                        try:
                            elem = driver.find_element_by_id("cell-lead-type-undefined")
                            if leadtype in elem.text:
                                log_success(tenant_name + " ""Login >> Leads Page >>  Search by leadtype  >> Pass")
                                clearall(driver, Pagename="Leads", Fieldname="leadtype")
                            else:
                                log_failure(
                                    tenant_name + " ""Login >> Leads Page >>  Search by leadtype  >> no data matched ")
                        except:
                            elem = driver.find_element_by_xpath(
                                "//div[contains(text(), 'There are no records to display')]")
                            if 'There are no records to display' in elem.text:
                                log_failure(
                                    tenant_name + " ""Login >> Leads Page >>  Search by leadtype  >> Fail >>  No Data "
                                                  "Available")
                                clearall(driver, Pagename="Leads", Fieldname="leadtype")
                    else:
                        log_failure(tenant_name + " ""Login >> Leads Page >>  Search by leadtype  >> Input is Empty")
                except:
                    log_failure(tenant_name + " ""Login >> Leads Page >>  Search by lead type  >> Unexpected Error")
                ###############################  Search by inspection type Dropdown
                try:
                    if inspectiontype != "":
                        elem = driver.find_element_by_xpath(
                            "//span[@class='form-control text-truncate dropdown-toggle'][contains(text(),'Inspection Type')]")
                        elem.click()
                        time.sleep(1)
                        elem = driver.find_element_by_xpath(
                            "//div[@class='dropdown-menu show']//button[@class='dropdown-item'][contains(text(),'" + inspectiontype + "')]")
                        elem.click()
                        time.sleep(2)
                        try:
                            elem = driver.find_element_by_id("cell-inspection-type-undefined")
                            if inspectiontype in elem.text:
                                log_success(
                                    tenant_name + " ""Login >> Leads Page >>  Search by inspection type  >> Pass")
                                clearall(driver, Pagename="Leads", Fieldname="inspection type")
                            else:
                                log_failure(
                                    tenant_name + " ""Login >> Leads Page >>  Search by inspection type  >> no data "
                                                  "matched")
                        except:
                            elem = driver.find_element_by_xpath(
                                "//div[contains(text(), 'There are no records to display')]")
                            if 'There are no records to display' in elem.text:
                                log_failure(
                                    tenant_name + " ""Login >> Leads Page >>  Search by inspection type  >> Fail >> "
                                                  "No Data Available")
                                clearall(driver, Pagename="Leads", Fieldname="inspection type")
                    else:
                        log_failure(
                            tenant_name + " ""Login >> Leads Page >>  Search by inspection type  >> Input is Empty ")
                except:
                    log_failure(
                        tenant_name + " ""Login >> Leads Page >>  Search by inspection type  >> Unexpected Error")
                ###############################  Search by date Calendar
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
                                log_success(tenant_name + " ""Login >> Leads Page >>  Search by Created date  >> Pass")
                                clearall(driver, Pagename="Leads", Fieldname="Created date")
                            else:
                                log_failure(
                                    tenant_name + " ""Login >> Leads Page >>  Search by Created date  >> No Data "
                                                  "Matched")
                        except:
                            time.sleep(2)
                            elem = driver.find_element_by_xpath(
                                "//div[contains(text(),'There are no records to display')]")
                            if 'There are no records to display' in elem.text:
                                log_failure(
                                    tenant_name + " ""Login >> Leads Page >>  Search by Created date  >> Fail >> No "
                                                  "Data Available")
                                clearall(driver, Pagename="Leads", Fieldname="Created date")
                    else:
                        log_failure(
                            tenant_name + " ""Login >> Leads Page >>  Search by Created date  >> Input is Empty")
                except:
                    log_failure(tenant_name + " ""Login >> Leads Page >>  Search by Created date  >> Unexpected "
                                              "Error")
            except:
                log_failure(tenant_name + " ""Login >> Opening Leads Page  >> Unexpected Error")
    except:
        log_failure(tenant_name + " ""Login >> Leads Page Opening >> Fail")
