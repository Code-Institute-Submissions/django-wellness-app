from django.urls import path

from .views import MembershipSelectView, PaymentView

app_name = 'pro'

urlpatterns = [
    path('', MembershipSelectView.as_view(), name='select')
]
