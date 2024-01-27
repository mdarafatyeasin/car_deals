from django.shortcuts import render,redirect
from .forms import AddCarForm,CommentForm
from django.contrib import messages
from django.views.generic import DetailView
from . import models
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@login_required
def add_Car(request):
    if request.method == "POST":
        add_car_form = AddCarForm(request.POST, request.FILES)
        if add_car_form.is_valid():
            messages.success(request, "Car Added")
            add_car_form.save()
            return redirect("add_car")
    else:
        add_car_form = AddCarForm()
    return render(request, "add_car.html", {"form": add_car_form})

# detail
@method_decorator(login_required, name='dispatch')
class CarDetails(DetailView):
    model = models.car
    pk_url_kwarg = "id"
    template_name = "car_detail.html"
    def get(self, request, *args, **kwargs):
        # Access and print the current user's ID
        user_id = request.user.id
        print(request.user.id)
        return super().get(request, *args, **kwargs)
    

# detail
class detail_view(DetailView):
    model = models.car
    pk_url_kwarg = 'id'
    template_name = 'car_detail.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comment.all()
        comment_form = CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
