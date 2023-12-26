#!/usr/bin/python

"""get_photos_from_Flickr.py

    download pohotos form the Flickr, using spesific keywords
"""
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time, sys, argparse, os, logging

DOWNLOAD_DIR_NAME = 'Flickr'
TIME_PAGE_LOAD = 3
TIME_DOWNLOAD = 7
LOG_FMT = ' %(asctime)s: %(levelname)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=LOG_FMT)

MAX_NUM_OF_DOWNLOAD = 5
HOST_URL = 'https://www.flickr.com'

# TODO: get argument using argparse
# get search result page of the Flickr
browser = Chrome()
url = HOST_URL + '/search/?text='
logging.debug(f"search key word[s]: {sys.argv[1:]}")
browser.get(url + ' '.join(sys.argv[1:]))
#browser.get(url + 'duck baby')

# make a download directory
#   make a directory only when it doesn't exist
os.makedirs(DOWNLOAD_DIR_NAME, exist_ok=True)

class_name = 'view.photo-list-photo-view.awake'
try:
    photo_elems = browser.find_elements(By.CLASS_NAME, class_name)
except:
    logging.debug(f"""cought exception while processing find_elements
                by {class_name}""")

# get photo elements from the result page
""" target class name is "view photo-list-photo-view awake"
    Spaces in the class name must be '.' when using for find_elements().
"""
iterative_num = 0
for i in range(len(photo_elems)):
    if iterative_num >= MAX_NUM_OF_DOWNLOAD:
        break

    """needs to do find_element() every time because element value on 
       the page changes when visit the page.
    """
    class_name = 'view.photo-list-photo-view.awake'
    try:
        photo_elems = browser.find_elements(By.CLASS_NAME, class_name)
    except:
        logging.debug(f"""cought exception while processing find_elements
                    by {class_name}""")

    if len(photo_elems) < 1:
        logging.debug(f"was not able to find elements: [{class_name}]")
        sys.exit()
    elif len(photo_elems) < i + 1:
        break

    logging.debug(f"target page: [{photo_elems[i]}]")
    photo_elems[i].click()

    time.sleep(TIME_PAGE_LOAD)

    # move to the each photo page
    class_name = 'ui-icon-download'
    download_elem = browser.find_element(By.CLASS_NAME, class_name)
    download_elem.click()

    time.sleep(TIME_PAGE_LOAD)

    # select size
    """   When the auther doesn't allow to download this, "View all sizes"
        pop-up appears, instead various download size links. "View all 
        sizes" screen displays message, "The owner has disabled downloading
        of their photos"
    """
    link_text = 'Medium'
    small_elem = ""
    try:
        small_elem = browser.find_element(By.PARTIAL_LINK_TEXT, link_text)
    except:
        logging.debug(f"NotFound: [{link_text}]")


    # download photos
    if small_elem:
        try:
            small_elem.click()
        except:
            logging.debug("Failed to download")
            sys.exit()
        time.sleep(TIME_DOWNLOAD)
        iterative_num += 1

    browser.back()
    time.sleep(TIME_PAGE_LOAD)


browser.quit()
