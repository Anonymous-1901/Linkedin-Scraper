import json
from linkedin_api import Linkedin
import re

api = Linkedin("shadowgag1901@gmail.com","Shadow@1234_1901")

data = []
with open("jobs.json","r") as file:
    file_data = json.load(file)
    for d in file_data:
        if d["company_link"] != "not-found":
            data.append(d["company_link"]) 
data = list(set(data))
write_me_list = []
regex = r"(?<=\/company\/)[^\/\?]+"
for url in data:
    match = re.search(regex, url)
    if match:
        company_name = match.group()
    company_data = api.get_company(company_name)
    try:
        print(f"Company Name : {company_data['name']}\n")
    except UnicodeDecodeError:
        pass
    write_me = {}
    write_me["company_name"] = company_data['name']
    try:
        write_me["desc"] = company_data['description']
    except:
        write_me["desc"] = "none"
    write_me["employeeCount"] = str(company_data['staffCount'])
    write_me_list.append(write_me)

with open("company_info.json","w") as fw:
    json.dump(write_me_list,fw,indent=4)