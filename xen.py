from xenlib.cli import cli
from colorama import Fore, Back, Style, init

if __name__ == '__main__':
    print(
        f"{Fore.YELLOW}"
        "######################################################\n"
        "## WARNING: You are currently running Xen Tools     ##\n"
        "##          from Xen Tool's source code directory!  ##\n"
        "######################################################\n"
    )
    cli()