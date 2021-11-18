

# WELCOME TO XEN Tools

## XEN Tools-beta in pip ``` pip install xen-tools

and run in your terminal

XEN Tools install

``` ## how to use

```bash git clone https://github.com/xentinel/xen-tools

pip install -r requirements.txt ```

### Migrate Database `bash python manage.py db init python manage.py db migrate python manage.py db upgrade python manage.py --help `

### Create New Module `bash python manage.py module create -n "module_name" ` `bash python manage.py module create -n "module_name" --remote "github_repo_url" `

### Runserver `bash python manage.py run `

## Docker Compose

### Setup `bash $ docker-compose up -d $ curl `

### Stop Services `bash $ docker-compose stop `

### Run And Play `bash $ docker-compose start `