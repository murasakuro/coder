from django.http import HttpResponse
from django.template import loader

def template1 (request):
    data={
        "key1": "value"
    }
    
    template=loader.get_template("mi_primer_template.html")
    rendered_template=template.render(data)
    
    return HttpResponse(rendered_template)