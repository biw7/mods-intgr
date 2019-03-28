from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import logs

def main():
	#DADOS DE USUARIO PARA ACESSAR A CONTA
	usr = logs.usr
	pwd = logs.pwd
	mess = 'Acesse ---->>>>> dwz.ddns.net'


	#deleta cache
	profile = webdriver.FirefoxProfile()
	profile.set_preference("browser.cache.disk.enable", False)
	profile.set_preference("browser.cache.memory.enable", False)
	profile.set_preference("browser.cache.offline.enable", False)
	profile.set_preference("network.http.use-cache", False)

	# path p/ o geckoddriver exe
	driver = webdriver.Firefox(executable_path=r'')
	driver.implicitly_wait(15)

	#Login facebook
	driver.get("http://www.facebook.com")
	elem = driver.find_element_by_id("email")
	elem.send_keys(usr)
	elem = driver.find_element_by_id("pass")
	elem.send_keys(pwd)
	c = driver.find_element_by_id('loginbutton')
	c.click()
	driver.get("downloadzz.co.nf/galeria")
	text_box = driver.find_element_by_class_name('a2a_button_facebook')
	text_box.click()
	text_box.clear()
	text_box.send_keys(mess)
	post_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/table/tbody/tr/td/div/form/input[20]')
	post_button.click()


if __name__ == '__main__':
	main()
