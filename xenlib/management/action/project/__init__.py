import os
import click
from xenlib.cli import __version__

actions_exclude = ['checkin', 'register']

@click.group()
@click.version_option(__version__)
def cli_project():
    pass

def register_actions(cli_group=cli_project):
    try:
        act_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "project"))
        for filename in os.listdir(act_folder):
            if filename.endswith(".py") and filename.startswith("act_"):
                action_name = filename[4:-3]
                if action_name not in actions_exclude:
                    act_command = __import__("xenlib.management.action.project.act_{}".format(action_name), None, None, ['action'])
                    cli_group.add_command(act_command.action)
        return cli_project
    except ImportError:
        print('One or more actions failed to load! ({})'.format(filename))
