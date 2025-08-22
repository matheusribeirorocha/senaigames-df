from django.db import models

# Create your models 

class Membro(models.Model):
    email = models.CharField(max_length=80,null=False,blank=False)
    senha = models.CharField(max_length=50,null=False,blank=False)
    nome = models.CharField(max_length=80,null=False,blank=False)
    foto = models.CharField(max_length=30,null=True,blank=True)
    def __str__(self):
        return f"Nome [nome={self.nome}]"

class Genero(models.Model):
    nome = models.CharField(max_length=80,null=False,blank=False)
    
    def __str__(self):
        return f"Gênero [nome={self.nome}]"