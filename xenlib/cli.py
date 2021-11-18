import os
import click
from xenlib.helper.config.environment import Environment

__version__ = 'v0.2.0'
xen_env = Environment()

CONTEXT_SETTINGS = dict(auto_envvar_prefix="COMPLEX")

pass_environment = click.make_pass_decorator(Environment, ensure=True)
cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "management","command"))

class ComplexCLI(click.MultiCommand):
    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith(".py") and filename.startswith("cmd_"):
                rv.append(filename[4:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        try:
            mod = __import__(f"xenlib.management.command.cmd_{name}", None, None, ["cli"])
        except ImportError:
            print("Fail to load some commands")
            return
        return mod.cli

@click.command(cls=ComplexCLI, context_settings=CONTEXT_SETTINGS)
@click.option("--verbose", is_flag=True, help="Enables verbose mode")
@click.version_option(__version__)
@pass_environment
def cli_all(ctx, verbose):
    """New Xen Tools Client v2"""
    ctx.verbose = verbose
    ctx.log('test log')
    pass

def cli():
    if xen_env.project_name is not None:
        print('Default commands for project', xen_env.project_name)
        from xenlib.management.action.project import register_actions
        register_actions()()
    else:
        cli_all()