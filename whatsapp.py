import time
import os
import pathlib
from urllib.parse import quote
from typing import Union, Optional
from platform import system

import webbrowser as web
import pyautogui as pg
import wikipedia
import requests

from exceptions import *

def sendwhatmsg(phone_no: str, message: str, time_hour: int, time_min: int, wait_time: int = 20,
                tab_close: bool = False, close_time: int = 3) -> None:
    """Sends a WhatsApp Message"""
    # Phone number should be given as a string
    # If the browser Window is not maximized this function won't work
    # Use check_window to check this

    global sleep_time
    if "+" not in phone_no:
        raise CountryCodeException("Country code missing from phone_no")
    timehr = time_hour

    if time_hour not in range(25) or time_min not in range(60):
        raise Warning("Invalid Time Format")

    if time_hour == 0:
        time_hour = 24
    call_sec = (time_hour * 3600) + (time_min * 60)

    current_time = time.localtime()
    current_hour = current_time.tm_hour
    current_minute = current_time.tm_min
    current_second = current_time.tm_sec

    if current_hour == 0:
        current_hour = 24

    current_to_second = (current_hour * 3600) + (current_minute * 60) + current_second
    left_time = call_sec - current_to_second

    if left_time <= 0:
        left_time = 86400 + left_time

    if left_time < wait_time:
        raise CallTimeException(
            "Call time must be greater than wait_time as web.whatsapp.com takes some time to load")

    date = "%s:%s:%s" % (current_time.tm_mday, current_time.tm_mon, current_time.tm_year)
    time_write = "%s:%s" % (timehr, time_min)
    with open("pywhatkit_dbs.txt", "a", encoding='utf-8') as file:
        file.write("Date: %s\nTime: %s\nPhone number: %s\nMessage: %s" %
                   (date, time_write, phone_no, message))
        file.write("\n--------------------\n")
    sleep_time = left_time - wait_time
    print(
        f"In {print_sleep_time()} seconds web.whatsapp.com will open and after {wait_time} seconds message will "
        f"be delivered")
    time.sleep(sleep_time)
    parsed_message = quote(message)
    web.open('https://web.whatsapp.com/send?phone=' +
             phone_no )
    time.sleep(2)
    width, height = pg.size()
    time.sleep(3)
    pg.click(width / 2, height - height / 10)
    pg.typewrite(parsed_message + "\n")
    
    # pg.press('enter')
    if tab_close:
        close_tab(wait_time=close_time)


def sendwhatmsg_to_group(group_id: str, message: str, time_hour: int, time_min: int, wait_time: int = 20,
                         tab_close: bool = False, close_time: int = 3) -> None:
    """Send WhatsApp Message to a Group"""
    # Group ID is in the group's invite link
    # https://chat.whatsapp.com/AB123CDEFGHijklmn, here AB123CDEFGHijklmn is group ID

    if time_hour not in range(25) or time_min not in range(60):
        print("Invalid time format")

    timehr = time_hour

    if time_hour == 0:
        time_hour = 24
    call_second = (time_hour * 3600) + (time_min * 60)

    current_time = time.localtime()
    current_hour = current_time.tm_hour
    current_minute = current_time.tm_min
    current_second = current_time.tm_sec

    if current_hour == 0:
        current_hour = 24

    current_to_second = (current_hour * 3600) + (current_minute * 60) + current_second
    left_time = call_second - current_to_second

    if left_time <= 0:
        left_time = 86400 + left_time

    if left_time < wait_time:
        raise CallTimeException(
            "Call time must be greater than wait_time as web.whatsapp.com takes some time to load")

    date = "%s:%s:%s" % (current_time.tm_mday, current_time.tm_mon, current_time.tm_year)
    time_write = "%s:%s" % (timehr, time_min)
    with open("pywhatkit_dbs.txt", "a", encoding='utf-8') as file:
        file.write("Date: %s\nTime: %s\nGroup_id: %s\nMessage: %s" %
                   (date, time_write, group_id, message))
        file.write("\n--------------------\n")
    sleep_time = left_time - wait_time
    print(f"In {sleep_time} seconds web.whatsapp.com will open and after {wait_time} seconds message will be delivered")
    time.sleep(sleep_time)
    web.open('https://web.whatsapp.com/accept?code=' + group_id)
    time.sleep(2)
    width, height = pg.size()
    time.sleep(wait_time - 2)
    pg.click(width / 2, height - height / 10)
    pg.typewrite(message + "\n")
    if tab_close:
        close_tab(wait_time=close_time)


def close_tab(wait_time: int = 2) -> None:
    """Closes the Currently Opened Browser Tab"""

    time.sleep(wait_time)
    if system().lower() in ("windows", "linux"):
        pg.hotkey("ctrl", "w")
    elif system().lower() in "darwin":
        pg.hotkey("command", "w")
    else:
        raise Warning(f"{system().lower()} not supported!")
    pg.press("enter")


def print_sleep_time() -> Union[str, int]:
    """Prints the sleep time"""

    return sleep_time