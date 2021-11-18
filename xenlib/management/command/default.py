from xenlib.cli import pass_environment
import click


@click.command("run", short_help="Run project")
@pass_environment
def run(ctx):
    """Shows file changes in the current working directory."""
    ctx.log("Run project", ctx.project_name)
    ctx.vlog("bla bla bla, debug info")

@click.command("commit", short_help="Commit project")
@pass_environment
def commit(ctx):
    """Shows file changes in the current working directory."""
    ctx.log("Commit project", ctx.project_name)
