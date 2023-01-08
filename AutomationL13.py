from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log,sin

def sum(x):
    return log(abs(12*sin(int(x))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()
    browser.implicitly_wait(5)
    button = browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_value = browser.find_element(By.ID, "input_value").text
    answer = sum(x_value)
    field = browser.find_element(By.ID, "answer").send_keys(answer)
    submit = browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    
finally:
    browser.quit()    