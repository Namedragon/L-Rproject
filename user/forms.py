from django import forms

from user.models import profile


class ProfileForm(forms.ModelForm):


    def clean_max_dating_age(self):
        max_dating_age = self.cleaned_data.get('max_dating_age',0)
        min_dating_age = self.cleaned_data.get('min_dating_age',0)

        if max_dating_age < min_dating_age:
            raise forms.ValidationError('最大年龄小于最小年龄')

        return max_dating_age


    def clean_max_distance(self):
        max_distance = self.cleaned_data.get("max_distance",0)
        min_distance = self.cleaned_data.get("min_distance",0)

        if max_distance < min_distance:
            raise forms.ValidationError('最大范围小于最小范围')

        return max_distance




    class Meta:
        model = profile
        fields = '__all__'