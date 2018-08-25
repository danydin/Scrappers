from openpyxl import Workbook
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
import time


wb = Workbook()
ws = wb.active

class cls():

    def amazon(self, URL, stpoint, endpoint, minProfit, nob):

        def seperatepage(URL):
            driver2 = webdriver.Chrome()
            driver2.maximize_window()
            driver2.get(URL)
            isbncheck = check_exists_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[5]/div[10]/div[1]/div[1]/div[2]/div[1]/div[1]/span[2]")
            if isbncheck is True:
                isbn = driver2.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[5]/div[10]/div[1]/div[1]/div[2]/div[1]/div[1]/span[2]").text
                driver2.close()
                print(isbn)
                return isbn



        def check_exists_by_xpath(xpath2):
            try:
                driver.find_element_by_xpath(xpath2)
            except NoSuchElementException:
                return False
            return True

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(str(URL))
        while endpoint < nob:
            for a in range(stpoint, endpoint, 1):
                xpath: str = "//li[@id='result_" + str(a) + "']//span[@class='a-size-small']"
                check = check_exists_by_xpath(xpath)
                if check is True and "Trade in yours for an Amazon" in driver.find_element_by_xpath(xpath).text:

                    bookname = check_exists_by_xpath("//li[@id='result_"+str(a)+"']//div[contains(@class,'a-row a-spacing-small')]//div[1]")
                    profitcheck = str(driver.find_element_by_xpath("//li[@id='result_" + str(a) + "']//span[@class='a-size-small']").text)
                    profitcheck2 = profitcheck[46:50]
                    unocheck = check_exists_by_xpath("//li[@id='result_" + str(a) + "']//div[@class='a-row a-spacing-top-mini a-spacing-mini']//div[2]//a[1]")
                    if unocheck is True:
                        unocheck2 = str(driver.find_element_by_xpath("//li[@id='result_" + str(a) + "']//div[@class='a-row a-spacing-top-mini a-spacing-mini']//div[2]//a[1]").text)
                        unocheck3 = unocheck2[1:5]
                        profitcheckfloat = float(profitcheck2)
                        unocheckfloat = float(unocheck3)
                        minprofitfloat = float(minProfit)
                        compare = profitcheckfloat - unocheckfloat
                        if bookname is True:
                            if compare > minprofitfloat:
                                booknamedesc = driver.find_element_by_xpath("//li[@id='result_" + str(a) + "']//div[contains(@class,'a-row a-spacing-small')]//div[1]")
                                seperate = driver.find_element_by_xpath("//li[@id='result_" + str(a) + "']//div[contains(@class,'a-fixed-left-grid-col a-col-left')]//a[contains(@class,'a-link-normal a-text-normal')]").get_property('href')
                                print(booknamedesc.text)
                                seperate2 = (str(seperate))
                                isbn : str = seperatepage(str(seperate2))
                                ws.append([booknamedesc.text,minprofit,isbn])



            npcheck = check_exists_by_xpath("//a[@id='pagnNextLink']")
            if npcheck is True:
                nextpage = driver.find_element_by_xpath("//span[@class='srSprite pagnNextArrow']")
                nextpage.is_selected()
                nextpage.click()
                URL = driver.current_url
                driver.close()
                cls.amazon(self,str(URL),endpoint-10,endpoint+12,minprofit,nob)
        wb.save("textbook.xlsx")





keyword = str(input("ENTER SEARCH KEYWORD\n"))
minprofit = str(input("ENTER MINIMUM PROFIT\n"))
numberofbooks = int(input("ENTER NUMBER OF BOOKS TO CHECK\n"))
url = "https://www.amazon.com/s/ref=sr_pg_1?fst=p90x%3A1&rh=n%3A283155%2Ck%3Atextbook&page=1&keywords="+keyword+"&ie=UTF8&qid=1533137854"
obj = cls()
obj.amazon(url,0,18,minprofit, numberofbooks)
print("search finished")



