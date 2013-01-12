Simple favorites system for django
-----------------------------------

- Add ``url(r'^favorites/', include('favorites.urls')),`` to your project urls
- Add ``"demo.demo_app.context_processors.show_data",`` to your ``TEMPLATE_CONTEXT_PROCESSORS``
- Add ``favorites`` to your ``INSTALLED_APPS`` in your settings.py file


Template use
------------
- load ``favorite_tags`` in your template E.g: ``{% load favorite_tags %}``
- Check if favorited: ``{{ user|check_favorite:topic }}`` You can throw conditions against this.
- Favorite an object: ``{{user|favorite_object:topic}}`` This will generate a link to the add page (add ?json=True to return JSON)

