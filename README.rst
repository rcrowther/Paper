Paper
=======
A basic model and views. 

For tutorial, reference and demo purpose. Has little code-builder interest. Includes Admin, Django, and quickviews implementations of Create, Update, Delete, List, and Detail views. All available when installed.


Optional support modules
------------------------
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
    ...
    url(r'^paper/', include('paper.urls')),
		]

Migrate, ::

    $ python manage.py makemigrations
    $ python manage.py migrate

or, if this a demo, and you need a working table, and don't care about replication or construction security, ::

    $ python manage.py migrate --run-syncdb


Loading data
++++++++++++
Some data is available to populate the db table, ::

    python manage.py paper_load DutchPainters



The Model
---------
Is vaugely based in Drupal's 'node'. Before Drupal, to use Guido van Rossum's word, 'hyper-abstracted'. It's a body text with a title, summary, dates, and author fields.


Use as demo Model
-----------------
The views of the Paper Model are extensive. They should all work after install.

If you have admin enabled and access, Admin is builtin, ::

    http://127.0.0.1:8000/admin/paper/paper/
    # etc.
    
If you do not have admin access, or wish to demonstrate Django's generic form views on a model, the app has the code and templates. Bear in mind that this is a demo app, so the output is the simplest form of HTML, and no CSS has been applied, ::
 
    http://127.0.0.1:8000/paper/add/
    http://127.0.0.1:8000/paper/23/edit/
    http://127.0.0.1:8000/paper/23/delete/

To view a single model (DetailView), ::

    http://127.0.0.1:8000/paper/23/

To view a list of model data, ::
        
    http://127.0.0.1:8000/paper/

The app also has a set of views which will appear if the quickviews app is installed. Unlike Admin, these views are intended for the general user. Unlike Django generic views, they render with preset templates and CSS. Which is either a relief, or a shocking undermining of Django flexibility, depends on your needs, ::

    http://127.0.0.1:8000/paper/qv/add/
    http://127.0.0.1:8000/paper/qv/23/edit/
    http://127.0.0.1:8000/paper/qv/23/delete/ 
    http://127.0.0.1:8000/paper/qv/23/
    http://127.0.0.1:8000/paper/qv
    
After you are done with Paper, it can be easily uninstalled, see above.


Thoughts
--------
Django documentation does not describe anywhere how to enable Model-based CUD forms. No, I don't care what you say, it does not. So the code in this app may be of help.  

If you don't do Django all the time, Quickviews is a raft for crossing the pain of Django forms. And everyone needs forms. Go compare.

This is the base of a classic CMS. I'm laughing, if you are not.

 
.. _Quickviews: https://github.com/rcrowther/quickviews
