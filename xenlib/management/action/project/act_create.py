import click
#from xenlib.management.command.cmd_project import cli

@click.command('create')
def action():
    """create help"""
    click.echo('project created')

'''
def create():
    def processor():
        print('project created')
    return processor
'''
