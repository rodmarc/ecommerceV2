import pytest
from django.contrib.auth.models import User
from django.core.management import call_command

# Se debe poder crear un superuser de prueba para revisar con selenium el login
@pytest.fixture
def create_admin_user(django_user_model):
    """
    Return admin user
    """

    return django_user_model.objects.create_superuser("admintest", "admintest@correo.cl", "passwordtest")


# Lo siguiente reemplaza a hacer el llamado desde el prompt:
# $ django-admin loaddata ./db_admin_fixture.json
@pytest.fixture(scope="session")
def db_fixture_setup(django_db_setup, django_db_blocker):
    """
    Load DB data fixtures
    """
    with django_db_blocker.unblock():
        call_command("loaddata", "db_admin_fixture.json")