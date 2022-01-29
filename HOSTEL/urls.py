from django.urls import path
from.import views
urlpatterns=[ 
       path('/home',views.home),
       path('/admin_info',views.admin_info),
       path('/admin_login',views.admin_login),
       path('/student_login',views.student_login),
        path('/student_apply',views.student_apply),
        path('/student_apply_data',views.student_apply_data),
        path('/student_login_data',views.student_login_data),
        path('/student_home',views.student_home),
        path('/admin_home',views.admin_home),
        path('/contact',views.contact),
        path('/aboutus',views.aboutus),
        path('/admin_logout',views.admin_logout),
        path('/student_logout',views.student_logout),
        path('/manage_student_details_logout',views.manage_student_details_logout),
        path('/manage_student',views.manage_student),
        path('/student_details',views.student_details),
        path('/manage_room',views.manage_room),
        path('/show_room',views.show_room),
        path('/book_room',views.book_room),
        path('/view_details',views.view_details),
        path('/room_details',views.room_details),
        path('/manage_room_logout',views.manage_room_logout),
        #path('/room_details_data',views.room_details_data),
    
    ]
       
