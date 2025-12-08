from django.shortcuts import render


def home_page(request):
    template_data = {}
    template_data['page_title'] = 'Welcome to Riverside Pet Store | Home Page'

    return render(
        request,
        'root_app/index.html',
        { 'template_data': template_data }
    )


def about_page(request):
    return render(request, 'root_app/about.html')
