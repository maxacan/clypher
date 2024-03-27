Introduction to Clypher
=======================
**Clypher** is a small Python program that allows you to encrypt and decrypt files via a simple CLI interface.

.. note::
   
   This project is intended as a little personal project, and not as an actual secure solution for file encryption.

   If you're looking for a secure solution for storing sensitive files, look for other utilities, such as `VeraCrypt <https://www.veracrypt.fr/code/VeraCrypt/>`_.

   I cannot guarantee security, so only use this for low-security applications.

Getting Started
===============

Installation
------------
..
    _#TODO: Update this once the app is packaged

To use Clypher, first install it using **make**:

.. code-block:: console

    $ make install

Alternatively, you can install it using **pip**.

#. Navigate to the *project's root directory*. (Where ``setup.py`` is located.)

#. Install Clypher using **pip**:

.. code-block:: console

    $ pip install .

To check that everything went well, you can run the ``--version`` command.

.. code-block:: console

    $ python3 -m clypher version

This should output "Clypher v |version|". If it does, then the installation succeeded.


CLI Usage
---------

You interact with Clypher via command line arguments. If you've installed Clypher system-wide, you can just call it from the terminal:

.. code-block:: console

    $ clypher

Otherwise, call it as a python module:

.. code-block:: console 

    $ python3 -m clypher

To display a list of available arguments, run the ``--help`` command:

.. code-block:: console

    $ python3 -m clypher --help

This will display a list of all available commands, as well as a short description of each one.

You can get more information about a command, such as a detailed description and the arguments it takes, by adding ``--help`` after it:

.. code-block:: console

    $ python3 -m clypher enc --help

Specifying input files
++++++++++++++++++++++

Both the ``enc`` and ``dec`` commands can take one or more input files. Just pass them as arguments to said commands:

.. code-block:: console

    $ python3 -m clypher enc foo.txt

    $ python3 -m clypher dec foo.txt ./baz/bar.txt 


By default, Clypher ignores any duplicate input files. If the same file is passed as an input multiple times, it will only be processed once.


Specifying an output directory
++++++++++++++++++++++++++++++

By default, Clypher places any output files in the same directory as their source files. However, you can override this by using the ``--out`` option. Simply specify the desired output directory after the option, and Clypher will save all files to that directory:

.. code-block:: console

    $ python3 -m clypher foo.txt --out ./encrypted-foo/

.. 
    #TODO: Change this if/when multiple output directories are supported.

.. note:: 
    Specifying an ``--out`` directory will place **all** output files in that directory. As of version |version|, multiple output directories are not supported.

    If the output directory does not exist, or the program lacks write privileges, Clypher **will fail**.


Specifying a password
+++++++++++++++++++++

By default, Clypher will ask you to enter a password before encrypting or decrypting a file. 

You can pass a password as an argument by using the ``--pass`` option:

.. code-block:: console

    $ python3 -m clypher enc foo.txt --pass supersecretpassword1234

There are a few things to keep in mind about passwords:

.. 
    #TODO: Update this if/when multiple passwords are supported.

- When a password is specified, either by passing it as an argument or entering it when prompted by the program, **it is applied for all input files.** Currently, multiple passwords are not supported.
- As of version |version|, **Clypher does not enforce a specific password format**. You can use as many or as few characters as you want. As long as they are all printable ASCII characters, it *should* work.


Overwriting files
+++++++++++++++++

Clypher will throw an error if an output file already exists. To force the program to overwrite any conflicting files, simply pass the ``--fo`` option.

.. code-block:: console

    $ python3 -m clypher enc foo.txt --fo


Specifying an engine
++++++++++++++++++++

Clypher can use different *engines* to process files. To specify an engine, use the ``--engine`` option, followed by the name of the engine you want to use:

.. code-block:: console

    $ python3 -m clypher enc foo.txt --engine fernet


.. note:: 
    As of version |version|, the only available engine is the *FernetEngine*. It is used as the default engine.


You can learn more about engines in the :ref:`Engines` documentation.