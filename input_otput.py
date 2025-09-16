import os

def convert(num):
    for x in["bytes", "KB", "MB", "GB", "TB"]:
        if num < 1024.0:
            return "%3.if %s" %(num,x)
        num /=1024.0

def file_size(file_path):
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert(file_info.st_size)
    
file_path = r"C:\Users\Public\Desktop\Google Chrome.lnk"

print(file_size(file_path))
