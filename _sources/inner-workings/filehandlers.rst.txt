File Handlers
=============

As their name implies, **File Handlers** deal with *file operations*. They manage reading input files and writing output files, along with dealing with naming and interpreting different file structures.

The ``BaseFileHandler`` class
-----------------------------

As with engines, File Handlers subclass the ``BaseFileHandler`` class found in ``clypher.src.file_handlers.base_filehandler.py``, which provides a simple interface for common operations, such as reading and writing files.

.. autoclass:: file_handlers.base_filehandler.BaseFileHandler


Adding new File Handlers
------------------------

While it is uncertain whether future versions might continue to work this way, right now, any File Handler that subclassess ``BaseFileHandler`` and  implements a ``request()`` and a ``write()`` method will be considered valid.

The only convention is for ``request()`` to return ``bytes``, how it achieves this is completely up to you. 
