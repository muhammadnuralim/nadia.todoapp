import os
from dotenv import load_dotenv
from datetime import timedelta

basedir = os.path.dirname(__file__)
print(os.path.join(basedir, '.env'))
load_dotenv()