The CLI
=======

The **Command Line Interface**, powered by `Typer <https://typer.tiangolo.com/>`_ and `Rich <https://github.com/Textualize/rich>`_, provides a very simple API for managing arguments and printing to the console.

When the app is invoked, the function associated with the specified argument is called. Both the ``enc`` and ``dec`` then functions read the arguments passed to the program.

If the ``--pass`` option is not used, the CLI will ask the user for a password.

Once the password is set, the CLI will try to import the engine needed for processing the files. If not explicitly set, the ``--engine`` option will default to ``fernet``.

..
    #TODO: update this once the CLI also provides an API

If the import succeeds, the CLI will create an instance of the imported engine and pass it all of the arguments that are deemed necessary.


.. note::

    An actual CLI implementation is being worked on. Nothing described in this page is final and will probably change in the near future.