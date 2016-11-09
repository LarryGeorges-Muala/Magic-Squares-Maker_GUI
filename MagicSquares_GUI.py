#App Name: Magic Square Maker - Python
#Python Version 3.5
#Developper: Larry Georges Muala

import tkinter
from tkinter import messagebox

window = tkinter.Tk()

window.title('Magic Square Maker')

#Disable maximize button
window.resizable(0,0)

#Modify window icon
#window.wm_iconbitmap('lelu.ico')

#Set window background color
window.configure(background="gray2")

#############################################################
#Menu Bar

def about_app():
	print("App Name: Magic Square Maker GUI")
	print("App Description: Magic Square Maker GUI using tkinter")
	print("Python Version 3.5")
	print("Developper: Larry Georges Muala")
	
	messagebox.showinfo("App Info", "App Name: Magic Square Maker GUI\n" + 
						"\nApp description: Magic Square Maker GUI using tkinter\n" + 
						"\nPython Version 3.5 \n" + 
						"\nDevelopper: Larry Georges Muala")
#Menu design
menubar = tkinter.Menu(window)
myMenu = tkinter.Menu(menubar, tearoff=0)
myMenu.add_command(label="About", command=about_app)
myMenu.add_separator()
myMenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="App Info", menu=myMenu)

#Display menu
window.config(menu=menubar)

#############################################################

#magic square maker command
def squareMaker():		
	#ask user for size of magic square
	var_size = ent_size.get()
	
	#check that the input is a number
	if var_size.isdigit():
	
		n = int(var_size)
	
		#check that the input is odd
		if n % 2 != 0:
			clear_all()
			btn_generate = tkinter.Button(window, text="Create", command=squareMaker)
			btn_generate.grid()
			magicSquare(n)
			ent_size.focus()

		
		else:
			messagebox.showerror("Error", "Please enter an odd number")
			ent_size.delete(0, tkinter.END)
			ent_size.focus()
	else:
		messagebox.showerror("Error", "Please enter an odd number")
		ent_size.delete(0, tkinter.END)
		ent_size.focus()

#magic square maker on Enter button keyboard		
def squareMakerOnEnter(event):		
	#ask user for size of magic square
	var_size = ent_size.get()
	
	#check that the input is a number
	if var_size.isdigit():
	
		n = int(var_size)
	
		#check that the input is odd
		if n % 2 != 0:
			clear_all()
			btn_generate = tkinter.Button(window, text="Create", command=squareMaker)
			btn_generate.grid()
			magicSquare(n)
			ent_size.focus()

		
		else:
			messagebox.showerror("Error", "Please enter an odd number")
			ent_size.delete(0, tkinter.END)
			ent_size.focus()
	else:
		messagebox.showerror("Error", "Please enter an odd number")
		ent_size.delete(0, tkinter.END)
		ent_size.focus()

		
#magic square drawing function		
def magicSquare(n):	
	
	
	#creating the magic square layout and populating it with zeros
	magic_list = [[ 0 for column_s in range(n) ] for row_s in range(n)]


	#loops to assign magic square values to each entry in magic_list
	#using formula:
	# for Ith row and Jth column
	# value = { n*[(I + J - 1 + (n//2)) % n)] } + { [(I + 2*J - 2) % n] + 1 }

	for row_s in range(n):
		for column_s in range(n):
		
			row_value = row_s + 1
			column_value = column_s + 1

			value = ( n * ((row_value + column_value - 1 + (n//2)) % n) ) + ( ((row_value + 2 * column_value - 2) % n) + 1 )
			
			magic_list[row_s][column_s] = value
			
			#creating single buttons for GUI with each value

			btn = tkinter.Button(window, text=value, font=("Helvetica", 10), height = 1, width = 5)
			btn.grid(row=row_value, column=column_value)
			
			
	print("")
	#formatting magic_list by splitting elements and joining by 4 digits space
	for m in range(n):
		print(' '.join( '{:4d}'.format(x) for x in magic_list[m] ))
	
	
#delete buttons created by previous magic squares		
def clear_all():
    for widget in window.winfo_children():      
        if widget.winfo_class() == 'Button':   
            widget.grid_remove()              

#welcome label
lbl_size = tkinter.Label(window, text="Please enter the size of the magic square: ", bg="gray2", fg="white")
lbl_size.grid()		

#size text entry
ent_size = tkinter.Entry(window)
ent_size.grid()
ent_size.focus()

#square maker button		
btn_generate = tkinter.Button(window, text="Create", command=squareMaker)
btn_generate.grid()

#bind function squareMaker to button Enter		
window.bind("<Return>", squareMakerOnEnter)


	
window.mainloop()