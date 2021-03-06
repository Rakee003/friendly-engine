# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 22:05:47 2021

@author: Rakesh Kumar


Libraries Used:
   # TKinter 
"""

from tkinter import * 

#>>>>>>>>>>>>>For Adding(List Creation)

buffer_list=[]
count=0

'''
Add Function

Creating a list of list which can save Link.get() and Topic.get()

Add should contain:
    Link and Topic should refresh<Clear_text function>
    File Name Gui should hide <Hide function is executed here>
    Last added link and topic name should be shown with a option to delete(optionally): <confirm_Safety function is executed here>
        If pressed another function called Delete should get proceed further

'''

'''
Reference for list creation:  
    
    outside_list=[]
    for i in range(0,5):
        inside_list=[]
        inside_list.append(i)
        inside_list.append(i+1)
        outside_list.append(inside_list)

       #you can access any inside_list from the outside_list and append     
        outside_list[1].append(100)
        print(outside_list)  '''

def add():
    
    Linkk = Link.get()
    Topicc = Topic.get()
    for i in range(0,1):
        temp_list=[]
        temp_list.append(Linkk)
        temp_list.append(Topicc)
        buffer_list.append(temp_list)
    Clear_text()
    #confirm_Safety(Linkk,Topicc)
    print(len(buffer_list))
    print(buffer_list)
    





'''
Clear_text :
    It is used to refresh or delete the content inside the entry box (Link and Topic) when clear button is pressed.
'''

def Clear_text():
    Link_entry.delete(0,'end')
    Topic_entry.delete(0,'end')

'''
hide

This function is a static function which has a constant duty of hiding the Title GUI if Add is pressed
Can set a flag to enable and disable

'''

def hide():
    pass



'''
confirm_Safety Function

Creation of New GUI which shows previous Title, Topic values with a button named 'delete--->delete()-->is called' 
The values are dynamic and taken from buffer_list accessed via index (may be..!)

'''
'''def confirm_Safety(Link_message,Topic_message):
    Link_confirm_Safety = Label(app, text = Link_message)  
    Link_confirm_Safety.place(x = 250,y = 30)
    Topic_confirm_Safety = Label(app, text = Topic_message)
    Topic_confirm_Safety.place(x = 250,y = 60) '''
    



'''
Delete Function

This function is accompanied with confirm_Safety function . If Delete button is pressed,
Now the corresponding List and Topic is deleted from the buffer list (buy deleting the corresponding index value)
And call the confirm_Safety function with the previous Topic and Link value

'''
def delete():
    pass







#>>>>>>>>>>>>>>File Handling

def save_info():

    Link_info = Link.get()
    Topic_info = Topic.get()
    File_name=File.get()
    #Linker=('<a href="{}" target="{}">{}<br></a>'.format(Link_info,Topic_info,Topic_info))
    
    
    print(Link_info,Topic_info)
    
    file = open(File_name+".html","w")
    file.write("<html>")
    file.write("\n")
    file.write("<body>")
    file.write("\n")
    for i in buffer_list:
        (temp_link,temp_topic)=i
        Linkerr=('<a href="{}" target="{}">{}</a><br>'.format(temp_link,temp_topic,temp_topic))
        file.write(Linkerr)
        file.write("\n")
    #file.write(Linker)
    file.write("\n")
    
    file.write("</body>")
    file.write("\n")
    file.write("</html>")
    file.write("\n")
    '''
Reference:
        
    file.write("Your First Name " + firstname_info)
    
    file.write("\n")
    
    file.write("Your Last Name " + lastname_info)
    
    file.write("\n")
    
    file.write("Your Age " + str(age_info))
    
    file.close()
    
    '''
    
''' 
Trials:
<html>
<body>

<a href="https://www.youtube.com/watch?v=XAwZwj5H9RE" target="_blank">Youtube<br></a>
</body>
</html>  '''



#>>>>>>>>>>>>>Tkinter 


app = Tk()

app.geometry("500x500")

app.title("Friendly-Engine")

heading = Label(text="Link Generator",fg="black",bg="lightblue",width="500",height="3",font="10")

heading.pack()

Link_text = Label(text="Link :")
Topic_text = Label(text="Topic :")
File_text=Label(text="File Name :")


Link_text.place(x=15,y=70)
Topic_text.place(x=15,y=140)
File_text.place(x=15,y=210)


Link = StringVar()
Topic = StringVar()
File=StringVar()


Link_entry = Entry(textvariable=Link,width="30")
Topic_entry = Entry(textvariable=Topic,width="30")
File_entry=Entry(textvariable=File,width="30")


Link_entry.place(x=15,y=100)
Topic_entry.place(x=15,y=180)
File_entry.place(x=15,y=250)

submit_button = Button(app,text="Submit Data",command=save_info,width="30",height="2",bg="grey")

submit_button.place(x=15,y=290)

add_button=Button(app,text="Add",command=add,width="30",height="2",bg="yellow")
add_button.place(x=250,y=290)

#Clear Button

    
Clear_Button=Button(app,text="Clear",command=Clear_text,width="30",height="2",bg="lightgreen")
Clear_Button.place(x=250,y=100)



'''
Reference for Delete 
# Create Object
root = Tk()
  
# specify size of window.
root.geometry("400x500")
  
# delete content from Text Box
  
  
def delete_text():
    T.delete("1.0", "end")
  
  
# Create text widget
T = Text(root)
T.pack()
  
# Create Delete Button
Button(root, text="Delete", command=delete_text).pack()
  
# Excute Tkinter
root.mainloop()
'''


mainloop()