from django.core.management.base import BaseCommand, CommandError
from category import models as category_models
from products import models as products_models


class Command(BaseCommand):
    help = 'Migrate categories from products app to category apps '

    def handle(self, *args, **kwargs):
        old_cats = category_models.Category.objects.all()
        for cat in old_cats:
            category_models.Category.objects.create(title=cat.title)
        self.stdout.write(self.style.SUCCESS('Successfully migrated %s categories.' % old_cats.count()))
