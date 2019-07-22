'''
Created on 16 juil. 2019

@author: All

'''
from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    '''
        :Project: class héritant de Model et définissant les attributs et les fonctions d'un objet de type Project
        :title: reçoit un CharField contenant le nom du projet
        :description: reçoit un TextField contenant une description du projet
        :version: reçoit un IntegerField contenant un numéro de version sous forme d'entier
        :__str__: methode d'affichage par defaut 
            :return: le contenu de l'attribut title de l'objet
    '''
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    version = models.IntegerField()

    def __str__(self):
        return self.title


class Status(models.Model):
    '''
        :Status: class héritant de Model et définissant les attributs et les fonctions d'un objet de type Status
        :level: reçoit un CharField contenant un niveau d'avancement
        :__str__: methode d'affichage par defaut 
            :return: le contenu de l'attribut level de l'objet
    '''
    level = models.CharField(max_length=20)

    def __str__(self):
        return self.level


class Task(models.Model):
    '''
        :Task: class héritant de Model et définissant les attributs et les fonctions d'un objet de type Task
        :description: reçoit un CharField contenant une description de la tâche
        :title: reçoit un CharField contenant le nom de la tâche
        :starting_date: reçoit un DateTimeField contenant la date de mise en projet de la tâche
        :deadline: reçoit un DateTimeField contenant l'échéance de remise de la tâche
        :priority: reçoit un BooleanField définissant si une tâche est prioritaire ou non
        :id_user: reçoit un lien de clé étrangère vers l'id de l'utilisateur chargé de la tâche
        :id_status: reçoit un lien de clé étrangère vers l'id du status d'avancement de la tâche
        :id_project: reçoit un lien de clé étrangère vers l'id du projet auquel la tâche est rattachée
        :__str__: methode d'affichage par defaut 
            :return: le contenu de l'attribut title de l'objet
    '''
    description = models.CharField(max_length=250)
    title = models.CharField(max_length=50)
    starting_date = models.DateTimeField()
    deadline = models.DateTimeField()
    priority = models.BooleanField(default=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_status = models.ForeignKey(Status, on_delete=models.CASCADE)
    id_project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ' ' + self.title

 
class Information(models.Model):
    '''
        :Information: class héritant de Model et définissant les attributs et les fonctions d'un objet de type Information
        :title: reçoit un CharField contenant le titre de l'information
        :description: reçoit un TextField contenant l'information
        :id_task: reçoit un lien de clé étrangère vers l'id de la tâche à laquelle se réfère l'information
        :__str__: methode d'affichage par defaut 
            :return: le contenu de l'attribut title de l'objet
    '''    
    title = models.CharField(max_length=200)
    description = models.TextField()
    id_task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
