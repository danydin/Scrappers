from selenium import webdriver
import time


class Scrapper:
    def itty_to_tiny(self):
        foo = str(input('Enter your text: '))
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://itty.bitty.site')
        element = driver.find_element_by_xpath("//div[@id='content']")
        element.click()
        element.send_keys(foo)
        time.sleep(3)
        itty_url = driver.current_url
        print("itty url: " + itty_url)
        driver.get('https://tinyurl.com/')
        element2 = driver.find_element_by_xpath("//*[@id='url']")
        element2.send_keys(itty_url)
        btn = driver.find_element_by_xpath("//*[@id='submit']")
        btn.click()
        time.sleep(3)
        copy = driver.find_element_by_xpath("//small[contains(text(),'[Copy to clipboard]')]")
        copy.click()  # copied to clipboard
        tiny_url = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/b[1]")
        print('Tiny url: ' + tiny_url.text)
        print("SHORTENED URL COPIED TO CLIPBOARD!\n\nProgram will exit in 10 seconds.")
        time.sleep(10)

Scrapper().itty_to_tiny()