import requests
import argparse
import datetime
import whois
import os
from contextlib import redirect_stdout


EXPIRE_SOON_DAYS = 30


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    return parser


def load_urls4check(path):
    with open(path, encoding='utf-8') as url_file:
        return url_file.read()


def is_server_respond_with_200(url):
    try:
        response = requests.get('http://%s' % url)
    except requests.ConnectionError:
        return False
    return response.status_code == 200


def is_domain_expire_soon(domain_name):
    try:
        domain_info = whois.whois(domain_name)
    except whois.parser.PywhoisError:
        return
    try:
        relative, precise = domain_info.expiration_date
        expire_date = relative
    except TypeError:
        expire_date = domain_info.expiration_date
    if not expire_date:
        return
    today = datetime.date.today()
    expire_delta = today + datetime.timedelta(days=EXPIRE_SOON_DAYS)
    return expire_delta >= expire_date.date()


def print_result():
    if not os.stat('unsafe_domains.txt').st_size:
        print('Domain list is unsafe, check details')
        return
    print('Domain list is OK')

if __name__ == '__main__':
    arg_parser = create_parser()
    urls_path = arg_parser.parse_args().path
    urls = load_urls4check(urls_path)
    unsafe_domain_file = None
    for domain in urls.split():
        alive = is_server_respond_with_200(domain)
        expire_soon = is_domain_expire_soon(domain)
        if alive and not expire_soon:
            continue
        else:
            if not unsafe_domain_file:
                unsafe_domain_file = open('unsafe_domains.txt', 'w+')
            with redirect_stdout(unsafe_domain_file):
                print('-' * 20)
                print(domain)
                print('Is alive: %s' % alive)
                print('Expire soon: %s' % expire_soon)
    print_result()
