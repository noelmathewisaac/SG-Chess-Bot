import requests
import logging
import json
from datetime import datetime
import re
from calendar import month_name
from bs4 import BeautifulSoup,element

class Scraper():
            
    def sgca_scraper(self):
        """Function to scrape tournament data from chessacademysg.com"""
        source=requests.get('https://chessacademysg.com/')
        soup=BeautifulSoup(source.text, 'html.parser')
        posts=soup.find_all('article')

        links=[]
        event_date=[]
        deadline_date=[]
        text=[]
        title=[]
        event_link=[]
        parent=[] 

        for i in range(len(posts)):
            links.append("")
            links[i]=posts[i].a['href']
           
        for i in links:
            try:
                source=requests.get(i)
                soup=BeautifulSoup(source.text, 'html.parser')
                x=soup.find_all('div',{'class':'entry-content'})
                y=x[0].contents
                for tags in y:
                    try:
                        contents=tags.contents
                    except:
                        contents=[]
                    for num,content in enumerate(contents):
                        try:
                            if(type(content) == element.Tag):
                                content=content.text
                            content=content.replace('amp&;','')
                            content=content.strip()

                            if(re.search("Closing Date",content,re.IGNORECASE)):
                                if(len(content)<=20):

                                    if(type(contents[num+1])==element.Tag):
                                        contents[num+1]=contents[num+1].text
                                    contents[num+1]=contents[num+1].replace('amp&;','')
                                    contents[num+1]=contents[num+1].strip()
                                    temp=content+contents[num+1]

                                    if(len(contents[num+1])<=15):                                
                                        if(type(contents[num+2])==element.Tag):
                                            contents[num+2]=contents[num+2].text
                                        contents[num+2]=contents[num+2].replace('amp&;','')
                                        contents[num+2]=contents[num+2].strip()
                                        temp+= contents[num+2]

                                        if(len(contents[num+2])<=5):
                                            if(type(contents[num+3])==element.Tag):
                                                contents[num+3]=contents[num+3].text
                                            contents[num+3]=contents[num+3].replace('amp&;','')
                                            contents[num+3]=contents[num+3].strip()
                                            temp+= contents[num+3]

                                elif(len(content)>=500):
                                    temp_arr=content.split('\n')
                                    for el in temp_arr:
                                        if(re.search("Closing Date",el,re.IGNORECASE)):
                                            temp=el
                                else:
                                    temp=content

                                deadline_date.append(temp)
                                z=soup.find('h1',{'class':'entry-title'})
                                title.append(z.text.strip())
                                event_link.append(i)

                            if(re.search("Date & Time",content,re.IGNORECASE)): 

                                if(len(content)<=20):
                                    if(type(contents[num+1])==element.Tag):
                                        contents[num+1]=contents[num+1].text
                                    contents[num+1]=contents[num+1].replace('amp&;','')
                                    contents[num+1]=contents[num+1].strip()
                                    temp=content+contents[num+1]

                                elif(len(content)>=500):
                                    temp_arr=content.split('\n')
                                    for el in temp_arr:
                                        if(re.search("Date & Time",el,re.IGNORECASE)):
                                            temp=el
                                else:
                                    temp=content
                                event_date.append(temp)    

                        except:
                            print(content,'fail \n')
                            

            except:
                print(i,' failed')

        pattern=re.compile('([\sa-zA-Z0-9.]*Date & Time:|[\sa-zA-Z0-9.]*Closing Date:)')
        for i,j in enumerate(title):
            p=re.compile('([ ]{2,})')
            title[i]=p.sub(' ',title[i]).strip()
            event_date[i]=pattern.sub('',event_date[i]).strip()
            deadline_date[i]=pattern.sub('',deadline_date[i]).strip()

            #print(title[i],'\n',event_date[i],'\n',deadline_date[i],'\n',event_link[i],'\n-------------\n')
        return(title,event_date,deadline_date,event_link)
        
    def scraper(self):
        #Todo: Refactor Code

        source=requests.get('https://www.singaporechess.org.sg/events/local-events')
        soup=BeautifulSoup(source.text, 'html.parser')
        #source = open("html.html", "r")
        #soup=BeautifulSoup(source.read(),'lxml')

        #print("check")
        Event_name=soup.find_all('a',{'class':'eventtitle'})
        Links=soup.table.find_all('a',{"class":"eventtitle"})

        Event_date=[]
        for i in range(len(Event_name)):
            Event_name[i]=Event_name[i].text.strip()
            Links[i]="https://www.singaporechess.org.sg"+Links[i]['href']

        for h3 in soup.find_all('h3'):
            if(h3.next_sibling.strip()!=''):
                Event_date.append(h3.next_sibling.strip())
        
        deadline=soup.find_all('td')
        Event_deadline=[]
        temp=[]
        Deadline_month=[]
        Deadline_day=[]
        Deadline_year=[]
        Deadline_date=[]
        deadline_pattern = r'\b(?:by \d\d|entries|Registration Deadline)\b'
        deadline_pattern2 = r'\b(?:Registration Deadline)\b'

        def month_to_num(month_arr):        
            for i in range(0,len(month_arr),1):
                if(month_arr[i].lower()=="january" or month_arr[i].lower()=="jan"):
                    month_arr[i]='1'
                elif(month_arr[i].lower()=="february" or month_arr[i].lower()=="feb"):
                    month_arr[i]='2'
                elif(month_arr[i].lower()=="march" or month_arr[i].lower()=="mar"):
                    month_arr[i]='3'
                elif(month_arr[i].lower()=="april" or month_arr[i].lower()=="apr"):
                    month_arr[i]='4'
                elif(month_arr[i].lower()=="may"):
                    month_arr[i]='5'
                elif(month_arr[i].lower()=="june" or month_arr[i].lower()=="jun"):
                    month_arr[i]='6'
                elif(month_arr[i].lower()=="july" or month_arr[i].lower()=="jul"):
                    month_arr[i]='7'
                elif(month_arr[i].lower()=="august" or month_arr[i].lower()=="aug"):
                    month_arr[i]='8'
                elif(month_arr[i].lower()=="september" or month_arr[i].lower()=="sept" or month_arr[i].lower()=="sep"):
                    month_arr[i]='9'
                elif(month_arr[i].lower()=="october" or month_arr[i].lower()=="oct"):
                    month_arr[i]='10'
                elif(month_arr[i].lower()=="november" or month_arr[i].lower()=="nov"):
                    month_arr[i]='11'
                elif(month_arr[i].lower()=="december" or month_arr[i].lower()=="dec"):
                    month_arr[i]='12'
                else:
                    month_arr[i]=""
            return month_arr


        #Get event_deadline information
        for i in range(0,len(deadline),1):
            temp.append(deadline[i].find_all('p'))
            Event_deadline.append("")

        for i in range(0,len(deadline),1):
            for j in range(0,len(temp[i]),1):
                if(re.search(deadline_pattern, temp[i][j].text,re.IGNORECASE)!=None):
                    temp[i][j]=temp[i][j].text.replace("\xa0","",99)
                    Event_deadline[i]=Event_deadline[i]+temp[i][j]+' '                                         
            
        sgca=self.sgca_scraper()
        diff=len(Event_deadline)-len(Event_name)
        test=['']*diff
        Event_date=Event_date+test+sgca[1]
        Event_name=Event_name+test+sgca[0]
        Event_deadline=Event_deadline+sgca[2]
        Links=Links+test+sgca[3]

        for i in range(0,len(Event_deadline),1):
            Deadline_month.append("")
            Deadline_day.append("")
            Deadline_year.append("")
            Deadline_date.append("")

        pattern = "|".join(month_name[1:])
        Abb="|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec|closed"
        pattern=pattern+Abb
        for i in range(0,len(Event_deadline),1):
            try:
                if(Event_deadline[i]!=""):
                    Deadline_month[i]=re.search(pattern, Event_deadline[i], re.IGNORECASE).group(0)
                    if(re.search(pattern, Event_deadline[i], re.IGNORECASE).group(0).lower()!="closed"):
                        if(re.search("\d\d\d\d",Event_deadline[i])!=None):
                            Deadline_year[i]=re.search("\d\d\d\d",Event_deadline[i]).group(0)
                        else:
                            Deadline_year[i]=str(datetime.now().date().year)
                        Deadline_day[i]=re.search("\d\dst|\d\dnd|\d\drd|\d\dth|\dst|\dnd|\drd|\dth|\d\d\sJan|\d\d\sFeb|\d\d\sMar|\d\d\sApr|\d\d\sMay|\d\d\sJun|\d\d\sJul|\d\d\sAug|\d\d\sSep|\d\d\sOct|\d\d\sNov|\d\d\sDec|closed", Event_deadline[i],re.IGNORECASE).group(0)
                if(Deadline_day[i]!=""):
                    Deadline_day[i]=re.search("\d\d|\d", Deadline_day[i], re.IGNORECASE).group(0)        
            except:
                None

        Deadline_month = month_to_num(Deadline_month)        
            

        for i in range(0,len(Event_deadline),1):
            Deadline_day[i]=Deadline_day[i].replace(" ","")
            Deadline_month[i]=Deadline_month[i].replace(" ","")
            Deadline_year[i]=Deadline_year[i].replace(" ","")

        for i in range(0,len(Event_deadline),1):
            Deadline_date[i]=(Deadline_day[i]+"-"+Deadline_month[i]+"-"+Deadline_year[i])
            Deadline_date[i]=Deadline_date[i].replace("--","")
            if (Deadline_date[i]!=""):
                Deadline_date[i]=datetime.strptime(Deadline_date[i], '%d-%m-%Y')    

        Event_month,Event_day,Event_year,Tourney_date,Days_to_Tourney,Days_to_Deadline=([] for i in range (6))


        for i in range(0,len(Event_date),1):
            Event_month.append("")
            Event_day.append("")
            Event_year.append("")
            Tourney_date.append("")
            Days_to_Tourney.append("")
            Days_to_Deadline.append("")

            if(Event_date[i]!=''):
                Event_month[i]=re.search(pattern, Event_date[i], re.IGNORECASE).group(0)
                if(re.search(pattern, Event_date[i], re.IGNORECASE).group(0).lower()!="closed"):
                    if(re.search("\d\d\d\d",Event_date[i])==''):
                        Event_year=datetime.now().date().year()
                    else:
                        Event_year[i]=re.search("\d\d\d\d",Event_date[i]).group(0)
                    Event_day[i]=re.search("\d\dst|\d\dnd|\d\drd|\d\dth|\dst|\dnd|\drd|\dth|\d\d\sJan|\d\d\sFeb|\d\d\sMar|\d\d\sApr|\d\d\sMay|\d\d\sJun|\d\d\sJul|\d\d\sAug|\d\d\sSep|\d\d\sOct|\d\d\sNov|\d\d\sDec|\d\d|\d|closed", Event_date[i],re.IGNORECASE).group(0)
                    if(Event_day[i]!=""):
                        Event_day[i]=re.search("\d\d|\d", Event_day[i], re.IGNORECASE).group(0)       

        Event_month = month_to_num(Event_month)

        for i in range(0,len(Event_date),1):
            Event_day[i]=Event_day[i].replace(" ","")
            Event_month[i]=Event_month[i].replace(" ","")
            Event_year[i]=Event_year[i].replace(" ","")

        for i in range(0,len(Event_date),1):
            Tourney_date[i]=(Event_day[i]+"-"+Event_month[i]+"-"+Event_year[i])
            Tourney_date[i]=Tourney_date[i].replace("--","")
            if (Tourney_date[i]!=""):
                Tourney_date[i]=datetime.strptime(Tourney_date[i], '%d-%m-%Y')

        for i in range(0,len(Event_deadline),1):
            if(Event_deadline[i]!=''):
                if(re.search(deadline_pattern2, Event_deadline[i],re.IGNORECASE)!=None):
                    Event_deadline[i]=Event_deadline[i].replace("Registration Deadline","<b>Registration Deadline</b>")
                else:
                    Event_deadline[i]="<b>Registration Deadline</b>: "+ Event_deadline[i]

        today=datetime.now().date()
        #print(datetime.now().time())
        dash="-"*38
        upcoming_text=dash+"\n"
        iterator=0
        for i in range(0,len(Tourney_date),1):
            if(type(Tourney_date[i])!=str):
                Days_to_Tourney[i]=(Tourney_date[i].date()-today)
                Days_to_Tourney[i]=Days_to_Tourney[i].days
                if(Deadline_date[i]!=""):
                    Days_to_Deadline[i]=(Deadline_date[i].date()-today)
                    Days_to_Deadline[i]=Days_to_Deadline[i].days
                    if( Days_to_Deadline[i]<0):
                        Days_to_Deadline[i]='Registration Closed'

        for i in range(0,len(Event_deadline),1):
            try:
                if(Event_deadline[i]!=""):
                    if(re.search(pattern, Event_deadline[i], re.IGNORECASE).group(0).lower()=="closed"):
                        if(Days_to_Deadline[i]==''):
                            Days_to_Deadline[i]='Registration Closed'
            except:
                Event_deadline[i]=""

        return_list=[Event_name,Event_date,Event_deadline,Links,Days_to_Tourney,Days_to_Deadline,Tourney_date,Deadline_date]

        for i in range(len(Tourney_date)):
            if(Tourney_date[i]==''):
                for arr in range(0,len(return_list),1):
                    return_list[arr][i]='delete'

        def remove_values_from_list(the_list, val):
            return [value for value in the_list if value != val]


        final_list=[]
        for i in range(0,len(return_list),1):
            final_list.append(remove_values_from_list(return_list[i], 'delete'))

        lis = [(final_list[6][i], final_list[7][i],final_list[0][i],final_list[1][i],final_list[2][i],final_list[3][i],final_list[4][i],final_list[5][i]) for i in range(len(final_list[1]))]

        data = sorted(lis, key=lambda y: y[0])

        lis=data

        sgtourney_name,sgtourney_date,sgtourney_deadline,sgtourney_links,sgtourney_days_to_tourney,sgtourney_days_to_deadline=([] for i in range(6))
        for i in range(len(lis)):
            sgtourney_name.append(lis[i][2])
            sgtourney_date.append(lis[i][3])
            sgtourney_deadline.append(lis[i][4])
            sgtourney_links.append(lis[i][5])
            sgtourney_days_to_tourney.append(lis[i][6])
            sgtourney_days_to_deadline.append(lis[i][7])

        for i in range(len(sgtourney_days_to_tourney)):   
            if(type(sgtourney_days_to_tourney[i])!=str):
                if(sgtourney_days_to_tourney[i]>0):
                    iterator+=1
                    upcoming_text+="<b>"+str(iterator)+". "+sgtourney_name[i]+"</b>"+"\n\n"+"<b>Date</b>: "+sgtourney_date[i]+"\n"+sgtourney_deadline[i]+"\n"+"<b>Link</b>: "+sgtourney_links[i]+"\n"+dash+"\n"


        return upcoming_text,sgtourney_name,sgtourney_date,sgtourney_deadline,sgtourney_links,sgtourney_days_to_tourney,sgtourney_days_to_deadline       
