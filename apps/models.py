from django.db.models import Model, CharField, ForeignKey, CASCADE, IntegerField, DateTimeField, ImageField


class Category(Model):
    name = CharField(max_length=255)

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


class Tag(Model):
    name = CharField(max_length=255)


class Product(Model):
    name = CharField(max_length=255)
    image = ImageField(upload_to='products/%Y/%m/%d', null=True)
    price = IntegerField(default=0, blank=True)
    description = CharField(max_length=255)
    tags = ForeignKey('apps.Tag', CASCADE, null=True)
    category = ForeignKey('apps.Category', CASCADE)
    created_at = DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        if self.id is None:
            print("birinchi")
        else:
            print("keyingisi")

        super().save(force_insert, force_update, using, update_fields)
