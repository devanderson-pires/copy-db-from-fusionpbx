from datetime import datetime

def clean_string(str):
    if(str != None):
        return str.replace("%20", " ").replace("%3A", ":")

    return ""

def string_to_date(str):
    if(str != ""):
        return datetime.strptime(str, "%Y-%m-%d %H:%M:%S")

    return ""
