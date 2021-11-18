import os
import click
from typing_extensions import Required
from xenlib.cli import pass_environment
from xenlib.management.action.project import register_actions

@click.group() #chain=True)
def cli():
    """Project management"""
    pass

register_actions(cli)

'''
@cli.result_callback()
def process_pipeline(processors):
    i=0
    for processor in processors:
        i+=1
    
    if i>1:
        print('Unkown option(s)')
    else:
        processors[0]()
'''

'''
try:
    act_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..","action","project"))
    actions = []
    for filename in os.listdir(act_folder):
        if filename.endswith(".py") and filename.startswith("act_"):
            action_name = filename[0:-3]
            act_import = __import__("xenlib.management.action.project.{}".format(filename[0:-3]))

except ImportError:
    print('One or more actions failed to load')
'''