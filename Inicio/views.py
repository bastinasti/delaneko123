from django.shortcuts import render
from .models import Producto

# Create your views here.
def inicio(request):
    return render(request, 'Inicio/DelanekoShop.html')

def registro(request):
    return render(request, 'Inicio/Registro/registro.html')

def seccionperro(request):
    perro = Producto.objects.filter(idTipProducto = 2).order_by('idProducto')
    contexto = {"producto":perro}
    return render(request, 'Inicio/PagAnimales/Perros.html',contexto)

def secciongato(request):
    gato = Producto.objects.filter(idTipProducto = 1).order_by('idProducto')
    contexto = {"producto":gato}
    return render(request, 'Inicio/PagAnimales/Gato.html',contexto)

def seccionexotico(request):
    exotico = Producto.objects.filter(idTipProducto = 3).order_by('idProducto')
    contexto = {"producto":exotico}
    return render(request, 'Inicio/PagAnimales/Exotico.html',contexto)


def iniciosesion(request):
    return render (request, 'Inicio/InicioSesion/sesion.html')


def plantillaProducts(request, idProducto):
    productos = Producto.objects.filter(idProducto = idProducto).order_by('idProducto')
    contexto = {"producto":productos}
    return render (request, 'Inicio/PagAnimales/PagProductos/Products.html', contexto)

def carrito(request, slug):
    product = Producto.objects.get(slug = slug)

    initial = {"Items":[],"price":0.0,"count":0}
    session = request.session.get("data",initial)
    if slug in session ["items"]:
        #print("Producto ya existe en el carrito")
        messages.error(request,"Producto Ya existe en el Carrito")
    else:
        session["items"].append(slug)
        session["price"] += float(product.precio)
        session["count"] += 1
        request.session["data"] = session
        messages.success(request,"Agregado Exitosamente")
    return redirect(slug)

def micarrito(request):
    sess = request.session.get("data",{"items":[]})
    products = Producto.objects.filter(slug_in = sess["items"])
    contexto = {"producto":products,}
    return render(request,contexto)

def simple_checkout(request):
    template_name = "simple_checkout.html"
    return render (request, template_name)



#def registrarusuario(request):
 #   idUsuario = request.POST['idUsuario']
  #  rut = request.POST['rut']
   # clave = request.POST['clave']
    #nombre = request.POST['nombre']
    #apellido = request.POST['apellido']
#    correo = request.POST['correo']
#    telefono = request.POST['telefono']
    
    
 #   Usuario.objects.create(rut = rut, clave = clave, nombre = nombre, apellido = apellido, correo = correo, telefono = telefono)
#    return redirect('formulario')
#