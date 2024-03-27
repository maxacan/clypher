.. _encryptors:

Encryptors
==========

**Encryptors** provide the *encryption* and *decryption* functionality, along with any other behaviour needed by the encryption algorithm, such as key derivation and salt generation.

The ``BaseEncryptor`` class
---------------------------

All encryptors should subclass the ``BaseEncryptor`` class found in ``clypher.src.encryptors.base_encryptor.py``. It provides a very simple interface for the most common operations.

Attributes defined by the ``BaseEncryptor`` class
_________________________________________________

``password: bytes``

An ``utf-8`` encoded byte string. **This is the plaintext password** supplied by the user via the CLI.

As such, it may not meet the requirements of many encryption algorithms, and may only be used along with a Key Derivation Function to get a suitable passphrase.

Methods defined by the ``BaseEncryptor`` class
_________________________________________________

``encrypt(data: bytes) -> bytes``

Given ``data`` as ``bytes``, encrypt it and return the encrypted ``bytes``.

``decrypt(data: bytes) -> bytes``

Given ``data`` as ``bytes``, decrypt it and return the plaintext ``bytes``.
