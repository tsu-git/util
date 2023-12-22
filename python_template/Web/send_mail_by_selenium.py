#!/usr/bin/python

"""send_mail_by_selenium

    send a mail by command line
"""

"""Firefox failed to login due to the image-recognition
"""
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time, sys, argparse

WAIT_SECONDS = 15
parser = argparse.ArgumentParser(prog='send_mail_by_selenium.py',
            description='send a mail by command line')

# get ID and password through argument
parser.add_argument('-i', '--id', action='store')
parser.add_argument('-p', '--password', action='store')

# get TO, subject, content
parser.add_argument('-t', '--to', action='store')
parser.add_argument('-s', '--subject', action='store')
parser.add_argument('-c', '--content', action='store')

args = parser.parse_args()

# open gmail page
browser = Chrome()
browser.get('https://mail.google.com/mail/u/0/?pc=topnav-about-ja#inbox')

# login gmail
#   input id
user_elem = browser.find_element(By.ID, 'identifierId')
user_elem.send_keys(args.id)

#   submit next button
css_selector = ".VfPpkd-LgbsSe-OWXEXe-k8QpJ > span:nth-child(4)"
button_elem = browser.find_element(By.CSS_SELECTOR, css_selector)
button_elem.click() # submit() didn't work

time.sleep(WAIT_SECONDS) # needs seconds to appear the next page

#   input password
pass_elem = browser.find_element(By.NAME, 'Passwd')
pass_elem.send_keys(args.password)

#   submit next button
css_selector = '#passwordNext > div > button > span'
button_elem = browser.find_element(By.CSS_SELECTOR, css_selector)
button_elem.click()

time.sleep(WAIT_SECONDS) # needs seconds to appear the next page

# move to the compose message page
#   CSS selector: ".T-I-KE"
css_selector = '.T-I-KE'
button_elem = browser.find_element(By.CSS_SELECTOR, css_selector)
button_elem.click()

# input an mail address to send
css_selector = '#\:d6'
to_elem = browser.find_element(By.CSS_SELECTOR, css_selector)
to_elem.send_keys(args.to)

# input a subject
css_selector = '#\:9k'
subject_elem = browser.find_element(By.CSS_SELECTOR, css_selector)
subject_elem.send_keys(args.subject)

# input an body
css_selector = '#\:au'
body_elem = browser.find_element(By.CSS_SELECTOR, css_selector)
body_elem.send_keys(args.content)

# need to wait saving the mail as a draft
time.sleep(WAIT_SECONDS) # needs seconds to appear the next page

# submit send key
css_selector = '#\:9a'
button_elem = browser.find_element(By.CSS_SELECTOR, css_selector)
button_elem.click()
