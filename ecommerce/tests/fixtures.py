import pytest

# Se debe poder crear un superuser de prueba para revisar con selenium el login
@pytest.fixture
def create_admin_user(django_user_model):
    """
    Return admin user
    """

    return django_user_model.objects.create_superuser("admintest", "admintest@correo.cl", "passwordtest")