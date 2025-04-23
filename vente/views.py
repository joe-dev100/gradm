from datetime import datetime
from django.shortcuts import redirect, render

from vente.models import Session

# Create your views here.
def session_list(request):
    items=Session.objects.all().order_by('login__username')
    context = {
        'items': items,
    }
    return render(request, 'vente/session/partial/response.html', context)



def session_update(request, pk):
    session = Session.objects.get(pk=pk)
    items=Session.objects.all().order_by('login__username')
    
    if session.EstOuvert == True:
        session.EstOuvert = False
        session.LastDateClose = datetime.now()
       
    else:
        session.EstOuvert = True
        session.LastDateOpen = datetime.now()
    context = {
        'items': items,
    }

    session.save()
    print("********************************************************")
    print(session.EstOuvert)
    return render(request, 'vente/session/partial/response.html', context)