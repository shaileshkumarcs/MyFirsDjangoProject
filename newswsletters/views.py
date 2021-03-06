from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm, SignUpForm
from .models import SignUp

# Create your views here.
def home(request):
	title = 'Sign Up Now'
	# if request.user.is_authenticated():
	# 	title = "My Title %s" %(request.user)

	#add a form
	# if request.method == "POST":
	# 	print request.POST
	form = SignUpForm(request.POST or None)
	contaxt = {
		"title": title,
		"form": form
	}

	if form.is_valid():
		#form.save()
		print request.POST['email']  #not recommended
		instance = form.save(commit=False)

		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		# if not instance.full_name:
		# 	instance.full_name = "Kumar Dangi"
		instance.save()
		contaxt = {
			"title" : "Thank You"
		}
	if request.user.is_authenticated() and request.user.is_staff:
            #print(SignUp.objects.all())
            # for instance in SignUp.objects.all():
            #     print(instance.full_name)
            queryset = SignUp.objects.all().order_by("-timestamp")#.filter(full_name__icontains="shailesh")
            #print(SignUp.objects.all().order_by("-timestamp").filter(full_name__icontains="shailesh").count())
            contaxt = {
                "queryset":queryset
        }

	return render(request, "home.html", contaxt)



def contact(request):
	title = "Contact Us"
	title_align_center = True
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key in form.cleaned_data:
		# 	print key
			# form.cleaned_data.get(key)
		# for key, value in form.cleaned_data.iteritems():
		# 	print key,value
		form_email = form.cleaned_data.get("email")
		form_full_name = form.cleaned_data.get("full_name")
		form_message = form.cleaned_data.get("message")
		#print form_email,  form_message,  form_full_name
        subject = "Site contact form"
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'shailesh.dangi@pacdevelopers.com']
        contact_message = "%s : %s via %s" % ('fhsjkgf', 'jdhfakjds', 'djgfdj')
        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=False)

        context = {
            "form":form,
			"title":title,
			"title_align_center":title_align_center,
        }
	return render(request, "forms.html",context)