# 17_sites_monitoring

###Prerequisites:

Run in console `pip install -r requirements.txt` to install 3rd party modules.

---

Script will help you to check if site is alive (HTTP status code 200) 
and its prepaid domain name expiration date more than 1 month.

###How to use:

Script takes one required argument:
- `path` - path to text file with domain names;

```
**Note!** In text file domain names should be separated with spaces or new lines.
```
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
###Example:

**urls.txt** data:
```
devman.org
github.com
vk.com
```
####INPUT
`python check_site_health.py urls.txt`

####OUPUT
```
--------------------
devman.org
Is alive: True
Expire soon: False
--------------------
github.com
Is alive: True
Expire soon: False
--------------------
vk.com
Is alive: True
Expire soon: False
```
