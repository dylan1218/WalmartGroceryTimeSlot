from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time



#driver = webdriver.Chrome(executable_path='C:\\Program Files\\chromedriver\\chromedriver.exe')

chrome_options = Options()
chrome_options.add_argument("user-data-dir=C:\\Users\\Dylan\\AppData\\Local\\Google\\Chrome\\User Data\\Default") #Path to your chrome profile 
driver = webdriver.Chrome(executable_path='C:\\Program Files\\chromedriver\\chromedriver.exe', chrome_options=chrome_options)

def getWebPage():
    driver.get("https://grocery.walmart.com/")

def shoppingContentID():
    driver.implicitly_wait(5) # seconds
    driver.find_element_by_xpath('//*[@id="shoppingContent"]/div[1]/div[1]/div[1]/div[1]/button').click()

def enterZipInput():
    driver.implicitly_wait(5) # seconds
    zipInput = driver.find_element_by_xpath('//*[@id="panel-0"]/div/form/div/input')
    zipInput.click()
    zipInput.clear()
    zipInput.send_keys("08831") #enter zip code here

def setZipInput():
    driver.implicitly_wait(5) # seconds 
    zipInputSetter = driver.find_element_by_xpath('//*[@id="panel-0"]/div/form/div/button')
    zipInputSetter.click() #sets the entered zipcode and returns stores

def selectFirstZip():
    driver.implicitly_wait(5) # seconds 
    zipInputPost = driver.find_element_by_xpath('//*[@id="panel-0"]/div/ul/li[1]/label')
    zipInputPost.click() #selects the first zip input option 

def confirmZip():
    driver.implicitly_wait(5)
    zipInputConfirm = driver.find_element_by_xpath('/html/body/div/div[2]/aside[2]/section/div/button')
    zipInputConfirm.click() #confirms the selected store

'''
zipInputClear = driver.find_element_by_xpath('//*[@id="dialogTitle-Locations"]/button')
zipInputClear.click() #exits the zipinput modal
#will need to have the confirmation button click, functionality not set yet
'''
def getDateSlots():
    driver.implicitly_wait(5) # seconds
    timeSlotGet = driver.find_element_by_xpath('//*[@id="shoppingContent"]/div[1]/div[2]/button')
    timeSlotGet.click() #gets the list of available times

def getBookSlotArray():
    driver.implicitly_wait(5)
    bookSlotArray1 = driver.find_element_by_xpath("/html/body/div/div[1]/div/section/div[1]/div/div[3]/div[1]/div/button[1]") 
    #bookSlotArray1.text

def searchTimeSlots():
    for days in range(1, 7):
        bookSlotArray = driver.find_element_by_xpath('/html/body/div/div[1]/div/section/div[1]/div/div[3]/div[1]/div/button[' + str(days) + ']')
        print(bookSlotArray.text)
        if "Free pickup" in bookSlotArray.text:
            bookSlotArray.click()
            driver.implicitly_wait(5)
            for timeSlots in range(1,24):
                timeSlotArray = driver.find_element_by_xpath('/html/body/div/div[1]/div/section/div[1]/div/div[3]/div[2]/label['+str(timeSlots)+']/div')
                try:                   #/html/body/div/div[1]/div/section/div[1]/div/div[3]/div[2]/label[1]/input                                                                                  
                    timeSlotArray = driver.find_element_by_xpath('/html/body/div/div[1]/div/section/div[1]/div/div[3]/div[2]/label['+str(timeSlots)+']/div')
                    timeSlotArray.click()
                    print("Slot found, exiting")
                    return
                except:
                    continue
            break
    print("No slots found, retrying in 60 seconds")
    time.sleep(60) #stops script execution for 60 seconds
    driver.refresh() #refreshes the page
    searchTimeSlots() #recursive function called until slot is found



def getWalmartSlot():
    getWebPage()
    shoppingContentID()
    enterZipInput()
    setZipInput()
    selectFirstZip()
    confirmZip()
    getDateSlots()
    getBookSlotArray()
    searchTimeSlots()

def queryRepeatedly():
    try:
        getWalmartSlot()
    except:
        time.sleep(10)
        queryRepeatedly() #on error the getWalmartSlot function will restart

queryRepeatedly()
#driver.find_element_by_xpath('//*[@id="panel-0"]/div/form/div/input').setAttribute('value', '07728')

#Old Bridge xpath //*[@id="panel-0"]/div/ul/li[1]

