from selenium.webdriver.support.ui import Select
from Login import *
from Leads import *
from Reports_search import *
from Payments import *
from Deposits import *
from Functions import *
from selenium import webdriver
from Addlead import *
from schd_lead import schd_lead
from Users import users_search_test_case
from Teams import team_search_test_case
from Roles import roles_search_test_case
from QuickLinks import quicklinks
from Tenant_settings import tenant_settings
from Lead_Types import lead_type_search_test_case
from AddLeadType import add_leadtype
from AddUser import add_User
from Edit_user import edit_user

driver = webdriver.Chrome()
driver.set_window_size(1440, 486)
driver.maximize_window()
urlpath = url()
driver.get(urlpath)

#################################################################################################################################

###############checking login form validation and doing login


###login_validations(driver)
###############checking login using empty email password
# login(driver, '', '')
# #
# # ###############checking login using correct email and incorrect password
# login(driver, 'admin@inspectionpro.com', 'super54321')
# # #
# # # ###############checking login using incorrect email and correct password
# login(driver, 'admin', 'super@321')
#
# ###############checking login using correct email password olx
login(driver, 'admin@inspectionpro.com', 'super@321')

edit_user(driver, fname="Ahmad", lname="", Email="", Phone="",action="Update",start=1)

# users_search_test_case(driver, email="ahmad", phone="0303", role="ins")


#add_User(driver, fname="Testing", lname="User", Email="", Phone="03033830490",action="Create")
#add_leadtype(driver, name="Testing Lead", inspcncat="ahmad", desc="dummy", price="dummy",action="Save")

#lead_type_search_test_case(driver, name="a",ref="9")
#
# tenant_settings(driver, tenant_name="",logo=".\\Tenant_images\\OLX\logo.png", favicon=".\\Tenant_images\\OLX\/favicon.ico", phone="", phoneplaceholder="", regex="", noofrecord="", country="",action="Save")
#
#
# #quicklinks
# quicklinks(driver, opname="Create Quick Link", qlname="ahmad", Page_name="Leads",action="Done")
# quicklinks(driver, opname="Create Quick Link", qlname="ahmad1", Page_name="Leads",action="Cancel")
# quicklinks(driver, opname="Manage Quick Link", qlname="ahmad", Page_name="Leads",action="Delete")




# ###############checking login using correct email password dubizzle
#login(driver, 'admin@empgautos.com', 'super@321')

######Parameters(driver, Ref # , Name,  Phone , City, Status , Lead Type, Inspection Type ,Created Date
Lead_search_test_case(driver, '281', 'ahmad', '03033830490', 'Lahore', 'Completed', 'OLX Car Inspection','Olx Car Inspection', '')
#Lead_search_test_case(driver, '', '', '', '', 'Completed', '', '', '')

########Add Lead(driver, Leadtype Name,  Email,  Phone,  City, leadaction):
add_lead(driver, 'OLX Car Inspection (Rs 2,500)', 'ahmadlead', 'ahmad@gmail.com', '03031234567', 'Lahore', 'Create')

#olx
add_lead(driver, 'OLX Car Inspection (Rs 2,500)', 'ahmadlead', 'ahmad@gmail.com', '03031234567', 'Lahore', 'Create')

#dubizzle
add_lead(driver, 'Dubizzle Quality Assist (Rs 200)', 'ahmadlead', 'ahmad@gmail.com', '03031234567', 'Dubai', 'Create')


######Parameters(driver, disposition, city_area, team, address, comments):
#schd_lead(driver,'Schedule','','','','random comments')

#dubizzle
#(driver,'Schedule', 'Business Bay', '11', '5:45 PM', 'Ahmads team', 'address', 'random comment')

#olx
schd_lead(driver,'Schedule', 'Johar Town', '3', '11:45 AM', 'Ahmads Team', 'address', 'random comments')


# 1:00 PM
# schd_lead(driver,'Schedule', 'Johar Town', '9', '1:00 PM', 'Ahmads team', 'address', 'random comments')

#schd_lead(driver, 'Follow Up', '', '', '', 'random comments')

#schd_lead(driver, 'No Answer', '', '', '', 'random comments')



######Parameters(driver, status, Ref # ,Created Date,Completed Date)
#status In Progress,Completed
report_search_test_case(driver, 'Completed', '237', '', '')
#report_search_test_case(driver, 'In Progress', '237', '', '')
#report_search_test_case(driver, 'hello', '237', '', '')


######payments_search_test_case Parameters (driver, status, Ref # ,report # ,Collected_Date,Deposited Date)
#status Pending,, Collected , Deposited, Paid
payments_search_test_case(driver, 'Collected', '','', '', '')



######Parameters(driver, status="", ref="", inspector="", Created_Date=""):
#status Yes, No
#Paramters deposit_search_test_case(driver, status="", ref="", inspector="", Created_Date="",Action="")
#Action ="MarkVerified"
deposit_search_test_case(driver, status='Not Verified', ref='237', inspector="Muhammad", Created_Date="",Action="MarkVerified")
#if Deposit verified then action should be sent empty
deposit_search_test_case(driver, status='Verified', ref='237', inspector="Muhammad", Created_Date="",Action="")

users_search_test_case(driver, email="", phone="", role="ins")

team_search_test_case(driver, name='ahmad')

roles_search_test_case(driver, name="ins")

time.sleep(2)
driver.close()
