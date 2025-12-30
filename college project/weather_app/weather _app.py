# learn dictionary

# tinkter is using to get the screen which gves output
from tkinter import *
# ttk help us to import library for combobox(dropdown)
from tkinter import ttk
# requests help us to make api calls
import requests

# api
# city="delhi"
# data= requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid={8e57e5d18a705c3aef72fd101f71de9d}")


# making a function 
def data_get():
    city=city_name.get()
    data= requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=8e57e5d18a705c3aef72fd101f71de9d").json()
    
    #  the code from line 22 to 29 help us to add data to the box which were empty
    # means data ka weather wala key ka oth index ka main wali key ka data lao
    w_label1.config(text=data["weather"][0]["main"])
    
    wb1_label1.config(text=data["weather"][0]["description"])
    
    temp=data["main"]["temp"]-273.15
    temp1_label1.config(text=f"{temp:.2f} c")

    per1_label1.config(text=data["main"]["pressure"])










# tk is the class inside tkinter 
# we made  a varible so that we dont have to call class again and agian
win=Tk()
# tittle help us to give tittle to the page
win.title("Weather APP")
# config change or update the properties of a widget after it has been created.
win.config(bg="teal")
# geometry helps us to give size to the box
win.geometry("500x550")

# intial start (where origin of screen is calculate dis from top left corner)
# x=0 ,y=0 at top left corner


# heading box

#  label help us to create a new heading
# label is used to create normal heading or box which has something written in it
name_label=Label(win,text="Weather fetching", font=("arial",30,"bold"))
# place help us to give it size and place it accordingly 
name_label.place(height=50,width=350,x=72,y=50)







# dropdown

#  in python and backend we call dropdown as combobox

# list of city i want in dropdown
list_name=["Delhi","Goa","Haryana"]
# - stingvar is a special Tkinter variable class that holds a string value.
#  It acts as a bridge between Python variables and Tkinter widgets.

city_name=StringVar()
#  making  a combobox
# values attribute help us to add value in dropdown here we added the above array name list_name 
# another way to add value is:   values=["delhi","Goa"]
# textvariable means we are storing the name of city inside the combobox
com=ttk.Combobox(win,text="Select city",values=list_name, font= ("Arial",30,"bold"),textvariable=city_name)
#  now placing the dropdown
com.place(x=70, y=120, height=50,width=350)






# done buttton
# this inside () means in which class i want to make the following variable and its data
# command help us to connect function to the button 
done_button=Button(win,text="get data",font= ("Arial",30,"bold"),command=data_get)
done_button.place(x=130, y=180, height=50,width=220)






# output box
#  creating the options wear we want to show the final output
w_label=Label(win,text="Weather climate:",font= ("Arial",20))
w_label.place(x=25, y=260, height=50,width=210)
# box in front of the waeter climate box
w_label1=Label(win,text="",font= ("Arial",20))
w_label1.place(x=265, y=260, height=50,width=210)

wb_label=Label(win,text="Weather Discription:",font= ("Arial",16))
wb_label.place(x=25, y=330, height=50,width=210)
# box in front of the waeter climate box
wb1_label1=Label(win,text="",font= ("Arial",20))
wb1_label1.place(x=265, y=330, height=50,width=210)

temp_label=Label(win,text="Temperature:",font= ("Arial",20))
temp_label.place(x=25, y=400, height=50,width=210)
# box in front of the waeter climate box
temp1_label1=Label(win,text="",font= ("Arial",20))
temp1_label1.place(x=265, y=400, height=50,width=210)

per_label=Label(win,text="Pressure:",font= ("Arial",20))
per_label.place(x=25, y=470, height=50,width=210)
# box in front of the waeter climate box
per1_label1=Label(win,text="",font= ("Arial",20))
per1_label1.place(x=265, y=470, height=50,width=210)




# mainloop help us to give the output screen 
win.mainloop()#default size ayga









