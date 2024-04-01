.. _encryptors:

Encryptors
==========

**Encryptors** provide the *encryption* and *decryption* functionality, along with any other behaviour needed by the encryption algorithm, such as key derivation and salt generation.

They are designed to be used by the different :ref:`Engines`. As such, these are not supposed to be instantiated manually.

The ``BaseEncryptor`` class
---------------------------

.. autoclass:: encryptors.base_encryptor.BaseEncryptor

All encryptors should subclass the ``BaseEncryptor`` class found in ``clypher.src.encryptors.base_encryptor.py``. It provides a very simple interface for the most common operations.