The FernetEngine
================

The ``FernetEngine`` is the default engine that ships with Clypher. It uses the ``Fernet`` implementation found in the `cryptography <https://cryptography.io/en/latest/>`_ package.



The ``FernetEncryptor``
-----------------------

As previously stated, the engine is based around **Fernet** for the symmetric encryption and uses `Scrypt <https://cryptography.io/en/latest/hazmat/primitives/key-derivation-functions/#scrypt>`_ for deriving a key from the password specified by the user.

Every time the ``encrypt()`` method is called, a new key is derived using a 16 byte-long salt coming from ``os.urandom()``. This key is then used to instantiate a Fernet instance.

Generating a new key every time is slow, but should prevent multiple files from sharing the same encryption key.

When saving a file, the generated salt is appended to the start of the resulting bytes. This is necessary to allow for file decryption, as Scrypt will generate a different key if the salt is not the same, even if the password is correct.

Every time the ``decrypt()`` method is called, the stored salt is read from the input file and used to generate the key used to instantiate **Fernet**.

The ``FileHandler``
-------------------

The ``FernetEngine`` uses the default file handler. It appends the ``.clypher`` file extension to any encrypted files, and removes it when decrypting them.

