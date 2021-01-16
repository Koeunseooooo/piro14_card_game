from django import forms
from django.contrib.auth.models import User
from .models import CardBattle

class AttackForm(forms.ModelForm):
    class Meta:
        model = CardBattle
        fields = ("from_user_card_num", "to_user",)


    def __init__(self, *args, **kwargs):
        # print(kwargs["initial"]["current"])
        # print(type(kwargs["initial"]["current"]))
        super(AttackForm, self).__init__(*args, **kwargs)
        self.fields["to_user"].queryset = User.objects.all().exclude(
            id=kwargs["initial"]["current_user"]
        )
    # 참고문서
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/
    # https://stackoverflow.com/questions/18184415/user-object-has-no-attribute-get
    # https://wayhome25.github.io/django/2017/05/06/django-form/
    # #https://simpleisbetterthancomplex.com/questions/2017/03/22/how-to-dynamically-filter-modelchoices-queryset-in-a-modelform.html

 
class DefenseForm(forms.ModelForm):
    class Meta:
        model = CardBattle
        fields = ("to_user_card_num",)
