import click
#from xenlib.management.command.cmd_project import cli

@click.command('install')
def action():
    """install help"""
    click.echo('project installed')


'''
def install():
    def processor():
        print('project installed')
    return processor
'''

