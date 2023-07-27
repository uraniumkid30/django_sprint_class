from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm
from django.template.response import TemplateResponse
from django.views.generic.edit import FormView


def book_home(request):# request
    template_name = "home.html"
    all_my_books = Book.objects.all() # list of books
    context = {
        "my_books": all_my_books,
        "age": 16
    } # send this data to my template
    return render(request, template_name, context)


def book_list(request):
    message = ""
    owner_parameter = request.GET.get("owner")
    if owner_parameter:
        books = Book.objects.filter(owner=owner_parameter)
    else:
        books = Book.objects.all()  # list of all books
    for item in books:
        message += f"title: {item.title}, author: {item.owner} "
    return HttpResponse(message)

def book_detail(request, book_id):
    message = ""
    try:
        book_item = Book.objects.get(id=book_id)
        message += f"title: {book_item.title}, author: {book_item.owner}"
    except:
        print("encountered an error not found")
    return HttpResponse(message)

# 1st approach we are going to use functions based views
def create_book_record(request):
    template_name = "create_book_record.html" # i havent created yet
    context = {}
    form = BookForm
    # account for 2 actions in this view.
    #1 you need a get so that the user can see the form he needs to fill
    print(f"Action from the browser is {request.method}.")
    if request.method == "GET":
        context["book_form"] = form()
        return render(request, template_name, context)
    #2 we need a post to save the form that the user has filled
    elif request.method == "POST":
        data_from_browser = request.POST
        print(data_from_browser)
        form_data = form(data_from_browser)
        if form_data.is_valid():
            print(form_data.cleaned_data)
            title = form_data.cleaned_data["title"]
            owner = form_data.cleaned_data["owner"]
            rating = form_data.cleaned_data["rating"]
            description = form_data.cleaned_data["description"]
            Book.objects.create(
                title=title,
                owner=owner,
                rating=rating,
                description=description,
            )
            # app_name:name_of_the_path
            return redirect("book:home_url_for_book")
        else:
            print(" something went wrong")
            return HttpResponse("You have an error")

    
# 2nd approach we are going to use class based views
class CreateBookView(FormView):
    form_class = BookForm
    template_name = "create_book_record.html"

    def get(self, request, *args, **kwargs):
        context = {
            "book_form": self.form_class()
        }
        return TemplateResponse(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        pass
        
    