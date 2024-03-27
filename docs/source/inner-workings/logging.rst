Logging
=======

Clypher uses Python's Logging module to add add log support.

When the app is first run, a ``logs`` folder will be created in the package directory.

The default logging behaviour stores logfiles using a ``RotatingFileHandler``, which splits logs in 4KB chunks.

The complete logging config can be found in ``clypher.src.logging_config.logger_config.py``.

The ``get_logger_or_debug()`` function
--------------------------------------

To allow for easier debugging, there is a ``debug`` logger, which logs any messages that are marked as ``DEBUG`` or higher.

However, this level of information might not be useful for day to day use, so the default logger level is set to ``INFO``.

When called, the ``get_logger_or_debug(name:str)`` function checks for the ``CLYPHER_DEBUG`` environment flag. If it's set to ``True``, the function returns the debug logger.

If the flag is ``False``, the function returns a normal logger that is instantiated using the ``name`` argument.

This function is normally called at the top of any files that want to use logging:

.. code-block:: python

    from src.logging_config.logger_config import get_logger_or_debug

    LOG = get_logger_or_debug(__name__)

