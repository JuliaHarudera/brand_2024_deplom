from django.shortcuts import render, redirect
from .models import Category, Product
from django.views.generic import TemplateView
from .forms import ContactUsForm
from django.contrib import messages

# def main(request):
#    categories = Category.objects.filter(is_visible=True)
#    context = {'categories': categories}
#    return render(request, 'brand_main.html', context=context)


def category_detail(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    context = {'products': products}
    return render(request, 'products.html', context=context)


class IndexPage(TemplateView):
    template_name = 'brand_main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.filter(is_visible=True)
        context['categories'] = categories
        context['contactus_form'] = ContactUsForm()
        return context

    def post(self, request, *args, **kwargs):
        contactus_form = ContactUsForm(request.POST)

        if contactus_form.is_valid():
            contactus_form.save()
            messages.success(request, 'Contact done')
            return redirect('brand:home')

        context = self.get_context_data(**kwargs)
        context['contactus_form'] = ContactUsForm()
        messages.error(request, 'errors contact form')
        return render(request, 'brand_main.html', context=context)





