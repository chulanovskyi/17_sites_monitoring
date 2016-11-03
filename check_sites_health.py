import os
import datetime
import argparse
import json

import requests
import whois


EXPIRE_SOON_DAYS = 30


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    return parser


def load_urls4check(path):
    with open(path) as url_file:
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


def create_unsafe_file(urls):
	with open('unsafe_domains.txt', 'w') as unsafe:
		unsafe.write(json.dumps(urls))


if __name__ == '__main__':
    arg_parser = create_parser()
    urls_path = arg_parser.parse_args().path
    urls = load_urls4check(urls_path)
    unsafe_urls = list()
    for domain in urls.split():
        alive = is_server_respond_with_200(domain)
        expire_soon = is_domain_expire_soon(domain)
        if alive and not expire_soon:
            continue
        else:
        	unsafe_urls.append({
        		'name': domain,
        		'alive': alive,
        		'expire': expire_soon})
    if unsafe_urls:
    	create_unsafe_file(unsafe_urls)
    	print('Domain list is unsafe, check details')
    else:
    	print('Domain list is OK')
