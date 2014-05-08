'''
Configuration Settings

Includes keys for Twilio, etc.  Second stanza intended for Heroku deployment.
'''

# Uncommet to configure in file.
ACCOUNT_SID = "AC54bc9a152121d16d5fe470c1ce5f3b5b"
AUTH_TOKEN = "f423f07096e9eefd87fd59de6941cfc2"
BSSSPAM_APP_SID = "APeeddbea601f6215535ecc184ee0308f1"
BSS_SPAM_ID = "+19733102275"


# Begin Heroku configuration - configured through environment variables.
import os
ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
BSSSPAM_APP_SID = os.environ['BSSSPAM_APP_SID']
BSS_SPAM_ID = os.environ['BSS_SPAM_ID']
