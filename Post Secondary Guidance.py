'''
Post-Secondary Guidance Program
Created By: Hamzah Behery
Date: December 22nd 2018

*The Only Subjects That Were Completely Implemented Are Biology and Computer Science*
'''

#Modules
import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import string
import winsound
global length ,sub,sortSub,favList
favList=[]
length=0
sub =[]
sortSub=[]
#Frames Config
#########
root = tk.Tk()
mainframe = tk.Frame(root)
surveyFrame = tk.Frame(root)
surveyFrame2 = tk.Frame(root)
browseFrame = tk.Frame(root)

root.resizable(False, False)
root.config(background='#ddccff')
surveyFrame.config(background='#ffe6e6')
surveyFrame2.config(background='#ffe6e6')
browseFrame.config(background='#ffffe6')
mainframe.config(background='#eee6ff')

#########
#Functions
def rootShow():
    root.deiconify()

def results():
    global sub
    if length == 0 or nameVar.get() == "" or avgVar.get() == "" or citizenVar.get() == "":
        
        invalidAlert = tk.Toplevel()
        invalidAlert.resizable(False, False)
        invalidAlert.config(background='#ffffb3')
            
        invalidFrame = tk.Frame(invalidAlert)
        invalidFrame.grid(padx=10,pady=10)
        invalidFrame.config(background='#ffffe6')
        
        invalidMessage = tk.Text(invalidFrame, height=4,width=130,background='#ffffe6')
        invalidMessage.tag_configure('main', justify='center', foreground="red4", font=('Courier', 22))
        invalidMessage.tag_configure('invalid', foreground="purple4", font=('Courier', 22))
        invalidMessage.insert(tk.END,'Please Fill in All Fields to Proceed!\nMissing:','main')
        invalidMessage.grid(row=1,column=1)
        if nameVar.get() == "":  
            invalidMessage.insert(tk.END,' |Name| ','invalid')
        if avgVar.get() =="":
            invalidMessage.insert(tk.END,' |Average| ','invalid')
        if citizenVar.get() == "":
            invalidMessage.insert(tk.END,' |Citizenship| ','invalid')
        if length == 0:
            invalidMessage.insert(tk.END,' |Subject| ','invalid')
        invalidMessage.configure(state="disabled")
        winsound.PlaySound("error.wav", winsound.SND_ASYNC)
    else:
        results1 = tk.Toplevel()
        results1.resizable(False, False)
        results1.config(background='#ffffb3')
        
        results1Frame = tk.Frame(results1)
        results1Frame.config(background='#ffffb3')
        results1Frame.grid(padx=10,pady=10)
        
        number1Label = ttk.Label(results1Frame, background='#ffffb3', text = "1.")
        number1Label.grid(row=2,column=1,sticky=tk.W)
        number2Label = ttk.Label(results1Frame, background='#ffffb3', text = "2.")
        number2Label.grid(row=3,column=1,sticky=tk.W)
        
        uniResultsFrame1= ttk.LabelFrame(results1Frame, style = 'Y.Label',width=1200,height=200)
        uniResultsFrame1.grid_propagate(False)
        
        uniResultsFrame2= ttk.LabelFrame(results1Frame, style = 'Y.Label',width=1200,height=200)
        uniResultsFrame2.grid_propagate(False)

        uniResultsFrame3= ttk.LabelFrame(results1Frame, style = 'Y.Label',width=1200,height=200)
        uniResultsFrame3.grid_propagate(False)

        backButton4 = ttk.Button(results1Frame,text="Back to Menu",command = rootShow,width =13)
        backButton4.grid(row=4,column=3)
        favsListButton = ttk.Button(results1Frame,text="Favourites List",command = favs,width =15)
        favsListButton.grid(row=4,column=6)

        results1Text = tk.Text(results1Frame, height=6,width=130,background='#ffffe6')
        
        results1Text.tag_configure('main', foreground="red4", font=('Courier', 15),justify='center')
        results1Text.tag_configure('var', foreground="purple4", font=('Courier', 15),justify='center')

        results1Text.insert(tk.END, nameVar.get(),'var')
        results1Text.insert(tk.END,' ,We Recommend These Universities For You Due to Your:\n ','main')
        results1Text.insert(tk.END,f'${budgetVar.get()}','var')
        results1Text.insert(tk.END,f'/Yr Budget,Preferred Subject of ','main')
        results1Text.insert(tk.END,sub[0],'var')
        results1Text.insert(tk.END,', and Average Range of ','main')
        results1Text.insert(tk.END,avgVar.get(),'var')

        if sub[0] != "Biology" and sub[0] != "Computer Science":
            uniResultsFrame1.grid(row=2,column=2,columnspan=5,pady=10)
            uniResultsFrame2.grid(row=3,column=2,columnspan=5,pady=10)
            
            imageResultsFrame = ttk.LabelFrame(uniResultsFrame1, style = 'yellow.Label',width=175, height = 175)
            imageResultsFrame.grid(row=1,column=1,padx=10)            
            imageResultsFrame2 = ttk.LabelFrame(uniResultsFrame2, style = 'yellow.Label',width=175, height = 175)
            imageResultsFrame2.grid(row=1,column=1,padx=10)
        if citizenVar.get() == "Yes":
            results1Text.insert(tk.END,'. \nSince You Are a ','main')
            results1Text.insert(tk.END,'Canadian Citizen/Resident','var')
            results1Text.insert(tk.END,', You Would be Able to \nAfford Expensive Tuitions Through Student Grants/Loans','main')
        elif citizenVar.get() == "No":
            results1Text.insert(tk.END,'. \nSince You Are','main')
            results1Text.insert(tk.END,' Not a Canadian Citizen/Resident','var')
            results1Text.insert(tk.END,', it May be Difficult to \nAfford Expensive Tuitions.','main')

        results1Text.configure(state="disabled")
        results1Text.grid(row=1,column=1,columnspan=6)

        uni1ResultsLearnButton = ttk.Button(uniResultsFrame1,text="Learn More",command = lambda: learnMore(UniLabel),width =13,style = 'purple.TButton')
        uni1ResultsFavsButton = ttk.Button(uniResultsFrame1,text="Add to Fav.",command = lambda: addToFavs(UniLabel),width =13,style = 'purple.TButton')

        uni2ResultsLearnButton = ttk.Button(uniResultsFrame2,text="Learn More",command = lambda: learnMore(UniLabel),width =13,style = 'purple.TButton')
        uni2ResultsFavsButton = ttk.Button(uniResultsFrame2,text="Add to Fav.",command = lambda: addToFavs(UniLabel),width =13,style = 'purple.TButton')

        uni3ResultsLearnButton = ttk.Button(uniResultsFrame3,text="Learn More",command = lambda: learnMore(UniLabel),width =13,style = 'purple.TButton')
        uni3ResultsFavsButton = ttk.Button(uniResultsFrame3,text="Add to Fav.",command = lambda: addToFavs(UniLabel),width =13,style = 'purple.TButton')

        if sub[0] == "Biology" or sub[0] == "Computer Science":
            uni1ResultsLearnButton.grid(row=2, column=8, columnspan=2,sticky=tk.N + tk.E)
            uni1ResultsFavsButton.grid(row=2, column=8, columnspan=2,sticky=tk.S + tk.E)
            
            
            uni2ResultsLearnButton.grid(row=2, column=8, columnspan=2,sticky=tk.N + tk.E)
            uni2ResultsFavsButton.grid(row=2, column=8, columnspan=2,sticky=tk.S + tk.E)

            uni3ResultsLearnButton.grid(row=2, column=8, columnspan=2,sticky=tk.N + tk.E)
            uni3ResultsFavsButton.grid(row=2, column=8, columnspan=2,sticky=tk.S + tk.E)
            
        if sub[0] == "Biology":
        #Button Settings
            uni1ResultsLearnButton.config(command = lambda: learnMore(McGillUniLabel))
            uni1ResultsFavsButton.config(command = lambda: addToFavs(McGillUniLabel))

            uni2ResultsLearnButton.config(command = lambda: learnMore(torontoUniLabel))
            uni2ResultsFavsButton.config(command = lambda: addToFavs(torontoUniLabel))

            uni3ResultsLearnButton.config(command = lambda: learnMore(victoriaUniLabel))
            uni3ResultsFavsButton.config(command = lambda: addToFavs(victoriaUniLabel))
        
        #McGill Assets
            McGillResultImg = Image.open("McGill#1.jpg").resize((175, 175))
            McGillResultPhoto = ImageTk.PhotoImage(McGillResultImg)
            McGillResultImageLabel = tk.Label(uniResultsFrame1, image=McGillResultPhoto)
            McGillResultImageLabel.image = McGillResultPhoto
            
            
            McGillResultLabel = ttk.Label(uniResultsFrame1,style='uniLableY.TLabel',text = "University of McGill", justify='center')
            McGillResultRatingLabel = ttk.Label(uniResultsFrame1,style='uniLableY.TLabel',text = "-Ranked #3 in Canada", justify='center',foreground = 'red4')
            
            McGillResultSummary = tk.Text(uniResultsFrame1,height=8,width=95, background = '#ffffb3')
            McGillResultSummary.tag_configure('main', foreground="red4",font=('Courier', 14))
            McGillResultSummary.insert(tk.END, '''The University of McGill’s life science program is competitive,
and students applying will require an average between %90 - %100.
Along with that, tuition comes at a hefty price for both domestic
and international students, ranging from approximately $9 000
(domestic) to $20 000 (international) per year, including
ancillary fees.''', 'main')
            McGillResultSummary.configure(state="disabled")
        #Toronto Assets
            torontoResultLabel = ttk.Label(uniResultsFrame2,style='uniLableY.TLabel',text = "University of Toronto", justify='center')
            torontoResultRatingLabel = ttk.Label(uniResultsFrame2,style='uniLableY.TLabel',text = "-Ranked #1 in Canada", justify='center',foreground = 'red4')
            torontoResultSummary = tk.Text(uniResultsFrame2,height=8,width=95, background = '#ffffb3')
            torontoResultSummary.tag_configure('main', foreground="red4",font=('Courier', 14))
            torontoResultSummary.insert(tk.END, '''The University of Toronto’s biology programs are marvelous, with
students requiring an average between %80 - %89 to have a good
chance at acceptance. Along with that, tuition comes at a mid-range
price for both domestic and international students, ranging from
approximately $7 000 (domestic), and a difficult $45 000
(international) per year.''', 'main')
            torontoResultImg = Image.open("toronto#1.jpg").resize((175, 175))
            torontoResultPhoto = ImageTk.PhotoImage(torontoResultImg)
            torontoResultImageLabel = tk.Label(uniResultsFrame2, image=torontoResultPhoto)
            torontoResultImageLabel.image = torontoResultPhoto
            torontoResultSummary.configure(state="disabled")
        #Victoria Assets
            victoriaResultLabel = ttk.Label(uniResultsFrame3,style='uniLableY.TLabel',text = "University of Victoria", justify='center')
            victoriaResultRatingLabel = ttk.Label(uniResultsFrame3,style='uniLableY.TLabel',text = "-Ranked #15 in Canada", justify='center',foreground = 'red4')
            victoriaResultSummary = tk.Text(uniResultsFrame3,height=8,width=95, background = '#ffffb3')
            victoriaResultSummary.tag_configure('main', foreground="red4",font=('Courier', 13))
            victoriaResultSummary.insert(tk.END, '''The University of Victoria’s life science program is not very difficult to
get into, as students applying will require an average in the mid to high
%70s range to have feel confident about their applications. Along with
that, tuition comes at an affordable price for both domestic and
international students, ranging from approximately $6 428 (domestic) to
$20 000 (international) per year, including ancillary fees.''', 'main')
            victoriaResultImg = Image.open("victoria#1.jpg").resize((175, 175))
            victoriaResultPhoto = ImageTk.PhotoImage(victoriaResultImg)
            victoriaResultImageLabel = tk.Label(uniResultsFrame3, image=victoriaResultPhoto)
            victoriaResultImageLabel.image = victoriaResultPhoto
            victoriaResultSummary.configure(state="disabled")
        #Gridding Assets Onto Frames
            McGillResultLabel.grid(row=1,column=3,sticky=tk.N)
            McGillResultRatingLabel.grid(row=1, column=5,sticky=tk.N + tk.W)
            McGillResultSummary.grid(row=2,rowspan=1,column=3, columnspan = 5)
            McGillResultImageLabel.grid(row=1,column=1,padx=10,rowspan=3)
            
            torontoResultLabel.grid(row=1,column=3,sticky=tk.N)
            torontoResultRatingLabel.grid(row=1, column=5,sticky=tk.N)
            torontoResultSummary.grid(row=2,rowspan=1,column=3, columnspan = 5)
            torontoResultImageLabel.grid(row=1,column=1,padx=10,rowspan=3)
            
            victoriaResultLabel.grid(row=1,column=3,sticky=tk.N)
            victoriaResultRatingLabel.grid(row=1, column=5,sticky=tk.N)
            victoriaResultSummary.grid(row=2,rowspan=1,column=3, columnspan = 5,sticky=tk.N)
            victoriaResultImageLabel.grid(row=1,column=1,padx=10,rowspan=3)
        elif sub[0] == "Computer Science":
        #Button Settings
            uni1ResultsLearnButton.config(command = lambda: learnMore(waterlooUniLabel))
            uni1ResultsFavsButton.config(command = lambda: addToFavs(waterlooUniLabel))

            uni2ResultsLearnButton.config(command = lambda: learnMore(guelphUniLabel))
            uni2ResultsFavsButton.config(command = lambda: addToFavs(guelphUniLabel))

            uni3ResultsLearnButton.config(command = lambda: learnMore(windsorUniLabel))
            uni3ResultsFavsButton.config(command = lambda: addToFavs(windsorUniLabel))
        #Waterloo Assets
            waterlooResultUniLabel = ttk.Label(uniResultsFrame1,style='uniLableY.TLabel',text = "University of Waterloo", justify='center')
            waterlooResultRatingLabel = ttk.Label(uniResultsFrame1,style='uniLableY.TLabel',text = "-Ranked #9 in Canada", justify='center',foreground = 'red4')
            waterlooResultSummary = tk.Text(uniResultsFrame1,height=8,width=95, background = '#ffffb3')
            waterlooResultSummary.tag_configure('main', foreground="red4",font=('Courier', 14))
            waterlooResultSummary.insert(tk.END, '''The University of Waterloo’s computer science program is fairly
competitive, and students applying will require an average between
%90 - %100. Along with that, tuition comes at a hefty price for
both domestic and international students, ranging from approximately
$17 000 (domestic) to $33 000(international) per year, including
ancillary fees.''', 'main') 
            waterlooResultSummary.configure(state="disabled")
            waterlooResultImg = Image.open("waterloo#1.jpg").resize((175, 175))
            waterlooResultPhoto = ImageTk.PhotoImage(waterlooResultImg)
            waterlooResultImageLabel = tk.Label(uniResultsFrame1, image=waterlooResultPhoto)
            waterlooResultImageLabel.image = waterlooResultPhoto
        #Guelph Assets
            guelphResultUniLabel = ttk.Label(uniResultsFrame2,style='uniLableY.TLabel',text = "University of Guelph", justify='center')
            guelphResultRatingLabel = ttk.Label(uniResultsFrame2,style='uniLableY.TLabel',text = "-Ranked #19 in Canada", justify='center',foreground = 'red4')
            guelphResultSummary = tk.Text(uniResultsFrame2,height=8,width=95, background = '#ffffb3')
            guelphResultSummary.tag_configure('main', foreground="red4",font=('Courier', 14))
            guelphResultSummary.insert(tk.END, '''The University of Guelph’s computer science program is very
promising, as students applying will require an average between
%80 - %89 to have a good chance at acceptance. Along with that,
tuition comes at a mid-range price for both domestic and
international students, ranging from approximately $7 000
(domestic) to $22 000 (international) per year.''', 'main')
            guelphResultSummary.configure(state="disabled")
            guelphResultImg = Image.open("guelph#1.jpg").resize((175, 175))
            guelphResultPhoto = ImageTk.PhotoImage(guelphResultImg)
            guelphResultImageLabel = tk.Label(uniResultsFrame2, image=guelphResultPhoto)
            guelphResultImageLabel.image = guelphResultPhoto

        #Windsor Assets
            windsorResultUniLabel = ttk.Label(uniResultsFrame3,style='uniLableY.TLabel',text = "University of Windsor", justify='center')
            windsorResultRatingLabel = ttk.Label(uniResultsFrame3,style='uniLableY.TLabel',text = "-Ranked #22 in Canada", justify='center',foreground = 'red4')
            windsorResultSummary = tk.Text(uniResultsFrame3,height=8,width=95, background = '#ffffb3')
            windsorResultSummary.tag_configure('main', foreground="red4",font=('Courier', 13))
            windsorResultSummary.insert(tk.END, '''The University of Windsor’s computer science program is not very difficult
to get into, as students applying will require an average in the mid
to high %70s range to have feel confident about their applications.
Along with that, tuition comes at an affordable price for both domestic
and international students, ranging from approximately $5 500(domestic)
to $14 000 (international) per year, including ancillary fees.''', 'main')
            windsorResultSummary.configure(state="disabled")
            windsorResultImg = Image.open("windsor#1.jpg").resize((175, 175))
            windsorResultPhoto = ImageTk.PhotoImage(windsorResultImg)
            windsorResultImageLabel = tk.Label(uniResultsFrame3, image=windsorResultPhoto)
            windsorResultImageLabel.image = windsorResultPhoto
        #Gridding Assets Onto Frames
            waterlooResultUniLabel.grid(row=1,column=3,sticky=tk.N)
            waterlooResultRatingLabel.grid(row=1, column=5,sticky=tk.N + tk.W)
            waterlooResultSummary.grid(row=2,rowspan=1,column=3, columnspan = 5)
            waterlooResultImageLabel.grid(row=1,column=1,padx=10,rowspan=3)
            
            guelphResultUniLabel.grid(row=1,column=3,sticky=tk.N)
            guelphResultRatingLabel.grid(row=1, column=5,sticky=tk.N)
            guelphResultSummary.grid(row=2,rowspan=1,column=3, columnspan = 5)
            guelphResultImageLabel.grid(row=1,column=1,padx=10,rowspan=3)
            
            windsorResultUniLabel.grid(row=1,column=3,sticky=tk.N)
            windsorResultRatingLabel.grid(row=1, column=5,sticky=tk.N)
            windsorResultSummary.grid(row=2,rowspan=1,column=3, columnspan = 5,sticky=tk.N)
            windsorResultImageLabel.grid(row=1,column=1,padx=10,rowspan=3)
    #High
        if 14500 <= budgetVar.get() and avgVar.get() == '90%-100%' and citizenVar.get() == "No" or avgVar.get() == '90%-100%' and citizenVar.get() == "Yes" :
            if sub[0] == "Biology" or sub[0] == "Computer Science":
                uniResultsFrame1.grid(row=2,column=2,columnspan=5,pady=10)
                uniResultsFrame2.grid(row=3,column=2,columnspan=5,pady=10)
            else:
                pass
    #Mid
        elif 14500 <= budgetVar.get() and avgVar.get() == '80%-89%' and citizenVar.get() == "No" or avgVar.get() == '80%-89%' and citizenVar.get() == "Yes" or 9500 <= budgetVar.get() < 14500 and avgVar.get() == '80%-89%' and citizenVar.get() == "No":
            if sub[0] == "Biology" or sub[0] == "Computer Science":
                uniResultsFrame2.grid(row=2,column=2,columnspan=5,pady=10)
                uniResultsFrame3.grid(row=3,column=2,columnspan=5,pady=10)
            else:
                pass
    #Low
        elif avgVar.get() == '<80%' or budgetVar.get() < 9500 and citizenVar.get() == "No":
            if sub[0] == "Biology" or sub[0] == "Computer Science":
                uniResultsFrame3.grid(row=2,column=2,columnspan=5,pady=10)
                uniResultsFrame2.grid(row=3,column=2,columnspan=5,pady=10)
            else:
                pass
   
        if length == 2 and nameVar.get() != "" and avgVar.get() != "" and citizenVar.get() != "":
            results2 = tk.Toplevel()
            results2.resizable(False, False)
            results2.config(background='#ffffb3')
            
            results2Frame = tk.Frame(results2)
            results2Frame.config(background='#ffffb3')
            results2Frame.grid(padx=10,pady=10)


            uniResultsFrame1b= ttk.LabelFrame(results2Frame, style = 'Y.Label',width=1200,height=200)
            uniResultsFrame1b.grid_propagate(False)
            
            

            uniResultsFrame2b= ttk.LabelFrame(results2Frame, style = 'Y.Label',width=1200,height=200)
            uniResultsFrame2b.grid_propagate(False)
            

            
            uniResultsFrame3b= ttk.LabelFrame(results2Frame, style = 'Y.Label',width=1200,height=200)
            uniResultsFrame3b.grid_propagate(False)
            
            if sub[1] != "Biology" and sub[1] != "Computer Science":
                uniResultsFrame1b.grid(row=2,column=2,columnspan=5,pady=10)
                uniResultsFrame2b.grid(row=3,column=2,columnspan=5,pady=10)
                imageResultsFrameb = ttk.LabelFrame(uniResultsFrame1b, style = 'yellow.Label',width=175, height = 175)
                imageResultsFrameb.grid(row=1,column=1,padx=10)
                imageResultsFrame2b = ttk.LabelFrame(uniResultsFrame2b, style = 'yellow.Label',width=175, height = 175)
                imageResultsFrame2b.grid(row=1,column=1,padx=10)

            backButton4b = ttk.Button(results2Frame,text="Back to Menu",command = rootShow,width =13)
            backButton4b.grid(row=4,column=3)
            favsListButtonb = ttk.Button(results2Frame,text="Favourites List",command = favs,width =15)
            favsListButtonb.grid(row=4,column=6)
            
            number1Label2 = ttk.Label(results2Frame, background='#ffffb3', text = "1.")
            number1Label2.grid(row=2,column=1,sticky=tk.W)
            number2Label2 = ttk.Label(results2Frame, background='#ffffb3', text = "2.")
            number2Label2.grid(row=3,column=1,sticky=tk.W)
            
            results2Text = tk.Text(results2Frame, height=6,width=130,background='#ffffe6')
            
            results2Text.tag_configure('main', foreground="red4", font=('Courier', 15),justify='center')
            results2Text.tag_configure('var', foreground="purple4", font=('Courier', 15),justify='center')

            results2Text.insert(tk.END, nameVar.get(),'var')
            results2Text.insert(tk.END,' ,We Recommend These Universities For You Due to Your:\n ','main')
            results2Text.insert(tk.END,f'${budgetVar.get()}','var')
            results2Text.insert(tk.END,f'/Yr Budget,Preferred Subject of ','main')
            results2Text.insert(tk.END,sub[1],'var')
            results2Text.insert(tk.END,', and Average Range of ','main')
            results2Text.insert(tk.END,avgVar.get(),'var')
            if citizenVar.get() == "Yes":
                results2Text.insert(tk.END,'. \nSince You Are a ','main')
                results2Text.insert(tk.END,'Canadian Citizen/Resident','var')
                results2Text.insert(tk.END,', You Would be Able to \nAfford Expensive Tuitions Through Student Grants/Loans.','main')
            elif citizenVar.get() == "No":
                results2Text.insert(tk.END,'. \nSince You Are','main')
                results2Text.insert(tk.END,' Not a Canadian Citizen/Resident','var')
                results2Text.insert(tk.END,', it May be Difficult to \nAfford Expensive Tuitions.','main')
            results2Text.configure(state="disabled")
            results2Text.grid(row=1,column=1,columnspan=6)

            uni1ResultsLearnButton2 = ttk.Button(uniResultsFrame1b,text="Learn More",command = lambda: learnMore(UniLabel),width =13,style = 'purple.TButton')
            uni1ResultsFavsButton2 = ttk.Button(uniResultsFrame1b,text="Add to Fav.",command = lambda: addToFavs(UniLabel),width =13,style = 'purple.TButton')

            uni2ResultsLearnButton2 = ttk.Button(uniResultsFrame2b,text="Learn More",command = lambda: learnMore(UniLabel),width =13,style = 'purple.TButton')
            uni2ResultsFavsButton2 = ttk.Button(uniResultsFrame2b,text="Add to Fav.",command = lambda: addToFavs(UniLabel),width =13,style = 'purple.TButton')

            uni3ResultsLearnButton2 = ttk.Button(uniResultsFrame3b,text="Learn More",command = lambda: learnMore(UniLabel),width =13,style = 'purple.TButton')
            uni3ResultsFavsButton2 = ttk.Button(uniResultsFrame3b,text="Add to Fav.",command = lambda: addToFavs(UniLabel),width =13,style = 'purple.TButton')
            
            if sub[1] == "Biology" or sub[1] == "Computer Science":
                uni1ResultsLearnButton2.grid(row=2, column=8, columnspan=2,sticky=tk.N + tk.E)
                uni1ResultsFavsButton2.grid(row=2, column=8, columnspan=2,sticky=tk.S + tk.E)
                
                
                uni2ResultsLearnButton2.grid(row=2, column=8, columnspan=2,sticky=tk.N + tk.E)
                uni2ResultsFavsButton2.grid(row=2, column=8, columnspan=2,sticky=tk.S + tk.E)
    
                uni3ResultsLearnButton2.grid(row=2, column=8, columnspan=2,sticky=tk.N + tk.E)
                uni3ResultsFavsButton2.grid(row=2, column=8, columnspan=2,sticky=tk.S + tk.E)
            if sub[1] == "Biology":
                    #Button Settings
                uni1ResultsLearnButton2.config(command = lambda: learnMore(McGillUniLabel))
                uni1ResultsFavsButton2.config(command = lambda: addToFavs(McGillUniLabel))

                uni2ResultsLearnButton2.config(command = lambda: learnMore(torontoUniLabel))
                uni2ResultsFavsButton2.config(command = lambda: addToFavs(torontoUniLabel))

                uni3ResultsLearnButton2.config(command = lambda: learnMore(victoriaUniLabel))
                uni3ResultsFavsButton2.config(command = lambda: addToFavs(victoriaUniLabel))
                    #McGill Assets
                McGillResultImg2 = Image.open("McGill#1.jpg").resize((175, 175))
                McGillResultPhoto2 = ImageTk.PhotoImage(McGillResultImg2)
                McGillResultImageLabel2 = tk.Label(uniResultsFrame1b, image=McGillResultPhoto2)
                McGillResultImageLabel2.image = McGillResultPhoto2
                
                
                McGillResultLabel2 = ttk.Label(uniResultsFrame1b,style='uniLableY.TLabel',text = "University of McGill", justify='center')
                McGillResultRatingLabel2 = ttk.Label(uniResultsFrame1b,style='uniLableY.TLabel',text = "-Ranked #3 in Canada", justify='center',foreground = 'red4')
                
                McGillResultSummary2 = tk.Text(uniResultsFrame1b,height=8,width=95, background = '#ffffb3')
                McGillResultSummary2.tag_configure('main', foreground="red4",font=('Courier', 14))
                McGillResultSummary2.insert(tk.END, '''The University of McGill’s life science program is competitive,
and students applying will require an average between %90 - %100.
Along with that, tuition comes at a hefty price for both domestic
and international students, ranging from approximately $9 000
(domestic) to $20 000 (international) per year, including
ancillary fees.''', 'main')
                McGillResultSummary2.configure(state="disabled")
            #Toronto Assets
                torontoResultLabel2 = ttk.Label(uniResultsFrame2b,style='uniLableY.TLabel',text = "University of Toronto", justify='center')
                torontoResultRatingLabel2 = ttk.Label(uniResultsFrame2b,style='uniLableY.TLabel',text = "-Ranked #1 in Canada", justify='center',foreground = 'red4')
                torontoResultSummary2 = tk.Text(uniResultsFrame2b,height=8,width=95, background = '#ffffb3')
                torontoResultSummary2.tag_configure('main', foreground="red4",font=('Courier', 14))
                torontoResultSummary2.insert(tk.END, '''The University of Toronto’s biology programs are marvelous, with
students requiring an average between %80 - %89 to have a good
chance at acceptance. Along with that, tuition comes at a mid-range
price for both domestic and international students, ranging from
approximately $7 000 (domestic), and a difficult $45 000
(international) per year.''', 'main')
                torontoResultSummary2.configure(state="disabled")
                torontoResultImg2 = Image.open("toronto#1.jpg").resize((175, 175))
                torontoResultPhoto2 = ImageTk.PhotoImage(torontoResultImg2)
                torontoResultImageLabel2 = tk.Label(uniResultsFrame2b, image=torontoResultPhoto2)
                torontoResultImageLabel2.image = torontoResultPhoto2
            #Victoria Assets
                victoriaResultLabel2 = ttk.Label(uniResultsFrame3b,style='uniLableY.TLabel',text = "University of Victoria", justify='center')
                victoriaResultRatingLabel2 = ttk.Label(uniResultsFrame3b,style='uniLableY.TLabel',text = "-Ranked #15 in Canada", justify='center',foreground = 'red4')
                victoriaResultSummary2 = tk.Text(uniResultsFrame3b,height=8,width=95, background = '#ffffb3')
                victoriaResultSummary2.tag_configure('main', foreground="red4",font=('Courier', 13))
                victoriaResultSummary2.insert(tk.END, '''The University of Victoria’s life science program is not very difficult to
get into, as students applying will require an average in the mid to high
%70s range to have feel confident about their applications. Along with
that, tuition comes at an affordable price for both domestic and
international students, ranging from approximately $6 428 (domestic) to
$20 000 (international) per year, including ancillary fees.''', 'main')
                victoriaResultSummary2.configure(state="disabled")
                victoriaResultImg2 = Image.open("victoria#1.jpg").resize((175, 175))
                victoriaResultPhoto2 = ImageTk.PhotoImage(victoriaResultImg2)
                victoriaResultImageLabel2 = tk.Label(uniResultsFrame3b, image=victoriaResultPhoto2)
                victoriaResultImageLabel2.image = victoriaResultPhoto2
            #Gridding Assets Onto Frames
                McGillResultLabel2.grid(row=1,column=3,sticky=tk.N)
                McGillResultRatingLabel2.grid(row=1, column=5,sticky=tk.N + tk.W)
                McGillResultSummary2.grid(row=2,rowspan=1,column=3, columnspan = 5)
                McGillResultImageLabel2.grid(row=1,column=1,padx=10,rowspan=3)
                
                torontoResultLabel2.grid(row=1,column=3,sticky=tk.N)
                torontoResultRatingLabel2.grid(row=1, column=5,sticky=tk.N)
                torontoResultSummary2.grid(row=2,rowspan=1,column=3, columnspan = 5)
                torontoResultImageLabel2.grid(row=1,column=1,padx=10,rowspan=3)
                
                victoriaResultLabel2.grid(row=1,column=3,sticky=tk.N)
                victoriaResultRatingLabel2.grid(row=1, column=5,sticky=tk.N)
                victoriaResultSummary2.grid(row=2,rowspan=1,column=3, columnspan = 5,sticky=tk.N)
                victoriaResultImageLabel2.grid(row=1,column=1,padx=10,rowspan=3)
            elif sub[1] == "Computer Science":
            #Button Settings
                uni1ResultsLearnButton2.config(command = lambda: learnMore(waterlooUniLabel))
                uni1ResultsFavsButton2.config(command = lambda: addToFavs(waterlooUniLabel))

                uni2ResultsLearnButton2.config(command = lambda: learnMore(guelphUniLabel))
                uni2ResultsFavsButton2.config(command = lambda: addToFavs(guelphUniLabel))

                uni3ResultsLearnButton2.config(command = lambda: learnMore(windsorUniLabel))
                uni3ResultsFavsButton2.config(command = lambda: addToFavs(windsorUniLabel))
        #Waterloo Assets
                waterlooResultUniLabel2 = ttk.Label(uniResultsFrame1b,style='uniLableY.TLabel',text = "University of Waterloo", justify='center')
                waterlooResultRatingLabel2 = ttk.Label(uniResultsFrame1b,style='uniLableY.TLabel',text = "-Ranked #9 in Canada", justify='center',foreground = 'red4')
                waterlooResultSummary2 = tk.Text(uniResultsFrame1b,height=8,width=95, background = '#ffffb3')
                waterlooResultSummary2.tag_configure('main', foreground="red4",font=('Courier', 14))
                waterlooResultSummary2.insert(tk.END, '''The University of Waterloo’s computer science program is fairly
competitive, and students applying will require an average between
%90 - %100. Along with that, tuition comes at a hefty price for
both domestic and international students, ranging from approximately
$17 000 (domestic) to $33 000(international) per year, including
ancillary fees.''', 'main') 
                waterlooResultSummary2.configure(state="disabled")
                waterlooResultImg2 = Image.open("waterloo#1.jpg").resize((175, 175))
                waterlooResultPhoto2 = ImageTk.PhotoImage(waterlooResultImg2)
                waterlooResultImageLabel2 = tk.Label(uniResultsFrame1b, image=waterlooResultPhoto2)
                waterlooResultImageLabel2.image = waterlooResultPhoto2
            #Guelph Assets
                guelphResultUniLabel2 = ttk.Label(uniResultsFrame2b,style='uniLableY.TLabel',text = "University of Guelph", justify='center')
                guelphResultRatingLabel2 = ttk.Label(uniResultsFrame2b,style='uniLableY.TLabel',text = "-Ranked #19 in Canada", justify='center',foreground = 'red4')
                guelphResultSummary2 = tk.Text(uniResultsFrame2b,height=8,width=95, background = '#ffffb3')
                guelphResultSummary2.tag_configure('main', foreground="red4",font=('Courier', 14))
                guelphResultSummary2.insert(tk.END, '''The University of Guelph’s computer science program is very
promising, as students applying will require an average between
%80 - %89 to have a good chance at acceptance. Along with that,
tuition comes at a mid-range price for both domestic and
international students, ranging from approximately $7 000
(domestic) to $22 000 (international) per year.''', 'main')
                guelphResultSummary2.configure(state="disabled")
                guelphResultImg2 = Image.open("guelph#1.jpg").resize((175, 175))
                guelphResultPhoto2 = ImageTk.PhotoImage(guelphResultImg2)
                guelphResultImageLabel2 = tk.Label(uniResultsFrame2b, image=guelphResultPhoto2)
                guelphResultImageLabel2.image = guelphResultPhoto2

            #Windsor Assets
                windsorResultUniLabel2 = ttk.Label(uniResultsFrame3b,style='uniLableY.TLabel',text = "University of Windsor", justify='center')
                windsorResultRatingLabel2 = ttk.Label(uniResultsFrame3b,style='uniLableY.TLabel',text = "-Ranked #22 in Canada", justify='center',foreground = 'red4')
                windsorResultSummary2 = tk.Text(uniResultsFrame3b,height=8,width=95, background = '#ffffb3')
                windsorResultSummary2.tag_configure('main', foreground="red4",font=('Courier', 13))
                windsorResultSummary2.insert(tk.END, '''The University of Windsor’s computer science program is not very difficult
to get into, as students applying will require an average in the mid
to high %70s range to have feel confident about their applications.
Along with that, tuition comes at an affordable price for both domestic
and international students, ranging from approximately $5 500(domestic)
to $14 000 (international) per year, including ancillary fees.''', 'main')
                windsorResultSummary2.configure(state="disabled")
                windsorResultImg2 = Image.open("windsor#1.jpg").resize((175, 175))
                windsorResultPhoto2 = ImageTk.PhotoImage(windsorResultImg2)
                windsorResultImageLabel2 = tk.Label(uniResultsFrame3b, image=windsorResultPhoto2)
                windsorResultImageLabel2.image = windsorResultPhoto2
            #Gridding Assets Onto Frames
                waterlooResultUniLabel2.grid(row=1,column=3,sticky=tk.N)
                waterlooResultRatingLabel2.grid(row=1, column=5,sticky=tk.N + tk.W)
                waterlooResultSummary2.grid(row=2,rowspan=1,column=3, columnspan = 5)
                waterlooResultImageLabel2.grid(row=1,column=1,padx=10,rowspan=3)
                
                guelphResultUniLabel2.grid(row=1,column=3,sticky=tk.N)
                guelphResultRatingLabel2.grid(row=1, column=5,sticky=tk.N)
                guelphResultSummary2.grid(row=2,rowspan=1,column=3, columnspan = 5)
                guelphResultImageLabel2.grid(row=1,column=1,padx=10,rowspan=3)
                
                windsorResultUniLabel2.grid(row=1,column=3,sticky=tk.N)
                windsorResultRatingLabel2.grid(row=1, column=5,sticky=tk.N)
                windsorResultSummary2.grid(row=2,rowspan=1,column=3, columnspan = 5,sticky=tk.N)
                windsorResultImageLabel2.grid(row=1,column=1,padx=10,rowspan=3)
            
            #High    
            if 14500 <= budgetVar.get() and avgVar.get() == '90%-100%' and citizenVar.get() == "No" or avgVar.get() == '90%-100%' and citizenVar.get() == "Yes":
                if sub[1] == "Biology" or sub[1] == "Computer Science":
                    uniResultsFrame1b.grid(row=2,column=2,columnspan=5,pady=10)
                    uniResultsFrame2b.grid(row=3,column=2,columnspan=5,pady=10)
                else:
                    pass
            #Mid
            elif 14500 <= budgetVar.get() and avgVar.get() == '80%-89%' and citizenVar.get() == "No" or avgVar.get() == '80%-89%' and citizenVar.get() == "Yes" or 9500 <= budgetVar.get() < 14500 and avgVar.get() == '80%-89%' and citizenVar.get() == "No":
                if sub[1] == "Biology" or sub[1] == "Computer Science":
                    uniResultsFrame2b.grid(row=2,column=2,columnspan=5,pady=10)
                    uniResultsFrame3b.grid(row=3,column=2,columnspan=5,pady=10)
                else:
                    pass
            #Low
            elif avgVar.get() == '<80%' or budgetVar.get() < 9500 and citizenVar.get() == "No":
                if sub[1] == "Biology" or sub[1] == "Computer Science":
                    uniResultsFrame3b.grid(row=2,column=2,columnspan=5,pady=10)
                    uniResultsFrame2b.grid(row=3,column=2,columnspan=5,pady=10)
                else:
                    pass
        root.withdraw()
    
    
  
def changeScreen(frameFrom, frameTo):
    frameTo.grid(padx = 10, pady = 10)
    frameFrom.grid_remove()
    
    if frameTo == surveyFrame or frameTo == surveyFrame2:
        root.config(background='#ffcccc')
    elif frameTo == browseFrame:
        root.config(background='#ffffb3')
    elif frameTo == mainframe:
        root.config(background='#ddccff')
    
def gridUnis(var):
    global sortSub
    sortSub = []
    sort = sortVar.get()
    subject = var.get()
    libLabel.config(text=f'University Library for {subject}')

    unisList = [uniFrame1, uniFrame2, uniFrame3]
    for frame in unisList:

        uniWidgetlist = frame.winfo_children()

        for item in uniWidgetlist :
            if item.winfo_children() :
                 uniWidgetlist.append(item.winfo_children())
                 
        for widget in uniWidgetlist:
            widget.grid_forget()
    if subject == "Biology" or subject == "Computer Science":       
        uni1LearnButton.grid(row=2, column=8, columnspan=2,sticky=tk.N + tk.E)
        uni1FavsButton.grid(row=2, column=8, columnspan=2,sticky=tk.S + tk.E)

        uni2LearnButton.grid(row=2, column=8, columnspan=2,sticky=tk.N + tk.E)
        uni2FavsButton.grid(row=2, column=8, columnspan=2,sticky=tk.S + tk.E)

        uni3LearnButton.grid(row=2, column=8, columnspan=2,sticky=tk.N + tk.E)
        uni3FavsButton.grid(row=2, column=8, columnspan=2,sticky=tk.S + tk.E)
        if subject == "Biology":
            sortSub.append("Biology")
            uni1LearnButton.config(command = lambda: learnMore(McGillUniLabel))
            uni1FavsButton.config(command = lambda: addToFavs(McGillUniLabel))
            McGillUniLabel.grid(row=1,column=3,sticky=tk.N)
            McGillRatingLabel.grid(row=1, column=5,sticky=tk.N + tk.W)
            McGillSummary.grid(row=2,rowspan=1,column=3, columnspan = 5)
            
            uni2LearnButton.config(command = lambda: learnMore(torontoUniLabel))
            uni2FavsButton.config(command = lambda: addToFavs(torontoUniLabel))
            torontoUniLabel.grid(row=1,column=3,sticky=tk.N)
            torontoRatingLabel.grid(row=1, column=5,sticky=tk.N)
            torontoSummary.grid(row=2,rowspan=1,column=3, columnspan = 5)
            
            
            uni3LearnButton.config(command = lambda: learnMore(victoriaUniLabel))
            uni3FavsButton.config(command = lambda: addToFavs(victoriaUniLabel))
            victoriaUniLabel.grid(row=1,column=3,sticky=tk.N)
            victoriaRatingLabel.grid(row=1, column=5,sticky=tk.N)
            victoriaSummary.grid(row=2,rowspan=1,column=3, columnspan = 5,sticky=tk.N)
            
            
            McGillImageLabel.grid(row=1,column=1,rowspan=3,columnspan=2)
            torontoImageLabel.grid(row=1,column=1,rowspan=3)
            victoriaImageLabel.grid(row=1,column=1,rowspan=3)
            if sortVar.get() == 'Ranking (Highest)':
                uniFrame1.grid(row = 4, column=1, columnspan=8,pady=5)
                uniFrame2.grid(row = 3, column=1, columnspan=8,pady=5)
                uniFrame3.grid(row = 5, column=1, columnspan=8,pady=5)
            elif sortVar.get() == 'Tuition (Highest)':
                uniFrame1.grid(row = 3, column=1, columnspan=8,pady=5)
                uniFrame2.grid(row = 4, column=1, columnspan=8,pady=5)
                uniFrame3.grid(row = 5, column=1, columnspan=8,pady=5)
            elif sortVar.get() == 'Main Campus Size':
                uniFrame1.grid(row = 3, column=1, columnspan=8,pady=5)
                uniFrame2.grid(row = 5, column=1, columnspan=8,pady=5)
                uniFrame3.grid(row = 4, column=1, columnspan=8,pady=5)
        elif subject == "Computer Science":
            sortSub.append("Computer Science")
            uni1LearnButton.config(command = lambda: learnMore(waterlooUniLabel))
            uni1FavsButton.config(command = lambda: addToFavs(waterlooUniLabel))
            waterlooUniLabel.grid(row=1,column=3,sticky=tk.N)
            waterlooRatingLabel.grid(row=1, column=5,sticky=tk.N)
            waterlooSummary.grid(row=2,rowspan=1,column=3, columnspan = 5)
            
            uni2LearnButton.config(command = lambda: learnMore(guelphUniLabel))
            uni2FavsButton.config(command = lambda: addToFavs(guelphUniLabel))
            guelphUniLabel.grid(row=1,column=3,sticky=tk.N)
            guelphRatingLabel.grid(row=1, column=5,sticky=tk.N + tk.W)
            guelphSummary.grid(row=2,rowspan=1,column=3, columnspan = 5)
        
            uni3LearnButton.config(command = lambda: learnMore(windsorUniLabel))
            uni3FavsButton.config(command = lambda: addToFavs(windsorUniLabel))
            windsorUniLabel.grid(row=1,column=3,sticky=tk.N)
            windsorRatingLabel.grid(row=1, column=5,sticky=tk.N)
            windsorSummary.grid(row=2,rowspan=1,column=3, columnspan = 5,sticky=tk.N)
            
            
            waterlooImageLabel.grid(row=1,column=1,rowspan=3)
            guelphImageLabel.grid(row=1,column=1,rowspan=3)
            windsorImageLabel.grid(row=1,column=1,rowspan=3)
            if sortVar.get() == 'Ranking (Highest)':
                uniFrame1.grid(row = 3, column=1, columnspan=8,pady=5)
                uniFrame2.grid(row = 4, column=1, columnspan=8,pady=5)
                uniFrame3.grid(row = 5, column=1, columnspan=8,pady=5)
            elif sortVar.get() == 'Tuition (Highest)':
                uniFrame1.grid(row = 3, column=1, columnspan=8,pady=5)
                uniFrame2.grid(row = 4, column=1, columnspan=8,pady=5)
                uniFrame3.grid(row = 5, column=1, columnspan=8,pady=5)
            elif sortVar.get() == 'Main Campus Size':
                uniFrame1.grid(row = 4, column=1, columnspan=8,pady=5)
                uniFrame2.grid(row = 3, column=1, columnspan=8,pady=5)
                uniFrame3.grid(row = 5, column=1, columnspan=8,pady=5)
    else:
        uniFrame1.grid(row = 3, column=1, columnspan=8,pady=5)
        uniFrame2.grid(row = 4, column=1, columnspan=8,pady=5)
        uniFrame3.grid(row = 5, column=1, columnspan=8,pady=5)
        imageFrame.grid(row=1,column=1)
        imageFrame2.grid(row=1,column=1)
        imageFrame3.grid(row=1,column=1)
        

def sort(event):
    global sortSub
    sortSubLength = len(sortSub)
    if sortSubLength == 0:
        pass
    elif sortSubLength == 1:
        if sortSub[0] == "Biology":
            if sortVar.get() == 'Ranking (Highest)':
                uniFrame1.grid(row = 4, column=1, columnspan=8,pady=5)
                uniFrame2.grid(row = 3, column=1, columnspan=8,pady=5)
                uniFrame3.grid(row = 5, column=1, columnspan=8,pady=5)
            elif sortVar.get() == 'Tuition (Highest)':
                uniFrame1.grid(row = 3, column=1, columnspan=8,pady=5)
                uniFrame2.grid(row = 4, column=1, columnspan=8,pady=5)
                uniFrame3.grid(row = 5, column=1, columnspan=8,pady=5)
            elif sortVar.get() == 'Main Campus Size':
                uniFrame1.grid(row = 3, column=1, columnspan=8,pady=5)
                uniFrame2.grid(row = 5, column=1, columnspan=8,pady=5)
                uniFrame3.grid(row = 4, column=1, columnspan=8,pady=5)
        elif sortSub[0] == "Computer Science":
            if sortVar.get() == 'Ranking (Highest)':
                uniFrame1.grid(row = 3, column=1, columnspan=8,pady=5)
                uniFrame2.grid(row = 4, column=1, columnspan=8,pady=5)
                uniFrame3.grid(row = 5, column=1, columnspan=8,pady=5)
            elif sortVar.get() == 'Tuition (Highest)':
                uniFrame1.grid(row = 3, column=1, columnspan=8,pady=5)
                uniFrame2.grid(row = 4, column=1, columnspan=8,pady=5)
                uniFrame3.grid(row = 5, column=1, columnspan=8,pady=5)
            elif sortVar.get() == 'Main Campus Size':
                uniFrame1.grid(row = 4, column=1, columnspan=8,pady=5)
                uniFrame2.grid(row = 3, column=1, columnspan=8,pady=5)
                uniFrame3.grid(row = 5, column=1, columnspan=8,pady=5)

def favsDel():
    global f
    f.destroy()
    favs()

def favs():
    global favList , t 
    numberOfFavs = len(favList)
    t = tk.Toplevel()
    t.resizable(False, False)
    t.config(background='#ddccff')
    favsFrame = tk.Frame(t)
    favsFrame.grid(padx=10,pady=10)
    favsFrame.config(background='#eee6ff')
    if numberOfFavs == 0:
        favTitle = ttk.Label(favsFrame,text = f"No Favourties Yet!", justify ='center',background='#eee6ff')
        favTitle.grid(row=1,column=2,columnspan=1,sticky=tk.E)

    else:
        for i in favList:
            favUni = ttk.Label(favsFrame,text = f'{i["text"]}',style = 'sub.TLabel', justify ='left',background='#eee6ff')
            if i == favList[0]:
                fav1 = ttk.Label(favsFrame,text = '1.', justify ='left',background='#eee6ff')
                favLearnButton = ttk.Button(favsFrame,text="Learn More",command = lambda: learnMore(favList[0]),width =13)
                favRemoveButton = ttk.Button(favsFrame,text="Remove",command = lambda: remove(favList[0]),width =13)
                fav1.grid(row=2, column=1,pady=10)
                favUni.grid(row=2, column=2,padx=5,pady=10)
                favLearnButton.grid(row=2,column=3,padx=5,pady=10)
                favRemoveButton.grid(row=2,column=4,padx=5,pady=10)
            elif i == favList[1]:
                fav2 = ttk.Label(favsFrame,text = '2.', justify ='left',background='#eee6ff')
                favLearnButton = ttk.Button(favsFrame,text="Learn More",command = lambda: learnMore(favList[1]),width =13)
                favRemoveButton = ttk.Button(favsFrame,text="Remove",command = lambda: remove(favList[1]),width =13)
                fav2.grid(row=3, column=1,pady=10)
                favUni.grid(row=3, column=2,padx=5,pady=10)
                favLearnButton.grid(row=3,column=3,padx=5,pady=10)
                favRemoveButton.grid(row=3,column=4,padx=5,pady=10)
            elif i == favList[2]:
                fav3 = ttk.Label(favsFrame,text = '3.', justify ='left',background='#eee6ff')
                favLearnButton = ttk.Button(favsFrame,text="Learn More",command = lambda: learnMore(favList[2]),width =13)
                favRemoveButton = ttk.Button(favsFrame,text="Remove",command = lambda: remove(favList[2]),width =13)
                fav3.grid(row=4, column=1,pady=10)
                favUni.grid(row=4, column=2,padx=5,pady=10)
                favLearnButton.grid(row=4,column=3,padx=5,pady=10)
                favRemoveButton.grid(row=4,column=4,padx=5,pady=10)

        favTitle = ttk.Label(favsFrame,text = f"Favourite Universities", justify ='center',background='#eee6ff')
        favTitle.grid(row=1,column=2, columnspan=2)

def remove(uniLabel):
    global favList , t
    t.destroy()
    favList.remove(uniLabel)
    favs()
    r = tk.Toplevel()
    r.resizable(False, False)
    r.config(background='#ddccff')
    removedFrame = tk.Frame(r)
    removedFrame.grid(padx=10,pady=10)
    removedFrame.config(background='#eee6ff')
    removedLabel = ttk.Label(removedFrame,text = f"{uniLabel['text']} has been removed from your favourites list.", justify ='center',background='#eee6ff')
    removedLabel.grid(row=1,column=1)
def checkBoxes(checkboxVar):
    global length,sub
    counter = 0
    sub=[]
    if artCheckVar.get() == "Art":
        counter+=1
        sub.append(artCheckVar.get())
    if mathCheckVar.get() == "Mathematics":
        counter+=1
        sub.append(mathCheckVar.get())
    if literatureCheckVar.get() == "Literature":
        counter+=1
        sub.append(literatureCheckVar.get())
    if histCheckVar.get() == "History":
        counter+=1
        sub.append(histCheckVar.get())
    if physCheckVar.get() == "Physics":
        counter+=1
        sub.append(physCheckVar.get())
    if chemCheckVar.get() == "Chemistry":
        counter+=1
        sub.append(chemCheckVar.get())
    if bioCheckVar.get() == "Biology":
        counter+=1
        sub.append(bioCheckVar.get())
    if compCheckVar.get() == "Computer Science":
        counter+=1
        sub.append(compCheckVar.get())
    if counter > 2:
        subIndx = sub.index(checkboxVar.get())
        checkboxVar.set(0)
        sub.pop(subIndx)
        alert = tk.Toplevel()
        alert.resizable(False, False)
        alert.config(background='#ffcccc')
        
        alertFrame = tk.Frame(alert)
        alertFrame.grid(padx=10,pady=10)
        alertFrame.config(background='#ffe6e6')
        
        alertMessage = ttk.Label(alertFrame,text = "You Can Only Select Two Subjects!", justify='center',background='#ffe6e6')
        alertMessage.grid(row=1,column=1)
        winsound.PlaySound("error.wav", winsound.SND_ASYNC)
    length = len(sub)
    if length == 2:
        subjectLabel.config(text=f'Choose 1-2 Favourite Subjects: {sub[0]} and {sub[1]}')
    elif length == 1:
        subjectLabel.config(text=f'Choose 1-2 Favourite Subjects: {sub[0]}')
    elif length == 0:
        subjectLabel.config(text=f'Choose 1-2 Favourite Subjects:')

def addToFavs(uniLabel):
    global favList , f
    numberOfFavs = len(favList)
    f = tk.Toplevel()
    f.resizable(False, False)
    f.config(background='#ddccff')
    addedFavsFrame = tk.Frame(f)
    addedFavsFrame.grid(padx=10,pady=10)
    addedFavsFrame.config(background='#eee6ff')
    if uniLabel in favList:
        favLabel = ttk.Label(addedFavsFrame,text = f'{uniLabel["text"]} has already been added to your favourties!', justify ='center',background='#ffe6e6')
        f.config(background='#ffcccc')
        addedFavsFrame.config(background='#ffe6e6')
        winsound.PlaySound("error.wav", winsound.SND_ASYNC)
    elif uniLabel not in favList and numberOfFavs < 3:
        favLabel = ttk.Label(addedFavsFrame,text = f'{uniLabel["text"]} has been added to your favourties!', justify ='center',background='#eee6ff')
        
        favList.append(uniLabel)
    elif numberOfFavs == 3:
        f.config(background='#ffffb3')
        addedFavsFrame.config(background='#ffffe6')
        favLabel = ttk.Label(addedFavsFrame,text = f'Maximum of three items in your favourites, please remove one to add more.', justify ='center',background='#ffffe6') 
        winsound.PlaySound("error.wav", winsound.SND_ASYNC)
    favsButton2 = ttk.Button(addedFavsFrame,text="Favourites List",command = favsDel,width =15)
    addedFavsFrame.grid(padx=10,pady=10)
    favLabel.grid(row=1,column=1, columnspan=3)
    favsButton2.grid(row=2,column=2)
    
    

def learnMore(uniLabel):
    title = uniLabel
    l = tk.Toplevel()
    l.resizable(False, False)
    l.config(background='#ffcccc')
    learnMoreFrame = tk.Frame(l)
    learnMoreFrame.config(background='#ffe6e6')
    learnMoreFrame.grid(padx=10,pady=10)
#Waterloo
    waterlooLearnImg = Image.open("waterloo#1.jpg").resize((175, 175))
    waterlooLearnPhoto = ImageTk.PhotoImage(waterlooLearnImg)
    waterlooLearnImageLabel = tk.Label(learnMoreFrame, image=waterlooLearnPhoto)
    waterlooLearnImageLabel.image = waterlooLearnPhoto
    waterlooDescription = tk.Text(learnMoreFrame, height=20,width=115, background = '#ffe6e6')
    waterlooDescription.tag_configure('main', foreground="purple4",font=('Courier', 14),justify='center')
    waterlooDescription.insert(tk.END, '''
The University of Waterloo’s computer science program is fairly competitive,
and students applying will require an average between %90 - %100. Along with
that, tuition comes at a hefty price for both domestic and international
students, ranging from approximately $17 000 (domestic) to $33 000
(international) per year, including ancillary fees.  The University of
Waterloo, located in Waterloo, Ontario, houses a fantastic computer science
faculty, and offers a wide selection of computer science programs in the fields
of artificial intelligence, information security, programming, and more. The
entire campus covers an area of approximately 450 hectares, with upwards of
36 000 students attending each year. The University of Waterloo is ranked 9th
in Canada, and in the top 200 among other universities in the world, as of the
present day. Undergraduates who graduate from this university will receive a
bachelor’s of computer science.''','main')
    waterlooDescription.configure(state="disabled")
    waterloo2Img = Image.open("waterloo#2.jpg").resize((175, 175))
    waterloo2Photo = ImageTk.PhotoImage(waterloo2Img)
    waterloo2ImageLabel = tk.Label(learnMoreFrame, image=waterloo2Photo)
    waterloo2ImageLabel.image = waterloo2Photo
#Guelph
    guelphLearnImg = Image.open("guelph#1.jpg").resize((175, 175))
    guelphLearnPhoto = ImageTk.PhotoImage(guelphLearnImg)
    guelphLearnImageLabel = tk.Label(learnMoreFrame, image=guelphLearnPhoto)
    guelphLearnImageLabel.image = guelphLearnPhoto
    guelphDescription = tk.Text(learnMoreFrame, height=20,width=115, background = '#ffe6e6')
    guelphDescription.tag_configure('main', foreground="purple4",font=('Courier', 14),justify='center')
    guelphDescription.insert(tk.END, '''
The University of Guelph’s computer science program is very promising, as students
applying will require an average between %80 - %89 to have a good chance at
acceptance. Along with that, tuition comes at a mid-range price for both domestic
and international students, ranging from approximately $7 000 (domestic) to
$22 000 (international) per year. The University of Guelph, located in Guelph,
Ontario, offers great computer science programs, where students can gain knowledge
about new technologies, deal with problem solving through several everyday issues
faced with software development, and generally become accustomed to an applied
academic foundation.The entire campus covers an area of approximately 589 hectares,
with upwards of 30 000 students attending each year. The University of Guelph is
ranked 19th in Canada, and in the top 600th among other universities in the world,
as of the present day. Undergraduates who graduate from this university will
receive a bachelor’s of computing. ''','main')
    guelphDescription.configure(state="disabled")
    guelph2Img = Image.open("guelph#2.jpg").resize((175, 175))
    guelph2Photo = ImageTk.PhotoImage(guelph2Img)
    guelph2ImageLabel = tk.Label(learnMoreFrame, image=guelph2Photo)
    guelph2ImageLabel.image = guelph2Photo
#Windsor
    windsorLearnImg = Image.open("windsor#1.jpg").resize((175, 175))
    windsorLearnPhoto = ImageTk.PhotoImage(windsorLearnImg)
    windsorLearnImageLabel = tk.Label(learnMoreFrame, image=windsorLearnPhoto)
    windsorLearnImageLabel.image = windsorLearnPhoto
    windsorDescription = tk.Text(learnMoreFrame, height=20,width=115, background = '#ffe6e6')
    windsorDescription.tag_configure('main', foreground="purple4",font=('Courier', 14),justify='center')
    windsorDescription.insert(tk.END, '''
The University of Windsor’s computer science program is not very difficult to get
into, as students applying will require an average in the mid to high %70s range
to have feel confident about their applications. Along with that, tuition comes
at an affordable price for both domestic and international students, ranging from
approximately $5 500 (domestic) to $14 000 (international) per year, including
ancillary fees. The University of Windsor , located in Windsor, Ontario, does a
good job introducing computer science to students through its many programs, in
areas such as software designs, computing, and networking. The entire campus
covers an area of approximately 51 hectares, with upwards of 16 000 students
attending each year. The University of Windsor is ranked 22nd in Canada, and in
the top 800 among other universities in the world, as of the present day.
Undergraduates who graduate from this university will receive a bachelor’s of
computer science. ''','main')
    windsorDescription.configure(state="disabled")
    windsor2Img = Image.open("windsor#2.jpg").resize((175, 175))
    windsor2Photo = ImageTk.PhotoImage(windsor2Img)
    windsor2ImageLabel = tk.Label(learnMoreFrame, image=windsor2Photo)
    windsor2ImageLabel.image = windsor2Photo
#McGill
    McGillLearnImg = Image.open("McGill#1.jpg").resize((175, 175))
    McGillLearnPhoto = ImageTk.PhotoImage(McGillLearnImg)
    McGillLearnImageLabel = tk.Label(learnMoreFrame, image=McGillLearnPhoto)
    McGillLearnImageLabel.image = McGillLearnPhoto
    McGillDescription = tk.Text(learnMoreFrame, height=20,width=115, background = '#ffe6e6')
    McGillDescription.tag_configure('main', foreground="purple4",font=('Courier', 14),justify='center')
    McGillDescription.insert(tk.END, '''
The University of McGill’s life sciences program is fairly competitive, and
students applying will require an average between %90 - %100. Along with that,
tuition comes at a hefty price for both domestic and international students,
ranging from approximately $9 000 (domestic) to $20 000 (international) per year,
including ancillary fees.  The University of McGill, located in Montreal, Quebec,
houses a fantastic biology faculty, and offers a wide selection of life science
programs in the fields of health, psychology, animal/plant biology, and more.
Its campuses cover an area of approximately 650  hectares, with upwards of 40
500 students attending each year. The University of McGill is ranked 3rd in Canada,
and in the top 50 among other universities in the world, as of 2019. Undergraduates
who graduate from this university will receive a bachelor’s of science, and can
choose to specialize into many different professions.''','main')
    McGillDescription.configure(state="disabled")
    McGill2Img = Image.open("McGill#2.jpg").resize((175, 175))
    McGill2Photo = ImageTk.PhotoImage(McGill2Img)
    McGill2ImageLabel = tk.Label(learnMoreFrame, image=McGill2Photo)
    McGill2ImageLabel.image = McGill2Photo
#Toronto
    torontoLearnImg = Image.open("toronto#1.jpg").resize((175, 175))
    torontoLearnPhoto = ImageTk.PhotoImage(torontoLearnImg)
    torontoLearnImageLabel = tk.Label(learnMoreFrame, image=torontoLearnPhoto)
    torontoLearnImageLabel.image = torontoLearnPhoto
    torontoDescription = tk.Text(learnMoreFrame, height=20,width=115, background = '#ffe6e6')
    torontoDescription.tag_configure('main', foreground="purple4",font=('Courier', 14),justify='center')
    torontoDescription.insert(tk.END, '''
The University of Toronto’s biology  programs are marvelous, with students
requiring an average between %80 - %89 to have a good chance at acceptance. Along
with that, tuition comes at a mid-range price for both domestic and international
students, ranging from approximately $7 000 (domestic), and a difficult $45 000
(international)per year. The University of Toronto, located in Toronto, Ontario
(main campus), offers wide selection of life science programs, where students can
gain knowledge about physiotherapy, nursing, the medical field, and more. The
Toronto campus covers an area of approximately 71 hectares, with upwards of 61 000
students attending each year. The University of Toronto is ranked 1st in Canada,
and in the top 25 among other universities in the world, as of the present day.
Undergraduates who graduate from this university will receive a bachelor’s of
science, and have the freedom to specialize it into a variety of careers. ''','main')
    torontoDescription.configure(state="disabled")
    toronto2Img = Image.open("toronto#2.jpg").resize((175, 175))
    toronto2Photo = ImageTk.PhotoImage(toronto2Img)
    toronto2ImageLabel = tk.Label(learnMoreFrame, image=toronto2Photo)
    toronto2ImageLabel.image = toronto2Photo
#Victoria
    victoriaLearnImg = Image.open("victoria#1.jpg").resize((175, 175))
    victoriaLearnPhoto = ImageTk.PhotoImage(victoriaLearnImg)
    victoriaLearnImageLabel = tk.Label(learnMoreFrame, image=victoriaLearnPhoto)
    victoriaLearnImageLabel.image = victoriaLearnPhoto
    victoriaDescription = tk.Text(learnMoreFrame, height=20,width=115, background = '#ffe6e6')
    victoriaDescription.tag_configure('main', foreground="purple4",font=('Courier', 14),justify='center')
    victoriaDescription.insert(tk.END, '''
The University of Victoria’s life science program is not very difficult to get
into, as students applying will require an average in the mid to high %70s range
to have feel confident about their applications. Along with that, tuition comes
at an affordable price for both domestic and international students, ranging from
approximately $6 428 (domestic) to $20 000 (international) per year, including
ancillary fees. The University of Victoria , located in Victoria, British Columbia,
does a good job introducing life science to students through its many programs,
in areas such as bioengineering, veterinary science, and health education. The
entirecampus covers an area of approximately 163 hectares, with upwards of 21 000
students attending each year. The University of Victoria is ranked 15th in Canada,
and in the top 350 among other universities in the world, as of the present day.
Undergraduateswho graduate from this university will receive a bachelor’s of
science, and have the freedom to specialize it into a variety of careers.''','main')
    victoriaDescription.configure(state="disabled")
    victoria2Img = Image.open("victoria#2.jpg").resize((175, 175))
    victoria2Photo = ImageTk.PhotoImage(victoria2Img)
    victoria2ImageLabel = tk.Label(learnMoreFrame, image=victoria2Photo)
    victoria2ImageLabel.image = victoria2Photo

    uniTitle = ttk.Label(learnMoreFrame , text = f'{uniLabel["text"]}',background='#ffe6e6')
    uniTitle.grid(row=1,column=5,sticky=tk.N)
    if uniLabel== waterlooUniLabel:
        waterlooLearnImageLabel.grid(row=1,column=1,rowspan=3)
        waterloo2ImageLabel.grid(row=4,column=1,rowspan=3)
        waterlooDescription.grid(row=2,column=3,columnspan=5,rowspan=6)
    elif uniLabel == guelphUniLabel:
        guelphLearnImageLabel.grid(row=1,column=1,rowspan=3)
        guelph2ImageLabel.grid(row=4,column=1,rowspan=3)
        guelphDescription.grid(row=2,column=3,columnspan=5,rowspan=6)
    elif uniLabel == windsorUniLabel:
        windsorLearnImageLabel.grid(row=1,column=1,rowspan=3)
        windsor2ImageLabel.grid(row=4,column=1,rowspan=3)
        windsorDescription.grid(row=2,column=3,columnspan=5,rowspan=6)
    elif uniLabel == torontoUniLabel:
        torontoLearnImageLabel.grid(row=1,column=1,rowspan=3)
        toronto2ImageLabel.grid(row=4,column=1,rowspan=3)
        torontoDescription.grid(row=2,column=3,columnspan=5,rowspan=6)
    elif uniLabel == victoriaUniLabel:
        victoriaLearnImageLabel.grid(row=1,column=1,rowspan=3)
        victoria2ImageLabel.grid(row=4,column=1,rowspan=3)
        victoriaDescription.grid(row=2,column=3,columnspan=5,rowspan=6)
    elif uniLabel == McGillUniLabel:
        McGillLearnImageLabel.grid(row=1,column=1,rowspan=3)
        McGill2ImageLabel.grid(row=4,column=1,rowspan=3)
        McGillDescription.grid(row=2,column=3,columnspan=5,rowspan=6)
def displayName(event):
    if event.char in string.printable:
        name = nameVar.get() + event.char
    elif event.keysym == 'BackSpace':
        name = nameVar.get()[0:-1]
    else:
        name = nameVar.get()
    nameLabel.config(text = f'Name: {name}')
def displayAvg():
    if avgVar.get() == "":
        avgLabel.config(text=f'Average Range:')
    else:
        avgLabel.config(text=f'Average Range: {avgVar.get()}')
def displayBudget(event):
    budgetLabel.config(text=f'Budget For Total Expenses($ Per Year): ${budgetVar.get()}')    
#########
#Widgets
    #MAINFRAME

bgImg = Image.open("a.jpg").resize((450,300))
bgImg.putalpha(150)
bgPhoto = ImageTk.PhotoImage(bgImg)
backgroundImage=tk.PhotoImage()
backgroundLabel = tk.Label(mainframe, image=bgPhoto)

welcomeLabel = ttk.Label(mainframe,text = "Welcome to the Post-Secondary Guidance Program!\nHaving trouble figuring out where to go after high school?", justify='center',background='#eee6ff')

startButton = ttk.Button(mainframe,  text="Start",command = lambda: changeScreen(mainframe, surveyFrame))
startLabel = ttk.Label(mainframe,justify='center',style= 'sub.TLabel', text = "the questionnaire today!",background='#eee6ff')

orLabel = ttk.Label(mainframe,style= 'Mblue.TLabel', text = "and always feel free to")

browseButton = ttk.Button(mainframe,  text="Browse",command = lambda: changeScreen(mainframe, browseFrame))
browseLabel = ttk.Label(mainframe, justify='center',style= 'sub.TLabel', text = "our full university library!",background='#eee6ff')
hamzahLabel = ttk.Label(mainframe, justify='center', text = "By Hamzah Behery",background='#eee6ff', foreground="#ffbf00", font=('Courier', 15))

    #SURVEYFRAME
futureLabel = ttk.Label(surveyFrame, text = "Find Your Future", justify='center',background='#ffe6e6')
promptLabel = ttk.Label(surveyFrame,style= 'Ssmall.TLabel', text = "Please answer the following questions for optimal results:", justify='center')
nameLabel  = ttk.Label(surveyFrame,style= 'sub.TLabel', text = "Name:", justify='center',background='#ffe6e6')
nameVar = tk.StringVar()
nameVar.set("")
nameEntry = ttk.Entry(surveyFrame, textvariable = nameVar, width = 40, font=('Courier',25))
nameEntry.bind("<Key>", displayName)
subjectLabel = ttk.Label(surveyFrame,style= 'Ssmall.TLabel', text = "Choose 1-2 Favourite Subjects:", justify='center',background='#ffe6e6')
subjectFrame= ttk.LabelFrame(surveyFrame, style = 'Label')

artCheckVar  = tk.StringVar()
artBox = ttk.Checkbutton(subjectFrame, text = "Art", onvalue = "Art", offvalue = 0, variable = artCheckVar,command = lambda: checkBoxes(artCheckVar))

mathCheckVar  = tk.StringVar()
mathBox = ttk.Checkbutton(subjectFrame, text = "Mathematics", onvalue = "Mathematics", offvalue = 0, variable = mathCheckVar,command = lambda: checkBoxes(mathCheckVar))

literatureCheckVar  = tk.StringVar()
literatureBox = ttk.Checkbutton(subjectFrame, text = "Literature", onvalue = "Literature", offvalue = 0, variable = literatureCheckVar,command = lambda: checkBoxes(literatureCheckVar))

chemCheckVar  = tk.StringVar()
chemBox = ttk.Checkbutton(subjectFrame, text = "Chemistry", onvalue = "Chemistry", offvalue = 0, variable = chemCheckVar,command = lambda: checkBoxes(chemCheckVar))

physCheckVar  = tk.StringVar()
physBox = ttk.Checkbutton(subjectFrame, text = "Physics", onvalue = "Physics", offvalue = 0, variable = physCheckVar,command = lambda: checkBoxes(physCheckVar))

histCheckVar  = tk.StringVar()
histBox = ttk.Checkbutton(subjectFrame, text = "History", onvalue = "History", offvalue = 0, variable = histCheckVar,command = lambda: checkBoxes(histCheckVar))

bioCheckVar  = tk.StringVar()
bioBox = ttk.Checkbutton(subjectFrame, text = "Biology", onvalue = "Biology", offvalue = 0, variable = bioCheckVar,command = lambda: checkBoxes(bioCheckVar))

compCheckVar = tk.StringVar()
compBox = ttk.Checkbutton(subjectFrame, text = "Computer Science", onvalue = "Computer Science", offvalue = 0, variable = compCheckVar,command = lambda: checkBoxes(compCheckVar))

nextButton1 = ttk.Button(surveyFrame,  text="Next",command = lambda: changeScreen(surveyFrame, surveyFrame2),width =5)
backButton1 = ttk.Button(surveyFrame,  text="Back",command = lambda: changeScreen(surveyFrame, mainframe),width =5)
    #SURVEYFRAME2
futureLabel2 = ttk.Label(surveyFrame2,text = "Find Your Future", justify='center',background='#ffe6e6')
promptLabel2 = ttk.Label(surveyFrame2,style= 'Ssmall.TLabel', text = "Please answer the following questions for optimal results:", justify='center')
avgLabel  = ttk.Label(surveyFrame2,style= 'sub.TLabel', text = "Average Range:", justify='center',background='#ffe6e6')
avgVar = tk.StringVar()
avgSpinbox = tk.Spinbox(surveyFrame2, textvariable = avgVar, width = 20, font=('Courier',17), values= ["",'<80%','80%-89%','90%-100%'],command = displayAvg,state = 'readonly')
budgetLabel  = ttk.Label(surveyFrame2,style= 'sub.TLabel', text = "Budget For Total Expenses($ Per Year):", justify='center',background='#ffe6e6')
budgetVar = tk.IntVar()
budgetScale = tk.Scale(surveyFrame2, variable = budgetVar, from_=5000, to=45000,resolution=100,orient = 'horizontal',showvalue=True,trough ='#eee6ff',background='#ffe6e6',font=('Courier',17) ,width=35, length=100)
budgetScale.bind("<ButtonRelease-1>", displayBudget)
resultsButton = ttk.Button(surveyFrame2,  text="Results!",command = results,width =8)
backButton2 = ttk.Button(surveyFrame2,  text="Back",command = lambda: changeScreen(surveyFrame2, surveyFrame),width =8)
citizenLabel  = ttk.Label(surveyFrame2,style= 'sub.TLabel', text = "Canadian Citizen/Resident?", justify='center',background='#ffe6e6')
citizenVar = tk.StringVar()
citizenVar.set("")
citizenFrame= ttk.LabelFrame(surveyFrame2, style = 'Label')
yesRadio = ttk.Radiobutton(citizenFrame, variable = citizenVar, text = "Yes", value = "Yes")
noRadio = ttk.Radiobutton(citizenFrame,  variable = citizenVar, text = "No ", value = "No")
    #BROWSEFRAME
artVar = tk.StringVar()
artVar.set("Art")
artButton = ttk.Button(browseFrame,  text=artVar.get(),width =5,style='yellow.TButton',command =lambda:  gridUnis(artVar))

litVar = tk.StringVar()
litVar.set("Literature")
litButton = ttk.Button(browseFrame,  text=litVar.get(),width =10,style='yellow.TButton',command = lambda: gridUnis(litVar))

chemVar = tk.StringVar()
chemVar.set("Chemistry")
chemButton = ttk.Button(browseFrame,  text=chemVar.get(),width =9,style='yellow.TButton',command = lambda: gridUnis(chemVar))

physVar = tk.StringVar()
physVar.set("Physics")
physButton = ttk.Button(browseFrame,  text=physVar.get(),width =7,style='yellow.TButton',command = lambda: gridUnis(physVar))

mathVar = tk.StringVar()
mathVar.set("Mathematics")
mathButton = ttk.Button(browseFrame,  text=mathVar.get(),width =11,style='yellow.TButton',command = lambda: gridUnis(mathVar))

histVar = tk.StringVar()
histVar.set("History")
histButton = ttk.Button(browseFrame,  text=histVar.get(),width =7,style='yellow.TButton',command = lambda: gridUnis(histVar))

bioButtonVar = tk.StringVar()
bioButtonVar.set("Biology")
bioButton = ttk.Button(browseFrame,  text=bioButtonVar.get(),command = lambda: gridUnis(bioButtonVar),width =7)

compButtonVar = tk.StringVar()
compButtonVar.set("Computer Science")
compButton = ttk.Button(browseFrame,  text=compButtonVar.get(),command = lambda: gridUnis(compButtonVar),width =16)

libLabel = ttk.Label(browseFrame,style='browseLable.TLabel',text = "Please Select a Subject from Above", justify='center')

uniFrame1= ttk.LabelFrame(browseFrame, style = 'yellow.Label',width=1200,height=200)
uniFrame1.grid_propagate(False)
imageFrame = ttk.LabelFrame(uniFrame1, style = 'Y.Label',width=175, height = 175)

uniFrame2= ttk.LabelFrame(browseFrame, style = 'yellow.Label',width=1200,height=200)
uniFrame2.grid_propagate(False)
imageFrame2 = ttk.LabelFrame(uniFrame2, style = 'Y.Label',width=175, height = 175)

uniFrame3= ttk.LabelFrame(browseFrame, style = 'yellow.Label',width=1200,height=200)
uniFrame3.grid_propagate(False)
imageFrame3 = ttk.LabelFrame(uniFrame3, style = 'Y.Label',width=175, height = 175)

uni1LearnButton = ttk.Button(uniFrame1,text="Learn More",command = lambda: learnMore(UniLabel),width =13,style = 'purple.TButton')
uni1FavsButton = ttk.Button(uniFrame1,text="Add to Fav.",command = lambda: addToFavs(UniLabel),width =13,style = 'purple.TButton')

uni2LearnButton = ttk.Button(uniFrame2,text="Learn More",command = lambda: learnMore(UniLabel),width =13,style = 'purple.TButton')
uni2FavsButton = ttk.Button(uniFrame2,text="Add to Fav.",command = lambda: addToFavs(UniLabel),width =13,style = 'purple.TButton')

uni3LearnButton = ttk.Button(uniFrame3,text="Learn More",command = lambda: learnMore(UniLabel),width =13,style = 'purple.TButton')
uni3FavsButton = ttk.Button(uniFrame3,text="Add to Fav.",command = lambda: addToFavs(UniLabel),width =13,style = 'purple.TButton')
    #Computer Science

waterlooUniLabel = ttk.Label(uniFrame1,style='uniLable.TLabel',text = "University of Waterloo", justify='center')
waterlooRatingLabel = ttk.Label(uniFrame1,style='uniLable.TLabel',text = "-Ranked #9 in Canada", justify='center',foreground = 'red4')
waterlooSummary = tk.Text(uniFrame1,height=8,width=95, background = '#ffffb3')
waterlooSummary.tag_configure('main', foreground="red4",font=('Courier', 14))
waterlooSummary.insert(tk.END, '''The University of Waterloo’s computer science program is fairly
competitive, and students applying will require an average between
%90 - %100. Along with that, tuition comes at a hefty price for
both domestic and international students, ranging from approximately
$17 000 (domestic) to $33 000(international) per year, including
ancillary fees.''', 'main') 
waterlooSummary.configure(state="disabled")
waterlooImg = Image.open("waterloo#1.jpg").resize((175, 175))
waterlooPhoto = ImageTk.PhotoImage(waterlooImg)
waterlooImageLabel = tk.Label(uniFrame1, image=waterlooPhoto)
waterlooImageLabel.image = waterlooPhoto


guelphUniLabel = ttk.Label(uniFrame2,style='uniLable.TLabel',text = "University of Guelph", justify='center')
guelphRatingLabel = ttk.Label(uniFrame2,style='uniLable.TLabel',text = "-Ranked #19 in Canada", justify='center',foreground = 'red4')
guelphSummary = tk.Text(uniFrame2,height=8,width=95, background = '#ffffb3')
guelphSummary.tag_configure('main', foreground="red4",font=('Courier', 14))
guelphSummary.insert(tk.END, '''The University of Guelph’s computer science program is very
promising, as students applying will require an average between
%80 - %89 to have a good chance at acceptance. Along with that,
tuition comes at a mid-range price for both domestic and
international students, ranging from approximately $7 000
(domestic) to $22 000 (international) per year.''', 'main')
guelphSummary.configure(state="disabled")
guelphImg = Image.open("guelph#1.jpg").resize((175, 175))
guelphPhoto = ImageTk.PhotoImage(guelphImg)
guelphImageLabel = tk.Label(uniFrame2, image=guelphPhoto)
guelphImageLabel.image = guelphPhoto



windsorUniLabel = ttk.Label(uniFrame3,style='uniLable.TLabel',text = "University of Windsor", justify='center')
windsorRatingLabel = ttk.Label(uniFrame3,style='uniLable.TLabel',text = "-Ranked #22 in Canada", justify='center',foreground = 'red4')
windsorSummary = tk.Text(uniFrame3,height=8,width=95, background = '#ffffb3')
windsorSummary.tag_configure('main', foreground="red4",font=('Courier', 13))
windsorSummary.insert(tk.END, '''The University of Windsor’s computer science program is not very difficult
to get into, as students applying will require an average in the mid
to high %70s range to have feel confident about their applications.
Along with that, tuition comes at an affordable price for both domestic
and international students, ranging from approximately $5 500(domestic)
to $14 000 (international) per year, including ancillary fees.''', 'main')
windsorSummary.configure(state="disabled")
windsorImg = Image.open("windsor#1.jpg").resize((175, 175))
windsorPhoto = ImageTk.PhotoImage(windsorImg)
windsorImageLabel = tk.Label(uniFrame3, image=windsorPhoto)
windsorImageLabel.image = windsorPhoto

    #Biology
McGillUniLabel = ttk.Label(uniFrame1,style='uniLable.TLabel',text = "University of McGill", justify='center')
McGillRatingLabel = ttk.Label(uniFrame1,style='uniLable.TLabel',text = "-Ranked #3 in Canada", justify='center',foreground = 'red4')
McGillSummary = tk.Text(uniFrame1,height=8,width=95, background = '#ffffb3')
McGillSummary.tag_configure('main', foreground="red4",font=('Courier', 14))
McGillSummary.insert(tk.END, '''The University of McGill’s life science program is competitive,
and students applying will require an average between %90 - %100.
Along with that, tuition comes at a hefty price for both domestic
and international students, ranging from approximately $9 000
(domestic) to $20 000 (international) per year, including
ancillary fees.''', 'main')
McGillSummary.configure(state="disabled")
McGillImg = Image.open("McGill#1.jpg").resize((175, 175))
McGillPhoto = ImageTk.PhotoImage(McGillImg)
McGillImageLabel = tk.Label(uniFrame1, image=McGillPhoto)
McGillImageLabel.image = McGillPhoto


torontoUniLabel = ttk.Label(uniFrame2,style='uniLable.TLabel',text = "University of Toronto", justify='center')
torontoRatingLabel = ttk.Label(uniFrame2,style='uniLable.TLabel',text = "-Ranked #1 in Canada", justify='center',foreground = 'red4')
torontoSummary = tk.Text(uniFrame2,height=8,width=95, background = '#ffffb3')
torontoSummary.tag_configure('main', foreground="red4",font=('Courier', 14))
torontoSummary.insert(tk.END, '''The University of Toronto’s biology programs are marvelous, with
students requiring an average between %80 - %89 to have a good
chance at acceptance. Along with that, tuition comes at a mid-range
price for both domestic and international students, ranging from
approximately $7 000 (domestic), and a difficult $45 000
(international) per year.''', 'main')
torontoSummary.configure(state="disabled")
torontoImg = Image.open("toronto#1.jpg").resize((175, 175))
torontoPhoto = ImageTk.PhotoImage(torontoImg)
torontoImageLabel = tk.Label(uniFrame2, image=torontoPhoto)
torontoImageLabel.image = torontoPhoto

victoriaUniLabel = ttk.Label(uniFrame3,style='uniLable.TLabel',text = "University of Victoria", justify='center')
victoriaRatingLabel = ttk.Label(uniFrame3,style='uniLable.TLabel',text = "-Ranked #15 in Canada", justify='center',foreground = 'red4')
victoriaSummary = tk.Text(uniFrame3,height=8,width=95, background = '#ffffb3')
victoriaSummary.tag_configure('main', foreground="red4",font=('Courier', 13))
victoriaSummary.insert(tk.END, '''The University of Victoria’s life science program is not very difficult to
get into, as students applying will require an average in the mid to high
%70s range to have feel confident about their applications. Along with
that, tuition comes at an affordable price for both domestic and
international students, ranging from approximately $6 428 (domestic) to
$20 000 (international) per year, including ancillary fees.''', 'main')
victoriaSummary.configure(state="disabled")
victoriaImg = Image.open("victoria#1.jpg").resize((175, 175))
victoriaPhoto = ImageTk.PhotoImage(victoriaImg)
victoriaImageLabel = tk.Label(uniFrame3, image=victoriaPhoto)
victoriaImageLabel.image = victoriaPhoto

backButton3 = ttk.Button(browseFrame,text="Back to Menu",command = lambda: changeScreen(browseFrame,mainframe),width =13)
sortLabel = ttk.Label(browseFrame, style='sub.TLabel', text="Sort By:",background = '#ffffe6')
sortVar = tk.StringVar()
sortCombo = ttk.Combobox(browseFrame, values = ["Ranking (Highest)","Tuition (Highest)","Main Campus Size"],textvariable = sortVar,style='TCombobox',font=('Courier', 20))
sortVar.set("Ranking (Highest)")
root.option_add('*TCombobox*Listbox.font', ('Courier',15))
root.option_add('*TCombobox*Listbox.foreground', 'purple4')
sortCombo.bind("<<ComboboxSelected>>", sort)
favsButton = ttk.Button(browseFrame,text="Favourites List",command = favs,width =15)
#######
#Styles
styleButton = ttk.Style()
styleButton.configure('TButton', foreground="red4", font=('Courier', 19))
styleButton.configure('yellow.TButton', foreground="yellow4", font=('Courier', 19))
styleButton.configure('purple.TButton', foreground="purple4", font=('Courier', 19))

styleLabel = ttk.Style()
styleLabel.configure('TLabel', foreground="red4", font=('Courier', 22))
styleLabel.configure('sub.TLabel', foreground="purple4", font=('Courier', 19))
styleLabel.configure('Mblue.TLabel', foreground="blue4", font=('Courier', 20),background='#eee6ff')
styleLabel.configure('Msmall.TLabel', foreground="red4", font=('Courier', 15),background='#eee6ff')
styleLabel.configure('Sblue.TLabel', foreground="blue4", font=('Courier', 20),background='#ffe6e6')
styleLabel.configure('Ssmall.TLabel', foreground="blue4", font=('Courier', 15),background='#ffe6e6')
styleLabel.configure('browseLable.TLabel', foreground="red4", font=('Courier', 25),background='#ffffe6')
styleLabel.configure('uniLable.TLabel', foreground="blue4", font=('Courier', 22),background='#ffffb3')
styleLabel.configure('uniLableY.TLabel', foreground="blue4", font=('Courier', 22),background='#ffffe6')
styleLabel.configure('uniSummary.TLabel', foreground="red4", font=('Courier', 13),background='#ffffb3')

sCheck = ttk.Style()
sCheck.configure('TCheckbutton', background='#eee6ff', font=('Courier', 15))

sRadio = ttk.Style()
sRadio.configure('TRadiobutton',background='#ffe6e6',font=('Courier', 20),foreground="red4")

sLabelFrame = ttk.Style()
sLabelFrame.configure('Label', background = '#eee6ff')
sLabelFrame.configure('yellow.Label', background = '#ffffb3')
sLabelFrame.configure('Y.Label', background = '#ffffe6')

sCombo = ttk.Style()
sCombo.configure('TCombobox', background = '#ffffb3',foreground ='purple4')

######
#GRID

mainframe.grid(padx = 10, pady = 10)

    #MAINFRAME
welcomeLabel.grid(row=1, column=1, columnspan=3,pady=10)
backgroundLabel.grid(column =3, row = 2, rowspan = 3)
startLabel.grid(row=2, column=2,sticky=tk.W)
startButton.grid(row=2, column=1,sticky=tk.E)
browseLabel.grid(row=3, column=2 ,sticky=tk.W)
browseButton.grid(row=3, column=1,sticky=tk.E)
hamzahLabel.grid(row=4, column=1)

    #SURVEYFRAME
futureLabel.grid(row=1, column=2,pady=20)
promptLabel.grid(row=2, column=2,pady=10)
nameLabel.grid(row=3, column=2,pady=10)
nameEntry.grid(row=4,column=2)
subjectLabel.grid(row=5,column=2,pady=20)
subjectFrame.grid(row=6,column=2,pady=10)
artBox.grid(row=1, column =1,sticky=tk.W)
mathBox.grid(row=1, column =2,sticky=tk.W)
literatureBox.grid(row=2, column =1,sticky=tk.W)
chemBox.grid(row=2, column =2,sticky=tk.W)
histBox.grid(row=3, column =1,sticky=tk.W)
physBox.grid(row=3, column =2,sticky=tk.W)
compBox.grid(row=4, column =1,sticky=tk.W)
bioBox.grid(row=4, column =2,sticky=tk.W)
backButton1.grid(row = 6, column =1)
nextButton1.grid(row = 6, column =3)

    #SURVEYFRAME2
futureLabel2.grid(row=1, column=2,pady=20)
promptLabel2.grid(row=2, column=2,pady=10)
avgLabel.grid(row=3, column=2,pady=10)
avgSpinbox.grid(row=4,column=2)
budgetLabel.grid(row=5,column=2,pady=20)
budgetScale.grid(row=6, column=2,ipadx=70,pady=10)
backButton2.grid(row = 6, column =1)
resultsButton.grid(row = 6, column =3)
citizenLabel.grid(row=7,column=2,pady=10)
citizenFrame.grid(row=8,column=2)
yesRadio.grid(row=1, column=1,padx=20,sticky=tk.N)
noRadio.grid(row=1, column=2,padx=20,sticky=tk.N)

    #BRWOSEFRAME
artButton.grid(row=1, column=1,padx=5)
litButton.grid(row=1, column=2,padx=5)
histButton.grid(row=1, column=3,padx=5)
mathButton.grid(row=1, column=4,padx=5)
physButton.grid(row=1, column=5,padx=5)
chemButton.grid(row=1, column=6,padx=5)
bioButton.grid(row=1, column=7,padx=5)
compButton.grid(row=1, column=8,padx=5)
libLabel.grid(row = 2, column=1, columnspan=8,pady=5)
backButton3.grid(row=6, column=1, columnspan=3)
sortLabel.grid(row=6, column=4,sticky=tk.W)
sortCombo.grid(row=6, column=5,columnspan=3,sticky=tk.W)
favsButton.grid(row=6, column=8,sticky = tk.W, columnspan=2)
uniFrame1.grid(row = 3, column=1, columnspan=8,pady=5)
uniFrame2.grid(row = 4, column=1, columnspan=8,pady=5)
uniFrame3.grid(row = 5, column=1, columnspan=8,pady=5)
root.mainloop()
