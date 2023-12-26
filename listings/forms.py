from django import forms

from listings.models import Band

from listings.models import Listing

from listings.models import Desert

from listings.models import Chat

from listings.models import home


class ContactUsForm(forms.Form):
   name = forms.CharField(required=False)
   email = forms.EmailField()
   message = forms.CharField(max_length=1000)

class ChatForm(forms.Form):

   content = forms.CharField(max_length=500, required=True)

class EmailSentForm(forms.Form):   
   print(" ")
           
class BandForm(forms.ModelForm):
   class Meta:
     model = Band
     #exclude = ('active', 'official_homepage')  # ajoutez cette ligne
     exclude = ('active',)  # ajoutez cette ligne

class ListingForm(forms.ModelForm):
   class Meta:
     model = Listing
     exclude = ('active',)  # ajoutez cette ligne



class DesertForm(forms.ModelForm):
   class Meta:
     model = Desert
     exclude = ('active',)  # ajoutez cette ligne




