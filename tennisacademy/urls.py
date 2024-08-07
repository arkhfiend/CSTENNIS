"""
URL configuration for tennisacademy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from players import views,admin_view
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('players.urls')),
    # path('',home),
    path('', views.ShowHome, name="show_home"),
    path('show_aboutus', views.ShowAboutUs, name="show_aboutus"),
    path('admin_home', admin_view.admin_home, name="admin_home"),

    path('logout_user', views.logout_user, name="logout"),
    path('admin_profile', admin_view.admin_profile, name="admin_profile"),

#     Admin_urls

    path('add_staff/', admin_view.add_staff, name="add_staff"),
    # path('add_staff_save/', admin_view.add_staff_save, name="add_staff_save"),
    path('add_course/', admin_view.add_course, name="add_course"),
    # path('add_course_save/', admin_view.add_course_save, name="add_course_save"),
    path('add_student/', admin_view.add_student, name="add_student"),
    # path('add_student_save/', admin_view.add_student_save, name="add_student_save"),
    path('add_subject/', admin_view.add_subject, name="add_subject"),
    # path('add_subject_save/', admin_view.add_subject_save, name="add_subject_save"),
    path('manage_staff/', admin_view.manage_staff, name="manage_staff"),
    path('manage_student/', admin_view.manage_student, name="manage_student"),
    path('manage_course/', admin_view.manage_course, name="manage_course"),
    path('manage_subject/', admin_view.manage_subject, name="manage_subject"),
    path('edit_staff/<str:staff_id>/', admin_view.edit_staff, name="edit_staff"),
    # path('edit_staff_save/', admin_view.edit_staff_save, name="edit_staff_save"),
    # path('edit_student/<str:student_id>/', admin_view.edit_student, name="edit_student"),
    # path('edit_student_save/', admin_view.edit_student_save, name="edit_student_save"),
    path('edit_subject/<str:subject_id>/', admin_view.edit_subject, name="edit_subject"),
    # path('edit_subject_save/', admin_view.edit_subject_save, name="edit_subject_save"),
    path('edit_course/<str:course_id>/', admin_view.edit_course, name="edit_course"),
    # path('edit_course_save/', admin_view.edit_course_save, name="edit_course_save"),
    path('manage_session/', admin_view.manage_session, name="manage_session"),
    # path('add_session_save/', admin_view.add_session_save, name="add_session_save"),
    # path('check_email_exist/', admin_view.check_email_exist, name="check_email_exist"),
    # path('check_username_exist/', admin_view.check_username_exist, name="check_username_exist"),
    path('student_feedback_message/', admin_view.student_feedback_message, name="student_feedback_message"),
    # path('student_feedback_message_replied/', admin_view.student_feedback_message_replied,
    #      name="student_feedback_message_replied"),
    path('staff_feedback_message/', admin_view.staff_feedback_message, name="staff_feedback_message"),
    # path('staff_feedback_message_replied/', admin_view.staff_feedback_message_replied,
    #      name="staff_feedback_message_replied"),
    # path('student_leave_view/', admin_view.student_leave_view, name="student_leave_view"),
    # path('staff_leave_view/', admin_view.staff_leave_view, name="staff_leave_view"),
    # path('student_approve_leave/<str:leave_id>/', admin_view.student_approve_leave, name="student_approve_leave"),
    # path('student_disapprove_leave/<str:leave_id>/', admin_view.student_disapprove_leave,
    #      name="student_disapprove_leave"),
    # path('staff_disapprove_leave/<str:leave_id>/', admin_view.staff_disapprove_leave, name="staff_disapprove_leave"),
    # path('staff_approve_leave/<str:leave_id>/', admin_view.staff_approve_leave, name="staff_approve_leave"),
    path('admin_view_attendance/', admin_view.admin_view_attendance, name="admin_view_attendance"),
    # path('admin_get_attendance_dates/', admin_view.admin_get_attendance_dates, name="admin_get_attendance_dates"),
    # path('admin_get_attendance_student/', admin_view.admin_get_attendance_student, name="admin_get_attendance_student"),
    path('admin_profile/', admin_view.admin_profile, name="admin_profile"),
    # path('admin_profile_save/', admin_view.admin_profile_save, name="admin_profile_save"),
    path('admin_send_notification_staff/', admin_view.admin_send_notification_staff,
         name="admin_send_notification_staff"),
    path('admin_send_notification_student/', admin_view.admin_send_notification_student,
         name="admin_send_notification_student"),
    # path('send_student_notification/', admin_view.send_student_notification, name="send_student_notification"),
    # path('send_staff_notification/', admin_view.send_staff_notification, name="send_staff_notification"),

]


