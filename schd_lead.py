
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.keys import Keys

from Functions import log_failure
from Functions import log_success
from Functions import tenant_name
import time


# from selenium.common.exceptions import NoSuchElementException


def schd_lead(driver, disposition="", city_area="", schddate="", schdtime="", team="", address="", comments=""):
    elem = driver.find_element_by_xpath("//li[@class='breadcrumb-item active']")
    ref_id = elem.text
    validations = 0
    try:
        elem = driver.find_element_by_xpath("//h5[contains(text(),'Lead Info')]")
        if "Lead Info" in elem.text:
            log_success(
                tenant_name + " " + "Login >> Leads Page >> Lead id >>"" " + str(
                    ref_id) + " "">> Scheduling Lead Page opened >> Pass")
            if disposition !='':
                try:
                    # Selecting disposition
                    elem = driver.find_element_by_xpath(
                        "(//span[@class='form-control text-truncate dropdown-toggle'])[contains(text(),'Select Disposition')]")
                    elem.click()
                    try:
                        elem = driver.find_element_by_xpath(
                            "//button[@class='dropdown-item'][contains(text(),'" + disposition + "')]")
                        elem.click()
                        log_success(
                            tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >> Selecting Disposition >> Pass")
                        time.sleep(3)
                    except:
                        log_failure(
                            tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >> Selecting Disposition >> Fail")
                except:
                    log_failure(
                        tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >> Selecting Disposition Dropdown >> Failure")
                if disposition =='Schedule':
                    if city_area != "":
                        try:
                            # Selecting city
                            elem = driver.find_element_by_xpath("//input[@placeholder='Select City Area']")
                            elem.click()
                            time.sleep(2)
                            try:
                                elem = driver.find_element_by_xpath(
                                    "//a[@class='dropdown-item']/span[contains(text(),'" + city_area + "')]")
                                elem.click()
                                log_success(
                                    tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >> Selecting City Area >> Pass")
                            except:
                                log_failure(
                                    tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >> Selecting City Area >> Fail")
                                elem = driver.find_element_by_xpath("//h5[contains(text(),'Lead Info')]")
                                elem.click()
                                pass
                        except:
                            log_failure(
                                tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >> Selecting City Area Dropdown >> Failure")
                            elem = driver.find_element_by_xpath("//h5[contains(text(),'Lead Info')]")
                            elem.click()
                    else:
                        log_success(tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >> City input is Empty")

                    if schddate != "" and schdtime !="":
                        try:
                            # Selecting date
                            elem = driver.find_element_by_id("exampleFormControlSelect3")
                            elem.click()
                            time.sleep(2)
                            try:
                                # date = created_date
                                elem = driver.find_element_by_xpath \
                                    ("//div[@aria-label][text() = '" + schddate + "'][@aria-disabled='true']")
                                if elem:
                                    log_failure(
                                        tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >> >> Date Selection  >> Given Date not available for Selection")
                            except:
                                try:
                                    elem = driver.find_element_by_xpath(
                                        "//div[@aria-label][text() = '" + schddate + "'][@aria-disabled='false']")
                                    if elem:
                                        elem.click()
                                        log_success(
                                            tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >> Date Selection >> Pass")
                                except:
                                    log_failure(
                                        tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >> Date Selection >> Unexpected Error")
                            try:
                                # date = created_date
                                #//li[@class='react-datepicker__time-list-item '][contains(text(),'4:45 PM')]
                                elem = driver.find_element_by_xpath("//li[@class='react-datepicker__time-list-item '][(text()='"+ schdtime +"')]")
                                elem.click()
                                log_success(
                                    tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >> Time Selection >> Pass")
                            except:
                                elem = driver.find_element_by_xpath(
                                    "//li[@class='react-datepicker__time-list-item  react-datepicker__time-list-item--disabled'][(text()='"+schdtime+"')]")
                                if elem:
                                    log_failure(
                                        tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >> Given Time Slot not available")
                                pass
                        except:
                            log_failure(
                                tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >> Selecting Date and Time >> Failure")
                    elif not schddate and schdtime != "":
                        try:
                            # date = created_date
                            elem = driver.find_element_by_xpath(
                                "//li[@class='react-datepicker__time-list-item '][contains(text(),'"+schdtime+"')]")
                            elem.click()
                            log_success(
                                tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >> Time Selection >> Pass")
                        except:
                            elem = driver.find_element_by_xpath(
                                "//li[@class='react-datepicker__time-list-item  react-datepicker__time-list-item--disabled'][contains(text(),'"+schdtime+"')]")
                            if elem:
                                log_failure(
                                    tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >> Given Time Slot not available")
                            pass
                    if team != "":
                        try:
                            # Selecting city
                            elem = driver.find_element_by_xpath("//input[@placeholder='Assign To']")
                            elem.click()
                            time.sleep(2)
                            try:
                                elem = driver.find_element_by_xpath(
                                    "//a[@class='dropdown-item']/span[contains(text(),'"+team+"')]")
                                elem.click()
                                log_success(
                                    tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >> Selecting Team >> Pass")
                            except:
                                log_failure(
                                    tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >> Selecting Team >> Fail")
                                try:
                                    elem = driver.find_element_by_xpath(
                                        "(//p[@class='invalid-error'])[1]")
                                    print("Case >> Team given not available in list")
                                    if "Please select team" in elem.text:
                                        log_success(
                                            tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >> Team Validation  >> Given Team value not available >> Pass")
                                        validations += 1
                                    else:
                                        log_failure(
                                            tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >> Team Validation >> Given Team value not available >> Fail")
                                except:
                                    pass
                        except:
                            log_failure(
                                tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >> Selecting Team Dropdown >> Failure")

                    else:
                        log_failure(tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >> Team input is Empty")
                        pass

                    if address != "":
                        try:
                            # Selecting city
                            elem = driver.find_element_by_xpath("//textarea[@placeholder='Enter Address']")
                            elem.click()
                            time.sleep(2)
                            try:
                                elem.send_keys(address)
                                log_success(
                                    tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >>"" " + str(
                                        ref_id) + " "" >> Address Input >> Pass")
                            except:
                                log_failure(
                                    tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >>"" " + str(
                                        ref_id) + " "" >> Address Input >> Fail")
                        except:
                            log_failure(
                                tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >>"" " + str(
                                    ref_id) + " "" >> Selecting Address Field >> Failure")

                    else:
                        log_success(tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >> Address input is Empty ")
                        pass

                    if comments != "":
                        try:
                            # entering comments
                            elem = driver.find_element_by_xpath("//textarea[@placeholder='Enter Comments']")
                            elem.click()
                            time.sleep(2)
                            try:
                                elem.send_keys(comments)
                                log_success(
                                    tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >> Comments Input >> Pass")
                            except:
                                log_failure(
                                    tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >> Comments Input >> Fail")
                        except:
                            log_failure(
                                tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >> Selecting Comments Field >> Failure")
                    else:
                        log_success(tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >> Comments input is Empty ")
                        pass
                    if validations == 0:
                        # Clicking on Create button
                        elem = driver.find_element_by_xpath(
                            "(//button[@class='btn btn-primary theme__primary-btn pull-left'])")
                        elem.click()
                        log_success(
                            tenant_name + " ""Login >> Leads Page >>  Scheduling Lead >> Schedule Button Clicked >> Pass")
                        try:
                            time.sleep(2)
                            elem = driver.find_element_by_xpath("(//div[@class='alert alert-success fade show'])")
                            if "Start_time: should be greater than current time" in elem.text:
                                log_success(
                                    tenant_name + " ""Login >> Leads Page >>  Scheduling Lead >> Start Time should be greater validation >> Pass")
                                validations += 1
                                log_success(
                                    tenant_name + " ""Login >> Leads Page >> Scheduling Lead >>  Number of validations triggered >>"" " + str(
                                        validations))

                            # Team: Ahmads Team is not available at this moment
                            if "is not available at this moment" in elem.text:
                                log_success(
                                    tenant_name + " ""Login >> Leads Page >>  Scheduling Lead >>"+team+" not available currently validation >> Pass")
                                validations += 1
                                log_success(
                                    tenant_name + " ""Login >> Leads Page >> Scheduling Lead >>  Number of validations triggered >>"" " + str(
                                        validations))
                        except:
                            for i in range(1, 4):
                                try:
                                    elem = driver.find_element_by_xpath("(//p[@class='invalid-error'])[" + str(i) + "]")
                                    if "Please select team" in elem.text:
                                        print("Case >> Team not given")
                                        log_success(
                                            tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >> Empty Team Validation  >> Pass")
                                        validations += 1
                                    if "Please enter address" in elem.text:
                                        print("Case >> Address not given")
                                        log_success(
                                            tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >> Empty Address Validation  >> Pass")
                                        validations += 1
                                    if "Please select city area" in elem.text:
                                        print("Case >> City given not available in list")
                                        log_success(
                                            tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >> Empty City Validation >> Pass")
                                        validations += 1
                                except:
                                    time.sleep(5)
                                    try:
                                        elem = driver.find_element_by_xpath("//h3[contains(text(),'Leads')]")
                                        if "LEADS" in elem.text:
                                            try:
                                                for i in range(0, 14):
                                                    elem = driver.find_element_by_xpath(
                                                        "//div[@id='row-"+str(i)+"']/div[@id='cell-ref-undefined']")
                                                    if elem.text == str(ref_id):
                                                        elem = driver.find_element_by_xpath(
                                                            "//div[@id='row-"+str(i)+"']/div[@id='cell-status-undefined']")
                                                        if elem.text == 'Scheduled':
                                                            log_success(
                                                                tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >>"" " + str(
                                                                    ref_id) + " "" >> Lead Scheduled >> Pass")
                                                            break
                                            except:
                                                log_success(
                                                    tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >>"" " + str(
                                                        ref_id) + " "" >> Lead Scheduled >> Fail")
                                    except:
                                        log_success(
                                            tenant_name + " ""Login >> Adding Lead  >> Scheduling Lead >> "" " + str(
                                                validations) + " >> Unexpected Error occuured ")
                                    break

                    if validations > 0:
                        # Re Rerouting to Leads Page
                        elem = driver.find_element_by_xpath("//span[contains(text(),'Leads')]")
                        elem.click()
                        time.sleep(2)
                        try:
                            elem = driver.find_element_by_xpath("//h3[contains(text(),'Leads')]")
                            if "LEADS" in elem.text:
                                log_success(tenant_name + " ""Login >> Adding Lead  >> Scheduling Lead >> Validations "
                                                          "Triggered >> "" " + str(
                                    validations) + " >> Re Rerouting to Leads "
                                                   "Page >> Pass ")
                        except:
                            log_success(tenant_name + " ""Login >> Adding Lead  >> Scheduling Lead >> Validations "
                                                      "Triggered >> "" " + str(
                                validations) + " >> Re Rerouting to Leads Page >> Fail ")
                if disposition in ('No Answer','Not Interested','Service Inquiry','Number Switched Off','Scheduling Issue'):
                    if comments != "":
                        try:
                            # entering comments
                            elem = driver.find_element_by_xpath("//textarea[@placeholder='Enter Comments']")
                            elem.click()
                            time.sleep(2)
                            try:
                                elem.send_keys(comments)
                                log_success(
                                    tenant_name + " ""Login >> Leads Page >> Scheduling Lead >>  Marking Lead as Lost  >> Comments Input >> Pass")
                            except:
                                log_failure(
                                    tenant_name + " ""Login >> Leads Page >> Scheduling Lead >>  Marking Lead as Lost  >> Comments Input >> Fail")
                            try:
                                elem = driver.find_element_by_xpath(
                                    "(//button[@class='btn btn-primary theme__primary-btn pull-left'])")
                                elem.click()
                                log_success(
                                    tenant_name + " ""Login >> Leads Page >>  Scheduling Lead >> Marking Lead as Lost  >> Confirm Button Clicked >> Pass")
                                try:
                                    for i in range(0, 14):
                                        elem = driver.find_element_by_xpath(
                                            "//div[@id='row-" + str(i) + "']/div[@id='cell-ref-undefined']")
                                        if elem.text == str(ref_id):
                                            elem = driver.find_element_by_xpath(
                                                "//div[@id='row-" + str(i) + "']/div[@id='cell-status-undefined']")
                                            if elem.text == 'Lost':
                                                log_success(
                                                    tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >>"" " + str(
                                                        ref_id) + " "" >> Lead Lost >> Pass")
                                                break
                                except:
                                    log_success(
                                        tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >>"" " + str(
                                            ref_id) + " "" >> Lead Lost >> Fail")

                            except:
                                log_failure(
                                    tenant_name + " ""Login >> Leads Page >>  Scheduling Lead >> Marking Lead as Lost  >> Confirm Button Clicked >> Failure")
                        except:
                            log_failure(
                                tenant_name + " ""Login >> Leads Page >>  Scheduling Lead >>  Marking Lead as Lost  >> Selecting Comments Field >> Failure")
                    else:
                        log_success(tenant_name + " ""Login >> Leads Page >>  Scheduling Lead >>  Marking Lead as Lost >> Comments input is Empty ")
                        try:
                            elem = driver.find_element_by_xpath(
                                "(//button[@class='btn btn-primary theme__primary-btn pull-left'])")
                            elem.click()
                            log_success(
                                tenant_name + " ""Login >> Leads Page >>  Scheduling Lead >> Marking Lead as Lost  >> Confirm Button Clicked >> Pass")
                            try:
                                for i in range(0, 14):
                                    elem = driver.find_element_by_xpath(
                                        "//div[@id='row-" + str(i) + "']/div[@id='cell-ref-undefined']")
                                    if elem.text == str(ref_id):
                                        elem = driver.find_element_by_xpath(
                                            "//div[@id='row-" + str(i) + "']/div[@id='cell-status-undefined']")
                                        if elem.text == 'Lost':
                                            log_success(
                                                tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >>"" " + str(
                                                    ref_id) + " "" >> Lead Lost >> Pass")
                                            break
                            except:
                                log_success(
                                    tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >>"" " + str(
                                        ref_id) + " "" >> Lead Lost >> Fail")

                        except:
                            log_failure(
                                tenant_name + " ""Login >> Leads Page >>  Scheduling Lead >> Marking Lead as Lost  >> Confirm Button Clicked >> Failure")

                if disposition =='Follow Up':
                    if schddate != "" and schdtime !="":
                        try:
                            # Selecting date
                            elem = driver.find_element_by_id("exampleFormControlSelect3")
                            elem.click()
                            time.sleep(2)
                            try:
                                # date = created_date
                                elem = driver.find_element_by_xpath \
                                    ("//div[@aria-label][text() = '" + schddate + "'][@aria-disabled='true']")
                                if elem:
                                    log_failure(
                                        tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >> Adding FollowUp >> Date Selection  >> Given Date not available for Selection")
                            except:
                                try:
                                    elem = driver.find_element_by_xpath(
                                        "//div[@aria-label][text() = '" + schddate + "'][@aria-disabled='false']")
                                    if elem:
                                        elem.click()
                                        log_success(
                                            tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >>  Adding FollowUp >> Date Selection >> Pass")
                                except:
                                    log_failure(
                                        tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >>  Adding FollowUp >> Date Selection >> Unexpected Error")
                            try:
                                # date = created_date
                                #//li[@class='react-datepicker__time-list-item '][contains(text(),'4:45 PM')]
                                elem = driver.find_element_by_xpath("//li[@class='react-datepicker__time-list-item '][contains(text(),'"+ schdtime +"')]")
                                elem.click()
                                log_success(
                                    tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >>  Adding FollowUp >> Time Selection >> Pass")
                            except:
                                elem = driver.find_element_by_xpath(
                                    "//li[@class='react-datepicker__time-list-item  react-datepicker__time-list-item--disabled'][contains(text(),'"+schdtime+"')]")
                                if elem:
                                    log_failure(
                                        tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >>  Adding FollowUp >> Given Time Slot not available")
                                pass

                            #Confirm button followup
                            try:
                                elem = driver.find_element_by_xpath(
                                    "(//button[@class='btn btn-primary theme__primary-btn pull-left'])")
                                elem.click()
                                log_success(
                                    tenant_name + " ""Login >> Leads Page >>  Scheduling Lead >> Adding FollowUp >> Confirm Button Clicked >> Pass")
                            except:
                                log_failure(
                                    tenant_name + " ""Login >> Leads Page >>  Scheduling Lead >> Adding FollowUp  >> Confirm Button Clicked >> Failure")


                        except:
                            log_failure(
                                tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >>  Adding FollowUp >> Selecting Date and Time >> Failure")
                    if not schddate and schdtime != "":
                        try:
                            # date = created_date
                            elem = driver.find_element_by_xpath(
                                "//li[@class='react-datepicker__time-list-item '][contains(text(),'"+schdtime+"')]")
                            elem.click()
                            log_success(
                                tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >>  Adding FollowUp >> Time Selection >> Pass")
                        except:
                            elem = driver.find_element_by_xpath(
                                "//li[@class='react-datepicker__time-list-item  react-datepicker__time-list-item--disabled'][contains(text(),'"+schdtime+"')]")
                            if elem:
                                log_failure(
                                    tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >>  Adding FollowUp >> Given Time Slot not available")
                            pass
                        if comments != "":
                            try:
                                # entering comments
                                elem = driver.find_element_by_xpath("//textarea[@placeholder='Enter Comments']")
                                elem.click()
                                time.sleep(2)
                                try:
                                    elem.send_keys(comments)
                                    log_success(
                                        tenant_name + " ""Login >> Leads Page >> Scheduling Lead >>  Adding FollowUp  >> Comments Input >> Pass")
                                except:
                                    log_failure(
                                        tenant_name + " ""Login >> Leads Page >> Scheduling Lead >>  Adding FollowUp  >> Comments Input >> Fail")
                            except:
                                log_failure(
                                    tenant_name + " ""Login >> Leads Page >> Scheduling Lead >>  Adding FollowUp  >> Selecting Comments Field >> Failure")
                        else:
                            log_success(tenant_name + " ""Login >> Leads Page >> Scheduling Lead >> Adding Followup >> Comments input is Empty ")
                            pass
                            # Confirm button followup
                        try:
                            elem = driver.find_element_by_xpath(
                                    "(//button[@class='btn btn-primary theme__primary-btn pull-left'])")
                            elem.click()
                            log_success(tenant_name + " ""Login >> Leads Page >>  Scheduling Lead >> Adding FollowUp >> Confirm Button Clicked >> Pass")
                        except:
                            log_failure(tenant_name + " ""Login >> Leads Page >>  Scheduling Lead >> Adding FollowUp  >> Confirm Button Clicked >> Failure")
                    if not schddate and  not schdtime:
                        if comments != "":
                            try:
                                # entering comments
                                elem = driver.find_element_by_xpath("//textarea[@placeholder='Enter Comments']")
                                elem.click()
                                time.sleep(2)
                                try:
                                    elem.send_keys(comments)
                                    log_success(
                                        tenant_name + " ""Login >> Leads Page >> Scheduling Lead >>  Adding FollowUp  >> Comments Input >> Pass")
                                except:
                                    log_failure(
                                        tenant_name + " ""Login >> Leads Page >> Scheduling Lead >>  Adding FollowUp  >> Comments Input >> Fail")
                            except:
                                log_failure(
                                    tenant_name + " ""Login >> Leads Page >> Scheduling Lead >>  Adding FollowUp  >> Selecting Comments Field >> Failure")
                        else:
                            log_success(tenant_name + " ""Login >> Leads Page >> Scheduling Lead >> Adding Followup >> Comments input is Empty ")
                            pass
                            # Confirm button followup
                        try:
                            elem = driver.find_element_by_xpath(
                                    "(//button[@class='btn btn-primary theme__primary-btn pull-left'])")
                            elem.click()
                            log_success(tenant_name + " ""Login >> Leads Page >>  Scheduling Lead >> Adding FollowUp >> Confirm Button Clicked >> Pass")
                            try:
                                for i in range(0, 14):
                                    elem = driver.find_element_by_xpath(
                                        "//div[@id='row-" + str(i) + "']/div[@id='cell-ref-undefined']")
                                    if elem.text == str(ref_id):
                                        elem = driver.find_element_by_xpath(
                                            "//div[@id='row-" + str(i) + "']/div[@id='cell-disposition-undefined']")
                                        if elem.text == 'Follow Up':
                                            log_success(
                                                tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >>"" " + str(
                                                    ref_id) + " "" >> Lead Followup  >> Pass")
                                            break
                            except:
                                log_success(
                                    tenant_name + " ""Login >> Leads Page >>  Scheduling Lead  >>"" " + str(
                                        ref_id) + " "" >> Lead Followup >> Fail")
                        except:
                            log_failure(tenant_name + " ""Login >> Leads Page >>  Scheduling Lead >> Adding FollowUp  >> Confirm Button Clicked >> Failure")

        else:
            log_failure(
                tenant_name + " " + "Login >> Leads Page >> Lead id >>"" " + str(
                    ref_id) + " ""Scheduling Lead  >> Fail >> Disposition Empty")
            # tenant_name + " " + "Login >> Leads Page >>  Adding Lead >> Scheduling Lead >> Disposition Empty cannot Proceed")
    except:
        log_failure(
            tenant_name + " " + "Login >> Leads Page >>  Adding Lead >> Scheduling Lead Page opened >> Unexpected Error")
