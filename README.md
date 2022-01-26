# Ecommerce V2

Este proyecto está basado en un curso para generar un ecommerce usando django.
Esta es la versión 2 de ese curso (6 videos).

El primer video muestra en realidad consideraciones conceptuales para la base de datos,
que pueden saltarse.
El segundo video de la lista ya comienza efectivamente los pasos para crear el proyecto.

Video incial:
<https://www.youtube.com/watch?v=EbLEyM9SyZQ&list=PLOLrQ9Pn6cay_cQkyg-WYYiJ_EKU8KWKh&index=2>

Segundo video:
<https://www.youtube.com/watch?v=s3HuIRD5sUY&list=PLOLrQ9Pn6cay_cQkyg-WYYiJ_EKU8KWKh&index=2>

## Generación del proyecto

1. Si se quiere crear un ambiente de instalación local al proyecto (Opcional)

```
$ py -m venv venv
$ source venv/bin/activate
$ pip install django
```

2. Para crear el proyecto


```
 $ django-admin startproject ecommerce .
```

3. Para crear el ambiente de tests. En este caso el framework "pytest"


```
 $ pip install pytest
```

4. Luego en https://pypi.org se busca pytest django y se instala la version pytest-django 4.4.0 de Jun 6, 2021 (o alguna más nueva si es que hay)


```
 $ pip install pytest-django
```

5. Luego se busca pytest-factoryboy y se baja. Provee un set de herramientas para crear datos automaticamente/dinamicamente para probar nuestro sistema.

```
 $ pip install pytest-factoryboy
```

6. Luego se busca pytest-selenium y se baja.

```
 $ pip install pytest-selenium
```

7. Luego se congela la lista de paquetes instalados

```
 $ pip freeze > requirements.txt
```

8. Instalar mysqlclient
```
$ pip install mysqlclient
```
Según el artículo https://sebhastian.com/failed-building-wheel-mysql-python/ si falla el building de wheel,
pero de todas maneras se instala mysqlclient (por ejemplo "Successfully installed mysqlclient-2.1.0"), no debería haber problemas.

Otra forma según https://stackoverflow.com/questions/66851598/error-while-installing-mysqlclient-in-django-project-on-cpanel sería
instalando en su lugar mysql-connector-python. 
Sin embargo, según https://qastack.mx/programming/43102442/whats-the-difference-between-mysqldb-mysqlclient-and-mysql-connector-python,
mysqlclient es hasta 10 veces más rápido.



9. Se crea la aplicacion dashboard dentro de la carpeta ecommerce.
```
$ django-admin startapp dashboard
```


Se borra el archivo test.py y se cambia por un directorio llamado tests. Para que el directorio sea encontrable debe crearse adentro
un archivo llamado 
```
__init__.py
```

10. Crear archivo pytest.ini en la raiz del proyecto

11. Crear archivo conftest.py en la raiz del proyecto. Sirve para configurar cosas antes de correr cualquier test

12. Bajar el driver de selenium para las pruebas desde https://chromedriver.chromium.org. Buscar según la versión de Chrome que tengamos.
Luego poner el driver en la carpeta raíz del proyecto

13. Crear una carpeta tests dentro de "ecommerce" y dentro crear un archivo llamado selenium.py para los seteos de los tests y otro archivo llamado
fixtures.py. Ambos luego se configuran dentro de conftest.py para su uso.

```
$ cat conftest.py

pytest_plugins = [
    "ecommerce.tests.fixtures", # Esto procesa archivo ecommerce/tests/fixtures.py
    "ecommerce.tests.selenium", # Esto procesa archivo ecommerce/tests/selenium.py
]
```


14. Se configura la base de datos en settings.py
Adicionalmente si la base de mysql se llama xyz, al usuario se le debe dar permisos
sobre la base de datos test_xyz para hacer tests (OJO: nombres de usuarios y claves son solo ejemplos y deben cambiarse y no escribirse aquí)
```
mysql> CREATE USER 'ecommercev2_username'@'localhost' IDENTIFIED BY 'ecommercev2_userpassword';
mysql> GRANT ALL PRIVILEGES ON ecommercev2_db.* TO 'ecommercev2_username'@'localhost';
mysql> GRANT ALL PRIVILEGES ON test_ecommercev2_db.* TO 'ecommercev2_username'@'localhost';
mysql> CREATE DATABASE ecommercev2_db;
```
15. Se genera las migraciones y se migra a la base de datos (previamente se debe crear la base de datos)
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

16. Se crea un super usuario
```
$ python3 manage.py createsuperuser       # admin/admin@correo.cl/admin12345
```

17. Se puede hacer tests con pytest