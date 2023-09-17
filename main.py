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
url_x = 175
url_y = 80
email_domain = 'kicksbycrunchy.com'
sleepTime = 0.7
basicSleepTime = 0.5
longerSleepTime = 4


def move_to_user_icon():
    time.sleep(longerSleepTime)
    pyautogui.moveTo(1432, 200)
    time.sleep(sleepTime)


def generate_first_name():
    return names.get_first_name()


def generate_lastname():
    return names.get_last_name()


def handle_registration():

    first_name = generate_first_name()
    last_name = generate_lastname()
    time.sleep(longerSleepTime)
    pyautogui.moveTo(321, 551)
    pyautogui.click()
    pyautogui.scroll(-7)

    # Fill in the first name
    pyautogui.moveTo(input_position, 210)
    time.sleep(basicSleepTime)
    pyautogui.click()
    keyboard.type(first_name)

    # Fill in the last name
    pyautogui.moveTo(input_position, 310)
    time.sleep(basicSleepTime)
    pyautogui.click()
    keyboard.type(last_name)

    # Fill in the email
    pyautogui.moveTo(input_position, 410)
    time.sleep(1)
    pyautogui.click()
    keyboard.type(first_name + '.' + last_name + '@' + email_domain)

    # Fill in the password
    pyautogui.moveTo(input_position, 510)
    time.sleep(basicSleepTime)
    pyautogui.click()
    keyboard.type(password)

    # Click on the newsletter checkbox
    pyautogui.moveTo(input_position, 850)
    time.sleep(basicSleepTime)
    pyautogui.click()

    # Submit the registration form
    pyautogui.moveTo(input_position, 910)
    time.sleep(longerSleepTime)
    pyautogui.click()
    time.sleep(longerSleepTime)


def handle_logut():
    pyautogui.moveTo(10, 10)
    move_to_user_icon()

    pyautogui.moveTo(1210, 523)
    time.sleep(longerSleepTime)
    pyautogui.click()


def handle_go_to_registration_page():
    time.sleep(basicSleepTime)
    pyautogui.moveTo(10, 10)
    move_to_user_icon()
    time.sleep(basicSleepTime)
    pyautogui.moveTo(1240, 309)
    time.sleep(longerSleepTime)
    pyautogui.click()

def holder ():
    pyautogui.click(175, 80)
    keyboard.type("192.168.1.1")
    pyautogui.press("enter")
    time.sleep(basicSleepTime) 
    pyautogui.click(900, 380)
    keyboard.type("9Q6G3TZE")
    pyautogui.click(900, 430) 
    pyautogui.click(350, 80)
    pyautogui.press("del")
    keyboard.type("http://192.168.1.1/supportRestart.html")

def handle_reset ():
    pyautogui.click(url_x, url_y)
    time.sleep(2)
    keyboard.type("192.168.1.1")
    pyautogui.press("enter")
    time.sleep(4) 
    pyautogui.click(900, 380)
    keyboard.type("9Q6G3TZE")
    time.sleep(2)
    pyautogui.click(940, 430) 
    time.sleep(2)
    pyautogui.click(350, 80)
    time.sleep(3) 
    pyautogui.press("del")
    keyboard.type("http://192.168.1.1/supportRestart.html")
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.click(950, 540)
    time.sleep(1)
    pyautogui.hotkey('shift', 'command', 'w')
    time.sleep(1)
    pyautogui.click(500, 20)
    time.sleep(1)
    pyautogui.hotkey('shift', 'command', 'n')
    time.sleep(360) 

def new_lando_entry ():
    pyautogui.click(url_x, url_y)
    keyboard.type("zalando.pl")
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.click(1200, 930)
    pyautogui.click(1200, 930)
    handle_go_to_registration_page()

x = 0

while (1):
    x+=1
    handle_registration()
    handle_logut()
    handle_go_to_registration_page()
    if x == 100:
      time.sleep(2)
      pyautogui.hotkey('shift', 'command', 'w')
      time.sleep(2)
      pyautogui.click(500, 40)
      time.sleep(2)
      pyautogui.hotkey('shift', 'command', 'n')
      time.sleep(2)
      handle_reset()
      new_lando_entry()
      x=0
