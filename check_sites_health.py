import requests
import argparse
import datetime
from whois import whois


EXPIRE_SOON_DAYS = 30


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    return parser


def load_urls4check(path):
    with open(path, encoding='utf-8') as url_file:
        return url_file.read()


def is_server_respond_with_200(url):
    response = requests.get('http://%s' % url)
    return response.status_code == 200


def is_domain_expire_soon(domain_name):
    domain_info = whois(domain_name)
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


if __name__ == '__main__':
    parser = create_parser()
    path = parser.parse_args().path
    urls = load_urls4check(path)
    for url in urls.split():
        print('-'*20)
        print(url)
        print('Is alive: %s' % is_server_respond_with_200(url))
        print('Expire soon: %s' % is_domain_expire_soon(url))
