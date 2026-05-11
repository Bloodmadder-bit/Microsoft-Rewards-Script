import json, os

config = {
        "baseURL": "https://rewards.bing.com",
        "sessionPath": "sessions",
        "headless": True,
        "clusters": 1,
        "errorDiagnostics": False,
        "workers": {
                    "doDailySet": True,
                    "doSpecialPromotions": True,
                    "doMorePromotions": True,
                    "doPunchCards": True,
                    "doAppPromotions": True,
                    "doDesktopSearch": True,
                    "doMobileSearch": True,
                    "doDailyCheckIn": True,
                    "doReadToEarn": True
        },
        "searchOnBingLocalQueries": False,
        "globalTimeout": "30sec",
        "searchSettings": {
                    "scrollRandomResults": True,
                    "clickRandomResults": True,
                    "parallelSearching": False,
                    "queryEngines": ["google", "wikipedia", "reddit", "local"],
                    "searchResultVisitTime": "10sec",
                    "searchDelay": {"min": "30sec", "max": "1min"},
                    "readDelay": {"min": "30sec", "max": "1min"}
        },
        "debugLogs": False,
        "proxy": {
                    "queryEngine": False
        },
        "consoleLogFilter": {
                    "enabled": False,
                    "mode": "blacklist",
                    "keywords": []
        },
        "webhook": {
                    "discord": {
                                    "enabled": False,
                                    "url": ""
                    },
                    "ntfy": {
                                    "enabled": False,
                                    "url": "",
                                    "topic": "",
                                    "token": "",
                                    "title": "Microsoft-Rewards-Script",
                                    "tags": ["bot", "notify"],
                                    "priority": 3
                    },
                    "webhookLogFilter": {
                                    "enabled": False,
                                    "mode": "blacklist",
                                    "keywords": []
                    }
        }
}

with open("dist/config.json", "w") as f:
        json.dump(config, f, indent=2)

accounts = [{
        "email": os.environ.get("MS_EMAIL", ""),
        "password": os.environ.get("MS_PASSWORD", ""),
        "totpSecret": "",
        "recoveryEmail": "",
        "geoLocale": "auto",
        "langCode": "en",
        "proxy": {
                    "proxyAxios": False,
                    "url": "",
                    "port": 0,
                    "username": "",
                    "password": ""
        },
        "saveFingerprint": {
                    "mobile": False,
                    "desktop": False
        }
}]

with open("dist/accounts.json", "w") as f:
        json.dump(accounts, f, indent=2)

print("Done!")
