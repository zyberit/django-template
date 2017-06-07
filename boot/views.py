

from django.http import HttpResponse

from django.contrib.auth.models import User



""" Boostrap views
Still probably not quite correct
"""

from django.db import DEFAULT_DB_ALIAS, connections
from django.db.migrations.executor import MigrationExecutor
def get_remaining_migrations():
    connection = connections[DEFAULT_DB_ALIAS]
    connection.prepare_database()
    executor = MigrationExecutor(connection)
    targets = executor.loader.graph.leaf_nodes()
    migrations= executor.migration_plan(targets)
    return migrations 

from django.core.management.commands.migrate import Command
def migrate():
    migrate = Command()
    options={'verbosity': 0, 'no_color': False, 'fake': False, 'database': 'default', 'settings': None, 'pythonpath': None, 'fake_initial': False, 'traceback': False, 'interactive': False, 'app_label': None, 'migration_name': None, 'run_syncdb': False}
    args = tuple()
    migrate.handle(*args, **options)

def createsuperuser(username,password):
    admin,created = User.objects.get_or_create(username=username)
    if created:
        admin.set_password(password)
        admin.is_staff = True
        admin.is_superuser = True
        admin.save()

def bootstrap(request):
    if get_remaining_migrations() != 0:
        migrate()
    createsuperuser("admin","GarBo66!")
    return HttpResponse("Done!")


""" Ping view
"""

def ping(request):
    return HttpResponse(str(len(get_remaining_migrations())))
