from django.shortcuts import render
# from pages.models import *

# Create your views here.
def dashHome(request):
    # profile = UserProfile.objects.filter(user = request.user)

    # ctxt = {
    #     'profile' : profile[0],
    # }
    # print(profile[0])

    return render(request, 'dashboard/dashHome.html') #, context=ctxt)
