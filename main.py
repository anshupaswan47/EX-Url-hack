from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from random import randint, choice

urls = ['https://exurl.in/976RGSbH','https://exurl.in/UDjgt','https://exurl.in/UZ0aCBW','https://exurl.in/ju1G03','https://exurl.in/DULKlhky','https://exurl.in/9jhQJ','https://exurl.in/nxQoRZzX','https://exurl.in/sQcD']

def save_used_user_agent(used_user_agent):
        with open('used_user_agents.txt', 'a') as file:
            file.write(used_user_agent+'\n')
            
def choose_random_user_agent():
    with open('user-agents.txt', 'r') as file:
        user_agents = file.readlines()

    try:
        with open('used_user_agents.txt', 'r') as file:
            used_user_agents = file.readlines()
    except FileNotFoundError:
        used_user_agents = []

    user_agents = [user_agent for user_agent in user_agents if user_agent not in used_user_agents]

    if len(user_agents) == 0:
        return "All user agents have been used."
    else:
        random_user_agent = choice(user_agents)
        # save_used_user_agent(random_user_agent)
        return random_user_agent.strip()


options = Options()
options.add_extension('Adblock.crx')
options.add_extension('urban.crx')
options.add_experimental_option("detach", True)
user_agent = choose_random_user_agent()
options.add_argument(f"user-agent={user_agent}")
options.add_argument("--headless=new")
options.add_argument('--ignore-certificate-errors')
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
    btn3 = '/html/body/div[2]/div[1]/div/div/div/div[1]/a/span[1]'
    try:
        driver.find_element(By.XPATH,btn1).click()
        print("Google 0 xpath")
    except:
        
        try:
            driver.find_element(By.XPATH,btn2).click()
            print("Google 1 xpath")
        except:
            
            try:
                driver.find_element(By.XPATH,btn3).click()
                print("Google 2 xpath")
            except:
                print("Google Error")
                pass

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
    
def find_ip(driver):
    driver.get('https://www.myip.com/')
    try:
        sleep(1)
        ip = driver.find_element(By.XPATH,'//*[@id="ip"]')
        ip = ip.text
    except:
        print('Error to get IP')
    return ip

def start(driver):
    print("IP : ",find_ip(driver))
    url = choice(urls)
    print(url)
    driver.get(url)
    sleep(8)
    google_page(driver)
    print('started')
    sleep(1)
    process(driver)

def clickby_id(driver, id, attempts=5):
    if attempts == 0:
        driver.quit()
        return  # Exit if attempts exhausted
    try:
        driver.find_element(By.ID, id).click()
        print("ID Success")
    except:
        print("ID error")
        clickby_id(driver, id, attempts-1) 
    
def clickby_xpath(driver, path, attempts=5):
    if attempts == 0:
        driver.quit()
        return  # Exit if attempts exhausted
    try:
        driver.find_element(By.XPATH, path).click()
        print("XPath Success")
    except:
        print("XPath error")
        sleep(1)
        try:
            clickby_xpath(driver, path, attempts-1)
        except:
            pass

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
    sleep(16)

    clickby_xpath(driver,'//*[@id="container"]/section[2]/div/div/section/div/div/div/div/div[8]/center[3]/div/a')
    print("Over")
    sleep(3)
    save_used_user_agent(user_agent)
    driver.quit()
    
vpn(driver)
