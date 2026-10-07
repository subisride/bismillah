from django.urls import path

from main.views import (
    show_main,
    show_experience,
    show_projects,
    create_project,
    delete_project,
    get_projects_json,
    register,
    login_user,
    logout_user,
    toggle_star
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("projects/add/", create_project, name="create_project"),
    path("experience/", show_experience, name="show_experience"),
    path("projects/", show_projects, name="show_projects"),
    path("projects/<uuid:project_id>/delete/", delete_project, name="delete_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("projects/<uuid:project_id>/star/", toggle_star, name="toggle_star",),
]
