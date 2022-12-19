import time
from telnetlib import EC

# import webbrowser
from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://prenotami.esteri.it/")

nombre = 'lalala'
passin = 'lalala'

ingresaremail = driver.find_element(By.XPATH, '//*[@id="login-email"]')
ingresaremail.send_keys(nombre)

ingresarpass = driver.find_element(By.XPATH, '//*[@id="login-password"]')
ingresarpass.send_keys(passin)

driver.find_element(By.XPATH, '//*[@id="login-form"]/button').click()

time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="advanced"]/span').click()

time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="dataTableServices"]/tbody/tr[4]/td[4]/a/button').click()

for n in range(0,100):
    driver.find_element(By.XPATH, '//*[@id="dataTableServices"]/tbody/tr[4]/td[4]/a/button').click()

    wait = WebDriverWait(driver, timeout=10, poll_frequency=1,
                         ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
    element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn btn-blue')))

    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/button').click()



#    driver.switch_to.new_window(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div/div')
#    driver.switch_to.frame(By.CLASS_NAME, 'jconfirm-box jconfirm-hilight-glow jconfirm-type-blue jconfirm-type-animated')
#    boton3 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/button')
#    boton3.click()


 #   driver.switch_to.active_element.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/button').click()




time.sleep(20)