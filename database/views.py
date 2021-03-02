from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from database.models import feedback
# from databse.models import 


def home(request):
    return render(request, 'index.html')


def submit(request):
    if request.method == 'POST':
        try:            
            name = request.POST.get('name')
            email = request.POST.get('email')
            comment = request.POST.get('comment')
            submit = feedback(name=name, email=email, comment=comment, date=datetime.today())

            submit.save()  
            return HttpResponse('''<title>Succeess</title>
                                <h1>
                                    <font color='green' face='Comic Sans MS'>
                                        <i>
                                            <u>
                                                <b>Congratulation, Your form has been submitted''')

        except:
            return HttpResponse('''<title>404 error</title>
                                <h1>
                                    <font color='blue' face='Comic Sans MS'>
                                        <i>
                                            <u>
                                                <b>Sorry!!! It is a technical 404 error!!!''')
        
    else:
        return HttpResponse('''<title>404 error</title>
                                <h1>
                                    <font color='red' face='Comic Sans MS'>
                                        <i>
                                            <u>
                                                <b>Sorry!!! It is a bad request 404 error!!!''')