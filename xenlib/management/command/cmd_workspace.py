from xenlib.cli import pass_environment
import click


@click.command("workspace", short_help="Workspace management")
@pass_environment
def cli(ctx):
    """Shows file changes in the current working directory."""
    ctx.log("Changed files: none")
    ctx.vlog("bla bla bla, debug info")
