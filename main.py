from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Scrolls the webpage down all the way. This is used
# for getting to the bottom so we have the start and
# next buttons visible.
def scroll(browser):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def main():
    # LearnGermanDW has a cookie banner displayed by default, so we can
    # use this to detect when the page loads.
    cookie = EC.presence_of_element_located((By.CLASS_NAME, 'cookie'))

    tBr = input("What browser do you have installed? (firefox/chrome) ")
    if tBr == 'chrome':
        browser = webdriver.Chrome()
    else:
        browser = webdriver.Firefox()

    site = input("Enter site (learngerman.dw start page): ")
    grade = input("Percentage: ")

    browser.get(site)

    scroll(browser)
    browser.find_element_by_id("start-lesson").click()

    # Waits until the website has loaded. (remember the
    # cookie variable from before?)
    WebDriverWait(browser, 10).until(cookie)

    scroll(browser)
    sleep(0.2)

    # This gets the page count of the lesson in the format `1 / pg`.
    pages = browser.find_element_by_class_name("exercise-nav-title").text
    pages = int(pages.split(" / ")[1])

    print("Pages: " + str(pages))
    ex = input(f"Exercises out of {str(pages)}: ")

    for i in range(pages):
        scroll(browser)
        browser.find_element_by_id("nextButton").click()
        
        # Waits for the banner again.
        WebDriverWait(browser, 10).until(cookie)
        sleep(0.1) # This wait is just in case your computer is lagging.

    browser.execute_script(f'document.getElementById("doneExerciseCount").innerHTML = "{ex}"') # Sets the exercise count.
    browser.execute_script(f'document.getElementsByClassName("result-points low")[0].innerHTML = "{grade} %"') # Sets your grade.
    
    # Here, if the grade is perfect, we set the result text to
    # what it would normally say when this happens.
    if grade == '100':
        browser.execute_script(f'document.getElementsByClassName("exercise-results-header")[0].innerHTML = "Perfect! You can be proud of yourself."')

    print("Finished.")
