"""
Fix the following buggy code.
Try add this to your remote repo once you are done.
"""

# LOGGING STUFF START; this is for debugging purposes.
###################################################################################################
import logging

# create a module-level logger with "getLogger"

logging.basicConfig(
    filename='discussion06.log',  # create file with the name "hw3.log" and store logging info there
    level=logging.DEBUG,   # This prints log information in debug mode (useful for developers)
    filemode='w',   # overwrite the log file every time this script is run
    format='%(name)-12s: %(levelname)-8s %(message)s',  # include the log name, log type "DEBUG", and the log message
    )

logger = logging.getLogger(__name__)

'''Use these instead of print statements
logging.debug() # for developers
logging.info() # general information, usually to track progress
logging.warning() # something unexpected but still able to run
logging.error() # issues that affects the proper functioning
logging.critical() # severe problem
'''
    
###################################################################################################
# LOGGING STUFF END.

if __name__ == '__main__':  # if we are executing this script ('main') by itself
	keep_going = True
	while keep_going:  # while loop ensures continuous operation
		### FIXME what happens if you enter something that isn't an int?
		num1 = input('Enter numerator >> ')
		num2 = input('Enter denominator >> ')
		
		if isinstance(num1, int):
			raise ValueError(f'numerator must be an integer: num1 = {num1}')
		if isinstance(num2, int):
			raise ValueError(f'denominator must be an integer: num2 = {num2}')
		if num2 == 0:
			raise ZeroDivisionError(f"Division by zero error; denominator shouldn't be zero! (num2 = {num2})")
		### FIXME what happens if denom is 0?
		try:
			num1 = int(num1)
			num2 = int(num2)
			print(num1, '/', num2, '=', num1/num2)
		except ValueError:
			print("ValueError: Input does not include integers.")
			logger.error(f"Input does not include integers.")
		except ZeroDivisionError:
			print("ZeroDivisionError; denominator shouldn't be zero! (num2 = {num2})")
			logger.error(f"ZeroDivisionError; denominator shouldn't be zero! (num2 = {num2})")
		### FIXME write the inputs/outputs and any errors encountered
		### to a log file	

		### FIXME is this the best way to do this?
		### Should we be checking inputs?
		### What if something not y/n is entered?
		end = True
		while end == True:
			rerun = input('Keep going? [Y/n] >> ')
			if rerun not in ['Y', 'y', 'N', 'n']:
				print("Invalid response. Type 'Y' to continue or 'N' to exit.")
			if rerun in ['Y', 'y']:
				end = False
			if rerun in ['N', 'n']:
				keep_going = False
				end = False
