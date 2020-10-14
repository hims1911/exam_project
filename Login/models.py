from django.db import models
# Create your models here.

class UserData(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    cn_password = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone_number = models.CharField( max_length=12)
    prn_number = models.CharField(max_length=20)
    GENDER = (
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Others"),

    )
    gender = models.CharField(max_length=6,choices=GENDER)
    CLG_NAME = (
        ("0", "Select College Name"),
        ("1", " Bharti Vidyapeeth Institute of Management and Information Technology, Belapur."),
        ("2", "Chikitsak Samuha's S. S. & L. S. Patkar College, Goregoan."),
        ("3", "N. G. Acharya & D. K. Marathe College of Arts, Science & Commerce, Chembur."),
        ("4", "Karmaveer Bhaurao Patil College, Vashi."),
        ("5", "S. P. N. Doshi Women's College,Ghatkopar."),
    )
    clg_name = models.CharField(max_length=6,choices=CLG_NAME)

class ClgId(models.Model):
    CLG_NAME = (
        ("#", "Select College Name"),
        ("1", " Bharti Vidyapeeth Institute of Management and Information Technology, Belapur ."),
        ("2", "Chikitsak Samuha's S. S. & L. S. Patkar College, Goregoan."),
        ("3", "N. G. Acharya & D. K. Marathe College of Arts, Science & Commerce, Chembur."),
        ("4", "Karmaveer Bhaurao Patil College, Vashi."),
        ("5", "S. P. N. Doshi Women's College,Ghatkopar."),
    )
    clg_name=models.CharField(max_length=6 ,choices=CLG_NAME)
