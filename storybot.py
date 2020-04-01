# VERSION 0.1.9.1

from art import *
import pandas as pd
import random
from random import randint
from time import sleep, strftime
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm
from tqdm import tqdm_gui
import sys
sys.path.insert(0, './utils/')
import secret
import hashtags
import userlist
import limits
import proxy
import warnings
import datetime

tprint("Welcome OGU")
sleep(0.5)
print("Made with Selenium")
sleep(0.5)
print("Version 0.1.9.1")
print("Loading Scripts...")
time_start = datetime.datetime.now()
for i in tqdm(range(6)):
    sleep(0.05)
    pass


use_proxy = input("Do you want to use a proxy? [y/n]: ")

if use_proxy == "y":
    use_proxy_config = input("Do you want to use the proxy config file? [y/n]: ")
    if use_proxy_config == "n":
        proxy_type = input("IP:PORT only? [y/n]: ")
        if proxy_type == "n":
            proxy_username = input("Enter your proxy username: ")
            proxy_password = input("Enter your proxy passowrd: ")
            proxy_host = input("Enter your proxy host (ip:port): ")
            from selenium.webdriver.firefox.options import Options
            from seleniumwire import webdriver
            #options = webdriver.ChromeOptions()

            options = {
                'proxy': {
                    'http': 'http://{}:{}@{}'.format(proxy_username, proxy_password, proxy_host),
                    'https': 'https://{}:{}@{}'.format(proxy_username, proxy_password, proxy_host)
                    }
            }
            ##options.add_argument("--mute-audio")
            warnings.filterwarnings("ignore", category=DeprecationWarning)
            profile = webdriver.FirefoxProfile()
            profile.set_preference("media.volume_scale", "0.0")
            ##webdriver = webdriver.Chrome(seleniumwire_options=options, chrome_options=options, executable_path='./chromedriver')
            webdriver = webdriver.Firefox(seleniumwire_options=options, firefox_options=options, executable_path="./geckodriver", firefox_profile=profile)
            sleep(2)
            webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
            sleep(3)
        else:
            proxy_host = input("Enter your proxy IP:PORT: ")
            from selenium.webdriver.firefox.options import Options
            #options = webdriver.ChromeOptions()

            warnings.filterwarnings("ignore", category=DeprecationWarning)
            options.add_argument('--proxy-server={}'.format(proxy_host))
            ##options.add_argument("--mute-audio")
            profile = webdriver.FirefoxProfile()
            profile.set_preference("media.volume_scale", "0.0")
            ##webdriver = webdriver.Chrome(chrome_options=options, executable_path='./chromedriver')
            webdriver = webdriver.Firefox(firefox_options=options, executable_path="./geckodriver", firefox_profile=profile)
            sleep(2)
            webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
            sleep(3)
    else:
        proxy_type = input("IP:PORT only? [y/n]: ")
        if proxy_type == "n":
            from selenium.webdriver.firefox.options import Options
            from seleniumwire import webdriver
            #options = webdriver.ChromeOptions()

            options = {
                'proxy': {
                    'http': 'http://{}:{}@{}'.format(proxy.proxy_username, proxy.proxy_password, proxy.proxy_host),
                    'https': 'https://{}:{}@{}'.format(proxy.proxy_username, proxy.proxy_password, proxy.proxy_host)
                    }
            }
            ##options.add_argument("--mute-audio")
            warnings.filterwarnings("ignore", category=DeprecationWarning)
            profile = webdriver.FirefoxProfile()
            profile.set_preference("media.volume_scale", "0.0")
            ##webdriver = webdriver.Chrome(seleniumwire_options=options, chrome_options=options, executable_path='./chromedriver')
            webdriver = webdriver.Firefox(seleniumwire_options=options, firefox_options=options, executable_path="./geckodriver", firefox_profile=profile)
            sleep(2)
            webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
            sleep(3)
        else:
            from selenium.webdriver.firefox.options import Options
            #options = webdriver.ChromeOptions()

            warnings.filterwarnings("ignore", category=DeprecationWarning)
            options.add_argument('--proxy-server={}'.format(proxy.proxy_host))
            ##options.add_argument("--mute-audio")
            profile = webdriver.FirefoxProfile()
            profile.set_preference("media.volume_scale", "0.0")
            ##webdriver = webdriver.Chrome(chrome_options=options, executable_path='./chromedriver')
            webdriver = webdriver.Firefox(firefox_options=options, executable_path="./geckodriver", firefox_profile=profile)
            sleep(2)
            webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
            sleep(3)
else:
    profile = webdriver.FirefoxProfile()
    profile.set_preference("media.volume_scale", "0.0")
    ##options = webdriver.ChromeOptions()
    ##options.add_argument("--mute-audio")
    ##webdriver = webdriver.Chrome(executable_path='./chromedriver')
    webdriver = webdriver.Firefox(executable_path="./geckodriver", firefox_profile=profile)
    sleep(2)
    webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    sleep(3)
username = webdriver.find_element_by_name('username')
username.send_keys(secret.username)
password = webdriver.find_element_by_name('password')
password.send_keys(secret.password)
sleep(2)
button_login = webdriver.find_element_by_xpath(
    '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button')
button_login.click()
sleep(10)

try:
    notnow = webdriver.find_element_by_css_selector(
        'button.aOOlW:nth-child(2)')
    notnow.click()  # comment these last 2 lines out, if you don't get a pop up asking about notifications
except NoSuchElementException:
    pass

num = 0
for user in userlist.users:
    sleep(2)
    webdriver.get('https://www.instagram.com/' +
                userlist.users[num] + '/')
    sleep(5)
    print("Getting followers with Stories to watch from: {}".format(userlist.users[num]))
    num += 1
    sleep(1)
    followers_list__open = webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
    followers_list__open.click()
    sleep(2)

    fBody  = webdriver.find_element_by_xpath("//div[@class='isgrP']")
    scroll = 0
    while scroll < limits.scroll_amount: # scroll 5 times
        webdriver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
        sleep(2)
        scroll += 1

    fList  = webdriver.find_elements_by_xpath("//div[@class='isgrP']//li")

    wbList = webdriver.find_elements_by_xpath("//div[@class='RR-M- h5uC0 SAvC5']")
    print("Users found with Story to watch: {}".format(len(wbList)))
    story_watching_done = 'false'
    stories_next_watch = "true"
    story_watching_counter = 0
    stories_bf_watched = 1

    try:
        for user_story in wbList:
            while story_watching_done == 'false':
                stories_next_watch = "true"
                wbList = webdriver.find_elements_by_xpath("//div[@class='RR-M- h5uC0 SAvC5']")
                webdriver.execute_script("arguments[0].scrollIntoView();", wbList[story_watching_counter])
                wbList[story_watching_counter].click()
                while stories_next_watch == "true":
                    try:
                        sleep(randint(2, 3))
                        webdriver.implicitly_wait(2)
                        watch_all_stories_next = webdriver.find_element_by_css_selector(".ow3u_").click()
                        stories_bf_watched += 1
                        print("Stories watched from followers: {}".format(stories_bf_watched))
                    except (NoSuchElementException, StaleElementReferenceException) as e:
                        stories_next_watch = "false"

                else:
                    try:
                        watch_all_stories_close_from_followers = webdriver.find_element_by_xpath("/html/body/div[1]/section/div/div/section/div[2]/button[3]/div")
                        watch_all_stories_close_from_followers.click()
                    except NoSuchElementException:
                        pass
                    wbList = webdriver.find_elements_by_xpath("//div[@class='RR-M- h5uC0 SAvC5']")
                    story_watching_counter += 1
                    sleep(1)
            else:
                pass
    except IndexError as error:
        print("Index Error..")
        print("Moving to next user...")
        pass
else:
    print("Script finished!")
    time_end = datetime.datetime.now()
    sleep(1)
    print ("Script Started at: {}".format(time_start.strftime("%Y-%m-%d %H:%M:%S")))
    sleep(1)
    print ("Script Ended at: {}".format(time_end.strftime("%Y-%m-%d %H:%M:%S")))
    sleep(1)
    print("Total Stories watched from users followers: {}".format(limits.user_watch_followers_stories, stories_bf_watched))
    sleep(1)
    print("closing browser...")
    sleep(1)
    webdriver.close()
