#coding=UTF-8
from django.contrib.auth import  logout
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from rango.models import Category,Page
from  rango.forms import CatForm,PageForm,UserForm,UserProfileForm
from bing_search import run_query
# Create your views here.
def index(request):
    cat_list=Category.objects.order_by('-likes')[:5]
    page_list=Page.objects.order_by('-views')[:5]
    #得到cat和pag的信息
    context_dict={'categories':cat_list,'pages':page_list}
   #得到session值
    visits=request.session.get('visit')
    if not visits:
       visits=2
    reset_last_visit_time=False
#是否有最后一次登录
    last_visit=request.session.get('last_visit')
    if last_visit:
        last_visit_time=datetime.strptime(last_visit[:-7],'%Y-%m-%d %H:%M:%S')
        if (datetime.now()-last_visit_time).seconds>0:
            visits=visits+1
            reset_last_visit_time=True
    else:
        reset_last_visit_time=True
    if reset_last_visit_time:
        request.session['last_visit']=str(datetime.now())
        request.session['visit']=visits
    context_dict['visits']=visits
    response=render(request,'rango/index.html',context_dict)
#     # 得到cookie值 将cookies 值提取出来加在字典中 返回给html
#     visits=int(request.COOKIES.get('visits','1'))
#     reset_last_visit_time=False
#     response=render(request,'rango/index.html',context_dict)
#     if 'last_visit' in request.COOKIES:
#         last_visit=request.COOKIES['last_visit']
#         last_visit_time=datetime.strptime(last_visit[:-7],"%Y-%m-%d %H:%M:%S")
#         #如果超过一天
#         if (datetime.now()-last_visit_time).seconds>5:
#             visits=visits+1
#             reset_last_visit_time=True
# # last visit cookie不存在
#     else:
#         reset_last_visit_time=True
#     context_dict['visits'] = visits
#     response = render(request, 'rango/index.html', context_dict)
#     if reset_last_visit_time:
#         #重置最后一次登录的时间
#         response.set_cookie('last_visit',datetime.now())
#         response.set_cookie('visits',visits)
    return response

def about(request):
    return render(request,'rango/about.html')
def category(request,cat_name_slug):
    context_dict={}
    context_dict['result_list']=None
    context_dict['query']=None
    if request.method=="POST":
        query=request.POST['query'].strip()
        if query:
            #run bing function to get the result list
            result_list=run_query(query)
            context_dict['result_list']=result_list
            context_dict['query']=query
    try:
        category=Category.objects.get(slug=cat_name_slug)
        print(category.views)
        category.views+=1
        category.save()
        #将所有的元素放在一个字典中
        context_dict['category_name']=category.name
        pages=Page.objects.filter(category=category)
        context_dict['pages']=pages
        context_dict['category']=category
        context_dict['category_name_slug']=cat_name_slug
    except:
        pass
    if not context_dict['query']:
        context_dict['query']=category.name
    return render(request,'rango/category.html',context_dict)
def     add_cat(request):
    if request.method=='POST':
        form=CatForm(request.POST)
        #form 是提交的谁
        if form.is_valid():
            if form.views<0:
                form.views=0
            form.save(commit=True)
            return index(request)
        else:
            print '错误'
            print form.errors
    else:
        form=CatForm()
    #     传递给add HTML页面一个字典
    return render(request,'rango/add_category.html',{'form':form})
def add_page(request,cat_name_slug):
    try:
        #根据 slug属性 找到page 的category
        cat=Category.objects.get(slug=cat_name_slug)
    except Category.DoesNotExist:
        cat=None
    print(request.method)
    if request.method=='POST':
        form=PageForm(request.POST)
        if form.is_valid():
            #如果存在category
            if cat:
                page=form.save(commit=False)
                page.category=cat
                page.views=0
                page.save()
                #添加完pages后 还要更新 category数据库  定向到category方法
            return category(request,cat_name_slug)
        else:
            print('false')
            print form.errors
    else:
        print('新建表格')
        form=PageForm()
        context_dict={'form':form,'category':cat}
    return render(request,'rango/add_Page.html',context_dict)

def register(request):
    registered=False
    if request.method=='POST':
        #如果是提交表格  将数据转换为form类型
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            if 'picture' in request.FILES:
                profile.picture=request.FILES['picture']
            profile.save()
            registered=True
        #表格内容出错
        else:
            print user_form.errors,profile_form.errors
    else:
        user_form=UserForm()
        profile_form=UserProfileForm()
    #如果不是提交请求 就跳转到注册的见面、
    #   如果是提交请求 就执行操作，写入数据库，然后跳转到注册页面 说明已经注册成功
    return render(request,'rango/register.html',{'user_form':user_form,
                                                 'profile_form':profile_form,
                                                 'registered':registered
                                                 })
def Login(request):
    if request.method=='POST':
        print('this is post')
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        #如果用户名和密码正确，重定向到 rango.index页面
        if user:
            if user.is_active:
                auth.login(request,user)
                return HttpResponseRedirect('/rango/index/')
            else:
                return HttpResponse('your rango account is disabled')
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        print 'wrong is there'
        return render(request,'rango/login.html',{})

@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/rango/')
@login_required
def restricted(request):
    str='if you login you can see this'
    return render(request,'rango/restricted.html')

def search(request):
    result_list=[]
    if request.method=='POST':
        query=request.POST['query'].strip()
        if query:
            result_list=run_query(query)
    return render(request,'rango/search.html',{'result_list':result_list})


def Track_url(request):
    page_id=None
    url='/rango/'
    if request.method=='GET':
        print(request.GET)
        print(request.path)
        print(request.body)
        if 'page_id' in request.GET :
            # 是个字典类型的 request
            page_id=request.GET['page_id']
        try:
            page=Page.objects.get(id=page_id)
            page.views=page.views+1
            page.save()
            url=page.url
            print(url)
        except:pass
    return redirect(url)
@login_required
def like_category(request):
    cat_id=None
    if request.method=='GET':
        cat_id=request.GET['category_id']
    likes=0
    if cat_id:
        cat=Category.objects.get(id=int(cat_id))
        if cat:
            likes=cat.likes+1
            cat.likes=likes
            cat.save()
    return HttpResponse(likes)

def get_category_list(max_results=0,start_with=''):
    cat_list=[]
    #如果 有元素 就 进行数据库筛选  max_result是返回的最大数目
    if start_with:
        cat_list=Category.objects.filter(name__startswith=start_with)
    if cat_list and max_results>0:
        if cat_list.count()>max_results:
            cat_list=cat_list[:max_results]
    return cat_list

def suggest_category(request):
    cat_list=[]
    starts_with=''
    if request.method=="GET":
        starts_with=request.GET['suggestion']
    cat_list=get_category_list(8,starts_with)
    return render(request,'rango/cats.html',{'cats':cat_list})

def auto_add_page(request):
    cat_id=None
    url=None
    title=None
    context_dict={}
    # 从request中得到page的信息 然后创建一个pages
    if request.method=='GET':
        cat_id=request.GET['category_id']
        url=request.get['url']
        title=request.get['title']
        if cat_id:
            category=Category.objects.get(id=int(cat_id))
            p=Page.objects.get_or_create(category=category,title=title,url=url)
            pages=Page.objects.filter(category=category).order_by('-views')
            #add our results list to the template
            context_dict['pages']=pages
    return render(request,'rango/page_list.html',context_dict)