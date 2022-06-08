
# scrap data from worldometer
import requests
from bs4 import BeautifulSoup
import plyer


## how to bring notifications, need download plyer, and keep all data in a function so it will be easy
def datacollected():
    def notification(title, message):
        plyer.notification.notify(
        title = title,
        message = message,
        app_icon='corona.ico',
        time_out = 15   # keep notification for 15 seconds
        )

    url = "https://www.worldometers.info/coronavirus/"
    res = requests.get(url)   # you can see 200 means all data has been fetched successfully
    soup = BeautifulSoup(res.content,'html.parser')   #get text in html form, import bs4
    tbody = soup.find("tbody")   #scrap data from worldometer,get data of table so it will be names as tbody
    abc = tbody.find_all('tr')
    countrynotification = cntdata.get()
    # keep world as by default when no country is entered
    if (countrynotification == ""):
        countrynotification="world"

    serial_number, countries, total_cases, new_cases, total_deaths, new_deaths, total_recovered, active_cases=[],[],[],[],[],[],[],[]
    serious_critical, total_cases_per_mn, total_deaths_per_mn,total_tests,total_tests_per_mn,total_pop=[],[],[],[],[],[]

    ## header are used to name the column in the downloaded file
    ## make all list of all columns
    header = ['serial_number', 'countries', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_recovered', 'active_cases',
    'serious_critical', 'total_cases_per_mn', 'total_deaths_per_mn','total_tests','total_tests_per_mn','total_pop']

    for i in abc:
        id = i.find_all("td")
        if(id[1].text.strip().lower()==countrynotification):
            totalcase1 = int(id[2].text.strip().replace(',',""))
            totaldeaths = id[4].text.strip()
            newcases = id[3].text.strip()
            newdeaths = id[5].text.strip()
            notification("CORONA RECENT UPDATES OF {}".format(countrynotification),
                         "Total Cases: {}\nTotal Deaths :{}\nNew Cases : {}\nNew Deaths : {}".format(
                             totalcase1,totaldeaths,newcases,newdeaths
                         ))

        serial_number.append(id[0].text.strip())
        countries.append(id[1].text.strip())
        total_cases.append(id[2].text.strip().replace(',',"")) #remobve the comma between numbers
        new_cases.append(id[3].text.strip())
        new_deaths.append(id[5].text.strip())
        total_deaths.append(id[4].text.strip())
        total_recovered.append(id[6].text.strip())
        active_cases.append(id[7].text.strip())
        serious_critical.append(id[8].text.strip())
        total_cases_per_mn.append(id[9].text.strip())
        total_deaths_per_mn.append(id[10].text.strip())
        total_tests.append(id[11].text.strip())
        total_tests_per_mn.append(id[12].text.strip())
        total_pop.append(id[13].text.strip())

    ## get three lists how to print data
# print(countries)
# print(total_cases)
# print(total_deaths)

    ## Get notifications: download plyer -- pip install plyer



    # print(id[1].text)  #id 1 is for country name all the coutry names will be printed

    # here use zip function so that store all the data together
    dataframe = pd.DataFrame(list(zip(serial_number, countries, total_cases, new_cases, total_deaths, new_deaths,
                            total_recovered, active_cases,
                            serious_critical, total_cases_per_mn, total_deaths_per_mn,total_tests,total_tests_per_mn,
                                      total_pop)),columns=header)

    # sort all data according to total cases in the world
    #which country has more cases
    sorts = dataframe.sort_values('total_cases',ascending=False)
    for a in flist:
        if(a =="html"):
            path2 = '{}/coronadata.html'.format(path)
            sorts.to_html(r'{}'.format(path2))
        if (a == "json"):
            path2 = '{}/coronadata.json'.format(path)
            sorts.to_json(r'{}'.format(path2))

        if (a == "csv"):
            path2 = '{}/coronadata.csv'.format(path)
            sorts.to_csv(r'{}'.format(path2))
#create message box
        if(len(flist) !=0):
            messagebox.showinfo("Notification","Corona Record is saved {}".format(path2),parent=coro)

## make functions disabled when it is clicked
def downloaddata():
    # if any dialog is clicked
    global path
    if(len(flist) != 0):
        path = filedialog.askdirectory()
    else:
        pass
    datacollected()
    flist.clear()  # after we finish out downloading it should come back to its normal state from disbaled state
    Inhtml.configure(state='normal')
    Injson.configure(state = 'normal')
    Inexcel.configure(state = 'normal')

def inhtmldownload():
    flist.append('html')
    Inhtml.configure(state= 'disabled')

def injsondownload():
    flist.append('json')
    Injson.configure(state= 'disabled')

def inexceldownload():
    flist.append('csv')
    Inexcel.configure(state= 'disabled')

## now create function to download all the files, give path wherever we want to download



# make label buttons and text space
# get date in ascending order with pandas to sort data
import pandas as pd
from tkinter import *
from tkinter import messagebox,filedialog
coro = Tk()
coro.title("Corona Virus Information")
coro.geometry('800x500+200+100')
coro.configure(bg = "#046173")
coro.iconbitmap('corona.ico')   # download only ico file
flist = []
path = ''



#### Labels
mainlabel = Label(coro, text = " Corona Virus Live Tracker",font = ("new roman", 30,"bold"),
                  bg = "#05897A", width= 33,fg="black", bd=5)
mainlabel.place(x = 0, y = 0)

label1 = Label(coro, text = "Country Name", font = ("arial", 20,"italic bold"),bg = "#046173")
label1.place(x=15,y=100)

label2 = Label(coro, text = "Download File in ", font = ("arial", 20,"italic bold"),bg = "#046173")
label2.place(x=15,y=200)

cntdata=StringVar()
entry1 = Entry(coro,textvariable=cntdata,font=("arial", 20,"italic bold"), relief=RIDGE,bd=2,width=32)
entry1.place(x = 280,y =100)

###BUTTONS
Inhtml = Button(coro,text="Html",bg='#2DAE9A',font=("arial",15,"italic bold"),relief = RIDGE,activebackground="#05945B",
                activeforeground="white",bd = 5, width=5,command=inhtmldownload)
Inhtml.place(x=300,y=200)

Injson = Button(coro,text="json",bg='#2DAE9A',font=("arial",15,"italic bold"),relief = RIDGE,activebackground="#05945B",
                activeforeground="white",bd = 5, width=5,command = injsondownload)
Injson.place(x=300,y=260)

Inexcel = Button(coro,text="Excel",bg='#2DAE9A',font=("arial",15,"italic bold"),relief = RIDGE,activebackground="#05945B",
                activeforeground="white",bd = 5, width=5,command = inexceldownload)
Inexcel.place(x=300,y=320)

Submit = Button(coro,text="Submit",bg='#CB0542',font=("arial",15,"italic bold"),relief = RIDGE,activebackground="#7B0519",
                activeforeground="white",bd = 5, width=25, command = downloaddata)
Submit.place(x=450,y=260)



coro.mainloop()



