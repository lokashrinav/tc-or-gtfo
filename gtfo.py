from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://www.teamblind.com")

time.sleep(2)

sign_in = driver.find_elements(By.CSS_SELECTOR, '.ml-auto.flex.duration-400.mr-4.flex.transition-all:nth-child(1)')[0]

sign_in.click()

time.sleep(5)

username = driver.find_elements(By.CSS_SELECTOR, '#email')[0]

username.send_keys("EMAIL-REPLACE")

password = driver.find_elements(By.CSS_SELECTOR, '#password')[0]

password.send_keys("PASSWORD-REPLACE")

sign_in2 = driver.find_elements(By.CSS_SELECTOR, '.inline-flex.items-center.justify-center.rounded-lg.text-sm.font-semibold.transition-colors.text-white.h-10.px-4.bg-black.hover\\:bg-gray-999.active\\:bg-black.w-full.disabled\\:bg-gray-200.disabled\\:text-gray-999')[0]

sign_in2.click()

time.sleep(5)

feed = driver.find_elements(By.CSS_SELECTOR, '.border.border-gray-300.bg-background-surface.p-4.lg\\:rounded-xl.lg\\:border-b-gray-300.relative.z-0.flex.max-h-\\[840px\\].cursor-pointer.flex-col.justify-between.gap-4.text-gray-900.hover\\:shadow-\\[0_4px_8px_0_rgba\\(101\\,105\\,108\\,0\\.10\\)\\]')

list1 = []

for i in range(20):
    curr_post = feed[i]
    link = curr_post.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
    list1.append(link)

for link in list1:
    print(link)
    driver.execute_script("window.location.href = arguments[0];", link)    
    time.sleep(3)
    
    text = driver.find_element(By.CSS_SELECTOR, '.break-words').text
    if 'tc' not in text.lower():
        text = driver.find_element(By.CSS_SELECTOR, 'textarea')
        text.send_keys("TC or GTFO")
        
        buttons = driver.find_elements(By.CSS_SELECTOR, '.inline-flex.items-center.justify-center.text-sm.font-semibold.transition-colors.bg-black')
        
        time.sleep(5)
        
        for elem in buttons:
            if elem.text and elem.text == "Post":                                
                elem.click()

                
    driver.back()
        




