import sys
from src.logger import logging


def error_message_detail(error,error_detail:sys):
    """
    Function to print detailed error message with line number and error message.
    """
    
    _,_,exc_tb=error_detail.exc_info()
    file_name =exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script [{0}] line number[{1}] error message [{2}]".format(file_name, exc_tb.tb_lineno, str(error))

    return error_message

class CustomException(Exception):
    '''
    class CustomException: This defines a new exception class that inherits from Python's built-in Exception class.
    Purpose: It allows you to raise and handle exceptions with additional context or customization.



    '''
    def __init__(self,error_message,error_detail:sys):


        '''__init__ Method: This is the constructor for the CustomException class.
        Parameters:
        error_message: A message describing the error.
        error_detail: sys: A parameter intended to pass additional details about the error, particularly system-related information (like traceback or exception type).
        super().__init__(error_message): This calls the constructor of the parent Exception class, initializing the error message as part of the base exception.
        '''

        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    

