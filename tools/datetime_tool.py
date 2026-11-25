from datetime import datetime
def get_datetime():

    current_datetime = datetime.now()

    result = {
        "date": current_datetime.strftime("%d-%m-%Y"),
        "time": current_datetime.strftime("%I:%M:%S %p"),
        "day": current_datetime.strftime("%A")
    }

    return result
