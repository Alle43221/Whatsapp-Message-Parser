import json
from datetime import datetime

source_file=input("Enter source file name: ")
destination_file=input("Enter destination file name: ")

Myname=input("Enter you Whatsapp name: ")
Other=input("Enter other Whatsapp name: ")

f=open(source_file,encoding="utf8")
g=open(destination_file, 'w',encoding="utf8")

Lines = json.load(f)
#print(len(Lines["chats"][0]["messages"]))
for i in Lines["chats"][0]["messages"]:
    string=""
    date =i["timestamp"]
    datetime_object = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
    string+=f"{datetime_object.day}/{datetime_object.month}/{datetime_object.year}, {datetime_object.hour}:{datetime_object.minute} - "
    if i["fromMe"]==True:
        string+=Myname + ': '
    else:
        string += Other + ': '
    if "type" in i:
        if i["type"]=="text":
            string += i["text"]
        else:
            string += "<Media omitted>"
    g.write(string+"\n")
f.close()
g.close()