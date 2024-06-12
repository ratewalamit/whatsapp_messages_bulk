from selenium import webdriver
driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
driver.get("https://web.whatsapp.com/")
text_area = driver.find_element(by="xpath", value='//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')
text_area.send_keys("9015648144")
chat_name = driver.find_element(by='xpath', value='//*[@id="pane-side"]/div[1]/div/div/div[4]')
chat_name.click()
message =  "Hi.. I am a simple python script.."
driver.find_element(by='xpath', value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(message)
send_button = driver.find_element(by='xpath', value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
send_button.click()
history

