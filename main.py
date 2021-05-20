from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():

    # initializing driver
    chrome_options = Options()
    driver = webdriver.Chrome("./chromedriver", options=chrome_options)

    # navigating to racing page
    driver.get("https://play.typeracer.com/")
    assert "TypeRacer" in driver.title
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//a[normalize-space()='Enter a Typing Race']").click()

    # wait till race can start
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='popupContent']//span["
                                                                              "@class='time']")))
    countdown = None
    while countdown != ":00":
        countdown = driver.find_element_by_xpath("//div[@class='popupContent']//span[@class='time']").text

    sleep(10000)
    driver.close()

if __name__ == "__main__":
    main()

    # //span
    #
    # setTimeout(function(){ debugger; }, 1000);
    # you have to freeze the page with this code
    # than find out the xpath of timer by contains(text)