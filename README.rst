Paper
=======
A basic model and views. 

Here for reference and demo purpose. Has little general interest. Includes both Admin and general user views for CRUD, List and Detail views. 


Requirements
--------------
Quickviews_

Uninstall
---------
The wise app is humble, ::

    python manage.py paper_uninstall -h
    
Install
-------



In settings.py, ::

	INSTALLED_APPS = [
		...
		'paper.apps.PaperConfig',
		]

In (site) url.py, ::

	urlpatterns = [
		path('paper/', include('paper.urls')),
		]

Migrate, ::

    > python manage.py makemigrations
    > python manage.py migrate




.. _Quickviews: https://github.com/rcrowther/quickviews
