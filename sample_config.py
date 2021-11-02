HEROKU = True # Make it False if you're not deploying on heroku.

if HEROKU:
    from os import environ

    bot_token = environ["bot_token"]
    API_ID = environ["API_ID"]
    HASH_ID = environ["HASH_ID"]
    bot_id = environ["bot_id"]
    owner_id = environ["owner_id"]
  

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:

    bot_token = "1976157545:AAFC5NmwiA420TnIygkf9piYs"
    API_ID = environ["API_ID"]
    HASH_ID = environ["HASH_ID"]
    bot_id = environ["bot_id"]
    owner_id = environ["owner_id"]
