import os
import sys
import click 
from dotenv import load_dotenv
from colorama import Fore, Back, Style, init

def find_config(file_name = ".env"):
    cur_dir = os.getcwd() # Dir from where search starts can be replaced with any path
    
    while True:
        file_list = os.listdir(cur_dir)
        parent_dir = os.path.dirname(cur_dir)
        if file_name in file_list:
            return os.path.join(cur_dir, file_name)
        else:
            if cur_dir == parent_dir: #if dir is root dir
                return False
            else:
                cur_dir = parent_dir

class Environment:
    def __init__(self):
        self.verbose = False
        self.home = os.getcwd()
        self.load_env()
        init(convert=True, autoreset=True)
    
    def load_env(self):
        env_file = find_config(".env-xen")
        if env_file:
            load_dotenv(env_file)
        self.project_name = os.getenv("PROJECT_NAME")

    def get_env(self, key):
        self.project_name = "laravel"
        return self.project_name

    def log(self, msg, *args):
        """Logs a message to stderr."""
        if args:
            msg %= args
        click.echo("[{}{}{}] {}".format(Style.BRIGHT+Fore.YELLOW, self.project_name, Style.RESET_ALL, msg), file=sys.stderr)

    def vlog(self, msg, *args):
        """Logs a message to stderr only if verbose is enabled."""
        if self.verbose:
            self.log(msg, *args)
