import os, time

from twilio.rest import TwilioRestClient

import SECRET_CONFIG as config

twilio_client = TwilioRestClient(config.twilio['account_sid'],config.twilio['auth_token'])


twilio_client.messages.create(to    = config.twilio['number_cversek'],
                              from_ = config.twilio['number_main'],
                              body  = "inPhant-sitter.twilio_test",
                             )
