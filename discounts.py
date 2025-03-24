import tkinter as tk


class discounts():
    def __init__(self , root):

        
        self.root = root #to initialize the root
        self.root.title("Discount Sales")

        # now we need to define the global varivable like self.variableName
        self.width = self.root.winfo_screenwidth() #here winfo gives information about the entire window
        self.height = self.root.winfo_screenheight()  
        self.root.geometry(f"{self.width}x{self.height}+0+0") #here +0 and +0 refers to that we want our window to start from firt row and first column
        title = tk.Label(self.root, text="Discount Sales Management" , bd=2.5 , relief="groove" , font=("Times New Roman",40, "bold"), bg=self.clr(220,200,180))
        title.pack(side="top" , fill="x")

        saleFrame = tk.Frame(self.root, bd=4 , relief="ridge" , bg=self.clr(200,180,180))
        saleFrame.place(width=self.width/3 , height=self.height-180 , x=30 ,y=100)

        self.detailFrame = tk.Frame(self.root, bd=4 ,relief="raised" , bg=self.clr(180,180,200) )
        self.detailFrame.place(width=self.width * 1/2 + 50 , height = self.height - 180 , x = self.width/3 + 100 , y=100)
        self.table()

    def clr(self,r,g,b):
        return f"#{r:02x}{g:02x}{b:02x}"
    
    def table(self):
        tableFrame = tk.Frame(self.detailFrame , bd=4 , relief="raised" , bg="purple")
        tableFrame.place(width=self.width/2 + 10 , height=self.height - 280, x=20 , y=80)

root = tk.Tk() 
obj = discounts(root)
root.mainloop()  # main loop is used to handle all the events in our projects
