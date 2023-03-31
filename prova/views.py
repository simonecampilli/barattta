from django.shortcuts import render

# Create your views here.
# views.py

from django.shortcuts import render, redirect
from .forms import PersonaForm
from .models import Persona

def aggiungi_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_persone') # redirect alla pagina di elenco persone
    else:
        form = PersonaForm()
    return render(request, 'aggiungi_persona.html', {'form': form})

# views.py

# views.py

from django.shortcuts import render
from .models import Persona


from django.shortcuts import render
from .models import Persona

def lista_persone(request):
    query = request.GET.get('q') # recupera il parametro di ricerca dalla query string
    if query:
        # Se la query è presente, esegue la ricerca per nome o cognome o entrambi
        persone = Persona.objects.filter(
            nome__icontains=query) | Persona.objects.filter(
            cognome__icontains=query)
    else:
        # Altrimenti, recupera tutte le persone dal database
        persone = Persona.objects.all()
    return render(request, 'lista_persone.html', {'persone': persone, 'query': query})
