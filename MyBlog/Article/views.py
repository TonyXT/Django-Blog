from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpResponseRedirect
from Article.forms import RegisterForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import auth
from django.contrib import messages
from Article.models import Article

def index(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'homepage.html')
        else:
            return render(request, 'StartPage.html',
                          {'visible': " is-visible", 'selected': "is-selected", 'liselected': "selected", 'form': form})
    else:
        form = RegisterForm()
    return render_to_response('StartPage.html', {'form': form, 'visible': "", 'selected': "", 'liselected': ""},
                              context_instance=RequestContext(request))
    # form=RegisterForm()
    # return render(request,'StartPage.html',{'form':form})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['username'] = username

            return HttpResponseRedirect(reverse('Article.views.gotohome'))
        else:
            messages.add_message(request, messages.INFO, 'username and password do not match')
            return render(request, 'StartPage.html')


@login_required(login_url='/')
def gotohome(request):
    username = request.session.get('username')
    post_list=Article.objects.filter(Author=username)
    return render(request, 'homepage.html', {'username': username,'post_list':post_list})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
