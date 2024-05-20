from django.db import models

def pk_dir(instance, filename):
    return "app/{0}/{1}".format(instance.pk, filename)

class Rawkes(models.Model):
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,unique=True,null=True)
	D = models.DateTimeField(blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 1000,blank=True,null=True)
	D = models.CharField(max_length = 1000,blank=True,null=True)
	D = models.CharField(max_length = 1000,blank=True,null=True)
	D = models.CharField(max_length = 1000,blank=True,null=True)
	D = models.CharField(max_length = 1000,blank=True,null=True)
	D = models.CharField(max_length = 1000,blank=True,null=True)
	D = models.CharField(max_length = 1000,blank=True,null=True)
	D = models.CharField(max_length = 1000,blank=True,null=True)
	def __str__(self):
		return self.No_KS

class Rawtang(models.Model):
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.ForeignKey(Rawkes,to_field='No_KS',on_delete=models.CASCADE,null=True)
	D = models.DateTimeField(blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 1000,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.IntegerField(blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	def __str__(self):
		return self.No_KS

class Rawramp(models.Model):
	D = models.IntegerField(blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.DateTimeField(blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 1000,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.DecimalField(max_digits=17, decimal_places=7,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	D = models.CharField(max_length = 100,blank=True,null=True)
	def __str__(self):
		return self.No_KS

class ChartRaw(models.Model):
	D = models.DateTimeField(auto_now_add = True)
	D = models.CharField()
	D = models.CharField()
	D = models.CharField()
	D = models.CharField()
	D = models.CharField()
	D = models.CharField()
	D = models.CharField()
	D = models.CharField()
	D = models.CharField()
	D = models.CharField()
	D = models.CharField(default="")
	D = models.CharField(default="")
	D = models.CharField(default="")
	D = models.CharField(default="")
	D = models.CharField(default="")
	D = models.CharField(default="")

class Nps(models.Model):
	D = models.DateTimeField(auto_now_add = True)
	D = models.CharField(default="")
	D = models.CharField(default="")
	D = models.CharField(default="")
	D = models.CharField(default="")
	D = models.FileField(upload_to=pk_dir)
	D = models.DecimalField(max_digits=17, decimal_places=7,blank=True,null=True)

class LocationActivity(models.Model):
	D = models.DateTimeField(auto_now_add = True)
	D = models.DecimalField(max_digits = 8,decimal_places = 6)
	D = models.DecimalField(max_digits = 9,decimal_places = 6)
	D = models.CharField(max_length=5,blank=True,null=True)
	D = models.CharField(max_length=5,blank=True,null=True)
	D = models.CharField(max_length=5,blank=True,null=True)
	D = models.CharField(max_length=5,blank=True,null=True)
	D = models.CharField(max_length=5,blank=True,null=True)

class SamplingSummary(models.Model):
	D = models.AutoField(primary_key=True)
	D = models.CharField(max_length = 100, blank=True, null=True)
	D = models.CharField(max_length = 100, blank=True, null=True)
	D = models.DateField(blank=True,null=True)
	D = models.TimeField(blank=True,null=True)
	D = models.TimeField(blank=True,null=True)

class SiteSampling(models.Model): 
	D = models.AutoField(primary_key=True)
	D = models.CharField(max_length = 100, blank=True, null=True)
	D = models.CharField(max_length = 100, blank=True, null=True)
	D = models.CharField(max_length = 100, blank=True, null=True)
	D = models.CharField(max_length = 100, blank=True, null=True)
	D = models.CharField(max_length = 100, blank=True, null=True)

class SamplingObservation(models.Model):
	D = models.AutoField(primary_key=True)
	D = models.ForeignKey(SiteSampling, on_delete=models.CASCADE)
	D = models.CharField(max_length = 400, blank=True, null=True)
	D = models.CharField(max_length = 400, blank=True, null=True)
	D = models.CharField(max_length = 400, blank=True, null=True)
	D = models.CharField(max_length = 400, blank=True, null=True)
	D = models.CharField(max_length = 400, blank=True, null=True)
	D = models.DurationField(blank=True, null=True)
	D = models.CharField(max_length = 1000, blank=True, null=True)
	D = models.FileField(upload_to='images/', blank=True, null=True)
	D = models.CharField(max_length = 400, blank=True, null=True)
	D = models.CharField(max_length = 400, blank=True, null=True)
	D = models.CharField(max_length = 400, blank=True, null=True)
	D = models.CharField(max_length = 400, blank=True, null=True)
	D = models.CharField(max_length = 400, blank=True, null=True)
	D = models.CharField(max_length = 400, blank=True, null=True)
	D = models.CharField(max_length = 1000, blank=True, null=True)
	D = models.FileField(upload_to='images/', blank=True, null=True)
	D = models.CharField(max_length = 400, blank=True, null=True)
	D = models.CharField(max_length = 400, blank=True, null=True)
	D = models.CharField(max_length = 400, blank=True, null=True)
	D = models.CharField(max_length = 400, blank=True, null=True)
	D = models.CharField(max_length = 1000, blank=True, null=True)
	D = models.FileField(upload_to='images/', blank=True, null=True)

class SamplingMeasurement(models.Model):
	D = models.AutoField(primary_key=True)
	D = models.ForeignKey(SiteSampling, on_delete=models.CASCADE)
	D = models.CharField(max_length = 400, blank=True, null=True)
	D = models.CharField(max_length = 400, blank=True, null=True)
	D = models.CharField(max_length = 400, blank=True, null=True)
	D = models.CharField(max_length = 400, blank=True, null=True)
	D = models.CharField(max_length = 400, blank=True, null=True)
	D = models.CharField(max_length = 400, blank=True, null=True)
	D = models.CharField(max_length = 400, blank=True, null=True)
	D = models.CharField(max_length = 400, blank=True, null=True)
	D = models.CharField(max_length = 400, blank=True, null=True)
	D = models.CharField(max_length = 400, blank=True, null=True)
	D = models.CharField(max_length = 400, blank=True, null=True)
	D = models.CharField(max_length = 400, blank=True, null=True)

class SampleCollection(models.Model):
	D = models.AutoField(primary_key=True)
	D = models.CharField(max_length = 100, blank=True, null=True)
	D = models.CharField(max_length = 1000, blank=True, null=True)
	D = models.ForeignKey(SamplingSummary, on_delete=models.CASCADE)
	D = models.ForeignKey(SiteSampling, on_delete=models.CASCADE)

class SenderDetails(models.Model):
	D = models.AutoField(primary_key=True)
	D = models.CharField(max_length = 100, blank=True, null=True)
	D = models.CharField(max_length = 100, blank=True, null=True)
	D = models.CharField(max_length = 100, blank=True, null=True)
	D = models.CharField(max_length = 100, blank=True, null=True)
	D = models.CharField(max_length = 100, blank=True, null=True)
	D = models.CharField(max_length = 100, blank=True, null=True)
	D = models.CharField(max_length = 100, blank=True, null=True)
	D = models.CharField(max_length = 100, blank=True, null=True)
	D = models.CharField(max_length = 100, blank=True, null=True)

class SampleDetails(models.Model):
	D = models.AutoField(primary_key=True)
	D = models.CharField(max_length = 100, blank=True, null=True)
	D = models.CharField(max_length = 100, blank=True, null=True)
	D = models.DateField(blank=True,null=True)
	D = models.TimeField(blank=True,null=True)
	D = models.ForeignKey(SenderDetails, on_delete=models.CASCADE)
	D = models.CharField(max_length = 100, blank=True, null=True)
	D = models.CharField(max_length = 100, blank=True, null=True)
	Container_Preservatives =  models.CharField(max_length = 100, blank=True, null=True)
	D = models.BooleanField()
	D = models.BooleanField()
	D = models.CharField(max_length = 1000, blank=True, null=True)

class SampleTransportation(models.Model):
	D = models.AutoField(primary_key=True)
	D = models.ForeignKey(SampleDetails, on_delete=models.CASCADE)
	D = models.CharField(max_length = 100, blank=True, null=True)
	D = models.CharField(max_length = 100, blank=True, null=True)
	D = models.DateField(blank=True,null=True)
	D = models.TimeField(blank=True,null=True)
	D = models.CharField(max_length = 100, blank=True, null=True)
	D = models.CharField(max_length = 100, blank=True, null=True)
	D = models.DateField(blank=True,null=True)
	D = models.TimeField(blank=True,null=True)
	D = models.CharField(max_length = 100, blank=True, null=True)
	D = models.CharField(max_length = 100, blank=True, null=True)
	D = models.CharField(max_length = 100, blank=True, null=True)
	D = models.CharField(max_length = 100, blank=True, null=True)
	D = models.DateField(blank=True,null=True)
	D = models.TimeField(blank=True,null=True)	
	D = models.CharField(max_length = 100, blank=True, null=True)
	D = models.CharField(max_length = 100, blank=True, null=True)
	D = models.DateField(blank=True,null=True)
	D = models.TimeField(blank=True,null=True)
	D = models.CharField(max_length = 100, blank=True, null=True)
	D = models.CharField(max_length = 100, blank=True, null=True)
