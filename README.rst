Simple favorites system for django
-----------------------------------

- Add ``url(r'^favorites/', include('favorites.urls')),`` to your project urls (see demo project)
- Add ``favorites`` to your ``INSTALLED_APPS`` in your settings.py file
- Copy context_processors or add the code to your current projects context_processors
- Append to your projects ``TEMPLATE_CONTEXT_PROCESSORS`` settings.py file the following: ``project.project_app.context_processors``

See demo project for more info


Template use
------------
- load ``favorite_tags`` in your template E.g: ``{% load favorite_tags %}``
- Check if favorited: ``{{ user|check_favorite:topic }}`` You can throw conditions against this.
- Favorite an object: ``{{ user|favorite_object:topic }}`` This will generate a link to the add page (add ?json=True to return JSON)

