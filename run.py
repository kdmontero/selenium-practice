from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from private import EMAIL, PASSWORD


WEBSITE = 'http://automationpractice.com/index.php'
CHROMEDRIVER_LOC = '/home/kevin/Downloads/chromedriver'

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
}
options.add_experimental_option('prefs', prefs)
# options.headless = True

service = Service(executable_path=CHROMEDRIVER_LOC)
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(10)
driver.get(WEBSITE)

# check if logged in
'''
try:
    check = driver.find_element(by='class name', value='account')
    print(check.text)
except:
    print('no check')
'''

login = driver.find_element(by='class name', value='header_user_info')
login.click()

email_field = driver.find_element(by='id', value='email')
password_field = driver.find_element(by='id', value='passwd')

email_field.send_keys(EMAIL)
password_field.send_keys(PASSWORD)

driver.find_element(by='id', value='SubmitLogin').click()

account_name = driver.find_element(by='class name', value='account')
print(f'{account_name.text} has successfully logged in')

sleep(5)
driver.quit()