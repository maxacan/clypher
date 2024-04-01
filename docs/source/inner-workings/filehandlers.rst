File Handlers
=============

As their name implies, **File Handlers** deal with *file operations*. They manage reading input files and writing output files, along with dealing with naming and interpreting different file structures.

The ``BaseFileHandler`` class
-----------------------------

As with engines, File Handlers subclass the ``BaseFileHandler`` class found in ``clypher.src.file_handlers.base_filehandler.py``, which provides a simple interface for common operations, such as reading and writing files.

.. autoclass:: src.file_handlers.base_filehandler.BaseFileHandler


Adding new File Handlers
------------------------

While it is uncertain whether future versions might continue to work this way, right now, any File Handler that subclassess ``BaseFileHandler`` and  implements a ``request()`` and a ``write()`` method will be considered valid.

The only convention is for ``request()`` to return ``bytes``, how it achieves this is completely up to you. 


.. 
    #TODO: Change this once directory support is added


.. note:: 

    Version |version| doesn't support encrypting entire directories, however, this is a limitation of the default FileHandler used and not a limitation of the CLI. There should be nothing that prevents a FileHandler from adding directory support.

    **Directory support is a planned feature that will be implemented in future versions.**

