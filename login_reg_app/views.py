from django.shortcuts import render, redirect, reverse
from login_reg_app.models import User
from django.db.models import Q
from django.contrib import messages
import bcrypt
from django.views import View
from login_reg_app.forms import LoginForm, RegisterForm
from django.urls import reverse
from login_reg_app.email import EmailThread

# Create your views here.

class LoginLocal(View):
    def get(self, request):
        
        if 'usuario' in request.session:
            messages.error(request, 'Ya estas logeado, para salir click en salir')
            return redirect ("/workload")
        
        contexto = {
            'formLogin': LoginForm(),
            }
        print(contexto)
        return render(request, 'login_reg_app/login.html', contexto)
    
    def post(self, request):
        print(request.POST)
        form = LoginForm(request.POST)
        
        if form.is_valid():
            
            user = User.objects.filter(Q(username=form.cleaned_data['username'])| Q(email=form.cleaned_data['username'])).first()
            if user:
                form_password = form.cleaned_data['password']
                if bcrypt.checkpw(form_password.encode(), user.password.encode()):
                # Si existe el usuario y si obtenemos True después de validar la contraseña, podemos poner la identificación del usuario en la sesión
                    print(f'*'*10,'estoy verificando')
                    messages.success(request, 'Bienvenido')
                    request.session['usuario'] = { 'nombre' : user.nombre, 'username' : user.username, 'email' : user.email, 'id' : user.id}
                    request.session['id'] = user.id
                    # iduser = request.session['usuario'] 
                    # idname=iduser['nombre']
                    return redirect(reverse('plantilla33_app:dashboard'))                    
                    # contexto = {}
                    # return render(request, 'login_reg_app/workload.html', contexto)

                else:
                    print(f'*'*10,'1. contraseña  email nombre incorrecto')
                    messages.error(request, 'Contraseña o username incorrecto')
            else: #si no existe el usuario
                messages.error(request, 'Contraseña o username incorrecto')
                print(f'*'*10,'2. contraseña  email nombre incorrecto')
                
            return redirect(reverse('login_reg_app:login'))
    
class RegisterLocal(View):
    def get(self, request):
        
        if 'usuario' in request.session:
            messages.error(request, 'Ya estas logeado, para salir click en salir')
            return redirect ("/workload") #esto se podria llevar a una clase para ahorrar codigo
        
        contexto = {
            'formRegister': RegisterForm(),
        }
        print(contexto)
        return render(request, 'login_reg_app/register.html', contexto)
    
    def post(self, request):
        print(request.POST)
        
        form = RegisterForm(request.POST) #cargar los datos al formulario
        # print(form)

        
        if form.is_valid():
            usuario=form.save(commit=False) #commit=false no se guarda en la Bds
            usuario.password =bcrypt.hashpw(usuario.password.encode(), bcrypt.gensalt()).decode()
            usuario.save()
            messages.success(request, 'usuario agregado correctamente')
            
            EmailThread("Correo de Prueba ASINCRONICA", 
                        'login_reg_app/correo.html', 
                        ['ingenieroteleco@gmail.com']
                        ).start()
            
            
            return redirect(reverse('login_reg_app:login'))
        else:            
            contexto = {
                'formRegister': RegisterForm,
            }
            print('*'*20,contexto)
            messages.error(request, 'con errores en los campos, solucionar')
            return render(request, 'login_reg_app/register.html', contexto)  #devolver el mismo form, para no cargar uno nuevo
        

def logout(request):
    if 'usuario' in request.session:
        del request.session['usuario']
        messages.info(request, "Para volver a entrar debes logearte nuevamente")
        return redirect(reverse('login_reg_app:login'))

def workload(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'login_reg_app/workload.html', context)
    
class validador(View):  #se puede optimizar? reusando la clase, como hago para el return
    def get(self, request):
        
        # if 'usuario' in request.session:
        #     messages.error(request, 'Ya estas logeado, para salir click en salir')
        #     return redirect ("/workload")
        
        contexto = {
            'formLogin': LoginForm(),
            }
        print(contexto)
        return render(request, 'login_reg_app/validador.html', contexto)
    
# def Login_Reg(request):
#     return render(request, 'login_reg.html')

# def Register(request):
#     print(request.POST)
#     errors = User.objects.validate_register(request.POST)
#     if len(errors) > 0:
#         print("Errors",errors)
#         for key, value in errors.items():
#             messages.error(request, value)
#         return redirect('/')
#     else:
#         pwhash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
#         user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pwhash.decode())
#         print("User: ", user)
#         request.session['id'] = user.id
#     return redirect('/dashboard')

# def Login(request):
#     errors = User.objects.validate_login(request.POST)
#     if len(errors) > 0:
#         for key, value in errors.items():
#             messages.error(request, value)
#         return redirect('/')
#     else:
#         user = User.objects.get(email=request.POST['email'])
#         request.session['id'] = user.id
#     return redirect('/dashboard')

# def Success(request):
#     user = User.objects.get(id=request.session['id'])
#     return render(request, 'login_reg_app/success.html', {'user':user})

# def Logout(request):
#     request.session.clear()
#     print("Logged Out")
#     return redirect('/')
