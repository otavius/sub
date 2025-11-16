from django import forms 
from app.models import Article

class CreateArticleForm(forms.Form):
    ARTICLE_STATUS = (
        ("draft","draft"),
        ("inprogress", "inprogress"),
        ("published", "oublished"),
    )

    title = forms.CharField(max_length=100)
    status = forms.ChoiceField(choices=ARTICLE_STATUS)
    content = forms.CharField(widget=forms.Textarea)
    word_count = forms.IntegerField()
    x_post = forms.CharField(widget=forms.Textarea, required=False)

# class CreateArticleForm(forms.ModelForm):
#     class Meta:
#         model = Article 
#         fields = ("title", "content", "x_post", "status")
