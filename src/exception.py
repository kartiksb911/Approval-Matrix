import sys
import logging

# define a function where we call try block(tb) , file name , error(except_block)
def error_msg_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() # (error_detail = sys) gives information about the exception
    file_name = exc_tb.tb_frame.f_code.co_filename # exception tryblock ,frame by frame(one by one),folder by folder,file by file
    error_message ="Error occured in your python script name [{0}],line[{1}],error message[{2}]".format(
        file_name , exc_tb.tb_lineno, str(error)
    )
    return error_message


# define a class where 2 arguments error_message(exception as e) and error_details(sys)
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_msg_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message    