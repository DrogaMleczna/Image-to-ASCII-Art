import cv2 as cv
import tkinter as tk
from tkinter import filedialog as fd
import os

#Create a dialog box to open the file, choose font type and change the scaling
root = tk.Tk()
root.title("Select File")
root.resizable(False, False)
root.geometry('450x225')
font = "m"
scaling = tk.DoubleVar()
scale = 10

#Monospace-proportional font toggle
def spacing_toggle():
    global font
    if font_spacing_button.config('text')[-1] == 'Proportional':
        font_spacing_button.config(text='Monospace')
        font = "m"
    else:
        font_spacing_button.config(text='Proportional')
        font = "p"

#File select button
def select_file():
    global file
    file = fd.askopenfilename(filetypes = [("PNG File", ("*.png", "*.PNG")), ("JPEG File", ("*.jpg", "*.jpeg", "*.JPG", "*.JPEG"))])
    root.destroy()

#Update the scaling value
def slider_changed(event):
    global scale
    scale = scaling.get()

#Scale slider
slider = tk.Scale(root,from_=1,to=200,orient="horizontal",command=slider_changed,variable=scaling,resolution=1, length=250)
slider.set(10)
slider.pack()
slider.place(anchor = "center", relx = 0.5, rely = 0.45)

#The "scaling" label
label = tk.Label(root,text="Scaling (default 10):", font=15)
label.pack()
label.place(anchor="center", relx=0.5, rely=0.3)

#The font spacing button
font_spacing_button = tk.Button(root,text="Monospace", width=10, command=spacing_toggle)
font_spacing_button.pack(pady=10)
font_spacing_button.place(anchor="center", relx=0.5, rely=0.1)

#File opening button
open_button = tk.Button(root,text="Open File",font=15,command=select_file, width=10, height=2)
open_button.pack(expand=True)
open_button.place(anchor="center", relx=0.5, rely=0.8)

root.mainloop()

#Open the image and text file 
outfile = (file.split(sep="."))[0] + ".txt"
outfile = outfile.replace(" ", "")

image = cv.imread(file)
image = cv.resize(image, (int(image.shape[1]/scale),int(image.shape[0]/scale)), interpolation = cv.INTER_AREA)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

#main logic
with open(outfile, "w") as f:
       
       #Monospace font
       if font == "m":
           for i in gray:
               for j in i:
                   if j <= 25:
                       f.write("  ")
                   elif 26 <= j <= 50:
                       f.write('..')
                   elif 51 <= j <= 75:
                       f.write("::")
                   elif 76 <= j <= 100:
                       f.write('++')
                   elif 101 <= j <= 125:
                       f.write("II")
                   elif 126 <= j <= 150:
                       f.write('qq')
                   elif 151 <= j <= 175:
                       f.write("kk")
                   elif 176 <= j <= 200:
                       f.write(r'%%')
                   elif 201 <= j <= 225:
                       f.write("##")
                   elif 226 <= j <= 255:
                       f.write('@@')
                   else:
                       print(j)
               f.write("\n")

       #Proportional font
       elif font == "p":
           for i in gray:
               for j in i:
                   if j <= 25:
                       f.write("         ")
                   elif 26 <= j <= 50:
                       f.write('.........')
                   elif 51 <= j <= 75:
                       f.write(":::::::::")
                   elif 76 <= j <= 100:
                       f.write('+++')
                   elif 101 <= j <= 125:
                       f.write("IIIIIII")
                   elif 126 <= j <= 150:
                       f.write('qqq')
                   elif 151 <= j <= 175:
                       f.write("kkk")
                   elif 176 <= j <= 200:
                       f.write(r'%%')
                   elif 201 <= j <= 225:
                       f.write("###")
                   elif 226 <= j <= 255:
                       f.write('@@')
                   else:
                       print(j)
               f.write("\n")

#A VERY ugly method to get to the root drive directory
os.chdir(r"..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..")

#Get the relative output file path, because apparently Windows can't stomach an absolute path in  the 'type' command
outfile = outfile.replace(os.getcwd().replace("\\","/"), "")
outfile = outfile.replace("/", "\\")


#show the output
if os.name == "nt":
    os.system(f"type {outfile[0:]}")
elif os.name == "posix":
    os.system(f"cat {outfile[0:]}")
input()