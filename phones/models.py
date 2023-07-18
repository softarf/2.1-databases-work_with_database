from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    release_date = models.CharField(null=True, blank=True)
    lte_exists = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(max_length=50, editable=False)    # hide from admin
    #
    objects = models.Manager()          # Диспетчер записей. Для PyCharm Community объявлять явно.

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Phone, self).save(*args, **kwargs)
