from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup_page/',views.signup_page, name='signup'),
    path('signup/',views.signup, name='signup'),
    path('login_page/',views.login_page),
    path('student_login/',views.student_login),
    path('start/<int:quiz_id>/',views.start),
    path('next/',views.next),
    path('create_quiz/',views.create),
    path('school/login/create_quiz/',views.create),
    path('save_quiz/',views.save_quiz)

]