from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import logs

def main():
	
	usr = logs.usr
	pwd = logs.pwd
	mess = 'Acesse ---->>>>> dwz.ddns.net'


	
	profile = webdriver.FirefoxProfile()
	profile.set_preference("browser.cache.disk.enable", False)
	profile.set_preference("browser.cache.memory.enable", False)
	profile.set_preference("browser.cache.offline.enable", False)
	profile.set_preference("network.http.use-cache", False)

	
        #adicionar caminho para o driver
	driver = webdriver.Firefox(executable_path= '')
	driver.implicitly_wait(15)

	driver.get("http://www.facebook.com")
	elem = driver.find_element_by_id("email")
	elem.send_keys(usr)
	elem = driver.find_element_by_id("pass")
	elem.send_keys(pwd)
	c = driver.find_element_by_id('loginbutton')
	c.click()

	driver.get("http://downloadzz.co.nf/")
	text_box = driver.find_element_by_xpath('/html/body/header/div[2]/a[1]')
	text_box.click()
	element = driver.find_element_by_name("source")
	target = driver.find_element_by_name("target")

	ActionChains(driver).drag_and_drop(element, target).perform()



if __name__ == '__main__':
	main()
