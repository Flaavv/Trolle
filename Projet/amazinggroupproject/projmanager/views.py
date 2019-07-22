'''
Created on 16 juil. 2019

@author: All

'''
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def Auth_User(request):
    '''
        :Auth_User: vue d'authentification des utilisateurs
        :form: reçoit le formulaire Login_Form vide ou prérempli par methode POST
        :existing_user: reçoit le résultat de la fonction d'authentification authenticate
            Si existing_user existe :
                Connecte l'utilisateur
                :return: redirige vers la page projects
            Si existing_user n'existe pas:
                Affiche un message d'erreur indiquant quel champ n'est pas correct
        :return: rappelle la page loginuser avec les données du formulaire préremplies
    '''
    message_mdp = '' 
    message_nom = '' 
    if request.method == 'POST':
        form = Login_Form(request.POST)
        entered_username = request.POST['your_name']
        entered_password = request.POST['your_password']
        existing_user = authenticate(username=entered_username, password=entered_password)
        if existing_user is not None: 
            login(request, existing_user)
            return HttpResponseRedirect(reverse('projmanager:projects'))
        else: 
            allExistingUsers = User.objects.all()
            form = Login_Form({'your_name':''})
            message_mdp = ""
            message_nom = "Inconnu.  Recommencez." 
            for user in allExistingUsers:
                if user.username == entered_username: 
                    form = Login_Form({'your_name':entered_username})
                    message_mdp = "Incorrecte. Recommencer."
                    message_nom = ""    
    else:
        form = Login_Form()
    return render(request, 'projmanager/login.html', {
        'form': form, 'msg_mdp': message_mdp, 'msg_nom': message_nom})


@login_required
def List_project(request):
    '''
        :List_project: vue de l'ensemble des projets
        :title_list_project: récupère tous les objets de type Project
        :context: génère un dictionnaire contenant l'ensemble des objets Project
        :return: renvoi le contenu du dictionaire context pour traitement dans le template
    '''
    title_list_project = Project.objects.all()
    context = {'title_list_project': title_list_project}
    return render(request, 'projmanager/projects.html', context)        


@login_required
def List_task_for_project(request, project_id):
    '''
        :List_task_for_project: vue de l'ensemble des tâches attachées à un projet
        :task: récupère tous les objets Task pour lesquels project_id correspond à l'id de l'objet Project
        :return: renvoi un dictionnaire contenant l'ensemble des objets Task dans la requête
    '''
    task = get_object_or_404(Project, pk=project_id)
    return render(request, 'projmanager/tasks.html', {'zekey': task})


@login_required
def Task_Show(request, task_id):
    '''
        :Task_Show: vue détaillée d'une tâche
        :task: récupère l'objet Task dont l'id est task_id
        :return: renvoi un dictionnaire contenant l'objet Task de la requête
    '''
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'projmanager/Task_Show.html', {'task': task})    

    
@login_required
def New_Task(request):
    '''
        :New_Task: vue d'ajout d'une nouvelle tâche
        :form: reçoit le formulaire TaskForm vide ou rempli par la methode POST
        Si le formulaire est valid:
            Sauvegarde le formulaire dans la base de donnée
            :return: redirige vers la page projects
        :return: rappelle la page new_task avec les données du formulaire préremplies
    '''
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('projmanager:projects'))    
    return render(request, 'projmanager/new_task.html', locals())


@login_required
def Task_Update(request, task_id):
    '''
        :Task_Update: vue de modification de tâche
        :instance: reçoit les données de l'objet de type Task dont l'id vaut task_id 
        :form: reçoit le formulaire TaskForm rempli par les données de instance ou par la methode POST
        Si le formulaire est valid:
            Sauvegarde le formulaire dans la base de donnée
            :return: redirige vers la page projects
        :return: rappelle la page taskupdate avec les données du formulaire préremplies
    '''
    instance = Task.objects.get(id=task_id)
    form = TaskForm(request.POST or None, instance=instance)        
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('projmanager:projects'))                
    return render(request, 'projmanager/taskupdate.html', locals())


@login_required
def New_Project(request):
    '''
        :New_Project: vue d'ajout d'un nouveau projet
        :form: reçoit le formulaire ProjectForm vide ou rempli par la methode POST
        Si le formulaire est valid:
            Sauvegarde le formulaire dans la base de donnée
            :return: redirige vers la page projects
        :return: rappelle la page New_project avec les données du formulaire préremplies
    '''
    form = ProjectForm(request.POST or None)
    if form.is_valid(): 
        form.save()
        return HttpResponseRedirect(reverse('projmanager:projects'))
    return render(request, 'projmanager/New_project.html', locals())


def Deconnect(request):
    '''
        :Deconnect: vue de déconnexion
            Appelle une fonction logout qui écrase l'authentification de l'utilisateur
        :return: redirige vers la page loginuser
    '''
    logout(request)
    return redirect(reverse('projmanager:loginuser'))    

 
@login_required
def Informations(request, task_id):
    '''
        :Informations: vue de l'ensemble des informations d'une tâche
        :Infos: récupère l'objet de type Task dont l'id est task_id
        :return: renvoi un dictionnaire contenant l'objet de la requête
    '''
    Infos = get_object_or_404(Task, pk=task_id)
    return render(request, 'projmanager/Informations.html', {'Infos': Infos})


@login_required
def New_Information(request):
    '''
        :New_Information: vue d'ajout d'une nouvelle information
        :form: reçoit le formulaire InformationForm vide ou rempli par la methode POST
        Si le formulaire est valid:
            Sauvegarde le formulaire dans la base de donnée
            :return: redirige vers la page projects
        :return: rappelle la page New_project avec les données du formulaire préremplies
    '''
    form = InformationForm(request.POST or None)
    if form.is_valid(): 
        form.save()
        return HttpResponseRedirect(reverse('projmanager:projects'))
    return render(request, 'projmanager/New_information.html', locals())
