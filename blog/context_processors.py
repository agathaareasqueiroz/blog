# blog\context_processors.py

def site_globals(request):
    return {
        'ownername': 'Joca da Silva',   # ← Nome do proprietário(a) do site
        'show_aside': True,             # ← Se `False`, `<aside>` é ocultado
    }