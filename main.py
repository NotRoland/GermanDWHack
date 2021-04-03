from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element_present = EC.presence_of_element_located((By.CLASS_NAME, 'cookie'))

tBr = input("What browser do you have installed? (firefox/chrome) ")
if tBr == 'chrome':
    browser = webdriver.Chrome()
else:
    browser = webdriver.Firefox()

site = input("Enter site (learngerman.dw start page): ")
grade = input("Percentage: ")

browser.get(site)

browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
browser.find_element_by_id("start-lesson").click()
WebDriverWait(browser, 10).until(element_present)

browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(0.2)

pages = browser.find_element_by_class_name("exercise-nav-title").text
pages = int(pages.split(" / ")[1])

print("Pages: " + str(pages))
ex = input(f"Exercises out of {str(pages)}: ")

for i in range(pages):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.find_element_by_id("nextButton").click()
    WebDriverWait(browser, 10).until(element_present)
    sleep(0.1)

browser.execute_script(f'document.getElementById("doneExerciseCount").innerHTML = "{ex}"')
browser.execute_script(f'document.getElementsByClassName("result-points low")[0].innerHTML = "{grade} %"')
if grade == '100':
    browser.execute_script(f'document.getElementsByClassName("exercise-results-header")[0].innerHTML = "Perfect! You can be proud of yourself."')

print("Finished.")
