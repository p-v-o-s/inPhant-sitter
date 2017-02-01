import os, time

from twilio.rest import TwilioRestClient

import SECRET_CONFIG as config

twilio_client = TwilioRestClient(config.twilio['account_sid'],config.twilio['auth_token'])

d = {}
try:
    while True:
        info = os.popen("ps -eo pcpu,pmem,pid,user,args | grep \"\\sdwblair\\s\" | grep \"phant\"").read()
        data = info.strip().split()
        d['cpu'] = float(data[0])
        d['mem'] = float(data[1])
        d['pid'] = int(data[2])
        print(d)
        if d['cpu'] >= 5 or d['mem'] >= 50:
            print("Killing process pid=%d" % d['pid'])
            print(os.popen("kill %d" % d['pid']).read())
            twilio_client.messages.create(to    = config.twilio['my_number'],
                                          from_ = config.twilio['my_number'],
                                          body  = "inPhant-sitter.watch.py: killed at: %r" % d,
                                         )
        time.sleep(10)
except KeyboardInterrupt:
    print("exiting...")
