# هنا هعمل هثبت المكتبات ال محتاجينها وهعمل استدعاء ليها
#from unittest import result
from sys import excepthook

import requests
import bs4
import csv
from itertools import zip_longest
job_title=[]
company_name=[]
location_name=[]
job_skill=[]
date=[]
links=[]
#هنا بعمل طلب على شان ادخل على اللنك واحفظ الصفحة
page_num=0
while True:
    url = f"https://wuzzuf.net/search/jobs/?a=hpb&q=e-marketer&start={page_num}"
    result = requests.get(url)
    src = result.content

    #print(src)

    #هنا هنعمل اوبجت جديد  على شان نقدر نفصل فى المعلومات ال طالعة (parse content)

    soup = bs4.BeautifulSoup(src, "lxml")
    #print(soup)
    page_limit=int(soup.find("strong").text)
    if(page_num>page_limit//15):
        print("page ended, terminate")
        break
    # هنطلع الحاجات ال محتاجنها من الصفة مثل اسم الوظيفة ,اسم الشركة , الموقع , المهارات المطلوبة , وقت الطرح

    job_titles=soup.find_all("h2",{"class":"css-m604qf"})
    #print(job_title)

    company_names=soup.find_all("a",{"class":"css-17s97q8"})
    #print(campany_name)

    locations_names=soup.find_all("span",{"class":"css-5wys0k"})
    #print(locations_name)


    job_skills=soup.find_all("div",{"class":"css-y4udm8"})
    #print(job_skills)

    posteds_old=soup.find_all("div",{"class":"css-do6t5g"})
    posteds_new=soup.find_all("div",{"class":"css-4c4ojb"})
    posted=[*posteds_new,*posteds_old]
    #هنا هنعمل لوب على شان نلف فى الكونتت كلها ونستخرج ال احنا محتاجينه منها

    for i in range(len(job_titles)):
        job_title.append(job_titles[i].text)
        links.append("https://wuzzuf.net"+job_titles[i].find("a").attrs['href'])
        company_name.append(company_names[i].text)
        location_name.append(locations_names[i].text)
        job_skill.append(job_skills[i].text)
        date.append(posted[i].text)
    f_list = [job_title, company_name, date, location_name, job_skill, links]  # """هنا هنعمل حاجة اسمعها ان باكنج"""

    for all in zip(*f_list):
        print(all)
    page_num+=1
    print("\npage switched\n")

#print(posted)

# print(job_title)
# print("\n")
# print(company_name)
# print("\n")
# print(locations_name)
# print("\n")
# print(job_skil ls)

#هنا هنخزن المعلومات ال اتستخرجنها ونملى بيها الفايل الخاص بنا


exp=zip_longest(*f_list)
with open("D:\تالتة حاسبات\python\python3.csv","w") as thefile:
    wrr=csv.writer(thefile)
    wrr.writerow(["job title","company name", "date","location","skills","links"])
    wrr.writerows(exp)

