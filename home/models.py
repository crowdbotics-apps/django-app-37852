from django.db import models


class App(models.Model): 
    TYPECHOICES = [
        ('Web', 'Web'),
        ('Mobile', 'Mobile')
    ]

    FRAMEWORKC = [
        ('Django', 'Django'),
        ('React', 'React')
    ]
    id =  models.AutoField(primary_key=True)  
    name = models.CharField(max_length=20)  
    type = models.CharField(max_length=100,choices=TYPECHOICES) 
    framework = models.CharField(max_length=100,choices=FRAMEWORKC) 
    
    description = models.CharField(max_length=100,null=True)  
    domain_name = models.CharField(max_length=100,null=True)  
    
    class Meta:  
        db_table = "app"  

class Plans(models.Model): 
    id =  models.AutoField(primary_key=True)  
    name = models.CharField(max_length=20)    
    description = models.CharField(max_length=100)  
    price = models.IntegerField(null=True)  
    
    class Meta:  
        db_table = "plan"  
        


class Subscription(models.Model):
    plans = [
        ('1', 'Free'),
        ('2', 'Standard'),
        ('3', 'Pro')
    ]

    
    id =  models.AutoField(primary_key=True)  
    plan = models.CharField(max_length=30,choices=plans)    
    app = models.ForeignKey("app",on_delete=models.CASCADE )
    active = models.BooleanField()  
    
    class Meta:  
        db_table = "subscriptions" 