from django.shortcuts import render, redirect
from .models import Contact


# Create your views here.
def index(request):
    contacts = Contact.objects.all()
    search_input = request.GET.get("search-area")
    if search_input:
        contacts = Contact.objects.filter(full_name__icontains=search_input)
    else:
        contacts = Contact.objects.all()
        search_input = ""
    return render(
        request, "index.html", {"contacts": contacts, "search_input": search_input}
    )


def add_contact(request):
    if request.method == "POST":
        new_contact = Contact(
            full_name=request.POST["fullname"],
            relationship=request.POST["relationship"],
            email=request.POST["email"],
            phone_number=request.POST["phone-number"],
            address=request.POST["address"],
        )
        new_contact.save()
        return redirect("/")

    return render(request, "new.html")


def contactprofile(request, pk):
    contact = Contact.objects.get(id=pk)
    return render(request, "contact_profile.html", {"contact": contact})


def edit_contact(request, pk):
    contacts = Contact.objects.get(id=pk)
    if request.method == "POST":
        contacts.full_name = request.POST.get("fullname", "")
        contacts.relationship = request.POST.get("relationship", "")
        contacts.phone_number = request.POST.get(
            "Phone", ""
        )  # in get we write the name that belongs to that html page not the models.pyz
        contacts.email = request.POST.get("mail", "")
        contacts.address = request.POST.get("address", "")
        contacts.save()

        return redirect("/profile/" + str(contacts.id))
    return render(request, "edit.html", {"contacts": contacts})


def delete_contact(request, pk):
    contacts = Contact.objects.get(id=pk)

    if request.method == "POST":
        contacts.delete()
        return redirect("/")
    return render(request, "delete.html", {"contacts": contacts})
