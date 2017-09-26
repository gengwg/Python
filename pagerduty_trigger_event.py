#!/usr/bin/env python

import sys
import json
import requests
import urllib3

urllib3.disable_warnings()


def trigger_incident(SV_SERVICE_KEY, DESCRIPTION):
    headers = {
        "Content-type": "application/json",
        "Accept": "application/json"
    }
    payload = json.dumps({
        "service_key": SV_SERVICE_KEY,
        "event_type": "trigger",
        "description": DESCRIPTION,
    })
    r = requests.post(
        'https://events.pagerduty.com/generic/2010-04-15/create_event.json',
        headers=headers,
        data=payload,
    )
    print r.status_code
    print r.text


def main(service_key, desc):
    trigger_incident(service_key, desc)


if __name__ == '__main__':
    if not sys.argv[1]:
        print ("pagerduty service key required")
        sys.exit(1)
    main(service_key=sys.argv[1], desc=sys.argv[2])
