import tkinter as tk


class discounts():
    def __init__(self , root):

        
        self.root = root #to initialize the root
        self.root.title("Discount Sales")

        # now we need to define the global varivable like self.variableName
        self.width = self.root.winfo_screenwidth() #here winfo gives information about the entire window
        self.height = self.root.winfo_screenheight()  
        self.root.geometry(f"{self.width}x{self.height}+0+0") #here +0 and +0 refers to that we want our window to start from firt row and first column
        title = tk.Label(self.root, text="Discount Sales Management" , bd=3 , relief="groove" , font=("Times New Roman",50, "bold"), bg="gray")
        title.pack(side="top" , fill="x")


root = tk.Tk()
obj = discounts(root)
root.mainloop()  # main loop is used to handle all the events in our projects
