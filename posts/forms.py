from django import forms
from posts.models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'title', 'description']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        description = cleaned_data.get("description")
        if (title and description) and title.lower() == description.lower():
            raise forms.ValidationError("Title and description should be different")
        return cleaned_data