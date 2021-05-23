from django.conf.urls import url
from django.shortcuts import render, redirect
from django.urls import reverse
import stripe
from .models import Plan, PlanType, CanAccess
from django.http import JsonResponse
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

stripe.api_key = "sk_test_51IkYavSEV2gnCPG20RfHko44Y1eooN01Kjd9bMU9vGo5a2WlNNr5XYqKoLKWBlLvkY3TGDv2evZMHO24EnMNrLUT00n1k2ztHs"

@login_required
def home(request):
    plantype = PlanType.objects.all()

    context = {
        'plans':plantype,
    }
    return render(request, 'plan/home.html', context)

def register(request):
    if request.method == 'POST':
        print('method is post ....')
        form = UserRegistrationForm(request.POST)
        print('form is not yet submitted ...')
        if form.is_valid():
            print('form is valid')
            messages.success(request, 'Account Created Successfully')
            form.save()
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1']
            )
            login(request, new_user)
            print('login successfull ....')
            return redirect('home')
    else:
        form = UserRegistrationForm()

    context = {
        'form':form,
    }
    return render(request, 'plan/register.html', context)



@login_required
def same_areas(request, width, height):
    plans = Plan.objects.filter(plantype__width=width, plantype__height=height)
    plntype = PlanType.objects.filter(width=width, height=height)
    print('plan run success')
    canaccess = CanAccess.objects.filter(user=request.user)
    pln = {}
    for i in plans:
        try:
            CanAccess.objects.get(user=request.user, plan=i)
            pln[i] = 'Yes'
        except:
            pln[i] = 'No'
        
    pln = dict(pln)
    for key, value in pln.items():
        print(key, value)
    print(pln)
    print('this is also running')
 
    context = {
        'plans':plans,
        'canaccess':canaccess,
        'pln':pln.items(),
    }
    return render(request, 'plan/plantypes.html', context)


@login_required
def individual_plan(request, args):
    pk = args
    print(pk, type(pk))
    plan = Plan.objects.get(id=pk)
    context = {
        'plan':plan,
    }
    return render(request, 'plan/individual.html', context)


@login_required
def payment(request, pk):
    plan = Plan.objects.get(pk=pk)
    try:
        CanAccess.objects.get(plan=plan, user=request.user)
        return redirect('individual-plan', pk)
        # return redirect(reverse('individual', args=[pk]))
    except:
        return render(request, 'plan/stripe_payment.html', {'pk':pk})
        
    # print(request.user,id)
    # return redirect(reverse('charge', args=[id]))


@login_required
def charge(request, id):
	if request.method == 'POST':
		print('Data:', request.POST, id)
		amount, newid = 50,id

		customer = stripe.Customer.create(
			email=request.user.email,
			name=request.user.username,
			source=request.POST['stripeToken']
			)

		charge = stripe.Charge.create(
			customer=customer,
			amount=amount*100,
			currency='inr',
			description="Donation"
			)
	return redirect(reverse('success', args=[amount, newid]))
    # return render(request, 'plan/success.html')


@login_required
def successMsg(request, amount, newid):
    print(amount, newid)
    # id = list(args[1])
    plan = Plan.objects.get(id=int(newid))
    can_access_user = CanAccess.objects.create(user=request.user, plan=plan)
    can_access_user.save()
    return redirect(reverse('individual-plan', args=[newid]))
