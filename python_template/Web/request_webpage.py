#!/usr/bin/python
"""Get a webpage.

    When you need to pass through a proxy, give command line option and
    provide user id and proxy password following the prompt.

    It seems that the requests module put log automatically using the 
    logging module and its basicConfig.
"""

if __name__ == "__main__":
    import sys
    import requests
    import os
    import argparse
    import logging

    DOMAIN = "example_domain"
    ENCODED_SEP = "%5C"
    PROXY_SVR = "127.0.0.1"
    PROXY_PRT = "8080"
    LOG_FMT = ' %(asctime)s: %(levelname)s: %(message)s'

    logging.basicConfig(level=logging.DEBUG, format=LOG_FMT)

    parser = argparse.ArgumentParser(
                prog='request_webpage.py',
                description='download a webpage')
    parser.add_argument('-p', '--proxy_auth', action='store_true')

    args = parser.parse_args()

    prompt_1 = "input user id without domain: "
    prompt_2 = "input password: "

    if args.proxy_auth:
        uid = input(prompt_1).strip()
        password = input(prompt_2).strip()

        proxy_info_with_auth = (f"http://{DOMAIN}{ENCODED_SEP}{uid}:"
                            f"{password}@{PROXY_SVR}:{PROXY_PRT}")

        os.environ['HTTP_PROXY'] = proxy_info_with_auth
        os.environ['HTTPS_PROXY'] = proxy_info_with_auth

        logging.debug(f"uid: [{uid}], password: [{password}]")
        logging.debug(f"proxy_info: [{proxy_info_with_auth}]")


    prompt_3 = "input URL: "
    url = input(prompt_3).strip()
    logging.debug(f"url: [{url}]")

    try:
        with requests.get(url, stream=True) as resp:
            print("### request.headers")
            for k, v in resp.request.headers.items():
                print(f"    {k}: {v}")
            print("### headers")
            for k, v in resp.headers.items():
                print(f"    {k}: {v}")
            print(f"status_code [{resp.status_code}]")

            with open("donwloaded_page.html", "wb") as page:
                for chunk in resp.iter_content(100000):
                    page.write(chunk)

    except Exception as exc:
        logging.error(f"webpage download error [{exc}]")
        sys.exit()

    sys.exit()

