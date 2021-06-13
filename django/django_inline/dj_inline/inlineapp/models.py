'''https://www.jbssolutions.com/resources/blog/improve-djangos-admin-interface-using-inlines/#:~:text=When%20two%20Django%20models%20share,extremely%20useful%20for%20many%20applications.&text=And%20here%20is%20the%20admin.py%20file%20for%20the%20Starfleet%20app.'''


from django.db import models

# Create your models here.
class Rule(models.Model):
    name = models.CharField(max_length=200)

class Channel(models.Model):
    id = models.CharField(max_length=9,primary_key=True)
    name = models.CharField(max_length=100)
    rule = models.ForeignKey(Rule,related_name='channels', on_delete=models.CASCADE,blank=True)



class Officer(models.Model):
    name = models.CharField(max_length=256)
    rank = models.ForeignKey('Rank', on_delete=models.CASCADE)
    ship_assignment = models.ForeignKey('Ship', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Rank(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Ship(models.Model):
    name = models.CharField(max_length=256)
    registry = models.CharField(max_length=256)
    captain = models.OneToOneField('Officer', default=None, on_delete=models.CASCADE, blank=True, null=True)
    ship_class = models.CharField(max_length=256)
    status = models.CharField(max_length=256)

    def __str__(self):
        return self.name