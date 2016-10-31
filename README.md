# 17_sites_monitoring

###Prerequisites:

Run in console `pip install -r requirements.txt` to install 3rd party modules.

---

Script will help you to check if site is alive (HTTP status code 200) 
and its prepaid domain name expiration date more than 1 month.

###How to use:

Script takes one required argument:
- `path` - path to text file with domain names;

**Note!** Domain names in domain list file should be separated with spaces or new lines.

*Good structure:* 
```
devman.org github.com vk.com
```
*Good structure:*
```
devman.org
github.com
vk.com
```
**_Not valid structure:_**
```
devman.org; http://github.com | vk.com
```

---

###Example:

**urls.txt** data:
```
devman.org
github.com
vk.com
someothersite.com
facebook.con
```
####INPUT
`python check_site_health.py urls.txt`

####OUPUT
- If all domains in file are alive and won't expire soon then you should see:
`Domain list is OK`
- If some domains are don't fit the conditions above then their status will be saved
in file called 'unsafe_domains.txt'.

**unsafe_domains.txt** data:
```
--------------------
someothersite.com
Is alive: False
Expire soon: None
--------------------
facebook.con
Is alive: False
Expire soon: None
```


Что не так

> unsafe_domain_file = open('unsafe_domains.txt', 'w+')
> направление мысли правильное, реализация плохая. Перенаправление stdout и stderr - это прерогатива вызывающей программы. Не надо делать это за нее.
смотрю решил идти другим путем ... Ну ок

def print_result():
try:
os.stat('unsafe_domains.txt')
print('Domain list is unsafe, check details')
except FileNotFoundError:
print('Domain list is OK')
вот это просто звиздец...

for domain in urls.split():
if not unsafe_file_created:
with open('unsafe_domains.txt', 'w') as unsafe:
unsafe_file_created = True
with open('unsafe_domains.txt', 'a') as unsafe:
# ....
а вот это вообще за гранью

свяжись со мной в slack @pelid
