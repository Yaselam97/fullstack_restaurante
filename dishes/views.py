from django.shortcuts import render
from .models import Dish
from .models import ContactMessage
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
import json

def dishes(request):
    # Recupera i piatti dal database
    dishes_queryset = Dish.objects.all()
    
    # Crea una lista di dizionari con i dati rilevanti
    dishes_data = [
        {
            "id": dish.id,
            "name": dish.name,
            "price": dish.price
        } 
        for dish in dishes_queryset
    ]
    
    # Serializza i dati in JSON per passarli al template
    dishes_json = json.dumps(dishes_data, cls=DjangoJSONEncoder)
    
    return render(request, 'dishes/dishes.html', {
        'dishes': dishes_queryset,  # Per visualizzazione tradizionale
        'dishes_json': dishes_json  # Per il JavaScript
    })

def contattaci(request):
    if request.method == "POST":
        # Recupera i dati inviati dal modulo
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Salva il messaggio nel database
        ContactMessage.objects.create(name=name, email=email, message=message)

        # Risposta di successo
        return JsonResponse({"success": True})

    # Mostra solo il modulo di contatto
    return render(request, 'dishes/contattaci.html')