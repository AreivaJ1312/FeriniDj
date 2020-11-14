from django.urls import path
from .views import home, aros, Contacto, ListadoAros, nuevo_aro,modificar_aro, elimimar_aro, registro_usuario
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name ="home"),
    path('aros', aros, name ="aros"),
    path('Contacto', Contacto, name ="Contacto"),
    path('ListadoAros',ListadoAros ,name= "ListadoAros" ),
    path('nuevo_aro', nuevo_aro, name= "nuevo_aro"),
    path('modificar_aro/<id>', modificar_aro, name="modificar_aro"),
    path('eliminar_aro/<id>',elimimar_aro, name="eliminar_aro"),
    path('registro_usuario', registro_usuario, name= "registro_usuario"),
     path('reset/password_reset', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html', email_template_name='registration/password_reset_email.html'), name="password_reset"),
    path('reset/password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name="password_reset_done"),
    path('reset/password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/password_reset/done', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]