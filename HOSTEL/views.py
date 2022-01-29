from django.shortcuts import render,HttpResponse,redirect
import mysql.connector as mysql
from django.middleware import csrf
# Create your views here.
def home(request):    
   return render(request,'home.html')
def admin_login(request):
     return render(request,'admin_login.html')
def admin_info(request):
    Emailid=request.GET.get("Email")
    Password=request.GET.get("pass")
    if Emailid =='narmadha987@gmail.com' and Password =='narmadha123':
       return render(request,'admin_home.html')
    else:
       return render(request,'admin_login_error.html')
def student_login(request):
     return render(request,'student_login.html')
def student_apply(request):
     return render(request,'student_apply.html')
def student_apply_data(request):
        Regno=request.GET.get("RegNo")
        Name=request.GET.get("Name")
        Email=request.GET.get("Email")
        Mobile=request.GET.get("MobileNo")
        Course=request.GET.get("Course")
        Semester=request.GET.get("Semester")
        Address=request.GET.get("Address")
        Password=request.GET.get("pass")
        Cpassword=request.GET.get("Cpass")  
        conn=mysql.connect(host="localhost",user="root",password="Narmadha!04",database="hostel")
        cr = conn.cursor()
        query="insert into Studentdata values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')".format(Regno,
          Name,Email,Mobile,Course,Semester,Address,Password,Cpassword)
        cr.execute(query)
        conn.commit()
        conn.close()
        return render(request,'student_apply.html')
def student_login_data(request):
	Username=request.GET.get("Email")
	Password=request.GET.get("pass")
	conn=mysql.connect(host="localhost",user="root",password="Narmadha!04",database="hostel")
	cr=conn.cursor()
	cr.execute("select * from Studentdata")
	while True:
		row=cr.fetchone()
		if row is None:
			break;
		elif row[2]==Username and row[7]==Password:
			return render(request,'student_home.html')
	return render(request,'student_login.html')
def contact(request):
     return render(request,'contact.html')
def aboutus(request):
     return render(request,'aboutus.html')
def admin_home(request):
     return render(request,'admin_home.html')
def admin_logout(request):
     return render(request,'admin_login.html')
def manage_student_details_logout(request):
     return render(request,'admin_home.html')
def student_logout(request):
     return render(request,'student_login.html')
def manage_student(request):
          return render(request,'manage_student.html')
def student_details(request):
        conn=mysql.connect(host="localhost",user="root",password="Narmadha!04",database="hostel")
        cr = conn.cursor()
        query="select* from Studentdata"
        cr.execute(query)
        result = cr.fetchall()
        conn.commit()
        conn.close()
        return render(request,'student_details.html',{'result':result})
def manage_room(request): 
	
		Name=request.GET.get("Name")
		Department=request.GET.get("Department")
		MobileNo=request.GET.get("MobileNo")
		RoomNo=request.GET.get("RoomNo")
		Foodstatus=request.GET.get("Foodstatus")
		Duration=request.GET.get("Duration")
		Fees=request.GET.get("Fees")  	              
		conn=mysql.connect(host="localhost",user="root",
		password="Narmadha! 			04",database="room")                            
		cr = conn.cursor()
		query="insert into roomdetails values('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(Name,Department,
		  MobileNo,RoomNo,Foodstatus,Duration,Fees)
		cr.execute(query)
		conn.commit()
		conn.close()	
		return render(request,'manage_room.html')
def show_room(request):
	conn=mysql.connect(host="localhost",user="root",password="Narmadha!04",database="adminroom")
	cr = conn.cursor()
	query="select* from adminbookroom"
	cr.execute(query)
	result = cr.fetchall()
	conn.commit()
	conn.close()
	return render(request,'show_room.html',{'result':result})
def book_room(request):
	
		Name=request.GET.get("Name")
		Department=request.GET.get("Department")
		MobileNo=request.GET.get("MobileNo")
		RoomNo=request.GET.get("RoomNo")
		BlockNo=request.GET.get("BlockNo")
		Foodstatus=request.GET.get("Foodstatus")
		Duration=request.GET.get("Duration")
		conn=mysql.connect(host="localhost",user="root",
		password="Narmadha!04",database="Room")    
		cr = conn.cursor()
		
		query="insert into bookroom values('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(Name,Department,
		  MobileNo,RoomNo,BlockNo,Foodstatus,Duration)
		cr.execute(query)
		conn.commit()
		conn.close()
		
		return render(request,'book_room.html')

def view_details(request):
        conn=mysql.connect(host="localhost",user="root",password="Narmadha!04",database="Room")
        cr = conn.cursor()
        query="select* from bookroom"
        cr.execute(query)
        result = cr.fetchall()
        conn.commit()
        conn.close()
        return render(request,'view_details.html',{'result':result})
def student_home(request): 
        return render(request,'student_home.html')
def room_details(request):
        return render(request,'room_details')
def room_details(request):
        BlockNo=request.GET.get("BlockNo")
        RoomNo=request.GET.get("RoomNo")
        Foodstatus=request.GET.get("Foodstatus")
        Roomtype=request.GET.get("Roomtype")
        Duration=request.GET.get("Duration")
        Fees=request.GET.get("Fees")
        conn=mysql.connect(host="localhost",user="root",password="Narmadha!04",database="adminroom")    
        cr = conn.cursor()
        query="insert into adminbookroom values('{0}','{1}','{2}','{3}','{4}','{5}')".format(BlockNo,RoomNo,Foodstatus,Roomtype,Duration,Fees)
        cr.execute(query)
        conn.commit()
        conn.close()
        return render(request,'room_details.html')
def manage_room_logout(request):
        return render(request,'admin_home.html')





          



      
