from django.db.models import Model, CharField, ForeignKey, CASCADE, IntegerField, DateTimeField, ImageField, \
    BooleanField, PositiveSmallIntegerField, SET_NULL, TextField, TextChoices


class Category(Model):
    name = CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


from django.contrib import admin


class Origin(Model):
    name = CharField(max_length=100)

    def __str__(self):
        return self.name



class Entity(Model):
    class GENDER(TextChoices):
        GENDER_MALE = 'male', "Male"
        GENDER_FEMALE = 'female', "Female"
        GENDER_OTHERS = 'unknown', "Others/Unknown"

    name = CharField(max_length=100)
    alternative_name = CharField(max_length=100, null=True, blank=True)

    category = ForeignKey('apps.Category', CASCADE)
    origin = ForeignKey('apps.Origin', CASCADE)
    gender = CharField(max_length=100, choices=GENDER.choices)
    description = TextField()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


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


class Hero(Entity):
    is_immortal = BooleanField(default=True)

    benevolence_factor = PositiveSmallIntegerField(help_text="How benevolent this hero is?")
    arbitrariness_factor = PositiveSmallIntegerField(help_text="How arbitrary this hero is?")
    # relationships
    father = ForeignKey('self', SET_NULL, "+", null=True, blank=True)
    mother = ForeignKey('self', SET_NULL, "+", null=True, blank=True)
    spouse = ForeignKey('self', SET_NULL, "+", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Heroes"


class Villain(Entity):
    is_immortal = BooleanField(default=False)

    malevolence_factor = PositiveSmallIntegerField(help_text="How malevolent this villain is?")
    power_factor = PositiveSmallIntegerField(help_text="How powerful this villain is?")
    is_unique = BooleanField(default=True)
    count = PositiveSmallIntegerField(default=1)
