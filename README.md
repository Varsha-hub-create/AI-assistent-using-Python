# AI-assistent-using-Python
from tkinter import*
import pyttsx3
from PIL import Image,ImageTk
import speech_to_text
import text_to_speech
import action
import weather
root=Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False,False)
root.config(bg="#FFE5B4")

#ask fun
def ask():
    try:
        print("Calling Speech_to_text...")
        user_val = speech_to_text.Speech_to_text()
        print("User Input:", user_val)
        bot_val = action.Action(user_val)
        print("Bot Response:", bot_val)

        text.insert(END, 'User ---> ' + user_val + "\n")
        if bot_val is not None:
            text.insert(END, "BOT <--- " + str(bot_val) + "\n")
        if bot_val == "Ok Sir":
            root.destroy()
    except Exception as e:
        print("Error in ask():", e)

# def Action(input_text):
#     print("Processing:", input_text)
#     # Add logic and debug outputs here
#     return "Sample Bot Response"  # Replace with actual logic

#send fun
def Send():
    send=entry.get()
    bot=action.Action(send)
    text.insert(END, 'User ---> ' + send + "\n")
    if bot !=None:
        text.insert(END,"Bot<---"+str(bot)+"\n")
    if bot=="Ok sir":
        root.destroy()

#delete fun
def Delete():
    # Placeholder function for the "Delete" button
    print("Delete function triggered")


#frame
frame=LabelFrame(root,padx=100,pady=7,borderwidth=3,relief="raised")
frame.config(bg="#FFE5B4")
frame.grid(row=0,column=1,padx=55,pady=10)

#text label
text_label=Label(frame,text="AI Assistant",font=("comic Sans ms",14,"bold"),bg="#DE7E5D")
text_label.grid(row=0,column=0,padx=20,pady=10)

#image
image = ImageTk.PhotoImage(Image.open("C:/Users/varsh/OneDrive/Pictures/AI/ai.jpg"))
image_label = Label(frame, image=image)
image_label.grid(row=1, column=0, pady=20)



#adding sum text widget

text = Text(root, font=('courier 10 bold'), bg="#DE7E5D")
text.place(x=100, y=375, width=375, height=100)


#entry widget
entry=Entry(root,justify=CENTER)
entry.place(x=100,y=500,width=350,height=30)

#button 1
button1=Button(root,text="Ask",bg="#DE7E5D",pady=16,padx=40,borderwidth=3,relief=SOLID,command=ask)
button1.place(x=70,y=575)

#button 2
button2=Button(root,text="Send",bg="#DE7E5D",pady=16,padx=40,borderwidth=3,relief=SOLID,command=Send)
button2.place(x=400,y=575)

#button 3
button3=Button(root,text="Delete",bg="#DE7E5D",pady=16,padx=40,borderwidth=3,relief=SOLID,command=Delete)
button3.place(x=225,y=575)


# # Optional scrollbar
# scroll = Scrollbar(root, command=text.yview)
# scroll.place(x=475, y=375, height=100)
# text.config(yscrollcommand=scroll.set)

# # Default text
# text.insert('1.0', "Welcome to AI Assistant!")

    
root.mainloop()
