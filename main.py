from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from random import randint, choice
from fake_useragent import UserAgent
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
urls = ['https://exurl.in/976RGSbH','https://exurl.in/UDjgt','https://exurl.in/UZ0aCBW','https://exurl.in/ju1G03','https://exurl.in/DULKlhky','https://exurl.in/9jhQJ','https://exurl.in/nxQoRZzX','https://exurl.in/sQcD']


def get_random_user_agent():
    ua = UserAgent()
    return ua.random

options = Options()
options.add_extension('Adblock.crx')
options.add_extension('urban.crx')
options.add_experimental_option("detach", True)
user_agent = get_random_user_agent()
options.add_argument(f"user-agent={user_agent}")
# options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get("chrome-extension://eppiocemhmnlbhjplcgkofciiegomcon/popup/index.html#/welcome-consent")
driver.maximize_window()

def vpn_proccess(driver):
    driver.switch_to.window(driver.window_handles[0])
    a = '/html/body/div/div/div[3]/div[2]/div/div[1]/input'
    b = '/html/body/div/div/div[3]/div[2]/div/div[2]/div/ul/li[1]'
    driver.find_element(By.XPATH,value=a).click()
    driver.find_element(By.XPATH,value=b).click()
    driver.execute_script("window.open();")
    driver.switch_to.window(driver.window_handles[1])
    start(driver)

def google_page(driver):
    btn1 = '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/span/a/h3'
    btn2 = '//*[@id="main"]/div[3]/div/div[1]/a/div/div[1]/h3/div'
    try:
        driver.find_element(By.XPATH,btn1).click()
    except:
        driver.find_element(By.XPATH,btn2).click()

def vpn(driver):
    driver.get("chrome-extension://eppiocemhmnlbhjplcgkofciiegomcon/popup/index.html#/welcome-consent")
    driver.switch_to.window(driver.window_handles[0])
    sleep(10)
    # driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/button[2]").click()
    clickby_xpath(driver,"/html/body/div/div/div[2]/div/div/div/button[2]")
    # driver.find_element(By.XPATH,value="/html/body/div/div/div[3]/div[2]/div/div[1]/input").click()
    clickby_xpath(driver,"/html/body/div/div/div[3]/div[2]/div/div[1]/input")
    driver.implicitly_wait(5)
    # i=randint(1,5)
    i=1
    # driver.find_element(By.XPATH,value="/html/body/div/div/div[3]/div[2]/div/div[2]/div/ul/li["+str(i)+"]").click()
    clickby_xpath(driver,"/html/body/div/div/div[3]/div[2]/div/div[2]/div/ul/li["+str(i)+"]")
    sleep(4)
    driver.switch_to.window(driver.window_handles[1])
    sleep(1)
    start(driver)
    
def start(driver):
    url = choice(urls)
    print(url)
    driver.get(url)
    sleep(8)
    # btn = '//*[@id="main"]/div[3]/div/div[1]/a/div/div[1]/h3/div'
    # driver.get('https://battlechamp.in/')
    google_page(driver)
    print('started')
    sleep(1)
    process(driver)

def clickby_id(driver,id):
    try:
        driver.find_element(By.ID, id).click()
    except:
        driver.execute_script("window.scrollTo(0, 2);")
        clickby_id(driver,id)
    
def clickby_xpath(driver,path):
    try:
        driver.find_element(By.XPATH,path).click()
    except:
        clickby_xpath(driver,path)

def process(driver):
    # verify
    clickby_id(driver,"link") 
    print("All right")
    sleep(16)
    print("Verified")
    # human verify
    clickby_id(driver,"tp98")
    print("wait")
    sleep(4)
    print("Human Verified")
    # 1 continue
    clickby_id(driver,"btn6")
    print("1- continue")
    sleep(16)

    # wait
    clickby_id(driver,"tp98")
    print("wait")
    sleep(4)

    #  2 continue
    clickby_id(driver,"btn6")
    print("2- continue")
    sleep(20)

    clickby_xpath(driver,'//*[@id="container"]/section[2]/div/div/section/div/div/div/div/div[8]/center[3]/div/a')
    print("Over")
    sleep(3)
    driver.quit()
    
    
    

vpn(driver)
