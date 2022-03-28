import string
from django.db import models
#from sklearn.feature_extraction import img_to_graph

# Create your models here.
class Destination:
    id : int
    name : str
    desc : str
    price : int