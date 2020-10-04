from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .filters import *
from .models import *


# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def post(request, pk):
    post = Post.objects.get(id=pk)

    context = {
        'post': post,
    }
    return render(request, 'main/post_template.html', context)


def blog(request):
    tags = Tag.objects.all()
    image = '../static/images/backgrounds/blog.png'

    myFilter = Filter(request.GET, queryset=Post.objects.order_by('-id'))
    posts = myFilter.qs

    page = request.GET.get('page')
    paginator = Paginator(posts, 3)

    crumb = 'блог'

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'crumb': crumb,
        'tags': tags,
        'filter': myFilter,
        'image': image,
    }
    return render(request, 'main/blog.html', context)


def about(request):
    crumb = 'о нас'
    image = '../static/images/backgrounds/about.png'

    team = Author.objects.all()
    posts = Post.objects.order_by('-id')

    page = request.GET.get('page')
    paginator = Paginator(posts, 3)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'team': team,
        'image': image,
        'crumb': crumb,

    }
    return render(request, 'main/about.html', context)


def usability(request):
    image = '../../static/images/backgrounds/usability.png'
    crumb = 'юзабилити-аудит сайта'

    portfolio = Portfolio.objects.order_by('-id')[:6]


    context = {
        'crumb': crumb,
        'image': image,
        'portfolio': portfolio,
    }
    return render(request, 'main/usability.html', context)


def portfolio(request):
    tags = Tag.objects.all()
    portfolio = Portfolio.objects.order_by('-id')

    myFilter = Filter(request.GET, queryset=portfolio)
    portfolio = myFilter.qs

    crumb = 'портфолио'

    context = {
        'crumb': crumb,
        'portfolio': portfolio,
        'tags': tags,
    }
    return render(request, 'main/portfolio.html', context)


def internet_marketing(request):
    image = '../static/images/backgrounds/internet-marketing/bg-image.png'
    portfolio = Portfolio.objects.order_by('-id')[:6]

    crumb = 'интернет-маркетинг'

    context = {
        'crumb': crumb,
        'image': image,
        'portfolio': portfolio,
    }
    return render(request, 'main/internet-marketing.html', context)


def digital_strategy(request):
    image = '../../static/images/backgrounds/digital-strat/bg-image.png'
    crumb = 'digital-стратегия'
    portfolio = Portfolio.objects.order_by('-id')[:6]

    context = {
        'crumb': crumb,
        'image': image,
        'portfolio': portfolio,
    }
    return render(request, 'main/digital-strat.html', context)


def seo(request):
    image = '../../static/images/backgrounds/seo-prod/bg-image.png'
    portfolio = Portfolio.objects.order_by('-id')[:6]
    crumb = 'SEO продвижение'

    context = {
        'crumb': crumb,
        'image': image,
        'portfolio': portfolio,
    }
    return render(request, 'main/seo-prod.html', context)


def chat_bots(request):
    crumb = 'разработка чат-ботов'
    image = '../../static/images/backgrounds/chat-bots/bg-image.png'

    context = {
        'crumb': crumb,
        'image': image,
    }
    return render(request, 'main/chat-bot.html', context)


def context_advert(request, crumb, image):
    crumb = 'контекстная реклама'
    image = '../../static/images/backgrounds/context-ad/bg-image.png'

    context = {
        'crumb': crumb,
        'image': image,
    }
    return render(request, 'main/context-advert.html', context)


def support(request):
    crumb = 'техническая поддержка'
    image = '../../static/images/backgrounds/support-page/bg-image.png'

    context = {
        'crumb': crumb,
        'image': image,
    }
    return render(request, 'main/support.html', context)


def web_development(request):
    crumb = 'веб-разработка'
    image = '../../static/images/backgrounds/web/bg-image.png'

    context = {
        'crumb': crumb,
        'image': image,
    }
    return render(request, 'main/web-development.html', context)


def smm(request):
    crumb = 'SMM'
    image = '../../static/images/backgrounds/smm/bg-image.png'

    context = {
        'crumb': crumb,
        'image': image,
    }
    return render(request, 'main/smm.html', context)


def contacts(request):
    crumb = 'контакты'

    context = {
        'crumb': crumb,
    }
    return render(request, 'main/contacts.html', context)


def promo_mobile(request):
    crumb = 'продвижение приложений'
    image = '../../static/images/backgrounds/promo-mobile/bg-image.png'

    context = {
        'crumb': crumb,
        'image': image,
    }
    return render(request, 'main/promo-mobile.html', context)