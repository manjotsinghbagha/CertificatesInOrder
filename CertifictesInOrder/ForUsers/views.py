from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CertificteEraned

# Create your views here.
@login_required
def listcert(request):
    certificates = CertificteEraned.bjects.filter(enduser=request.user.profile)
    return render(request, 'listcert.html', certificates)


@login_required
def createtcert(request):
    certificates = CertificteEraned.bjects.filter(enduser=request.user.profile)
    return render(request, 'listcert.html', certificates)


# def hh(request):
#     if request.method == 'POST':
#         user_form = UpdateUserForm(request.POST, instance=request.user)
#         profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Your profile is updated successfully')
#             return redirect(to='users-profile')
#     else:
#         user_form = UpdateUserForm(instance=request.user)
#         profile_form = UpdateProfileForm(instance=request.user.profile)

#     return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})
