from category.models import Categorie

for i in range(1500):
    Categorie.objects.create(name=f'categorie_{i}')