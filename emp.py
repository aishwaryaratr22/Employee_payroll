from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql 
import time
import os
import subprocess
import reportlab
from reportlab.pdfgen import canvas
import tempfile

class EmployeeSystem:
    def __init__(self, root):
        self.root=root
        self.root.title("Employee Payroll management System")
        self.root.geometry("1350x700+0+0")
        title=Label(self.root,text="Employee Payroll Managemnt System", font=("times new roman", 30, "bold"), bg="#262626", fg="white").place(x=0,y=0,relwidth=1)
        btn_show_employees=Button(self.root,text="All Employee",command=self.employee_frame, font=("times new roman", 20),fg='Black').place(x=1100,y=5,height=30)

        self.var_emp_id=StringVar()
        self.var_designation=StringVar()
        self.var_name=StringVar()
        self.var_age=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_heird=StringVar()
        self.var_address=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_experience=StringVar()
        self.var_proof=StringVar()
        self.var_phone=StringVar()
        self.var_status=StringVar()

        Frame1=Frame(self.root,bd=3,relief=RIDGE)
        Frame1.place(x=10,y=70,width=750,height=620)

        title2=Label(Frame1,text="Employee Details", font=("times new roman", 25), bg="lightgray", fg="black").place(x=0,y=0,relwidth=1)

        lb1_id=Label(Frame1,text="Employee Id :", font=("times new roman", 25),fg="white").place(x=10,y=50)
        self.txt_id=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_emp_id,bg = "lightgray",fg="black")
        self.txt_id.place(x=190,y=60,width=200)
        btn_search=Button(Frame1,text="Search",command=self.search, font=("times new roman", 25),fg="Black").place(x=410,y=60,height=35)

        lb1_designation=Label(Frame1,text="Designation :", font=("times new roman", 25),fg="white").place(x=10,y=100)
        txt_designation=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_designation, bg = "lightgray",fg="black").place(x=190,y=110)
        lb1_dob=Label(Frame1,text="D.O.B :", font=("times new roman", 25),fg="white").place(x=380,y=100)
        txt_dob=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_dob, bg = "lightgray",fg="black").place(x=540,y=110)

        lb1_name=Label(Frame1,text="Name :", font=("times new roman", 25),fg="white").place(x=10,y=150)
        txt_name=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_name, bg = "lightgray",fg="black").place(x=190,y=160)
        lb1_doj=Label(Frame1,text="D.O.J :", font=("times new roman", 25),fg="white").place(x=380,y=150)
        txt_doj=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_doj, bg = "lightgray",fg="black").place(x=540,y=160)

        lb1_age=Label(Frame1,text="Age :", font=("times new roman", 25),fg="white").place(x=10,y=200)
        txt_age=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_age, bg = "lightgray",fg="black").place(x=190,y=210)
        lb1_experience=Label(Frame1,text="Experience :", font=("times new roman", 25),fg="white").place(x=380,y=200)
        txt_experience=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_experience, bg = "lightgray",fg="black").place(x=540,y=210)

        lb1_gender=Label(Frame1,text="Gender :", font=("times new roman", 25),fg="white").place(x=10,y=250)
        txt_gender=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_gender, bg = "lightgray",fg="black").place(x=190,y=260)
        lb1_proof=Label(Frame1,text="Proof Id :", font=("times new roman", 25),fg="white").place(x=380,y=250)
        txt_proof=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_proof, bg = "lightgray",fg="black").place(x=540,y=260)

        lb1_email=Label(Frame1,text="Email :", font=("times new roman", 25),fg="white").place(x=10,y=300)
        txt_email=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_email, bg = "lightgray",fg="black").place(x=190,y=310)
        lb1_contact=Label(Frame1,text="Phone No :", font=("times new roman", 25),fg="white").place(x=380,y=300)
        txt_contact=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_phone, bg = "lightgray",fg="black").place(x=540,y=310)

        lb1_heird=Label(Frame1,text="Heird Loc :", font=("times new roman", 25),fg="white").place(x=10,y=350)
        txt_heird=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_heird, bg = "lightgray",fg="black").place(x=190,y=360)
        lb1_status=Label(Frame1,text="Status :", font=("times new roman", 25),fg="white").place(x=380,y=350)
        txt_status=Entry(Frame1,font=("times new roman", 15),textvariable=self.var_status, bg = "lightgray",fg="black").place(x=540,y=360)

        lb1_add=Label(Frame1,text="Address :", font=("times new roman", 25),fg="white").place(x=10,y=400)
        self.txt_add=Text(Frame1,font=("times new roman", 15), bg = "lightgray",fg="black")
        self.txt_add.place(x=180,y=410,width=535,height=150)

        self.var_month=StringVar()
        self.var_year=StringVar()
        self.var_basic=StringVar()
        self.var_day=StringVar()
        self.var_absent=StringVar()
        self.var_medical=StringVar()
        self.var_pf=StringVar()
        self.var_convec=StringVar()
        self.var_net=StringVar()

        Frame2=Frame(self.root,bd=3,relief=RIDGE)
        Frame2.place(x=770,y=70,width=580,height=300)

        title3=Label(Frame2,text="Employee Salary Details", font=("times new roman", 30), bg="lightgray", fg="black").place(x=0,y=0,relwidth=1)

        lb1_month=Label(Frame2,text="Month ", font=("times new roman", 20),fg="white").place(x=10,y=50)
        txt_month=Entry(Frame2,font=("times new roman", 15),textvariable=self.var_month, bg = "lightgray",fg="black").place(x=80,y=50,width=100,height=29)

        lb1_year=Label(Frame2,text="Year ", font=("times new roman", 20),fg="white").place(x=200,y=50)
        txt_year=Entry(Frame2,font=("times new roman", 15),textvariable=self.var_year, bg = "lightgray",fg="black").place(x=250,y=50,width=100)

        lb1_basic=Label(Frame2,text="Salary ", font=("times new roman", 20),fg="white").place(x=375,y=50)
        txt_basic=Entry(Frame2,font=("times new roman", 15),textvariable=self.var_basic, bg = "lightgray",fg="black").place(x=450,y=50,width=100)

        lb1_day=Label(Frame2,text="Total Days ", font=("times new roman", 20),fg="white").place(x=10,y=120)
        txt_day=Entry(Frame2,font=("times new roman", 15),textvariable=self.var_day, bg = "lightgray",fg="black").place(x=165,y=125,width=140)

        lb1_absent=Label(Frame2,text="Absent ", font=("times new roman", 20),fg="white").place(x=350,y=120)
        txt_absent=Entry(Frame2,font=("times new roman", 15),textvariable=self.var_absent, bg = "lightgray",fg="black").place(x=440,y=125,width=120) 

        lb1_medical=Label(Frame2,text="Medical ", font=("times new roman", 20),fg="white").place(x=10,y=150)
        txt_medical=Entry(Frame2,font=("times new roman", 15),textvariable=self.var_medical, bg = "lightgray",fg="black").place(x=165,y=155,width=140)

        lb1_pf=Label(Frame2,text="Pf ", font=("times new roman", 20),fg="white").place(x=350,y=150)
        txt_pf=Entry(Frame2,font=("times new roman", 15),textvariable=self.var_pf, bg = "lightgray",fg="black").place(x=440,y=155,width=120)

        lb1_conve=Label(Frame2,text="Convec ", font=("times new roman", 20),fg="white").place(x=10,y=180)
        txt_conve=Entry(Frame2,font=("times new roman", 15),textvariable=self.var_convec, bg = "lightgray",fg="black").place(x=165,y=185,width=140)

        lb1_net=Label(Frame2,text="Net Salary ", font=("times new roman", 20),fg="white").place(x=350,y=183)
        txt_net=Entry(Frame2,font=("times new roman", 15),textvariable=self.var_net, bg = "lightgray",fg="black").place(x=440,y=185,width=120)

        btn_calculate=Button(Frame2,text="Calculate",command=self.calculate, font=("times new roman", 20),fg='Black').place(x=130,y=225,height=30)
        self.btn_save=Button(Frame2,text="Save",command=self.add, font=("times new roman", 20),fg="Black")
        self.btn_save.place(x=250,y=225,height=30,width=100)
        btn_clear=Button(Frame2,text="Clear",command=self.clear, font=("times new roman", 20),fg="Black").place(x=360,y=225,height=30,width=100)

        self.btn_update=Button(Frame2,text="Update",state=DISABLED,command=self.update, font=("times new roman", 20), bg='red',fg='Black')
        self.btn_update.place(x=200,y=258,height=30)
        self.btn_delete=Button(Frame2,text="Delete",state=DISABLED,command=self.delete, font=("times new roman", 20),fg="Black")
        self.btn_delete.place(x=300,y=258,height=30,width=100)


        Frame3=Frame(self.root,bd=3,relief=RIDGE)
        Frame3.place(x=770,y=380,width=580,height=310)

        var_txt=StringVar()
        self.var_operator=''
        def btn_click(num):
            self.var_operator=self.var_operator+str(num)
            var_txt.set(self.var_operator)

        def result():
            res=str(eval(self.var_operator))
            var_txt.set(res)
            self.var_operator=''  
        def clear_cal():
            var_txt.set('')
            self.var_operator=''  

        Cal_Frame=Frame(Frame3, bd=2, relief=RIDGE)
        Cal_Frame.place(x=2,y=2,width=229,height=300)

        txt_result=Entry(Cal_Frame, bg="lightgray",textvariable=var_txt, font=("times new roman",25,"bold"), fg="black")
        txt_result.place(x=0,y=0,relwidth=1,height=70)

        btn_7=Button(Cal_Frame,text='7',command=lambda:btn_click(7),font=("times new roman",15,"bold")).place(x=0,y=70,width=60,height=60)
        btn_8=Button(Cal_Frame,text='8',command=lambda:btn_click(8),font=("times new roman",15,"bold")).place(x=55,y=70,w=60,h=60)
        btn_9=Button(Cal_Frame,text='9',command=lambda:btn_click(9),font=("times new roman",15,"bold")).place(x=110,y=70,w=60,h=60)
        btn_div=Button(Cal_Frame,text='/',command=lambda:btn_click('/'),font=("times new roman",15,"bold")).place(x=165,y=70,w=60,h=60)

        btn_6=Button(Cal_Frame,text='6',command=lambda:btn_click(6),font=("times new roman",15,"bold")).place(x=0,y=123,width=60,height=60)
        btn_5=Button(Cal_Frame,text='5',command=lambda:btn_click(5),font=("times new roman",15,"bold")).place(x=55,y=123,w=60,h=60)
        btn_4=Button(Cal_Frame,text='4',command=lambda:btn_click(4),font=("times new roman",15,"bold")).place(x=110,y=123,w=60,h=60)
        btn_mul=Button(Cal_Frame,text='*',command=lambda:btn_click('*'),font=("times new roman",15,"bold")).place(x=165,y=123,w=60,h=60)

        btn_1=Button(Cal_Frame,text='1',command=lambda:btn_click(1),font=("times new roman",15,"bold")).place(x=0,y=179,width=60,height=60)
        btn_2=Button(Cal_Frame,text='2',command=lambda:btn_click(2),font=("times new roman",15,"bold")).place(x=55,y=179,w=60,h=60)
        btn_3=Button(Cal_Frame,text='3',command=lambda:btn_click(3),font=("times new roman",15,"bold")).place(x=110,y=179,w=60,h=60)
        btn_sub=Button(Cal_Frame,text='-',command=lambda:btn_click('-'),font=("times new roman",15,"bold")).place(x=165,y=179,w=60,h=60)

        btn_zer=Button(Cal_Frame,text='0',command=lambda:btn_click(0),font=("times new roman",15,"bold")).place(x=0,y=236,width=60,height=60)
        btn_dot=Button(Cal_Frame,text='C',command=clear_cal,font=("times new roman",15,"bold")).place(x=55,y=236,w=60,h=60)
        btn_add=Button(Cal_Frame,text='+',command=lambda:btn_click('+'),font=("times new roman",15,"bold")).place(x=110,y=236,w=60,h=60)
        btn_eql=Button(Cal_Frame,text='=',command=result,font=("times new roman",15,"bold")).place(x=165,y=236,w=60,h=60)

        sal_frame=Frame(Frame3,bd=2,relief=RIDGE)
        sal_frame.place(x=235,y=2,width=335,height=300)

        title_sal=Label(sal_frame,text="Salary Reciept", font=("times new roman", 25), bg="lightgray", fg="black").place(x=0,y=0,relwidth=1)

        sal_frame2=Frame(sal_frame,bg='white',bd=2,relief=RIDGE)
        sal_frame2.place(x=0,y=30,relwidth=1,height=230)

        self.sample=f'''\t  Company : TCS, \n\t  Address : 24-E Noida
---------------------------------------------------------
Employee ID\t\t:   
Salary of\t\t:   Mon-YYYY
Generated On\t\t:   DD-MM-YYYY
---------------------------------------------------------
Total Days\t\t:   DD
Total Present\t\t:   DD
Total Absent\t\t:   DD
Convence\t\t:   Rs.----
Medical\t\t:   Rs.----
PF\t\t:   Rs.----
Gross Payment\t\t:   Rs.------
Net Salary\t\t:   Rs.------
---------------------------------------------------------
This is computer generated slip, not
required any signature
'''

        scroll_y=Scrollbar(sal_frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)

        self.txt_salary_reciept=Text(sal_frame2,font=("times new roman",16),bg='lightgray',fg='black',yscrollcommand=scroll_y.set)
        self.txt_salary_reciept.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_reciept.yview)

        self.txt_salary_reciept.insert(END,self.sample)

        self.btn_print=Button(sal_frame,text="Print",state=DISABLED,command=self.print, font=("times new roman", 20),bg='lightblue')
        self.btn_print.place(x=200,y=260,height=35,width=115)

        self.check_connection()

 #==============All Functions==============       
    def search(self):
        try:
            con=pymysql.connect(host='localhost', user='root', password='root',db='ems', port=8889)
            cur=con.cursor()
            cur.execute("select * from emp_sal where e_id=%s", (self.var_emp_id.get()))
            rows=cur.fetchone()
            if rows==None:
                messagebox.showerror("Error","Invalid Employee ID, please try with another Employee ID", parent=self.root)
            else:
                print(rows)
                self.var_emp_id.set(rows[0])
                self.var_designation.set(rows[1])
                self.var_name.set(rows[2])
                self.var_age.set(rows[3])
                self.var_gender.set(rows[4])
                self.var_email.set(rows[5])
                self.var_heird.set(rows[6])
                self.var_doj.set(rows[7])
                self.var_dob.set(rows[8])
                self.var_experience.set(rows[9])
                self.var_proof.set(rows[10])
                self.var_phone.set(rows[11])
                self.var_status.set(rows[12])
                self.txt_add.delete('1.0',END)
                self.txt_add.insert(END,rows[13])
                self.var_month.set(rows[14])
                self.var_year.set(rows[15])
                self.var_basic.set(rows[16])
                self.var_day.set(rows[17])
                self.var_absent.set(rows[18])
                self.var_medical.set(rows[19])
                self.var_pf.set(rows[20])
                self.var_convec.set(rows[21])
                self.var_net.set(rows[22])

                file=open('Salary_reciept/'+str(rows[23]),'r')
                self.txt_salary_reciept.delete('1.0',END)
                for i in file:
                    self.txt_salary_reciept.insert(END,i)
                file.close()
                self.btn_save.config(state=DISABLED)
                self.btn_update.config(state=NORMAL)
                self.btn_delete.config(state=NORMAL)
                self.txt_id.config(state="readonly")
                self.btn_print.config(state=NORMAL)
        except Exception as ex:
                messagebox.showerror("Error", f'Error due to: {str(ex)}') 

    def clear(self):
        self.btn_save.config(state=NORMAL)
        self.btn_update.config(state=DISABLED)
        self.btn_delete.config(state=DISABLED)
        self.btn_print.config(state=DISABLED)
        self.txt_id.config(state=NORMAL)
        self.var_emp_id.set('')
        self.var_designation.set('')
        self.var_name.set('')
        self.var_age.set('')
        self.var_gender.set('')
        self.var_email.set('')
        self.var_heird.set('')
        self.var_doj.set('')
        self.var_dob.set('')
        self.var_experience.set('')
        self.var_proof.set('')
        self.var_phone.set('')
        self.var_status.set('')
        self.txt_add.delete('1.0',END)
        self.var_month.set('')
        self.var_year.set('')
        self.var_basic.set('')
        self.var_day.set('')
        self.var_absent.set('')
        self.var_medical.set('')
        self.var_pf.set('')
        self.var_convec.set('')
        self.var_net.set('')
        self.txt_salary_reciept.delete('1.0',END)
        self.txt_salary_reciept.insert(END,self.sample)



    def delete(self):
        if self.var_emp_id.get()=='':
            messagebox.showerror("Error","Employee ID msut be required")
        else:    
            try:
                con=pymysql.connect(host='localhost', user='root', password='root',db='ems', port=8889)
                cur=con.cursor()
                cur.execute("select * from emp_sal where e_id=%s", (self.var_emp_id.get()))
                rows=cur.fetchone()
                if rows==None:
                    messagebox.showerror("Error","Invalid Employee ID, please try with another Employee ID", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "Do you really want to delete")
                    print(op)
                    if op==True:
                        cur.execute("delete from emp_sal where e_id=%s", self.var_emp_id.get())
                        con.commit()
                        con.close()
                        messagebox.showerror("Delete","Employee deleted successfully", parent=self.root)
                        self.clear()
            except Exception as ex:
                    messagebox.showerror("Error", f'Error due to: {str(ex)}')

    def update(self): 
        if self.var_emp_id.get()=='' or self.var_net.get()=='' or self.var_name.get()=='':
            messagebox.showerror("Error", "Employee details required")
        else:    
            try:
                con=pymysql.connect(host='localhost', user='root', password='root',db='ems', port=8889)
                cur=con.cursor()
                cur.execute("select * from emp_sal where e_id=%s", (self.var_emp_id.get()))
                rows=cur.fetchone()
                if rows==None:
                    messagebox.showerror("Error","This Employee ID is invalid, try again with valid Employee ID", parent=self.root)
                else:
                    cur.execute("UPDATE `emp_sal` SET `designtion`=%s,`name`=%s,`age`=%s,`gender`=%s,`email`=%s,`hr_loc`=%s,`doj`=%s,`dob`=%s,`experience`=%s,`proof_id`=%s,`contact`=%s,`status`=%s,`address`=%s,`month`=%s,`year`=%s,`basic_sal`=%s,`t_days`=%s,`a_days`=%s,`medical`=%s,`pf`=%s,`convence`=%s,`net_sal`=%s,`salary_reciept`=%s WHERE `e_id`=%s",
                                (
                                self.var_designation.get(),
                                self.var_name.get(),
                                self.var_age.get(),
                                self.var_gender.get(),
                                self.var_email.get(),
                                self.var_heird.get(),
                                self.var_doj.get(),
                                self.var_dob.get(),
                                self.var_experience.get(),
                                self.var_proof.get(),
                                self.var_phone.get(),
                                self.var_status.get(),
                                self.txt_add.get('1.0',END),
                                self.var_month.get(),
                                self.var_year.get(),
                                self.var_basic.get(),
                                self.var_day.get(),
                                self.var_absent.get(),
                                self.var_medical.get(),
                                self.var_pf.get(),
                                self.var_convec.get(),
                                self.var_net.get(),
                                self.var_emp_id.get()+".txt",
                                self.var_emp_id.get()
                                ))
                    con.commit()
                    con.close() 
                    if not os.path.exists("salary_reciept"):
                        os.makedirs("salary_reciept")


                    file_path = os.path.join("salary_reciept", f"{self.var_emp_id.get()}.txt")
                    with open(file_path, 'w') as file:
                        file.write(self.txt_salary_reciept.get('1.0', END))
                    messagebox.showinfo("Sucess", "Record Updated Successfully")
            except Exception as ex:
                messagebox.showerror("Error", f'Error due to: {str(ex)}')

    def add(self): 
        if self.var_emp_id.get()=='' or self.var_net.get()=='' or self.var_name.get()=='':
            messagebox.showerror("Error", "Employee details required")
        else:    
            try:
                con=pymysql.connect(host='localhost', user='root', password='root',db='ems', port=8889)
                cur=con.cursor()
                cur.execute("select * from emp_sal where e_id=%s", (self.var_emp_id.get()))
                rows=cur.fetchone()
                if rows!=None:
                    messagebox.showerror("Error","This Employee ID is already available in our record, try again with another ID", parent=self.root)
                else:
                    cur.execute("insert into emp_sal values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (self.var_emp_id.get(),
                                self.var_designation.get(),
                                self.var_name.get(),
                                self.var_age.get(),
                                self.var_gender.get(),
                                self.var_email.get(),
                                self.var_heird.get(),
                                self.var_doj.get(),
                                self.var_dob.get(),
                                self.var_experience.get(),
                                self.var_proof.get(),
                                self.var_phone.get(),
                                self.var_status.get(),
                                self.txt_add.get('1.0',END),
                                self.var_month.get(),
                                self.var_year.get(),
                                self.var_basic.get(),
                                self.var_day.get(),
                                self.var_absent.get(),
                                self.var_medical.get(),
                                self.var_pf.get(),
                                self.var_convec.get(),
                                self.var_net.get(),
                                self.var_emp_id.get()+".txt"   
                                ))
                    con.commit()
                    con.close() 
                    if not os.path.exists("salary_reciept"):
                        os.makedirs("salary_reciept")


                    file_path = os.path.join("salary_reciept", f"{self.var_emp_id.get()}.txt")
                    with open(file_path, 'w') as file:
                        file.write(self.txt_salary_reciept.get('1.0', END))
                    messagebox.showinfo("Sucess", "Record Added Successfully")
                    self.btn_print.config(state=NORMAL)
            except Exception as ex:
                messagebox.showerror("Error", f'Error due to: {str(ex)}')



    def calculate(self):
        if self.var_month.get()=='' or self.var_year.get()=='' or self.var_basic.get()=='' or self.var_absent.get()=='' or self.var_convec.get()=='' or self.var_day.get()=='':
            messagebox.showerror("Error", "All fields are required")
        else :
            per_day=int(self.var_basic.get())/int(self.var_day.get())
            work_day=int(self.var_day.get())-int(self.var_absent.get())
            sal=per_day*work_day
            deduct=int(self.var_medical.get())+int(self.var_pf.get())
            addition=int(self.var_convec.get())
            net_sal=sal-deduct+addition
            self.var_net.set(str(round(net_sal,2)))    
            new_sample=f'''\t  Company : TCS, \n\t  Address : 24-E Noida
---------------------------------------------------------
Employee ID\t\t:   {self.var_emp_id.get()}
Salary of\t\t:   {self.var_month.get()}-{self.var_year.get()}
Generated On\t\t:   {str(time.strftime("%d-%m-%Y"))}
---------------------------------------------------------
Total Days\t\t:   {self.var_day.get()}
Total Present\t\t:   {str(int(self.var_day.get())-int(self.var_absent.get()))}
Total Absent\t\t:   {self.var_absent.get()}
Convence\t\t:   Rs.{self.var_convec.get()}
Medical\t\t:   Rs.{self.var_medical.get()}
PF\t\t:   Rs.{self.var_pf.get()}
Gross Payment\t\t:   Rs.{self.var_basic.get()}
Net Salary\t\t:   Rs.{self.var_net.get()}
---------------------------------------------------------
This is computer generated slip, not
required any signature
'''       
                 
            self.txt_salary_reciept.delete('1.0',END)
            self.txt_salary_reciept.insert(END,new_sample)

    def check_connection(self):
        try:
            con=pymysql.connect(host='localhost', user='root', password='root',db='ems', port=8889)
            cur=con.cursor()
            cur.execute("select * from emp_sal")
            rows=cur.fetchall()

        except Exception as ex:
            messagebox.showerror("Error", f'Error due to: {str(ex)}')

    def show(self):
        try:
            con=pymysql.connect(host='localhost', user='root', password='root',db='ems', port=8889)
            cur=con.cursor()
            cur.execute("select * from emp_sal")
            rows=cur.fetchall()
            self.employee_tree.delete(*self.employee_tree.get_children())
            for row in rows:
                self.employee_tree.insert('', END, values=row)
            con.close()    

        except Exception as ex:
            messagebox.showerror("Error", f'Error due to: {str(ex)}')        


    def employee_frame(self):
        self.root2=Toplevel(self.root)
        self.root2.title("Employee Payroll management System")
        self.root2.geometry("1000x500+120+100")
        self.root2.config(bg="white")
        title=Label(self.root2,text="All Employee Details", font=("times new roman", 30, "bold"), bg="#262626", fg="white").pack(side=TOP,fill=X)

        scrolly=Scrollbar(self.root2, orient=VERTICAL)
        scrollx=Scrollbar(self.root2,orient=HORIZONTAL)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.pack(side=BOTTOM,fill=X)


        self.employee_tree=ttk.Treeview(self.root2,columns=('e_id', 'designtion', 'name', 'age', 'gender', 'email', 'hr_loc', 'doj', 'dob', 'experience', 'proof_id', 'contact', 'status', 'address', 'month', 'year', 'basic_sal', 't_days', 'a_days', 'medical', 'pf', 'convence', 'net_sal', 'salary_reciept'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.employee_tree.heading('e_id',text='EID')
        self.employee_tree.heading('designtion',text='Designation')
        self.employee_tree.heading('name',text='Name')
        self.employee_tree.heading('age',text='Age')
        self.employee_tree.heading('gender',text='Gender')
        self.employee_tree.heading('email',text='Email')
        self.employee_tree.heading('hr_loc',text='Hr_Location')
        self.employee_tree.heading('doj',text='D.O.J')
        self.employee_tree.heading('dob',text='D.O.B')
        self.employee_tree.heading('experience',text='Experience')
        self.employee_tree.heading('proof_id',text='Proof ID')
        self.employee_tree.heading('contact',text='Phone Number')
        self.employee_tree.heading('status',text='Status')
        self.employee_tree.heading('address',text='Address')
        self.employee_tree.heading('month',text='Month')
        self.employee_tree.heading('year',text='Year')
        self.employee_tree.heading('basic_sal',text='Basic Salary')
        self.employee_tree.heading('t_days',text='Total Days')
        self.employee_tree.heading('a_days',text='Absent Days')
        self.employee_tree.heading('medical',text='Medical')
        self.employee_tree.heading('pf',text='P.F')
        self.employee_tree.heading('convence',text='Convence')
        self.employee_tree.heading('net_sal',text='Net Salary')
        self.employee_tree.heading('salary_reciept',text='Salary Reciept')
        self.employee_tree['show']='headings'

        self.employee_tree.column('e_id',width=50)
        self.employee_tree.column('designtion',width=150)
        self.employee_tree.column('name',width=150)
        self.employee_tree.column('age',width=100)
        self.employee_tree.column('gender',width=100)
        self.employee_tree.column('email',width=100)
        self.employee_tree.column('hr_loc',width=100)
        self.employee_tree.column('doj',width=100)
        self.employee_tree.column('dob',width=100)
        self.employee_tree.column('experience',width=100)
        self.employee_tree.column('proof_id',width=100)
        self.employee_tree.column('contact',width=100)
        self.employee_tree.column('status',width=100)
        self.employee_tree.column('address',width=200)
        self.employee_tree.column('month',width=100)
        self.employee_tree.column('year',width=100)
        self.employee_tree.column('basic_sal',width=100)
        self.employee_tree.column('t_days',width=100)
        self.employee_tree.column('a_days',width=100)
        self.employee_tree.column('medical',width=100)
        self.employee_tree.column('pf',width=100)
        self.employee_tree.column('convence',width=100)
        self.employee_tree.column('net_sal',width=100)
        self.employee_tree.column('salary_reciept',width=100)
        scrollx.config(command=self.employee_tree.xview)
        scrolly.config(command=self.employee_tree.yview)
        self.employee_tree.pack(fill=BOTH, expand=1)
        self.show()
        self.root2.mainloop()

    def print(self):
        try:
            file_path = os.path.join(tempfile.gettempdir(), f"{self.var_emp_id.get()}_salary_receipt.pdf")
            
            c = canvas.Canvas(file_path, pagesize=(600, 700))
            textobject = c.beginText(40, 680)
            textobject.setFont("Helvetica", 12)

            receipt_lines = self.txt_salary_reciept.get("1.0", END).split('\n')
            for line in receipt_lines:
                textobject.textLine(line)

            c.drawText(textobject)
            c.showPage()
            c.save()

            subprocess.run(["open", file_path])  

        except Exception as ex:
            messagebox.showerror("Error", f"Error while printing: {str(ex)}", parent=self.root)


root=Tk()
obj=EmployeeSystem(root)
root.mainloop()        