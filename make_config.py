import json
import os

config = {
    "accounts": [
        {
            "username": os.environ.get("MS_EMAIL", ""),
            "password": os.environ.get("MS_PASSWORD", "")
        }
    ],
    "baseURL": "https://rewards.bing.com",
    "sessionPath": "sessions",
    "headless": True,
    "runOnZeroPoints": False,
    "clusters": 1,
    "saveFingerprint": {"mobile": False, "desktop": False},
    "workers": {
        "doDailySet": True,
        "doMorePromotions": True,
        "doPunchCards": True,
        "doDesktopSearch": True,
        "doMobileSearch": True
    },
    "searchSettings": {
        "useGeoLocaleQueries": False,
        "scrollRandomly": True,
        "scrollDelay": 2000,
        "searchDelay": 3000,
        "retryMobileSearchAmount": 0
    },
    "globalTimeout": 30,
    "enabled": True,
    "debugLogs": False,
    "proxy": None,
    "consoleLogFilter": None,
    "webhook": None
}

with open("dist/config.json", "w") as f:
    json.dump(config, f, indent=2)

print("config.json created!")
