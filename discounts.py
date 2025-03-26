# import tkinter as tk
# from tkinter import ttk
# import pymysql
# from tkinter import messagebox
# from datetime import datetime




# class Sales():
#     def __init__(self , root):

        
#         self.root = root #to initialize the root
#         self.root.title("Discount Sales")

#         # now we need to define the global varivable like self.variableName
#         self.width = self.root.winfo_screenwidth() #here winfo gives information about the entire window
#         self.height = self.root.winfo_screenheight()  
#         self.root.geometry(f"{self.width}x{self.height}+0+0") #here +0 and +0 refers to that we want our window to start from firt row and first column
        
#         title = tk.Label(self.root, text="Discount Sales Management" , bd=2.5 , relief="groove" , font=("Times New Roman",40, "bold"), bg=self.clr(220,200,180))
#         title.pack(side="top" , fill="x")

#         #DISCOUNT FRAME
#         self.disFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(220,180,220))
#         self.disFrame.place(width=self.width/2-80, height=self.height-180, x=30, y=100)

#         #LABEL
#         # label = tk.Label(self.disFrame, text="Discount Sale Offers",bd=3,relief="groove", bg=self.clr(120,180,220), font=("Arial",30,"bold"))
#         # label.grid(row=0,column=0,padx=40,pady=6,columnspan=2)

#         #SALE FRAME
#         self.saleFrame = tk.Frame(self.root, bd=4 , relief="ridge" , bg=self.clr(200,180,180))
#         self.saleFrame.place(width=self.width/3 , height=self.height-180 , x=30 ,y=100)
#         self.disc()

#         #DETAIL FRAME
#         self.detailFrame = tk.Frame(self.root, bd=4 ,relief="raised" , bg=self.clr(180,180,200))
#         self.detailFrame.place(width=self.width * 1/2 + 50 , height = self.height - 180 , x = self.width/3 + 100 , y=100)
        
#         head = tk.Label(self.detailFrame, text="Product Details",bg=self.clr(180,180,200), font=("Times New Roman",40, "bold"))
#         head.pack(side="top" , fill="x")
#         self.table()

#     def table(self):
#         tableFrame = tk.Frame(self.detailFrame , bd=4 , relief="raised" , bg="cyan")
#         tableFrame.place(width=self.width/2 + 10 , height=self.height - 280, x=15 , y=80)


        
#         x_scroll = tk.Scrollbar(tableFrame,orient="horizontal")
#         x_scroll.pack(side="bottom",fill="x")

#         y_scroll = tk.Scrollbar(tableFrame,orient="vertical")
#         y_scroll.pack(side="right",fill="y")

#         self.table = ttk.Treeview(tableFrame , columns=("item","price","quantity","Expire"), xscrollcommand = x_scroll.set , yscrollcommand = y_scroll.set)
#         x_scroll.config(command=self.table.xview)
#         y_scroll.config(command=self.table.yview)

#         self.table.heading("item",text="ITEMS")
#         self.table.heading("price",text="PRICE")
#         self.table.heading("quantity",text="QUANTITY")
#         self.table.heading("Expire",text="EXPIRY")
#         self.table["show"]="headings"

#         self.table.column("item", width=150)
#         self.table.column("price", width=120)
#         self.table.column("quantity", width=100)
#         self.table.column("Expire", width=150)
        
#         self.table.pack(fill="both" , expand=1)

#     def disc(self):
#         try:
#             self.dbFunc()
#             self.cursor.execute("select * from sales")
#             data = self.cursor.fetchall()
#             today = datetime.now().date()
#             val=0
#             self.label={}
#             self.btn={}
#             self.table()



#             for i,pr,quan,exp in data:
#                 days = (exp - today).days
#                 if quan > 0 and days <= 60 and days > 30:
#                     Five_per = (5/100) * pr
#                     self.dis = pr - Five_per
#                     val+=1
#                     self.label[val] = tk.Label(self.saleFrame , text=f"{i} is now on 5% Off")
#                     self.label[val].grid(row=val , column=0 , padx=20 , pady=40  )
#                     self.btn[val] = tk.Button(self.saleFrame, text="Purchase", width=8 , bd=2 ,relief="raised", font=("Times New Roman",15 , "bold"))
#                     self.btn[val].grid(row=val , column=1 , padx=10 , pady=40 )



#         except Exception as e:
#             tk.messagebox.showerror("Error" , f"Error: {e}")

#     def clr(self,r,g,b):
#         return f"#{r:02x}{g:02x}{b:02x}"


#     def dbFunc(self):
#         self.con = pymysql.Connect(host="localhost", user="root", passwd="localhost321" ,database="discounts")
#         self.cursor = self.con.cursor()

        


# root = tk.Tk() 
# obj = Sales(root)
# root.mainloop()  # main loop is used to handle all the events in our projects




import tkinter as tk
from tkinter import ttk
import pymysql
from tkinter import messagebox
from datetime import datetime

class Sales():
    def __init__(self, root):
        self.root = root
        self.root.title("Discount Sales")

        # Getting screen dimensions
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()  
        self.root.geometry(f"{self.width}x{self.height}+0+0")
        
        # Title label
        title = tk.Label(self.root, text="Discount Sales Management", bd=2.5, relief="groove", font=("Times New Roman",40, "bold"), bg=self.clr(220,200,180))
        title.pack(side="top", fill="x")

        # Create all frames first
        self.saleFrame = tk.Frame(self.root, bd=4, relief="ridge", bg=self.clr(200,180,180))
        self.saleFrame.place(x=30, y=100, width=self.width/3, height=self.height-180)
        
        
        self.disFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(220,180,220))
        self.disFrame.place(width=self.width/2-80, height=self.height-180, x=30, y=100)

        # Detail Frame (right side - for product table)
        # self.detailFrame = tk.Frame(self.root, bd=4, relief="raised", bg=self.clr(180,180,200))
        # self.detailFrame.place(width=self.width * 1/2 + 50, height=self.height-180, 
        #                       x=self.width/3 + 100, y=100)

        self.detailFrame = tk.Frame(self.root, bd=4, relief="raised", bg=self.clr(180, 180, 200))
        self.detailFrame.place(x=self.width/3 + 60, y=100,width=self.width*2/3 - 90, height=self.height-180)

        
        # Then create the table and discount elements
        self.table()
        self.disc()

    def table(self):
        """Create the product details table in the detailFrame"""
        head = tk.Label(self.detailFrame, text="Product Details", bg=self.clr(180,180,200),font=("Times New Roman",40, "bold"))
        head.pack(side="top", fill="x")
        
        tableFrame = tk.Frame(self.detailFrame, bd=4, relief="raised", bg="cyan")
        tableFrame.pack(fill="both", expand=True, padx=10, pady=10)

        x_scroll = tk.Scrollbar(tableFrame, orient="horizontal")
        x_scroll.pack(side="bottom", fill="x")

        y_scroll = tk.Scrollbar(tableFrame, orient="vertical")
        y_scroll.pack(side="right", fill="y")

        self.product_table = ttk.Treeview(tableFrame, columns=("item","price","quantity","Expire"), 
                                        xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)
        x_scroll.config(command=self.product_table.xview)
        y_scroll.config(command=self.product_table.yview)

        self.product_table.heading("item", text="ITEMS")
        self.product_table.heading("price", text="PRICE")
        self.product_table.heading("quantity", text="QUANTITY")
        self.product_table.heading("Expire", text="EXPIRY")
        self.product_table["show"] = "headings"

        self.product_table.column("item", width=150 , anchor="w")
        self.product_table.column("price", width=120 , anchor="center")
        self.product_table.column("quantity", width=100, anchor="center")
        self.product_table.column("Expire", width=150 , anchor="center")
        
        self.product_table.pack(fill="both", expand=True)

    def disc(self):
        try:
            self.dbFunc()
            self.cursor.execute("select * from sales")
            data = self.cursor.fetchall()
            today = datetime.now().date()
            val = 0
            self.label = {}
            self.btn = {}

            for i, pr, quan, exp in data:
                days = (exp - today).days
                if quan > 0 and days <= 60 and days > 30:
                    Five_per = (5/100) * pr
                    self.dis = pr - Five_per
                    val += 1
                    self.label[val] = tk.Label(self.saleFrame, text=f"{i} is now on 5% Off")
                    self.label[val].grid(row=val, column=0, padx=20, pady=40)
                    self.btn[val] = tk.Button(self.saleFrame, text="Purchase", width=8, bd=2,
                                             relief="raised", font=("Times New Roman",15, "bold"))
                    self.btn[val].grid(row=val, column=1, padx=10, pady=40)

        except Exception as e:
            tk.messagebox.showerror("Error", f"Error: {e}")

    def clr(self, r, g, b):
        return f"#{r:02x}{g:02x}{b:02x}"

    def dbFunc(self):
        self.con = pymysql.Connect(host="localhost", user="root", 
                                 passwd="localhost321", database="discounts")
        self.cursor = self.con.cursor()

root = tk.Tk() 
obj = Sales(root)
root.mainloop()