#!/usr/bin/python

import unittest, random, string
from datetime import datetime

def gen_timestr() -> str:
    dt = datetime.now()
    return(dt.strftime('%H-%M-%S-%f'))

def random_name(len: int) -> str:
    source_characters = string.ascii_letters + string.digits
    random_list = [random.choice(source_characters) for i in range(len)]
    return(''.join(random_list))


def random_name_list(num_of_names: int) -> list:
    random_list = []

    for i in range(num_of_names):
        random_list.append(random_name(5))

    unique_list = list(set(random_list))

    return(unique_list)


class Test_get_linket_pages(unittest.TestCase):
    
    def test_random_name(self):
        self.assertTrue(len(random_name(1)), 1)
        self.assertTrue(len(random_name(5)), 5)
        self.assertTrue(len(random_name(10)), 10)

    def test_random_name_list(self):
        self.assertTrue(len(random_name_list(1)), 1)
        self.assertTrue(len(random_name_list(5)), 5)
        self.assertTrue(len(random_name_list(10)), 10)


if __name__ == "__main__":

    #unittest.main()

    from urllib.parse import urljoin
    import requests, bs4, sys, logging, shutil, os, argparse, re
    from pathlib import Path

    parser = argparse.ArgumentParser(
                prog='get_linked_pages.py',
                description="""search link[s] on the webpage and
                            download the page[s]""")
    parser.add_argument('url')
    parser.add_argument('-s', '--suffix', action='store')
    parser.add_argument('-d', '--debug', action='store_true')

    args = parser.parse_args()

    LOG_FMT = ' %(asctime)s: %(levelname)s: %(message)s'
    
    if args.debug is False:
        logging.disable(logging.WARNING)

    logging.basicConfig(level=logging.DEBUG, format=LOG_FMT)
    STORAGE_DIR = 'downloaded_pages'

    given_url = args.url
    print(given_url)

    # make a directory to store downloaded pages
    os.makedirs(STORAGE_DIR, exist_ok=True)

    # get all the links on the web page
    try:
        resp = requests.get(given_url)
        resp.raise_for_status()
    except Exception as exc:
        logging.error(f"webpage download error [{exc}]")
        sys.exit(False)

    logging.info("### request headers")
    for k, v in resp.request.headers.items():
        logging.info(f"    {k}: {v}")
    logging.info("### response headers")
    for k, v in resp.headers.items():
        logging.info(f"    {k}: {v}")
    logging.info(f"status_code [{resp.status_code}]")

    soup = bs4.BeautifulSoup(resp.text, 'html.parser')
    link_elems = soup.select("a[href]")
    broken_links = []

    # download the each webpage
    for link in link_elems:
        link_url = link.get('href')
        if link_url[0] == '#':  # ignore a fragment element
            continue
        absolute_link_url = urljoin(given_url, link.get('href'))
        relative_path = link.get('href')
        # only get content which has the suffix, when it's been given
        if args.suffix:
            if re.search(f".{args.suffix}$", relative_path) == None:
                continue

        logging.info(f"link: [{absolute_link_url}]")

        # get content of the page which the link refer
        try:
            sub_resp = requests.get(absolute_link_url)
        except Exception as exc:
            logging.error(f"webpage download error [{exc}]")
            # store the broken page link into an array
            broken_links.append(absolute_link_url)
            continue

        # generate local path to the local file
        if args.suffix and re.search(f".{args.suffix}$", relative_path):
            local_file = str(Path(STORAGE_DIR) / Path(relative_path).name)
        else:
            local_file = str(Path(STORAGE_DIR) / Path(gen_timestr())) + ".html"

        # put the content to the local file
        with open(local_file, 'wb') as page:
            for chunk in sub_resp.iter_content(100000):
                page.write(chunk)

        logging.info(f"saved: [{local_file}]")

       
    # print the broken page
    if len(broken_links):
        print("-" * 50)
        print("couldn't save the following page[s]")

        for link in broken_links:
            print(f"broken link: {link}")


    sys.exit(True)
