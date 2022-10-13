from django.db import models
from django.urls import reverse

# Create your models here.
class Musician(models.Model):
    #id=models.AutoField(Primary_Key=True)  hidden by default we dont have to write
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    instrument=models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('first_app:musician_detail',kwargs={'pk':self.pk})




class Album(models.Model):
        #id=models.AutoField(Primary_Key=True)  hidden by default we dont have to write
        artist=models.ForeignKey(Musician,on_delete=models.CASCADE,related_name='album_list')
        name=models.CharField(max_length=50)
        release_date=models.DateField()


        rating=(
        (1,'WORST'),
        (2,'BAD'),
        (3,'NOT BAD'),
        (4,'GOOD'),
        (5,'EXCELLENT'),
        )

        num_stars=models.IntegerField(choices=rating)

#        class Meta: {for chnage the table name}
#            db_table='album'



        def __str__(self):
            return self.name + ", Rating " + str(self.num_stars)
