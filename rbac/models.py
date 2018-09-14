from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=21)
    pwd = models.CharField(max_length=32)
    role = models.ManyToManyField(to="Role")

    class Meta:
        verbose_name_plural = "用户表"

    def __str__(self):
        return self.name

class Role(models.Model):
    title = models.CharField(max_length=32)
    permissonurl = models.ManyToManyField(to="PermisionUrl")

    class Meta:
        verbose_name_plural = "角色表"

    def __str__(self):
        return self.title

class PermisionUrl(models.Model):
    title = models.CharField(max_length=32)
    url = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = "url权限表"


    def __str__(self):
        return '%s%s'%(self.title,self.url)