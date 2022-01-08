CLIENT_ID = "582df9b8688b4835bb40c4ace30f78fc"
CLIENT_SECRET = "da0a7a2013cb4481becdedd90db8c011"
API_ID = 7981256
API_HASH = "4afb49d88945d5cd3e4891ff3dcee58f"
INITIAL_TOKEN = "AQCl3VZD-s4DGDTS-45j7yZ5EBeNc_XwQ40sRGG4JCmyFolHRagFbBMG4k-8ELz2uYyUeXMhtZTDZAjD7JGQbQB_aRMnYnfVWKxsvH5WN-P1yMvQHYluYhr9QydRVYCF80t1t0Sb_XFNpEndCC0KRv3x9Mwnnm1DCRmv_wONQk-9AoRolcv2tLZwmvurxT6j0M6a7Sf8dV_T2ri7YodsF-g_I3t1q79jlGv6Tu0i3rnHfzHfiObm"
INITIAL_BIO = "on a vacation"
LOG = "me"
# the escaping is necessary since we are testing against a regex pattern with it.
SHUTDOWN_COMMAND = "\/\/stop"
# The key which is used to determine if the current bio was generated from the bot ot from the user. This means:
# NEVER use whatever you put here in your original bio. NEVER. Don't do it!
KEY = '🎶'
# The bios MUST include the key. The bot will go though those and check if they are beneath telegrams character limit.
BIOS = [KEY + ' Now Playing: {interpret} - {title} {progress}/{duration}',
        KEY + ' Now Playing: {interpret} - {title}',
        KEY + ' : {interpret} - {title}',
        KEY + ' Now Playing: {title}',
        KEY + ' : {title}']
# Mind that some characters (e.g. emojis) count more in telegram more characters then in python. If you receive an
# AboutTooLongError and get redirected here, you need to increase the offset. Check the special characters you either
# have put in the KEY or in one of the BIOS with an official Telegram App and see how many characters they actually
# count, then change the OFFSET below accordingly. Since the standard KEY is one emoji and I don't have more emojis
# anywhere, it is set to one (One emoji counts as two characters, so I reduce 1 from the character limit).
OFFSET = 1
# reduce the OFFSET from our actual 70 character limit
LIMIT = 70 - OFFSET
