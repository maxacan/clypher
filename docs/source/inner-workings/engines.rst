.. _engines:

Engines
=======

Engines provide the core functionality of Clypher. They act as a mediator between a **File Handler** class and an **Encryptor** class.

The ``BaseEngine`` class
------------------------

All engines should subclass the ``BaseEngine`` class defined in ``clypher.src.engines.base_engine.py``, as it provides a set of base methods and attributes needed for instantiating and working with File Handlers and Encryptors.

Attributes defined by the ``BaseEngine`` class
______________________________________________

``password: str``

The password used for key derivation.

``infiles: list[pathlib.Path]``

The list of input files.

``output: Path``

If specified, the directory in which output files are going to be stored.

``force_ow: bool``

If ``True``, force overwriting of output files.

Methods defined by the ``BaseEngine`` class
___________________________________________

``start_encryption()``

``start_decryption()``

Both start the processing of input files. Once all input files have been processed, the program stops.

How an Engine operates
----------------------

Engines instantiate both a **File Handler** and an **Encryptor** instance, passing any arguments that they might require. 

When you call any of the *start methods* outlined above, the Engine class will execute the following three base steps:

- **Request a new file from its FileHandler instance:** This results in a file getting popped from its queue, read and returned as ``bytes``.
- **Send the returned bytes to its Encryptor instance:** The Encryptor will then encrypt or decrypt the file, and return the result as ``bytes``.
- **Send the bytes back to the FileHandler instance:** The FileHandler will write the output file and prepare the next file in the queue.

.. 
    #TODO: update this once the api is actually done
    #TODO: add docs on how to create a new engine and make it available

Occasionally, the Engine will send messages to the console using the CLI API.

How Engines get imported
---------------------------

Clypher was designed to enable easy integration of new engines, allowing for a nearly drag-and-drop experience.

Because the program allows for choosing an engine at runtime, importing all available engines results in, potentially, lots of unnecesary code being loaded. A simple on-the-fly import system was implemented to help mitigate this.

The ``engines`` module houses all available engines, along with the ``INSTALLED_ENGINES`` constant located in ``__init__.py``. Here is a quick look at its contents: 

.. code-block:: python

    INSTALLED_ENGINES = {
        "fernet": "src.engines.fernet_engine.FernetEngine",
        ...
    }


The keys in the dictionary represent the command line name of the engine that the user passes to the ``--engine`` option in the CLI. The values represent the path to the actual engine class.

When the CLI parses the ``--engine`` option, its value is passed to the ``import_engine()`` function located in the ``clypher.src.import_handler.import_handler.py`` file.

.. code-block:: python

    def import_engine(engine:str, engine_list: dict = INSTALLED_ENGINES):
        ...

This function looks up the value of the ``engine`` key in the ``engine_list`` dictionary. If the corresponding value is found, it is then parsed and the module name is sent to the ``importlib`` module, which tries to import it.

If the import succeeds, a simple ``getattr()`` call is made to get the actual engine class. If the call succeeds, the engine class is returned.

If something fails, such as a missing engine class or an engine that doesn't exist is supplied, the ``import_engine`` function raises the appropiate exception and Clypher exits.

Creating new engines
--------------------

Once you've programmed your new engine, installing it is as easy as adding an entry to the ``INSTALLED_ENGINES`` dictionary.

.. code-block:: python

    INSTALLED_ENGINES = {
        "fernet": "src.engines.fernet_engine.FernetEngine",
        "new_engine": "src.engines.new_engine.NewEngine",
    }

.. warning:: 

    Because ``importlib`` is used to import the engine, the value of the new entry **must be a valid Python module**. Otherwise, importing it might fail.

    Also, engine names **CANNOT** have words separated by whitespace, as the CLI will interpret them as different arguments.

Once installed, it can be used via the CLI:

.. code-block:: console

    $ python3 -m clypher enc foo.txt --engine new_engine