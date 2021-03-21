from datetime import datetime

def clean_string(str):
    return str.replace("%20", " ").replace("%3A", ":")

def string_to_date(str):
    return datetime.strptime(str, "%Y-%m-%d %H:%M:%S")