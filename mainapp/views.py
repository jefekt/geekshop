from django.shortcuts import render


# Create your views here.

links_menu = [
    {'href' : 'product_all', 'name' : 'все'},
    {'href' : 'product_home', 'name' : 'дом'},
    {'href' : 'product_office', 'name' : 'офис'},
    {'href' : 'product_modern', 'name' : 'модерн'},
    {'href' : 'product_classic', 'name' : 'классика'},


]

links_menu2 = [
    {'href' : 'product_popular', 'name' : 'Популярные'},
    {'href' : 'product_new', 'name' : 'Новые'},



]

def index(request):
    content = {
        'title': 'Главное',
        'links_menu2': links_menu2,
    }
    return render(request, 'mainapp/index.html', content)


def products(request):
    content = {
        'title' : 'Продукты',
        'links_menu' : links_menu,
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html')


def context(request):
    content = {
        'title': 'Магазин',
        'header': 'Добро пожаловать на сайт',
        'username': 'Иван Иванов',
        'products': [
            {'name': 'Стулья', 'price' : 4535},
            {'name': 'Диваны', 'price' : 1535 },
            {'name': 'Кровати', 'price' : 2635},

        ]
    }


    return render(request, 'mainapp/test_context.html', content)