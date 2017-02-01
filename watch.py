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
        if d['cpu'] >= config.watch['cpu_limit'] or d['mem'] >= config.watch['mem_limit']:
            print("Killing process pid=%d" % d['pid'])
            print(os.popen("kill %d" % d['pid']).read())
            twilio_client.messages.create(to    = config.twilio['number_cversek'],
                                          from_ = config.twilio['number_main'],
                                          body  = "inPhant-sitter_watch_py: killed at: %r" % d,
                                         )
        time.sleep(10)
except KeyboardInterrupt:
    print("exiting...")
