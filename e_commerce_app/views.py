from django.shortcuts import render
from django.http import HttpResponse
# Cat model that's connected to the Database
from .models import Category, Item
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
# Add LoginForm to this line...
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# ...and add the following line...
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class ItemCreate(CreateView):
    model = Item
    fields = 'name', 'description', 'price', 'category'
    success_url = '/item'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/items')


@method_decorator(login_required, name='dispatch')
class ItemUpdate(UpdateView):
    model = Item
    fields = ['name', 'description', 'price', 'category']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/items/' + str(self.object.pk))


@method_decorator(login_required, name='dispatch')
class ItemDelete(DeleteView):
    model = Item
    success_url = '/items'


# # Create your views here.
def index(request):
    items = list(Item.objects.all())
    return render(request, 'index.html', {'items': items})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def items_index(request):
    items = list(Item.objects.all())
    return render(request, 'items/index.html', {'items': items})


def items_show(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'items/show.html', {'item': item})

def categorys_index(request):
    categorys = list(Category.objects.all())
    return render(request, 'category/index.html', {'categorys': categorys})
                            
def categorys_show(request, category_id):
    category = Category.objects.get(id=category_id)
    items = list(Item.objects.filter(category_id=category_id))
    return render(request, 'category/show.html', {'category': category, 'items': items})

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    items = list(Item.objects.filter(user=user))

    return render(request, 'profile.html', {'username': username, 'items': items})


def login_view(request):
    # if post, then authenticate (user submitted username and password)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    print('The account has been disabled.')
            else:
                print('The username and/or password is incorrect.')
    else:  # it was a get request so send the emtpy login form
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
