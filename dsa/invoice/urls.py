from django.urls import path,include
from . import views as invoice_views
urlpatterns = [
    path('dashboard/', invoice_views.dashboard,name='dashboard'),

    path('customers/', invoice_views.customers,name='customers'),
    path('contacts/', invoice_views.contacts,name='contacts'),
    path('contacts_post/', invoice_views.contacts_post,name='contacts_post'),

    path('items/', invoice_views.items,name='items'),
    path('items/new/', invoice_views.items_new,name='items_new'),
    path('items_new_post/', invoice_views.items_new_post,name='items_new_post'),

    path('estimate/', invoice_views.estimate,name='estimate'),
    path('estimate/new/', invoice_views.estimate_new,name='estimate_new'),
    path('estimate_new_post/', invoice_views.estimate_new_post,name='estimate_new_post'),

    path('deliveryChallans/', invoice_views.deliveryChallans,name='deliveryChallans'),
    path('deliveryChallans/new/', invoice_views.deliveryChallansNew,name='deliveryChallansNew'),
    path('deliveryChallansNew_post/', invoice_views.deliveryChallansNew_post,name='deliveryChallansNew_post'),

    path('newInvoice/', invoice_views.newInvoice,name='newInvoice'),
    path('newInvoice_post/', invoice_views.newInvoice_post,name='newInvoice_post'),





    
]