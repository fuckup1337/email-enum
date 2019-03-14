from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options)

def quitSelenium():
    driver.quit()

def instagramCheck(email):
    driver.get("https://www.instagram.com/accounts/login/")
    assert "Login" in driver.title
    sleep(1.5)
    user = driver.find_element_by_name("username")
    user.send_keys(email)
    driver.find_element_by_xpath('//button["Log in"]').click()
    sleep(1)
    if "The username you entered does" in driver.page_source:
        result = "Not Found"
        return result
    if "The username you entered does" not in driver.page_source:
        result = "Found"
        return result
    else:
        print("Captcha encountered, you'll have to check this manually")

def twitterCheck(email):
    driver.get("https://twitter.com/account/begin_password_reset")
    assert "Password Reset" in driver.title
    sleep(1)
    user = driver.find_element_by_name("account_identifier")
    user.send_keys(email)
    driver.find_element_by_class_name("EdgeButton--primary").click()
    sleep(1)
    if "We couldn't find your account with that information" in driver.page_source:
        result = "Not Found"
        return result
    if "Enter your email, phone number, or username" not in driver.page_source:
        result = "Found"
        return result
    else:
        result = "Capthca encountered, you'll have to check this manually"
        return result

def snapchatCheck(email):
    driver.get("https://accounts.snapchat.com/accounts/password_reset_request")
    assert "Reset Password" in driver.title
    sleep(1.5)
    user = driver.find_element_by_name("emailaddress")
    user.send_keys(email)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/article/div/div[3]/form/div[3]/button").click()
    sleep(2)
    if "Email address is" in driver.page_source:
        result = "Not Found"
        return result
    if "Email address is invalid" not in driver.page_source and "If you know your current password, you may" in driver.page_source:
        result = "Capthca encountered, you'll have to check this manually"
        return result
    else:
        result = "Found"
        return result

def facebookCheck(email):
    driver.get("https://www.facebook.com/login/identify/?ctx=recover&ars=royal_blue_bar")
    assert "Forgot Password" in driver.title
    sleep(1)
    user = driver.find_element_by_xpath('//*[@id="identify_email"]')
    user.send_keys(email)
    user.send_keys(Keys.ENTER)
    #driver.find_element_by_xpath('//*[@id="u_0_2"]').click()
    sleep(2)
    if "No Search Results" in driver.page_source:
        result = "Not Found"
        return result
    if "No Search Results" and "No longer have access to these?" in driver.page_source:
        result = "Found"
        return result
    else:
        result = "Capthca encountered, you'll have to check this manually"
        return result
