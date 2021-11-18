import click
#from xenlib.management.command.cmd_project import cli

@click.command('checkin')
def action():
    """checkin help"""
    click.echo('project checked-in')
