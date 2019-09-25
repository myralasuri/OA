from django.db import models
# Create your models here.

class Employe(models.Model):
    id  = models.AutoField(primary_key=True)
    name = models.CharField( max_length=50)
    email = models.CharField( max_length=50)
    pin = models.CharField( max_length=50)
    manager = models.IntegerField(default=0)
    
    
    class Meta:
        verbose_name = ("Employe")
        verbose_name_plural = ("Employes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Employe_detail", kwargs={"pk": self.pk})

class Department(models.Model):
    emp = models.ForeignKey("Employe", verbose_name=("Emp_department"), on_delete=models.CASCADE)
    name = models.CharField( max_length=50)

    class Meta:
        verbose_name = ("Department")
        verbose_name_plural = ("Departments")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Department_detail", kwargs={"pk": self.pk})

class Position(models.Model):

    emp = models.ForeignKey("Employe", verbose_name=("emp_position"), on_delete=models.CASCADE)
    position = models.CharField(("Position"), max_length=50, default='employee')

    class Meta:
        verbose_name = ("Position")
        verbose_name_plural = ("Positions")

    def __str__(self):
        return self.emp.name

    def get_absolute_url(self):
        return reverse("Position_detail", kwargs={"pk": self.pk})

class Leaves(models.Model):
    emp = models.ForeignKey("Employe", verbose_name=("emp_leaves"), on_delete=models.CASCADE)
    request_status =[
        ('requested' , 'Requested'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    types = [
        ('leave', 'Leave'),
        ('execuse', 'Execuse')
    ]
    status = models.CharField(
        choices = request_status , max_length=50, default = '')
    LEave_type = models.CharField(choices = types , max_length=50, default = '') 
    class Meta:
        verbose_name = "Leaves"
        verbose_name_plural = "Leaves"
    def __str__(self):
        return ','.join([self.emp.name, self.status])

    def get_absolute_url(self):
        return reverse("Leaves_detail", kwargs={"pk": self.pk})