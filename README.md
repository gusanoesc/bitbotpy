# Bitbucket WebHook Updates Telegram Bot

### Original Author: [Adityatelange](https://github.com/adityatelange/bitbucket-telegram-bot-webhook)


## Introduction

This telegram bot uses webhooks to integrate applications with Bitbucket Cloud. [Webhook Documentation](https://confluence.atlassian.com/bitbucket/manage-webhooks-735643732.html)


## Setup

Bot must be hosted on server with having a domain name or an IP to work.

Webhooks do not work via polling method.


## Requirements

```
- python3
- pip3
- flask
- telepot
- A Telegram Bot
```


## Manual Installation

```bash
$ # git clone https://github.com/AdityaTelange/bitbucket-telegram-bot-webhook (Original source - deprecated)
$ git clone https://github.com/gusanoesc/bitbotpy.git
$ cd bitbotpy
$ pip3 install --user -r requirements.txt
```

**Edit *config.py* file**

```python
TOKEN='<bot_token_obtained_from_bot_father>'
OWNER_ID=None
NOTIFY_GRP_IDS = [
    xxxxxxxxx,
    -yyyyyyyyy
]
```


**Sample**

```python
TOKEN='xxxxxxxxx:qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq'
OWNER_ID=123456789
NOTIFY_GRP_IDS = [
    123456789,
    -123456789,
    -987645321
]
```


## Adding webhook to Bibucket Repo

1. Repository-settings => Webhooks (under Workflow) => Add Webhook

2. Fill in Details
    - Title: 'title'
    - URL: https://your_domain.com/bitbucket

3. Choose _Triggers_ and other Info.

4. *Save*


## Run

```python3
$ python3 ./server.py
```
--- 

## Docker Installation

You need Docker and Docker-compose previously installed.

```bash
$ cd bitbotpy
$ docker build -t bitbotpy:latest .
$ # docker run --rm  -p 80:80 --name bitbotpy bitbotpy:latest
$ docker-compose up -d
```

---

## Done !!!

Add your bot to groups and fill group id's into config.py

Now any of the selected Triggers will send you a message!


**Note: If you have a firewall or need more security, add only the CIDR list of bitbucket endpoints to your infrastructure:** [Bitbucket WhiteList](https://support.atlassian.com/bitbucket-cloud/docs/what-are-the-bitbucket-cloud-ip-addresses-i-should-use-to-configure-my-corporate-firewall/)
