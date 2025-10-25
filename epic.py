from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional

import requests

from dataclasses import dataclass
from typing import List, Optional

#unlock_expired_documents()

geo_data = requests.get("http://ip-api.com/json/").json()

latitude = geo_data["lat"]
longitude = geo_data["lon"]
timezone_id = geo_data["timezone"]
language_code = geo_data["countryCode"].lower()  # e.g., 'us' -> 'en-US'

def is_stream_online(username):
    """
    Returns True if the Twitch stream is online, False otherwise.
    Uses the public frontend Client-ID (no OAuth).
    """
    url = f"https://www.twitch.tv/{username}"
    headers = {
        "Client-ID": "kimne78kx3ncx6brgo4mv6wki5h1ko",  # Publicly known Client-ID
    }
    resp = requests.get(url, headers=headers)
    return "isLiveBroadcast" in resp.text
with SB(uc=True, test=True,locale=f"{language_code.upper()}") as yopyeaseyoi:
    yopyeaseyoi.execute_cdp_cmd(
        "Emulation.setGeolocationOverride",
        {
            "latitude": latitude,
            "longitude": longitude,
            "accuracy": 100
        }
    )
    yopyeaseyoi.execute_cdp_cmd(
        "Emulation.setTimezoneOverride",
        {"timezoneId": timezone_id}
    )

    if is_stream_online("gizewashere"):
        url = "https://www.twitch.tv/gizewashere"
        yopyeaseyoi.uc_open_with_reconnect(url, 5)
        try:
            if yopyeaseyoi.is_element_present('button:contains("Accept")'):
                yopyeaseyoi.uc_click('button:contains("Accept")', reconnect_time=4)
            if True:
                yopyeaseyoi2 = yopyeaseyoi.get_new_driver(undetectable=True)
                yopyeaseyoi2.uc_open_with_reconnect(url, 5)
                yopyeaseyoi.sleep(10)
                if yopyeaseyoi2.is_element_present('button:contains("Accept")'):
                    yopyeaseyoi2.uc_click('button:contains("Accept")', reconnect_time=4)
        except:
            print("error happened")
            while is_stream_online("gizewashere"):
                yopyeaseyoi.sleep(100)
            yopyeaseyoi.quit_extra_driver()
    yopyeaseyoi.sleep(1)

