from django.shortcuts import render
from ticketsales import views
from . models import ConsertModel,TimeModel,LocationModel
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . forms import ConsertCreateForm, SearchForm,ConsertEditForm
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.core.paginator import Paginator




def ConsertListView(request):
    searchform = SearchForm(request.GET)
    if searchform.is_valid():
        searchtext=searchform.cleaned_data['searchtext']
        consert = ConsertModel.objects.filter(name__contains =searchtext)
    else:
        consert = ConsertModel.objects.all()
        paginator = Paginator(consert,3)
        page_number = request.GET.get('page')
        blog_list = paginator.get_page(page_number)
    context = {
        'consert':consert,
        'consert_count':consert.count(),
        'searchform':searchform,
    }
    return render(request,'ticketsales/consert_list.html',context)
@login_required
def LocationListView(request):
    location = LocationModel.objects.all()
    context = {
        'location':location,
        
    }
    return render(request,'ticketsales/location_list.html',context)

def DetailListView(request,id):
    detail = ConsertModel.objects.get(pk = id)
    context = {
        'detail':detail,
        
    }
    return render(request,'ticketsales/detail_list.html',context)
@login_required
def TimeListView(request):
    #if request.user.is_authenticated and request.user.is_active:
        time = TimeModel.objects.all()
        context = {
            'time':time,
            
        }
        return render(request,'ticketsales/time_list.html',context)

    #else:
    #       return HttpResponseRedirect(reverse(views.loginview))
    
@login_required
def conserteditview(request,id):
    
    consert = ConsertModel.objects.get(pk = id )
    
    if request.method == 'POST':
        consertform = ConsertEditForm(request.POST,request.FILES, instance=consert)
        if consertform.is_valid():
            consertform.save()
            return HttpResponseRedirect(reverse(views.ConsertListView))
    else:
        consertform=ConsertEditForm(instance=consert)
    context = {
        'consertform':consertform,
        'poster':consert.poster,
    }
    return render(request,'ticketsales/consert_edit.html',context)
@login_required
def ConsertCreateView(request):
    if request.method == 'POST':
        createview = ConsertCreateForm(request.POST,request.FILES)
        if createview.is_valid():
            post_name = createview.cleaned_data['name']
            post_singername = createview.cleaned_data['singername']
            post_length = createview.cleaned_data['length']
            post_poster = createview.cleaned_data['poster']
            obj = ConsertModel(name = post_name , singername = post_singername , length = post_length , poster = post_poster)
            obj.save()
            messages.success(request,"Concert Create Successfully",extra_tags='success')
            return redirect('consert_list')
    else:
        createview = ConsertCreateForm()

    context = {
        'createview':createview,
    }
    return render(request,'ticketsales/create.html',context)
    
@login_required
def DeleteView(request,id):
    post = ConsertModel.objects.get(pk = id)
    post.delete()
    messages.success(request,"Concert Deleted Successfully",extra_tags='danger')
    return redirect('consert_list')


# @login_required
# def ConsertCreateView(request):
#     if request.method == 'POST':
#         form = ConsertCreateForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = ConsertCreateForm()
#     return render(request, 'ticketsales/create.html', {
#         'form': form
#         })
