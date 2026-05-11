import json, os

config = {
    "baseURL": "https://rewards.bing.com",
    "sessionPath": "sessions",
    "headless": True,
    "parallel": False,
    "runOnZeroPoints": False,
    "clusters": 1,
    "globalTimeout": "30s",
    "searchOnBingLocalQueries": False,
    "workers": {
        "doDailySet": True,
        "doMorePromotions": True,
        "doPunchCards": True,
        "doDesktopSearch": True,
        "doMobileSearch": True,
        "doDailyCheckIn": True,
        "doReadToEarn": True
    },
    "searchSettings": {
        "useGeoLocaleQueries": False,
        "scrollRandomResults": True,
        "clickRandomResults": True,
        "searchDelay": {"min": "3min", "max": "5min"},
        "retryMobileSearchAmount": 0
    },
    "proxy": {
        "url": "",
        "port": 0,
        "username": "",
        "password": ""
    },
    "consoleLogFilter": {"mode": "blacklist", "keywords": []},
    "webhook": {
        "enabled": False,
        "url": "",
        "webhookLogFilter": {"mode": "blacklist", "keywords": []}
    }
}

with open("dist/config.json", "w") as f:
    json.dump(config, f, indent=2)

accounts = [{"email": os.environ.get("MS_EMAIL", ""), "password": os.environ.get("MS_PASSWORD", "")}]

with open("dist/accounts.json", "w") as f:
    json.dump(accounts, f, indent=2)

print("Done!")
