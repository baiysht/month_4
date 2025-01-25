from django import forms
from posts.models import Post, Category


class PostCreateForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Title", "class": "form-control"}),
    )
    description = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Description"}),
    )
    image = forms.ImageField(required=True)

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        description = cleaned_data.get("description")
        if (title and description) and title.lower() == description.lower():
            raise forms.ValidationError("Title and description should be different")
        return cleaned_data

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Search'}))

    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, widget=forms.Select())

    orderings = (
        ("created_at", "created at"),
        ("-created_at", "created at(descending)"),
        ("updated_at", "updated at"),
        ("-updated_at", "updated at(descending)"),
    )
    ordering = forms.ChoiceField(choices=orderings, widget=forms.Select())


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'title', 'description']