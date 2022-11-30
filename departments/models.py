from django.db import models

# Create your models here.
class DepHero(models.Model):
    image = models.ImageField(upload_to="DepHeroImages")
    DEPARTMENTS = (("CSE","CSE"),("ECE","ECE"),("EEE","EEE"),("ME","ME"),("CE","CE"),("BSH","BSH"),("None","None"))
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")

class POES(models.Model):
    DEPARTMENTS = (("CSE","CSE"),("ECE","ECE"),("EEE","EEE"),("ME","ME"),("CE","CE"),("BSH","BSH"),("None","None"))
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    data = models.CharField(max_length=300)


class POS(models.Model):
    DEPARTMENTS = (("CSE","CSE"),("ECE","ECE"),("EEE","EEE"),("ME","ME"),("CE","CE"),("BSH","BSH"),("None","None"))
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    data = models.CharField(max_length=300)


class PSOS(models.Model):
    DEPARTMENTS = (("CSE","CSE"),("ECE","ECE"),("EEE","EEE"),("ME","ME"),("CE","CE"),("BSH","BSH"),("None","None"))
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    data = models.CharField(max_length=300)

class Vission(models.Model):
    DEPARTMENTS = (("CSE","CSE"),("ECE","ECE"),("EEE","EEE"),("ME","ME"),("CE","CE"),("BSH","BSH"),("None","None"))
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    vission = models.CharField(max_length=300)
 

class Mission(models.Model):
    DEPARTMENTS = (("CSE","CSE"),("ECE","ECE"),("EEE","EEE"),("ME","ME"),("CE","CE"),("BSH","BSH"),("None","None"))
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    Mission = models.CharField(max_length=300)
    def __str__(self):
        return self.Mission
 
class DepUpdates(models.Model):
    DEPARTMENTS = (("CSE","CSE"),("ECE","ECE"),("EEE","EEE"),("ME","ME"),("CE","CE"),("BSH","BSH"),("None","None"))
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    title = models.CharField(max_length=100)
    data = models.CharField(max_length=300)
    date = models.DateField()

    def __str__(self):
        return self.title


class Associations(models.Model):
    title = models.CharField(max_length=150)
    data = models.CharField(max_length=500)
    image = models.ImageField(upload_to="AssociationsImages")
    DEPARTMENTS = (("CSE","CSE"),("ECE","ECE"),("EEE","EEE"),("ME","ME"),("CE","CE"),("BSH","BSH"),("None","None"))
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    linkname = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.title


class ProfessionalBodies(models.Model):
    title = models.CharField(max_length=150)
    data = models.CharField(max_length=500)
    DEPARTMENTS = (("CSE","CSE"),("ECE","ECE"),("EEE","EEE"),("ME","ME"),("CE","CE"),("BSH","BSH"),("None","None"))
    department = models.CharField(max_length=200, choices = DEPARTMENTS, default="None")
    linkname = models.CharField(max_length=100)
    link = models.URLField()
    def __str__(self):
        return self.title

