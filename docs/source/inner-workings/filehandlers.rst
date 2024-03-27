File Handlers
=============

As their name implies, **File Handlers** deal with *file operations*. They manage reading input files and writing output files, along with dealing with naming and interpreting different file structures.

.. 
    #TODO: Add docs when a base file handler is implemented.

The ``BaseFileHandler`` class
-----------------------------

As with engines, File Handlers subclass the ``BaseFileHandler`` class found in ``clypher.src.file_handlers.base_filehandler.py``, which provides a simple interface for common operations, such as reading and writing files.

Attributes defined by the ``BaseFileHandler`` class
___________________________________________________

``file_list: list[pathlib.Path]``

The list of input files.

``out: pathlib.Path | None``

The output directory.

``force_ow: bool``

Force overwriting of output files.

``decrypting: bool``

Selects the working mode of the handler, as encrypting and decrypting might need different read/write behaviours.


Methods defined by the ``BaseFileHandler`` class
________________________________________________

``request() -> bytes | None``

Read the next file and return it as ``bytes``. If no more files are available, return ``None``.

``write(data: bytes) -> int``

Take ``data`` and write it to its corresponding output file. Return the number of bytes written as reported by the ``io.TextIOBase.write()`` method from the Python Standard Library.

Adding new File Handlers
------------------------

While it is uncertain whether future versions might continue to work this way, right now, any File Handler that subclassess ``BaseFileHandler`` and  implements a ``request()`` and a ``write()`` method will be considered valid.

The only convention is for ``request()`` to return ``bytes``, how it achieves this is completely up to you. 


.. 
    #TODO: Change this once directory support is added


.. note:: 

    Version |version| doesn't support encrypting entire directories, however, this is a limitation of the default FileHandler used and not a limitation of the CLI. There should be nothing that prevents a FileHandler from adding directory support.

    **Directory support is a planned feature that will be implemented in future versions.**

