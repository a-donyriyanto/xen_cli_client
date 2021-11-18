import click
#from xenlib.management.command.cmd_project import cli

@click.command('register')
def action():
    """register help"""
    click.echo('project registered')
