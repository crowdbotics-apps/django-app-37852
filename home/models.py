from django.db import models

# App model


class App(models.Model):
    # type choices for the app
    TYPECHOICES = [
        ('Web', 'Web'),
        ('Mobile', 'Mobile')
    ]

    # framework choices for the app
    FRAMEWORKC = [
        ('Django', 'Django'),
        ('React', 'React')
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=100, choices=TYPECHOICES)
    framework = models.CharField(max_length=100, choices=FRAMEWORKC)

    description = models.CharField(max_length=100, null=True)
    domain_name = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = "app"

# Plans model


class Plans(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    price = models.IntegerField(null=True)

    class Meta:
        db_table = "plan"

# Subscription Model


class Subscription(models.Model):
    # plans options
    plans = [
        ('1', 'Free'),
        ('2', 'Standard'),
        ('3', 'Pro')
    ]

    id = models.AutoField(primary_key=True)
    plan = models.CharField(max_length=30, choices=plans)
    # foreign key for apps
    app = models.ForeignKey("app", on_delete=models.CASCADE)
    active = models.BooleanField()

    class Meta:
        db_table = "subscriptions"
