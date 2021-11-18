import click
from xenlib.helper.config.environment import Environment

pass_environment = click.make_pass_decorator(Environment, ensure=True)

@click.command('run')
@pass_environment
def action(env):
    """checkin help"""
    click.echo('running project {}'.format(env.project_name))
