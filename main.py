import tkinter
import re
import customtkinter
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox
import os
import os.path


# Themes
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme(("dark-blue"))

# get the file name for saving
global open_status_name
open_status_name = False


# main menu
class optionFrame(customtkinter.CTkFrame,tkinter.Frame):
    # initialize all fuctions
    def __init__(self, master, **kwargs):
        #initialize parent class objects
        super().__init__(master, **kwargs)

        # The main menu Logo
        crud = customtkinter.CTkImage(dark_image=Image.open("CRUD.png"), size=(200, 200))
        # Putting the the window
        crud_label = customtkinter.CTkLabel(master=self, image=crud, text=" ")
        crud_label.pack()

        # Buttons
        button_create = customtkinter.CTkButton(master=self, text="Create",
                                                command=lambda: self.button_pressed("create"))
        button_create.pack(padx=20, pady=20)

        button_edit = customtkinter.CTkButton(master=self, text="Edit", command=lambda: self.button_pressed("edit"))
        button_edit.pack(padx=20, pady=20)

        button_delete = customtkinter.CTkButton(master=self, text="Delete",
                                                command=lambda: self.button_pressed("delete"))
        button_delete.pack(padx=20, pady=20)

    #button functions
    def button_pressed(self, commands):
        # create a file
        if commands == "create":
            global create_window
            create_window = customtkinter.CTkToplevel()
            create_window.title("Create")
            create_window.geometry("500x200")

            global name
            #getting the filename and type
            name = customtkinter.CTkEntry(master=create_window, placeholder_text="Enter File Name")
            name.pack(padx=20, pady=10)


            #create file button
            create_file = customtkinter.CTkButton(master=create_window, text="Create File", command=self.file_name)
            create_file.place(relx=0.34, rely=0.7, anchor=tkinter.CENTER)

            #exit Button
            Exitbtn = customtkinter.CTkButton(master=create_window, text="Exit", command=self.on_close)
            Exitbtn.place(relx=0.7, rely=0.7, anchor=tkinter.CENTER)



        # edit fundtion
        if commands == "edit":
            # find the file
            global select
            # when button click open new window
            select = customtkinter.CTkToplevel()
            #title
            select.title("Edit")
            # screen size
            select.geometry("1200x600")

            #putting the frame for textbox
            frame = customtkinter.CTkFrame(select)
            #setting the positions
            frame.pack(pady=50)

            #making the textbox global for other functions
            global textbox
            #making textbox
            textbox = customtkinter.CTkTextbox(master=frame, width=1090, height=555, corner_radius=0)
            textbox.grid(row=0, column=0, sticky="nsew")

            #making buttons in edit window
            button_save = customtkinter.CTkButton(master=select, text="Save", command=self.save)
            button_save.place(relx=0.1, rely=0.96, anchor=tkinter.CENTER)

            button_overwrite = customtkinter.CTkButton(master=select, text="Overwrite", command=self.overwrite)
            button_overwrite.place(relx=0.25, rely=0.96, anchor=tkinter.CENTER)

            button_open = customtkinter.CTkButton(master=select, text="Open", command=self.open)
            button_open.place(relx=0.40, rely=0.96, anchor=tkinter.CENTER)

            button_search = customtkinter.CTkButton(master=select, text="Search", command=self.search)
            button_search.place(relx=0.55, rely=0.96, anchor=tkinter.CENTER)

            button_exit = customtkinter.CTkButton(master=select, text="Exit", command=self.on_close2)
            button_exit.place(relx=0.70, rely=0.96, anchor=tkinter.CENTER)



        # Delete window function
        if commands == "delete":
            global delete_window
            delete_window = customtkinter.CTkToplevel()
            delete_window.title("Delete")
            delete_window.geometry("750x200")

            #setting buttons
            select_button = customtkinter.CTkButton(master=delete_window, text="Upload", command=self.selection)
            select_button.pack(padx=20, pady=10)

            delete_file = customtkinter.CTkButton(master=delete_window, text="Delete", command=self.delete_file)
            delete_file.place(relx=0.34, rely=0.7, anchor=tkinter.CENTER)

            btnExit = customtkinter.CTkButton(master=delete_window,text="Exit", command=self.on_close1)
            btnExit.place(relx=0.7, rely=0.7, anchor=tkinter.CENTER)


    # close dialog for create window
    def on_close(self):
        messagebox.showwarning("Close", "Are you sure you want to close the window?")
        create_window.destroy()

    #close dialog for edit window
    def on_close1(self):
        messagebox.showwarning("Close", "Are you sure you want to close the window?")
        delete_window.destroy()

    # close dialog for delete window
    def on_close2(self):
        messagebox.showwarning("Close", "Are you sure you want to close the window?")
        select.destroy()

    #creating the file
    def file_name(self):
        #setting the file path
        data_path = "C:\\Users\\Kurt\\PycharmProjects\\Prelim_Output\\Data"
        #getting the file name input
        data_final = os.path.join(data_path, str(name.get()))
        # checking if the file exists
        if os.path.exists(data_final):
            # dialog box to warn the user that the file existed
            messagebox.showwarning("File Existed", "File Already Existed")
        else:
            with open(data_final, "w") as f:
                # dialog box to message that the file is created successfully
                messagebox.showinfo("File Created", "File Created Successfully")
                # creating a new file
                os.startfile("C:\\Users\\Kurt\\PycharmProjects\\Prelim_Output\\Data")

    #finding the files
    def selection(self):
        global select
        # opening the file explorere to get the directory
        select = filedialog.askopenfilename(initialdir="C:\\Users\\Kurt\\PycharmProjects\\Prelim_Output\\Data",
                                            title="Select a file",
                                            filetypes=(("txt files", "*.txt")
                                                       , ("bin Files", "*.bin")
                                                       , ("CSV files", "*.csv"),
                                                       ("All Files", "*.*")))

        #for delete window
        if select:
            label = customtkinter.CTkLabel(master=delete_window, text=select)
            label.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

    #delete button function
    def delete_file(self):
        #using the select variable
        mainPath = select
        # checking of the file exists
        if os.path.exists(mainPath):
            #removing the file
            os.remove(mainPath)
            # sending the message that the file is deleted
            messagebox.showinfo("Deleted", "File Deleted")
        else:
            # sending the message that the file does not exists
            messagebox.showerror("Not Existing", "File Doesn't Exist")


    def open(self):
        # finding the file
        file_open = filedialog.askopenfilename(initialdir="C:\\Users\\Kurt\\PycharmProjects\\Prelim_Output\\Data",
                                            title="Select a file",
                                            filetypes=(("txt files", "*.txt")
                                                       , ("bin Files", "*.bin")
                                                       , ("CSV files", "*.csv"),
                                                       ("All Files", "*.*")))
        # for future purposes
        if file_open:
            global open_status_name
            open_status_name = file_open

        #opening the file and read the file
        text_file = open(file_open, 'r')
        # reading the file
        content = text_file.read()
        # inserting the data in the textbox
        textbox.insert("0.0", content)
        # closing the file
        text_file.close()

    def save(self):
        global open_status_name
        # if the file exists = True
        if open_status_name:
            #opening the file and making a new file to save the data
            text_file = open(open_status_name, 'w')
            # putting the data on the file
            text_file.write(textbox.get(1.0, 10000.0))
            # sending the messsage to the user that the files are saved
            messagebox.showinfo("Saved", "File Saved Successfully!")
            text_file.close()

    def overwrite(self):
        # its just like saving as in other softwares
        text_file = filedialog.asksaveasfilename(defaultextension='.*', initialdir="C:\\Users\\Kurt\\PycharmProjects\\Prelim_Output\\Data",
                                            title="Overwrite Files",
                                            filetypes=(("txt files", "*.txt")
                                                       , ("bin Files", "*.bin")
                                                       , ("CSV files", "*.csv"),
                                                       ("All Files", "*.*")))

    def search(self):
        global search_window
        # making the search window when the button is clicked in edit
        search_window = customtkinter.CTkToplevel()
        search_window.title("Search a Word")
        search_window.geometry("500x300")

        global search_entry
        # making a ui to input
        search_entry = customtkinter.CTkEntry(master=search_window, placeholder_text="Enter a Word")
        search_entry.pack()

        # making a search button for regex function
        search_button = customtkinter.CTkButton(master=search_window, text="Search", command=self.finalize)
        search_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    def finalize(self):
        # making a count that counts the word that exists in the file
        count = 0
        # splitting it to a list of words from the file
        find = textbox.get(1.0, 10000.0).split()
        #making a string var for updating labels
        text_var= tkinter.StringVar()
        for word in find:
            # checking the word if that exists
            if re.findall(search_entry.get(), word):
                # upping the count
                count += 1

                # making the label for the count
                label = tkinter.Label(search_window, textvariable=text_var)
                label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        # a string that display how many counts
        text_var.set("There are a total of " + str(count) + " in this file")


class program(customtkinter.CTk, tkinter.Tk):
    # to initiate the program
    def __init__(self):
        super().__init__()
        #window customization
        self.geometry("500x350")
        self.minsize(500, 480)
        self.title("CRUD")
        # making the CCMS as a logo
        self.iconbitmap("CCMS.ico")

        #the option side bar
        newFrame = optionFrame(master=self)
        newFrame.pack()

# run the program
root = program()
#main loop
root.mainloop()
