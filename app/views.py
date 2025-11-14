from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
#from app.forms import CreateArticleForm
from app.models import Article
from django.views.generic import CreateView

# Create your views here.
def home(request):
    articles = Article.objects.all()
    return render(request, "app/home.html", {"articles": articles})

class ArticleCreateView(CreateView):
    template_name = "app/article_create.html"
    model = Article
    fields = ["title", "status", "content", "word_count", "x_post"]
    success_url = reverse_lazy("home")






# Function base view  
# def create_article(request):
#     if request.method == "POST":
#         form = CreateArticleForm(request.POST)
#         if form.is_valid():
#             form_data = form.cleaned_data
#             new_article = Article(
#                 title = form_data["title"],
#                 status = form_data["status"],
#                 content = form_data["content"],
#                 word_count = form_data["word_count"],
#                 x_post = form_data["x_post"],
#             )
#             new_article.save()

#             return redirect("home")
#     else: 
#         form = CreateArticleForm()
#     return render(request, "app/article_create.html", {"form": form})