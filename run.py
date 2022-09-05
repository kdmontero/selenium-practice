from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


WEBSITE = 'http://automationpractice.com/index.php'
CHROMEDRIVER_LOC = '/home/kevin/Downloads/chromedriver'

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)

service = Service(executable_path=CHROMEDRIVER_LOC)
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(10)
driver.get(WEBSITE)


driver.quit()
