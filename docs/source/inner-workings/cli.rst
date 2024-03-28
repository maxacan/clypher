The CLI
=======

The **Command Line Interface**, powered by `Typer <https://typer.tiangolo.com/>`_ and `Rich <https://github.com/Textualize/rich>`_, provides a very simple API for managing arguments and printing to the console.

When the app is invoked, the function associated with the specified argument is called. Both the ``enc`` and ``dec`` then functions read the arguments passed to the program.

If the ``--pass`` option is not used, the CLI will ask the user for a password.

Once the password is set, the CLI will try to import the engine needed for processing the files. If not explicitly set, the ``--engine`` option will default to ``fernet``.

..
    #TODO: update this once the CLI also provides an API

If the import succeeds, the CLI will create an instance of the imported engine and pass it all of the arguments that are deemed necessary.


The ``ConsoleManager``
----------------------

Clypher uses a ``ConsoleManager`` class that provides a bunch of static methods for printing common messages, such as warnings, errors, success messages, etc.

The ``ConsoleManager`` class found in the ``src.cli.managers.py`` file is a very thin wrapper of the Rich `Console API <https://rich.readthedocs.io/en/stable/console.html>`_.

.. py:method:: ConsoleManager.print_version_msg()

    Prints the current version message.

.. py:method:: ConsoleManager.print_banner()

    Prints the Clypher banner that appears on startup.

.. py:method:: ConsoleManager.error(msg: str, show_tag: bool = True, color_msg: bool = True)

    Prints ``msg`` and adds a red *[ERROR]* tag. **Prints to stderr**.

.. py:method:: ConsoleManager.warn(msg: str, show_tag: bool = True, color_msg: bool = True)

    Prints ``msg`` and adds a red *[WARNING]* tag.

.. py:method:: ConsoleManager.info(msg: str, show_tag: bool = True)

    Prints ``msg`` and adds a blue *[INFO]* tag.

.. py:method:: ConsoleManager.success(msg: str, show_tag: bool = True)

    Prints ``msg`` and adds a green *[SUCCESS]* tag.

.. py:method:: ConsoleManager.ask_password(mode: str = "encryption") -> str:

    Prompts the user for a password, depending on the ``mode``.

.. py:method:: ConsoleManager.prompt(msg: str, *args, **kwargs) -> str:

    Prompts the user, prints ``msg``. Passes ``*args`` and ``**kwargs`` to the ``Typer.prompt()`` function. 

.. py:method:: ConsoleManager.confirm(msg: str, *args, **kwargs) -> str:

    Prompts the user for confirmation, prints ``msg``. Passes ``*args`` and ``**kwargs`` to the ``Typer.prompt()`` function. 

The ``ProgressManager``
-----------------------

To display progress bars, Clypher uses Rich's `Progress <https://rich.readthedocs.io/en/stable/progress.html>`_ class.

To simplify its use, the ``ProgressManager`` class provides a single ``step()`` method, which advances the progress bar depending on how many files are left.

.. py:class:: ProgressManager(msg: str, total: int)

.. py:attribute:: progress: Progress

    The ``Progress`` instance. Used as a context manager.

    .. code-block::python

        with ProgressManager.progress:
            do_something()

.. py:attribute:: _task: TaskID

    The ``ProgressManager`` class assumes only one task will ever be performed per instance. ``_task`` is the ``TaskID`` returned by the ``Progress.add_task()`` method.

    It is only ever used internally.

.. py:method:: ProgressManager.step(msg: str | None = None)

    When called, this method updates ``_task`` and prints ``msg`` if specified.

.. note::

    An actual CLI implementation is being worked on. Nothing described in this page is final and will probably change in the near future.