from django import forms

from .models import Player, ContactUs, LogIn, SuggestedLeague

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            "first_name",
            "last_name",
            "nickname",
            "email",
            "telephone",
            "password_first",
            "password_second",
            "company",
            "city",
            "playstation_id",
            "flag_playstation",
            "flag_xbox",
            "flag_pc",
            ]

# I DON'T LIKE THE DJANGO WIDGET FOR EMAIL AND PASSWORD
    #def __init__(self, *args, **kwargs):
    #    super(PlayerForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
    #    self.fields['password_first'].widget = forms.PasswordInput()
    #    self.fields['password_second'].widget = forms.PasswordInput()
    #    self.fields['email'].widget = forms.EmailInput()
        
    #def clean(self):   
    #    cleaned_data = super(PlayerForm, self).clean()
    #    if 'password_first' in self.cleaned_data and 'password_second' in self.cleaned_data:
    #        if self.cleaned_data['password_first'] != self.cleaned_data['password_second']:
    #            raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
    #        return self.cleaned_data

        

class LogInForm(forms.ModelForm):
    class Meta:
        model = LogIn
        fields = [
            "nickname",
            "password",
            ]
        
class EditPlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            "first_name",
            "last_name",
            "email",
            "telephone",
            "company",
            "city",
            "playstation_id",
            "flag_playstation",
            "flag_xbox",
            "flag_pc",
            ]
        
        
class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = [
            "first_name",
            "last_name",
            "email",
            "subject",
            "message",
            ]
        
    def __init__(self, *args, **kwargs):
        super(ContactUsForm, self).__init__(*args, **kwargs)
        self.fields['message'].widget.attrs['style'] = 'width:730px; height:300px;'
        
class SuggestLeagueForm(forms.ModelForm):
    class Meta:
        model = SuggestedLeague
        fields = [
            "game",
            "platform",
            "user_nickname",
            ]
        
    def __init__(self, *args, **kwargs):
        super(SuggestLeagueForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['user_nickname'].widget = forms.HiddenInput()
        self.fields['user_nickname'].initial = SuggestedLeague.objects.all()[:1]
        
        
class AvailabilityForm(forms.ModelForm):
    available = forms.CharField(widget=forms.Textarea)
    class Meta:
        #model = PlayerAvailability
        model = Player
        fields = [
            "nickname",
            "available",
            ]
    # http://stackoverflow.com/questions/110378/change-the-width-of-form-elements-created-with-modelform-in-django
    def __init__(self, *args, **kwargs):
        super(AvailabilityForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['available'].widget.attrs['cols'] = 70
        self.fields['available'].widget.attrs['rows'] = 10
        self.fields['available'].label = "Update your availability for the next days/weeks"#http://stackoverflow.com/questions/636905/django-form-set-label
        self.fields['nickname'].widget.attrs['cols'] = 0
        self.fields['nickname'].widget.attrs['rows'] = 0
        self.fields['nickname'].label = ""
        self.fields['nickname'].widget = forms.HiddenInput()