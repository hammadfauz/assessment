# Create your views here.
import string, itertools, json
from django.http import HttpResponse
from django.template import loader, Context

def form(request):
  t = loader.get_template('form.html')
  c = Context()
  return HttpResponse(t.render(c))

def permutator(request, someString):
  stringArray = string.split(someString)
  if len(stringArray) > 1:
    retval = json.dumps([' '.join(p) for p in itertools.permutations(stringArray)])
    response = HttpResponse(retval)
    response['Content-Type'] = 'application/json'
    return response
  //10 letter permutations are cpu intensive and take very long
  retval = json.dumps([''.join(p) for p in itertools.permutations(someString[0:3])])
  response = HttpResponse(retval)
  response['Content-Type'] = 'application/json'
  return response
