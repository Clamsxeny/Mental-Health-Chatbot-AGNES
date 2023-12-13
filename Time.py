from datetime import datetime

def gettime():
    current_time = datetime.now()
    formatted_date = current_time.strftime("%d/%m/%Y")
    formatted_time = current_time.strftime("%H:%M:%S")
    return f"Day today: {formatted_date}\nCurrent time: {formatted_time}"