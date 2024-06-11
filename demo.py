# CODE FOR TEST LOGGING
#from US_Visa.logger import logging
#logging.info("Testing logging file")

''' 
# CODE FOR TESTING EXCEPTION

from US_Visa.logger import logging
from US_Visa.exception import USvisaException
import sys

try:
    a = 1 / "10"
except Exception as e:
    logging.info(e)
    raise USvisaException(e,sys) from e
'''

'''
## If we want to import from constants then

from US_Visa.constants import *

print('DATABASE_NAME')

'''
