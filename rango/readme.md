=====
rango
=====

rango is a simple Django app to show a website used bootstrap and a recommend website for
 studying django. For each site, visitors can search the domain.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'rango',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^rango/', include('rango.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a rango (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/rango/ to participate in the rango.