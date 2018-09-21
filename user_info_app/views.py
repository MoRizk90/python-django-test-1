from django.http import HttpResponse
from django.shortcuts import render
from user_info_app.models import USER

# Create your views here.
def index(request):
    return render(request, 'index.html')

def user(request):
    the_users_list = USER.objects.order_by('first_name')
    user_dict = {'the_users' : the_users_list}
    print (user_dict)
    return render(request,'user.html', context = user_dict)
