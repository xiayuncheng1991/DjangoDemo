from django.template import loader,Context  
from django.http import HttpResponse  
from blog.models import BlogPost 


# Create your views here.
def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template('archive.html')
    c = Context({'post':posts})
    return HttpResponse(t.render(c))
