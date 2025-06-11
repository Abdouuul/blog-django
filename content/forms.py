from django import forms

class CommentForm(forms.Form):
    content = forms.CharField(
        label='Votre Commentaire',
        widget=forms.Textarea(attrs={
            'rows': 4,
            'placeholder': 'Ecrivez votre commentaire ici...'
        }),
        max_length=200

    )