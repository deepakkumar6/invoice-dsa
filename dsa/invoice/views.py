from django.shortcuts import render, HttpResponse
import smtplib
import os
# Create your views here.
# @@@@@@@@@@@@@@   indexes   @@@@@@@@@@@@
# dashboard
# Customers
# contacts
# items
# items - new
# estimates
# estimates - new
# challans
# challans new


def dashboard(request):

    # this will store the overall view of our invoice

    return render(request, "invoice/dashboard.html")


def customers(request):

    # this will help us to create the customers for our invoice

    return render(request, 'invoice/customers.html')


def contacts(request):

    # this will help us to save the customers details

    return render(request, 'invoice/contacts.html')


def contacts_post(request):

    # this will help us to save the customers details

    if request.method == "POST":
        # customer_type = request.POST.get("")
        sirname = request.POST.get("sirname")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        companyname = request.POST.get("companyname")
        displayname = request.POST.get("displayname")
        customer_email = request.POST.get("customer_email")
        phonenumber = request.POST.get("phonenumber")
        mobilenumber = request.POST.get("mobilenumber")
        customerwebsite = request.POST.get("customerwebsite")
        # sirname = request.POST.get("")
        # sirname = request.POST.get("")

        # we can save this data to database

        # we can also return this in json form

    return render(request, 'invoice/contacts.html')


def items(request):

    # this will help us to add our services and items like for shopping -> different shirts , pants , etc

    return render(request, 'invoice/items.html')


def items_new(request):

    # this will help us to store the details of particular items

    return render(request, 'invoice/items_new.html')


def items_new_post(request):
    if request.method == "POST":
        product_name = request.POST.get("product_name")
        number_of_product = request.POST.get("number_of_product")
        selling_price = request.POST.get("selling_price")
        product_desc = request.POST.get("product_desc")
        # product_name = request.POST.get("product_name")
        # product_name = request.POST.get("product_name")

        # we can save this data to database

    return render(request, 'invoice/items_new.html')


def estimate(request):

    # this will help us to create the estimate of our products

    return render(request, 'invoice/estimate.html')


def estimate_new(request):

    # this will help us to create the estimate of our products

    return render(request, 'invoice/estimate_new.html')


def estimate_new_post(request):

    if request.method == "POST":

        customername = request.POST.get("customername")
        estimatenumber = request.POST.get("estimatenumber")
        reference = request.POST.get("reference")
        estimate_date = request.POST.get("estimate_date")
        expiry_date = request.POST.get("expiry_date")
        salesperson = request.POST.get("salesperson")
        project_name = request.POST.get("project_name")

        # we can save this to database

    return render(request, 'invoice/estimate_new.html')


def deliveryChallans(request):

    # this will help us to create the estimate of our products

    return render(request, 'invoice/deliveryChallans.html')


def deliveryChallansNew(request):

    # this will help us to create the estimate of our products

    return render(request, 'invoice/deliveryChallansNew.html')


def deliveryChallansNew_post(request):

    if request.method == "POST":

        customername = request.POST.get("customername")
        deliverychallans = request.POST.get("deliverychallans")
        reference = request.POST.get("reference")
        deliverychallans_date = request.POST.get("deliverychallans_date")
        challanstypes = request.POST.get("challanstypes")

        # we have some option to save this in db

    return render(request, 'invoice/deliveryChallansNew.html')


def invoices(request):

    # this is the page where all the invoices present

    return render(request, "invoice/invoices.html")


def invoices_new(request):

    # this is the main thing we need to handle - our invoice

    return render(request, 'invoice/invoices_new.html')


def newinvoice_post(request):

    # this is the main thing we need to handle - our invoice
    if request.method == "POST":

        # there are lot of data to handle
        customer_name = request.POST.get("customer_name")
        invoice_number = request.POST.get("invoice_number")
        order_number = request.POST.get("order_number")
        invoice_date = request.POST.get("invoice_date")
        terms = request.POST.get("terms")
        due_date = request.POST.get("due_date")
        salesperson = request.POST.get("salesperson")
        subjects = request.POST.get("subjects")
        send_to = request.POST.get("send_to")

        # we can create the template using these data and send emails

        # we can access this email through database
        admin_email = 'deepakkumar006007@gmail.com'
        gmail_user = admin_email
        # gmail_password = os.environ["EMAIL_APP_PASSWORD"]
        gmail_password = 'zhzgynicfizanklq'

        # send_to = 'b18ec035@nitm.ac.in' # we can access the customer password from db
        message = """
        INVOICE

        From : {4},                             Date : {3}
        Email : {1},                            Invoice Number : {2}
        Dear {0},
        Please pay the bill by {6}
        The subject is {5}.
        Terms : {7}
        The Order Number is : {8}
        """.format(customer_name, admin_email, invoice_number, invoice_date,
                   salesperson, subjects, due_date, terms, order_number)
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            # server.ehlo()
            print('connected to server')
            server.starttls()
            server.login(gmail_user, gmail_password)
            print('login success')
            server.sendmail(gmail_user, send_to, message)
            server.close()
            print('Email sent!')
            return HttpResponse('email - sent')
        except:
            print('Something went wrong...')
            return HttpResponse('something went wrong -- ')
    # print(sys.exit())

    # i can return to request.body in postman or just send emails

    return render(request, 'invoice/newInvoice.html')


# way to send emails
# if request.method == 'POST':
#         heading = request.POST.get('heading')
#         messageContent = request.POST.get('body')
#         receiver = request.POST.get('to_email')
#         print(heading,messageContent,receiver) # to verify
#         send_mail(
#             heading,
#             messageContent,
#             'deepakkumar006007@gmail.com',
#             [receiver],
#             fail_silently=False,
#         )

# how to send email templates ->
# try:
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     # server.ehlo()
#     print('connected to server')
#     server.starttls()
#     server.login(gmail_user, gmail_password)
#     print('login success')
#     server.sendmail(gmail_user,send_to, message)
#     server.close()
#     print('Email sent!')
#     return HttpResponse('email - sent')
# except:
#     print('Something went wrong...')
#     return HttpResponse('something went wrong -- ')
#     # print(sys.exit())

# how to read from body and return the response
