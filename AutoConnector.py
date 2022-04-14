import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def doEverything():

    options = Options()
    options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
    driver_path = '/usr/local/bin/chromedriver'
    driver = webdriver.Chrome(options=options, executable_path=driver_path)
    driver.get('https://172.22.2.6/connect/PortalMain')
    time.sleep(2)

    try:
        driver.find_element_by_id('UserCheck_Logoff_Button_span')
        driver.find_element_by_id('UserCheck_Logoff_Button_span').click()
        driver.find_element_by_xpath(
            '//*[text()="Regain access to the network"]').click()
        time.sleep(1)
    except:
        pass
    finally:
        driver.find_element_by_id('details-button').click()
        time.sleep(.5)
        driver.find_element_by_id('proceed-link').click()
        time.sleep(1)
        driver.find_element_by_id(
            'LoginUserPassword_auth_username').send_keys('19ucs094')
        driver.find_element_by_id(
            'LoginUserPassword_auth_password').send_keys('105892')

        driver.find_element_by_id('UserCheck_Login_Button_span').click()
        time.sleep(1)
        driver.close()


doEverything()
