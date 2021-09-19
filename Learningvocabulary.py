import tkinter as tk
from tkinter import ttk 
import random
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=6, rowspan=6)

#header
header = tk.Label(root,text='Learning vocabulary is a lot of fun!',font=("Arial", 18))
header.grid(row=0, column=0,pady=10)

#logo
logo = Image.open('images.jpeg')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=0, row=1)

instructions = tk.Label(root, text="A simple app created by Charlotte to learn English vocabulary", font="Raleway")
instructions.grid(column=0, row=2)

vocabulary = {'notwithstand':'despite anything to the contray', 
                     'impress':'have a powerful and usually postive effect on',
                         'miniute':'a unit of time equal to 60seconds or 1/60th of an hour',
                         'flush':'rinse, clean, or empty with a liquid',
                         'article':'one of a class of artifacts',
                         'hey':'heyhey'}
random_sample = dict(random.sample(vocabulary.items(), 4)) #select 4 random items from the dict
random_values = dict(random.sample(vocabulary.items(), 4)).values()
random_item = random.choice(list(random_sample.items())) # select one word from the 4 words



def vocabulary():
        #instructions
    global answer_label,question_combobox,random_sample,random_item,random_values
    instructions = tk.Label(root, text="A simple app created by Charlotte to learn English vocabulary", font="Raleway")
    instructions.grid(column=0, row=2)

    vocabulary = {'notwithstand':'despite anything to the contray', 
                     'impress':'have a powerful and usually postive effect on',
                         'miniute':'a unit of time equal to 60seconds or 1/60th of an hour',
                         'flush':'rinse, clean, or empty with a liquid',
                         'article':'one of a class of artifacts',
                         'hey':'heyhey'}
    random_sample = dict(random.sample(vocabulary.items(), 4)) #select 4 random items from the dict
    random_values = dict(random.sample(vocabulary.items(), 4)).values()
    random_item = random.choice(list(random_sample.items())) # select one word from the 4 words
    
        
        #question 
    question_label=tk.Label(root,text="The word is '" + random_item[0] + "', and it means ")
    question_label.grid(row=4,column=0)
    question_choices = list(random_values)
    combobox_text = tk.StringVar()
    question_combobox = tk.ttk.Combobox(root,
                                      textvariable=combobox_text,
                                      values=question_choices,
                                      font=("Arial", 10))
    question_combobox.set(list(random_values)[0])
    question_combobox.grid(row=4, column=1,pady=30)
        #answer
    answer_label=tk.Label(root,text='Loading',font=("Arial", 18))
    answer_label.grid(row=5,column=0, pady=10)
    
def submit():
    global answer_label,question_combobox,random_sample,random_item,random_values
    if question_combobox.get() ==  random_item[1]:
        answer_label['text']='Yay, you got it right!'
    else:
        answer_label['text'] = "Don't give up, keep trying!"
        
#     answer_label
    
def delete():
    ### to delete a word that the user is familiar with 
#     global vocabulary
    del vocabulary[random_item[0]]
#     vocabulary

#begin button
begin_text = tk.StringVar()
begin_btn = tk.Button(root, textvariable=begin_text, command=lambda:vocabulary(), font="Raleway", bg="#20bebe", fg="black", height=2, width=15)
begin_text.set("Select a word")
begin_btn.grid(column=0, row=3)

#submit button 
submit_text = tk.StringVar()
submit_btn = tk.Button(root, textvariable=submit_text, command=lambda:submit(), font="Raleway", bg="#20bebe", fg="black", height=2, width=15)
submit_text.set("Submit my answer")
submit_btn.grid(column=0, row=6)

#delete button 
# delete_text = tk.StringVar()
# delete_btn = tk.Button(root, textvariable=delete_text, command=lambda:delete(), font="Raleway", bg="#20bebe", fg="black", height=2, width=15)
# delete_text.set("Delete this word")
# delete_btn.grid(column=1, row=6)

#quit button 
quit_text = tk.StringVar()
quit_btn = tk.Button(root, textvariable=quit_text, command=root.withdraw, font="Raleway", bg="#20bebe", fg="black", height=2, width=15)
quit_text.set("Quit")
quit_btn.grid(column=2, row=6)


canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

root.mainloop()