from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from Functions import *


def quicklinks(driver, opname="", qlname="", Page_name="", action=""):
    elem = driver.find_element_by_xpath("//span[contains(text(),'Leads')]")
    elem.click()
    if opname == "Create Quick Link":
        try:
            elem = driver.find_element_by_xpath(
                "(//div[@class='dropdown']/button[@class='btn btn-link btn btn-outline-transparent btn-sm']/*[name()='svg'])[1]")
            hover = ActionChains(driver).move_to_element(elem)
            hover.perform()
            log_success(
                tenant_name + " ""Login >> " + Page_name + " Page >>  QuickLinks Ellipse Selection >> Pass")
            try:
                elem = driver.find_element_by_xpath(
                    "(//div[@class='dropdown-menu show'][@aria-hidden='false']/button[text()='" + opname + "'])")
                elem.click()
                try:
                    if action == 'Done':
                        try:
                            elem = driver.find_element_by_xpath("//input[@placeholder='Name Your Search']")
                            elem.click()
                            elem.send_keys(qlname)
                            log_success(
                                tenant_name + " ""Login >> " + Page_name + " Page >>  QuickLinks >> Quicklink Name '" + qlname + "' Entered >> Pass")
                            try:
                                elem = driver.find_element_by_xpath("//button[text()='" + action + "']")
                                elem.click()
                                time.sleep(2)
                                try:
                                    elem = driver.find_element_by_xpath(
                                        "//div[@class='quick__link-chip']/div[text()='" + qlname + "']")
                                    if elem:
                                        log_success(
                                            tenant_name + " ""Login >> " + Page_name + " Page >>  QuickLink Creation >> Pass")
                                except:
                                    log_failure(
                                        tenant_name + " ""Login >> " + Page_name + " Page >>  QuickLinks Creation >> Fail")
                            except:
                                log_failure(
                                    tenant_name + " ""Login >> " + Page_name + " Page >>  QuickLinks Action Selection >> Fail")
                        except:
                            log_failure(
                                tenant_name + " ""Login >> " + Page_name + " Page >>  QuickLinks >> Quicklink Name '" + qlname + "' Entered >> Fail")

                    if action == 'Cancel':
                        try:
                            elem = driver.find_element_by_xpath("//input[@placeholder='Name Your Search']")
                            elem.click()
                            elem.send_keys(qlname)
                            log_success(
                                tenant_name + " ""Login >> " + Page_name + " Page >>  QuickLinks >> Quicklink Name '" + qlname + "' Entered >> Pass")
                            try:
                                elem = driver.find_element_by_xpath("//button[text()='" + action + "']")
                                elem.click()
                                try:
                                    elem = driver.find_element_by_xpath(
                                        "//div[@class='quick__link-chip']/div[text()='" + qlname + "']")
                                    if elem:
                                        log_failure(
                                            tenant_name + " ""Login >> " + Page_name + " Page >>  QuickLink Creation >>  QuickLink not Created with Action >> " + action + "  >> Fail")
                                except:
                                    log_success(
                                        tenant_name + " ""Login >> " + Page_name + " Page >>  QuickLink Creation >>  QuickLink not Created with Action >> " + action + "  >> Pass")
                            except:
                                log_failure(
                                    tenant_name + " ""Login >> " + Page_name + " Page >>  QuickLinks Action Selection >> Fail")
                        except:
                            log_failure(
                                tenant_name + " ""Login >> " + Page_name + " Page >>  QuickLinks >> Quicklink Name '" + qlname + "' Entered >> Fail")

                    if action not in ('Done', 'Cancel'):
                        log_failure(
                            tenant_name + " ""Login >> " + Page_name + " Page >>  QuickLinks Action '" + action + "' >> invalid Action")

                except:
                    log_failure(
                        tenant_name + " ""Login >> " + Page_name + " Page >>  QuickLinks Action >> " + action + "  >> Unexpected Error")

            except:
                log_failure(
                    tenant_name + " ""Login >> " + Page_name + " Page >>  QuickLinks >> " + qlname + " Selection >> Fail")
        except:
            log_failure(
                tenant_name + " ""Login >> " + Page_name + " Page >>  QuickLinks Ellipse Selection >> Fail")

    if opname == "Manage Quick Link":
        try:
            elem = driver.find_element_by_xpath(
                "(//div[@class='dropdown']/button[@class='btn btn-link btn btn-outline-transparent btn-sm']/*[name()='svg'])[1]")
            hover = ActionChains(driver).move_to_element(elem)
            hover.perform()
            log_success(
                tenant_name + " ""Login >> " + Page_name + " Page >>  QuickLinks Ellipse Selection >> Pass")
            try:
                elem = driver.find_element_by_xpath(
                    "(//div[@class='dropdown-menu show'][@aria-hidden='false']/button[text()='" + opname + "'])")
                elem.click()
                try:
                    if action == 'Delete':
                        elem = driver.find_element_by_xpath("//div[@id='quickLink']/div/p")
                        if elem:
                            for i in range(1, 5):
                                elem = driver.find_element_by_xpath("(//div[@id='quickLink']/div/p)[" + str(i) + "]")
                                if elem.text == qlname:
                                    try:
                                        elem = driver.find_element_by_xpath(
                                            "(//div[@id='quickLink']/div/*[name()='svg'])[" + str(i) + "]")
                                        elem.click()
                                        log_success(
                                            tenant_name + " ""Login >> " + Page_name + " Page >>  QuickLink  >>'" + qlname + "'>> Deletion with Action >> " + action + "  >> Pass")
                                        elem = driver.find_element_by_xpath("//button[text()='" + action + "']")
                                        elem.click()
                                        try:
                                            elem = driver.find_element_by_xpath(
                                                "//div[@class='quick__link-chip']/div[text()='" + qlname + "']")
                                            if elem:
                                                log_failure(
                                                    tenant_name + " ""Login >> " + Page_name + " Page >>  QuickLink Deletion >> Fail")
                                        except:
                                            log_success(
                                                tenant_name + " ""Login >> " + Page_name + " Page >>  QuickLinks Deletion >> Pass")
                                            break
                                    except:
                                        log_failure(
                                            tenant_name + " ""Login >> " + Page_name + " Page >>  QuickLink  >>'" + qlname + "'>> Deletion with Action >> " + action + "  >> Fail")

                    if action == 'Done':
                        try:
                            elem = driver.find_element_by_xpath("//button[text()='" + action + "']")
                            elem.click()
                            try:
                                elem = driver.find_element_by_xpath(
                                    "//div[@class='quick__link-chip']/div[text()='" + qlname + "']")
                                if elem:
                                    log_success(
                                        tenant_name + " ""Login >> " + Page_name + " Page >>  QuickLink Creation >>  QuickLink not Deleted with Action >> " + action + "  >> Pass")
                            except:
                                log_success(
                                    tenant_name + " ""Login >> " + Page_name + " Page >>  QuickLink Creation >>  QuickLink not Deleted/Available with Action >> " + action + "  >> Pass")
                        except:
                            log_failure(
                                tenant_name + " ""Login >> " + Page_name + " Page >>  QuickLinks Action Selection >> Fail")

                    if action == 'Cancel':
                        try:
                            elem = driver.find_element_by_xpath("//button[text()='" + action + "']")
                            elem.click()
                            try:
                                elem = driver.find_element_by_xpath(
                                    "//div[@class='quick__link-chip']/div[text()='" + qlname + "']")
                                if elem:
                                    log_success(
                                        tenant_name + " ""Login >> " + Page_name + " Page >>  QuickLink Creation >>  QuickLink not Deleted with Action >> " + action + "  >> Pass")
                            except:
                                log_success(
                                    tenant_name + " ""Login >> " + Page_name + " Page >>  QuickLink Creation >>  QuickLink not Deleted/Available with Action >> " + action + "  >> Pass")
                        except:
                            log_failure(
                                tenant_name + " ""Login >> " + Page_name + " Page >>  QuickLinks Action Selection >> Fail")

                    if action not in ('Done', 'Cancel'):
                        log_failure(
                            tenant_name + " ""Login >> " + Page_name + " Page >>  QuickLinks Action '" + action + "' >> invalid Action")

                except:
                    log_failure(
                        tenant_name + " ""Login >> " + Page_name + " Page >>  QuickLinks Action >> " + action + "  >> Unexpected Error")

            except:
                log_failure(
                    tenant_name + " ""Login >> " + Page_name + " Page >>  QuickLinks >> " + qlname + " Selection >> Fail")
        except:
            log_failure(
                tenant_name + " ""Login >> " + Page_name + " Page >>  QuickLinks Ellipse Selection >> Fail")
