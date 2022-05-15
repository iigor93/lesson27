import factory

from ads.models import Ads
from selections.models import Selection


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ads
    name = "new_ads_min_len_10"
    price = 44
    

class SelectionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Selection
    name = "SelectionName"
    owner_id = 1
