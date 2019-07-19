from django.shortcuts import render, HttpResponse
http_base = """ 
            <h1>Página de práctica</h1>
            <ul>
                <li><a href='/'>Portada</a></li>
                <li><a href='/about'>Acerca de</a></li>
                <li><a href='/portfolio'>Portafolio</a></li>
                <li><a href='/contact'>Contacto</a></li>
            </ul>"""
# Create your views here.
def home(request):
    return HttpResponse(http_base + """ <h2>les manda saludos al 
                        equipo ALFA el Ingeniero Ivek</h2>""")

def about(request):
  return HttpResponse(http_base + """<h2>Acerca de mi</h2> 
                        <h2>Soy Ingeniero Ivek amo la tecnologia
                        y me encanta Python</h2>""")

def portfolio(request):
    return HttpResponse(http_base + """<h2>Portafolio</h2> 
                        <h2>He realizado pocos 
                        proyectos pero bonitos</h2>""")

def contact(request):
    return HttpResponse(http_base + """ <h2>Contacto</h2>
                          <h2>mi correo de contacto es
                          ivekdelfin@gmail.com  </h2>""")
