import logging
import os
from datetime import datetime

# Generate a unique log file name based on the current date and time.
# The log file will have a timestamp in the format: "YYYY-MM-DD_HH-MM-SS.log"
log_file = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# Construct the path for the logs directory.
# Logs will be stored in a folder named "logs" in the current working directory.
logs_path = os.path.join(os.getcwd(), "logs")

# Ensure that the logs directory exists.
# If the directory does not exist, it will be created (including any necessary parent directories).
os.makedirs(logs_path, exist_ok=True)

# Generate the full path for the log file by combining the logs directory path and the log file name.
log_file_path = os.path.join(logs_path, log_file)

# Configure the logging system to write log messages to the generated log file.
logging.basicConfig(
    filename=log_file_path,  # Specify the file where log messages will be saved.
    format='%(asctime)s - %(lineno)d %(name)s - %(levelname)s - %(message)s',  # Define the log message format.
    # Format components:
    #   %(asctime)s: Timestamp of the log message.
    #   %(lineno)d: Line number in the code where the log call was made.
    #   %(name)s: Logger's name (usually 'root' unless explicitly named).
    #   %(levelname)s: Severity level of the log message (e.g., INFO, WARNING, ERROR).
    #   %(message)s: The actual log message text.
    level=logging.INFO  # Set the logging level to INFO or higher (INFO, WARNING, ERROR, CRITICAL).
)

# Example usage of logging (not part of the configuration code):
# logging.info("This is an info message.")
# logging.warning("This is a warning message.")
# logging.error("This is an error message.")



