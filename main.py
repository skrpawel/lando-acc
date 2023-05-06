import pyautogui
import time
import names
from pynput.keyboard import Controller
import webbrowser

# Initialize the keyboard controller
keyboard = Controller()

# Constants
password = 'Poteznehaslo1'
input_position = 680
email_domain = 'crunchykicksmail.com'
sleepTime = 0.7
basicSleepTime = 0.5
longerSleepTime = 4


def move_to_user_icon():
    pyautogui.moveTo(1446, 155)
    time.sleep(sleepTime)


def generate_first_name():
    return names.get_first_name()


def generate_lastname():
    return names.get_last_name()


def handle_registration():

    first_name = generate_first_name()
    last_name = generate_lastname()
    time.sleep(longerSleepTime)
    pyautogui.moveTo(200, 200)
    pyautogui.click()
    pyautogui.scroll(-7)

    # Fill in the first name
    pyautogui.moveTo(input_position, 160)
    time.sleep(basicSleepTime)
    pyautogui.click()
    keyboard.type(first_name)

    # Fill in the last name
    pyautogui.moveTo(input_position, 260)
    time.sleep(basicSleepTime)
    pyautogui.click()
    keyboard.type(last_name)

    # Fill in the email
    pyautogui.moveTo(input_position, 360)
    time.sleep(1)
    pyautogui.click()
    keyboard.type(first_name + '.' + last_name + '@' + email_domain)

    # Fill in the password
    pyautogui.moveTo(input_position, 460)
    time.sleep(basicSleepTime)
    pyautogui.click()
    keyboard.type(password)

    # Click on the newsletter checkbox
    pyautogui.moveTo(input_position, 800)
    time.sleep(basicSleepTime)
    pyautogui.click()

    # Submit the registration form
    pyautogui.moveTo(input_position, 860)
    time.sleep(longerSleepTime)
    pyautogui.click()


def handle_logut():
    pyautogui.moveTo(10, 10)
    time.sleep(longerSleepTime)
    move_to_user_icon()

    pyautogui.moveTo(1250, 495)
    time.sleep(longerSleepTime)
    pyautogui.click()


def handle_go_to_registration_page():
    pyautogui.moveTo(10, 10)
    time.sleep(basicSleepTime)
    move_to_user_icon()
    time.sleep(basicSleepTime)
    pyautogui.moveTo(1330, 265)
    time.sleep(longerSleepTime)
    pyautogui.click()


def handle_mails():
    pyautogui.click(200, 50)
    pyautogui.click(550, 355)
    time.sleep(sleepTime)
    pyautogui.moveTo(340, 375)
    time.sleep(sleepTime)
    pyautogui.click()
    pyautogui.moveTo(1000, 650)
    time.sleep(sleepTime)
    pyautogui.click(button='right')
    time.sleep(sleepTime)
    pyautogui.moveTo(1050, 660)
    pyautogui.click()
    time.sleep(sleepTime)
    pyautogui.moveTo(1823, 333)
    time.sleep(sleepTime)
    pyautogui.click()
    pyautogui.click(1550, 525)
    pyautogui.click(555, 50)
    time.sleep(sleepTime)


while (True):

    # handle_mails()
    handle_registration()
    handle_logut()
    handle_go_to_registration_page()
