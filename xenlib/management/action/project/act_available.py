import click
from xenlib.helper.api.project import check_project_available

@click.command('available')
def action():
    """available help"""
    list_project = check_project_available()
    print("Project Available : ")
    for available in list_project:
        print("  "+available['projects_name']+" -> "+available['projects_git_remoteurl']+" ("+available['projects_git_defaultbranch']+")")
