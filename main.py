import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup




def one_get():
	chrome_options = Options()
	#chrome_options.add_argument("--headless")
	actions = ActionChains(webdriver)
	driver = webdriver.Chrome(options=chrome_options)
	driver.get('https://ggsel.net/wheel')
	try:
		element = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.XPATH, "//a[@class='CircleSubscribeContent_button__VZOQd']"))
		)
	finally:

		driver.find_element("xpath",f"//a[@class='CircleSubscribeContent_button__VZOQd']").click()
		time.sleep(0.5)
		#print(driver.window_handles)
		driver.switch_to.window(driver.window_handles[0])
		time.sleep(1)
		#driver.close()



		driver.find_element("xpath",f"//a[@class='CirclePlayContent_button__1IMkY']").click()
		try:
			element = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located((By.XPATH, "//div[@class='BonusWheelModal_title__yrGo1']"))
			)
		finally:
			page = driver.page_source
			soup = BeautifulSoup(page, "lxml")
			n = soup.find_all('div', attrs={'class':'BonusWheelModal_tableThMobWrap__k6G6Q'})
			try:
				text = f"{n[1].find('a').text} {n[1].find('div').text}"
			except:
				text = 'Буква'
			
			with open('results.txt', 'a+') as file:
				file.write(f'{text}\n')

		driver.quit()


while True:
	
	one_get()