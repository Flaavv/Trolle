'''
Created on 16 juil. 2019

@author: All

'''
from django import forms
from .models import *


class ProjectForm(forms.ModelForm):
    '''
        Formulaire d'ajout de projet
        La class Meta récupère le Model Project et identifie les champs
        :fields: indique quels champs du Model seront utilisés pour produire le formulaire avec des champs adaptés
    '''
    class Meta:
        model = Project
        fields = '__all__'


class Login_Form(forms.Form):
    '''
        Formulaire de connexion
        :your_name: reçoit un CharField contenant le nom de l'utilisateur
        :your_password: reçoit un CharField contenant le nom de l'utilisateur avec le widget PasswordInput
        :PasswordInput: Widget qui applique une methode de hashage aux données entrées dans le champ
    '''
    your_name = forms.CharField(max_length=30, min_length=2)
    your_password = forms.CharField(min_length=1, widget=forms.PasswordInput)


class TaskForm(forms.ModelForm):
    '''
        Formulaire d'ajout et de modification de tâche
        La class Meta récupère le Model Task et identifie les champs
        :fields: indique quels champs du Model seront utilisés pour produire le formulaire avec des champs adaptés
    '''
    class Meta:
        model = Task
        fields = '__all__'


class InformationForm(forms.ModelForm):
    '''
        Formulaire d'ajout d'information
        La class Meta récupère le Model Information et identifie les champs
        :fields: indique quels champs du Model seront utilisés pour produire le formulaire avec des champs adaptés
    '''
    class Meta:
        model = Information
        fields = '__all__'
