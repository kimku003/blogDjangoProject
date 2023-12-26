from django.http import HttpResponse

from django.shortcuts import render

from listings.models import Band

from listings.models import Listing

from listings.models import Desert

from listings.models import Chat

from listings.forms import ContactUsForm

from listings.forms import EmailSentForm

from django.core.mail import send_mail

from django.shortcuts import redirect

from listings.forms import BandForm, ContactUsForm
 
from listings.forms import ListingForm

from listings.forms import DesertForm

from listings.forms import ChatForm

from listings.forms import home

from django.shortcuts import get_object_or_404, redirect

from django.http import JsonResponse

from django.template.loader import render_to_string

from render_block import render_block_to_string

def home(request):
    return render(request, 'listings/home.html')



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
def contact(request):
    if request.method == 'POST':
     # créer une instance de notre formulaire et le remplir avec les données POST
        print("La méthode de requête est :" , request.method)  
        print("Les données POST sont:" , request.POST)  
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
           )
        return redirect('email-sent') # ajoutez cette instruction de retour

            # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
            # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).

    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()

        return render(request,
                'listings/contact.html',
                {'form': form})












def email_sent(request):
    bands = Band.objects.all()
    #return render(request, 'listings/confirm.html', {'bands': bands})
    if request.method == 'POST':

        form = EmailSentForm(request.GET)

        if form.is_valid():
            
            return redirect('contact')
    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = EmailSentForm()


        #if form.is_valid():
            
           # return redirect('email-sent')
    #else:
        # ceci doit être une requête GET, donc créer un formulaire vide
       # form = EmailSentForm()

        return render(request,
                'listings/confirm.html',
                {'bands': bands})


def about(request):
    return render(request, 'listings/about.html')


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})

def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request,
            'listings/band_detail.html',
            {'band': band}) 



def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)

    else:
        form = BandForm()

    return render(request,
            'listings/band_create.html',
            {'form': form})

def band_update(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
       # mettre à jour le groupe existant dans la base de données
            form.save()
        # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
        return redirect('band-detail', band.id)
    else:
       form = BandForm(instance=band)
    return render(request,
          'listings/band_update.html',
         {'form': form}) 



def band_delete(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
     # supprimer le groupe de la base de données
        band.delete()
        # rediriger vers la liste des groupes
        return redirect('band-list')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement
   
    return render(request,
                    'listings/band_delete.html',
                    {'band': band}) 




      #VUES POUR LE MODÈLE LISTING

def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listing_list.html', {'listings': listings})

def listing_detail(request, id):
    listing = Listing.objects.get(id=id)
    return render(request,
            'listings/listing_detail.html',
            {'listing': listing}) 


def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Listing » et la sauvegarder dans la db
            listing = form.save()
            
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('listing-detail', listing.id)

    else:
        form = ListingForm()

    return render(request,
            'listings/listing_create.html',
            {'form': form})


def listing_update(request, id):
    listing = Listing.objects.get(id=id)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
        # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm(instance=listing)
    return render(request,
            'listings/listing_update.html',
            {'form': form}) 


def listing_delete(request, id):
    listing = Listing.objects.get(id=id)
    if request.method == 'POST':
   # supprimer le groupe de la base de données

        listing.delete()
    
        # rediriger vers la liste des boissons
        return redirect('listing-list')
   
    return render(request,
          'listings/listing_delete.html',
         {'listing': listing}) 





                            #VUE POUR LE MODÈLE DESERT

def desert_list(request):
    deserts = Desert.objects.all()
    return render(request, 'listings/desert_list.html', {'deserts': deserts})



def desert_detail(request, id):
    desert = Desert.objects.get(id=id)
    return render(request,
            'listings/desert_detail.html',
            {'desert': desert}) 




def desert_update(request, id):
    desert = Desert.objects.get(id=id)
    if request.method == 'POST':
        form = DesertForm(request.POST, instance=desert)
        if form.is_valid():
        # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('desert-detail', desert.id)
    else:
        form = DesertForm(instance=desert)
    return render(request,
            'listings/desert_update.html',
            {'form': form}) 



def desert_create(request):
    if request.method == 'POST':
        form = DesertForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            desert = form.save()
            
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('desert-detail', desert.id)

    else:
        form = ListingForm()

    return render(request,
            'listings/desert_create.html',
            {'form': form})


def desert_delete(request, id):
    desert = Desert.objects.get(id=id)
    if request.method == 'POST':
   # supprimer le groupe de la base de données

        desert.delete()
    
        # rediriger vers la liste de annonces
        return redirect('desert-list')
   
    return render(request,
          'listings/desert_delete.html',
         {'desert': desert}) 



            #Intégrtion d'une vue htmx





def chat(request):
    chats = Chat.objects.all().order_by('-timestamp')

    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            chat = Chat(content=form.cleaned_data['content'])
            chat.save()
            # Ajoutez le nouveau message à la liste des messages
            chats = Chat.objects.all().order_by('-timestamp')
        form_str = render_to_string('listings/chat.html', {'chats': chats, 'form': form}, request=request)
        return render(request, 'listings/chat.html', {'chats': chats, 'form': form})
    else:
        form = ChatForm()
        chats = Chat.objects.all().order_by('-timestamp')
        form_str = render_to_string('listings/chat.html', {'chats': chats, 'form': form}, request=request)
    return HttpResponse(form_str)


def delete_chat(request, chat_id):
    chat = get_object_or_404(Chat, pk=chat_id)
    chat.delete()
    return HttpResponse('')









































