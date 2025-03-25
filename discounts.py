# import tkinter as tk
# from tkinter import ttk
# import pymysql
# from tkinter import messagebox
# from datetime import datetime




# class discounts():
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
#         label = tk.Label(self.disFrame, text="Discount Sale Offers",bd=3,relief="groove", bg=self.clr(120,180,220), font=("Arial",30,"bold"))
#         label.grid(row=0,column=0,padx=40,pady=6,columnspan=2)

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

#     def clr(self,r,g,b):
#         return f"#{r:02x}{g:02x}{b:02x}"
    
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
#                     self.discounts = pr - Five_per
#                     val+=1
#                     self.label[val] = tk.Label(self.saleFrame , text=f"{i} is now availble only for Rs {self.discounts}")
#                     self.label[val].grid(row=val , column=0 , padx=20 , pady=40  )
#                     self.btn[val] = tk.Button(self.saleFrame, text="Purchase", width=8 , bd=2 ,relief="raised", font=("Times New Roman",15 , "bold"))
#                     self.btn[val].grid(row=val , column=0 , padx=10 , pady=40 )



#         except Exception as e:
#             tk.messagebox.showerror("Error" , f"Error: {e}")


#     def dbFunc(self):
#         self.con = pymysql.Connect(host="localhost", user="root", passwd="localhost321" ,database="discounts")
#         self.cursor = self.con.cursor()

        


# root = tk.Tk() 
# obj = discounts(root)
# root.mainloop()  # main loop is used to handle all the events in our projects






import tkinter as tk
import pymysql
from tkinter import messagebox,ttk
from datetime import datetime

class sale():
    def __init__(self, root):
        self.root = root
        self.root.title("Discount Sales")

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.width}x{self.height}+0+0")

        title = tk.Label(self.root, text="Discount Sales Management System", bd=4, relief="solid", bg=self.clr(120,220,200), font=("Arial",50,"bold"))
        title.pack(side="top", fill="x")

        # discount frame

        self.disFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(220,180,220))
        self.disFrame.place(width=self.width/2-80, height=self.height-180, x=30, y=100)

        lbl = tk.Label(self.disFrame, text="Discount Sale Offers",bd=3,relief="groove", bg=self.clr(120,180,220), font=("Arial",30,"bold"))
        lbl.grid(row=0,column=0,padx=40,pady=6,columnspan=2)
        

        # detail Frame
        self.detFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(120,220,20))
        self.detFrame.place(width=self.width/2-20,height=self.height-180, x=self.width/3+200, y=100)

        lbl2= tk.Label(self.detFrame, text="Item Details",bd=3,relief="groove", bg=self.clr(120,180,220), font=("Arial",30,"bold"))
        lbl2.pack(side="top", fill="x")
        

        self.discounts()
        

    def tabFun(self):
        tabFrame = tk.Frame(self.detFrame, bd=5, relief="sunken")
        tabFrame.place(width=self.width/2-60, height=self.height-280,x=16,y=70)

        x_scrol = tk.Scrollbar(tabFrame,orient="horizontal")
        x_scrol.pack(side="bottom",fill="x")

        y_scrol = tk.Scrollbar(tabFrame, orient="vertical")
        y_scrol.pack(side="right",fill="y")

        self.table = ttk.Treeview(tabFrame,xscrollcommand=x_scrol.set,yscrollcommand=y_scrol.set,
                                columns=("item","price","quantity","Expire"))
        
        x_scrol.config(command=self.table.xview)
        y_scrol.config(command=self.table.yview)
        
        self.table.heading("item", text="Item_Name")
        self.table.heading("price", text="Price")
        self.table.heading("quantity",text="Quantity")
        self.table.heading("Expire", text="Expiry")
        self.table["show"]= "headings"

        self.table.column("item", width=150)
        self.table.column("price", width=120)
        self.table.column("quantity", width=100)
        self.table.column("Expire", width=150)
        
        self.table.pack(fill="both", expand=1)

    def discounts(self):
        try:
            today = datetime.now().date()
            self.lbl={}
            self.btn={}

            val = 0
            self.dbFun()

            self.cur.execute("select * from disc")
            dbData= self.cur.fetchall()
            self.tabFun()
            self.table.delete(*self.table.get_children())
            for i in dbData:
                self.table.insert('',tk.END,values=i)

            self.cur.execute("select item,exp from disc")
            data = self.cur.fetchall()
            if len(data)==0:
                tk.messagebox.showinfo("Information","No more item is available for discount offer")

            for item,exp in data:
                days = (exp-today).days

                if days <=60 and days >30:
                                    
                    val +=1
                    self.lbl[item] = tk.Label(self.disFrame, text=f"For {item} Discount is 5%: ",
                                            bg=self.clr(220,180,220),font=("Arial",15,"bold"))
                    self.lbl[item].grid(row=val, column=0, padx=20,pady=30)

                    self.btn[item]= tk.Button(self.disFrame, text="Purchase", width=10, bd=2,relief="raised", font=("Arial",15,"bold"))
                    self.btn[item].config(command=lambda value=item: self.per5Fun(value))
                    self.btn[item].grid(row=val,column=1, padx=10,pady=30)

                elif days<=30 and days>0:
                    val +=1
                    self.lbl[item] = tk.Label(self.disFrame, text=f"For {item} Discount is 10%: ",
                                            bg=self.clr(220,180,220),font=("Arial",15,"bold"))
                    self.lbl[item].grid(row=val, column=0, padx=20,pady=30)

                    self.btn[item]= tk.Button(self.disFrame, text="Purchase", width=10, bd=2,relief="raised", font=("Arial",15,"bold"))
                    self.btn[item].config(command=lambda value=item: self.per10Fun(value))
                    self.btn[item].grid(row=val,column=1, padx=10,pady=30)

            self.con.close()
        except Exception as e:
            tk.messagebox.showerror("Error",f"Error: {e}")

    def per5Fun(self,val):
        try:     
            self.dbFun()
            self.cur.execute("select price,quant from disc where item=%s",val)  
            row = self.cur.fetchone() 
            per5= (5/100)*row[0] 
            discount = row[0]-per5

            upd = row[1]-1
            self.cur.execute("update disc set quant=%s where item=%s",(upd,val)) 
            self.con.commit() 
            tk.messagebox.showinfo("Success",f"You have purchased item {val} with 5% discount\nNow pay {discount} instead of {row[0]}")
            
            self.tabFun()
            self.table.delete(*self.table.get_children())
            self.cur.execute("select * from disc where item=%s",val)
            dbRow= self.cur.fetchone()
            self.table.insert('',tk.END, values=dbRow)
            
            if upd <=0:
                self.cur.execute("delete from disc where item=%s",val)
                self.con.commit()
                tk.messagebox.showinfo("Information",f"item {val} is no more available!")
                self.lbl[val].destroy()
                self.btn[val].destroy()              
                
        

        except Exception as e:
            tk.messagebox.showerror("Error",f"Error: {e}")

    def per10Fun(self, val):
        try:     
            self.dbFun()
            self.cur.execute("select price,quant from disc where item=%s",val)  
            row = self.cur.fetchone() 
            per10= (10/100)*row[0] 
            discount = row[0]-per10

            upd = row[1]-1
            self.cur.execute("update disc set quant=%s where item=%s",(upd,val)) 
            self.con.commit() 
            tk.messagebox.showinfo("Success",f"You have purchased item {val} with 10% discount\nNow pay {discount} instead of {row[0]}")
            
            self.tabFun()
            self.table.delete(*self.table.get_children())
            self.cur.execute("select * from disc where item=%s",val)
            dbRow= self.cur.fetchone()
            
            self.table.insert('',tk.END, values=dbRow)
            if upd <=0:
                self.cur.execute("delete from disc where item=%s",val)
                self.con.commit()
                tk.messagebox.showinfo("Information",f"item {val} is no more available!")
                self.lbl[val].destroy()
                self.btn[val].destroy() 

        

        except Exception as e:
            tk.messagebox.showerror("Error",f"Error: {e}")


    def dbFun(self):
        self.con = pymysql.connect(host="localhost", user="root", passwd="localhost321", database="discounts")
        self.cur = self.con.cursor()

    def clr(self,r,g,b):
        return f"#{r:02x}{g:02x}{b:02x}"


root = tk.Tk()
obj = sale(root)
root.mainloop()