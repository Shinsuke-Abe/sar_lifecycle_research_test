import os

def hello(event, context):
    return {
        "message": "This function for research repository lifecycle",
        "event": "hello!",
        "database": os.environ['HELLO_TABLE'] 
    }
