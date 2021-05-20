from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    # how quick should input be
    while True:
        typespeed = float(input("enter distance between entering keys: to beat everyone 0.04 is fully sufficient" + "\n"))
        if typespeed < 0.03:
            print("too small")
        else:
            break

    # initializing driver
    chrome_options = Options()
    driver = webdriver.Chrome("./chromedriver", options=chrome_options)

    # navigating to racing page
    driver.get("https://play.typeracer.com/")
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//a[normalize-space()='Enter a Typing Race']").click()

    # wait till race can start
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='popupContent']//span["
                                                                              "@class='time']")))

    # store the whole exercise text
    text = ""
    given_text = driver.find_elements_by_xpath("//span[@unselectable='on']")
    for index, element in enumerate(given_text):
        text = text + element.text
        if index == len(given_text) - 2:
            text = text + " "

    countdown = None
    while countdown != ":00":
        countdown = driver.find_element_by_xpath("//div[@class='popupContent']//span[@class='time']").text

    # input text
    input_field = driver.find_element_by_xpath("//input[@class = 'txtInput']")
    for character in text:
        input_field.send_keys(character)
        sleep(typespeed)

    sleep(10000)
    driver.close()

if __name__ == "__main__":
    main()
