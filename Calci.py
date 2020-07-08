from tkinter import *

class Calculator():
       def __init__(self,master):
              self.master=master
              master.title("Python Calci")

              self.screen=Text(master,state='disabled',background="Olive",foreground="black",width=40,height=4)

              self.screen.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
              self.screen.config(state="normal")
              self.equation=''
              b1=self.createbutton(7)
              b2=self.createbutton(8)
              b3=self.createbutton(9)
              b4=self.createbutton(u"\u232B",None)
              b5=self.createbutton(4)
              b6=self.createbutton(5)
              b7=self.createbutton(6)
              b8=self.createbutton(u"\u00F7")
              b9=self.createbutton(1)
              b10=self.createbutton(2)
              b11=self.createbutton(3)
              b12=self.createbutton('*')
              b13=self.createbutton('.')
              b14=self.createbutton('0')
              b15=self.createbutton('+')
              b16=self.createbutton('-')
              b17=self.createbutton('=',None,34)

              buttons=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17]
              count=0
              for row in range(1,5):
                     for column in range(4):
                            buttons[count].grid(row=row,column=column)
                            count+=1
              buttons[16].grid(row=5,column=0,columnspan=4)
       def createbutton(self,val,write=True,width=7):
              return Button(self.master,text=val,command=lambda :self.click(val,write),width=width)
       def click(self,text,write):
              if text=='=' and self.equation:
                     self.equation=re.sub(u"\u00F7", " / " , self.equation)
                     print(self.equation)
                     answer=str(eval(self.equation))
                     self.clear_screen()
                     self.insert_screen(answer,newline=True)
              elif text==u"\u232B":
                     self.clear_screen()
              
              else:
                     self.insert_screen(text)
       def clear_screen(self):
              self.equation=''
              self.screen.config(state='normal')
              self.screen.delete('1.0',END)
       def insert_screen(self,value,newline=False):
              self.screen.config(state='normal')
              self.screen.insert(END,value)
              self.equation+=str(value)
              self.screen.config(state="disabled")
              








              


                     
                     


                     





root=Tk()
my_gui=Calculator(root)
root.mainloop()
