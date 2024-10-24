import logging
import os
from datetime import datetime 

# Creating the log file dynamically with the current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Correctly calling os.getcwd() function
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)


# Creating the 'logs' directory if it doesn't exist
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

# Defining the log file path
LOG_FILE_PATH = os.path.join(logs_path)

# Configuring the logging setup
logging.basicConfig(
    filename=LOG_FILE_PATH
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    
)



'''
Notes :

if we want to set the mutliple logger use the 

logger1 = logging.getLogger("logger1")
loggerl.setLevel(logging.Level_name)

if in basic configuaration handler is set to console and file handler then ne need to add the console handler for the logger1



'''