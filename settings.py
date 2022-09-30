import os
import dotenv

"""All data should be initialized in the .env file"""

dotenv.load_dotenv('.env')
LOGIN_STANDARD = os.environ['LOGIN_STANDARD']
LOGIN_LOCKED = os.environ['LOGIN_LOCKED']
LOGIN_PROBLEM = os.environ['LOGIN_PROBLEM']
LOGIN_GLITCH = os.environ['LOGIN_GLITCH']
LOGIN_LIST = [LOGIN_STANDARD, LOGIN_LOCKED, LOGIN_PROBLEM, LOGIN_GLITCH]
PASSWORD = os.environ['PASSWORD']
TOKEN = os.environ['TOKEN']
