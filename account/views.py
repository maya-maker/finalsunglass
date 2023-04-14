from django.shortcuts import render,redirect
from .models import Customer
from django.contrib.auth.hashers import make_password,check_password



def signup(request):
    if request.method == "GET":
        return render(request,'singup.html')
    

    else:
        data = request.POST
        full_name = data.get('full_name')
        email = data.get('email')
        mobile_no = data.get('mobile_no')
        create_password = data.get('create_password')
        repeat_password = data.get('repeat_password')
        print(full_name)
        print(len(create_password))
        print(repeat_password)

        error = None
        if create_password!= repeat_password:
            error = "password is invalid"
        elif len(full_name)<4:
            error = "full name is less then "
        
        if not error:

            customer = Customer(full_name=full_name,
                                email=email,
                                mobile_no = mobile_no,
                                create_password=create_password
                                )
            customer.create_password = make_password(create_password)
            customer.save()
            return redirect('login')
        
        else:
            data = {
                "error":error
            }
            return render(request,'singup.html',data)


def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    
    else:
        data = request.POST
        email = data.get('email')
        password = data.get('password')
        print(email)
        print(password)
        customer = Customer.get_customer_by_email(email)
        print(customer)
        error_message = None
        if customer:
            flag = check_password(password,customer.create_password)
            if flag:
                request.session['customer']= customer.id
                request.session['email']= customer.email

                return redirect('index')
            else:
                error_message = "email & password invalid"
        else:
            error_message = "email & password invalid"
        return render(request,'login.html', {'error_message':error_message})
        

def logout(request):
    del request.session['customer']
    return redirect('index')
            
