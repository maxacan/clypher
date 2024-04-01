How Clypher Works
=================

Clypher consists of two main components; the **Command Line Interface (CLI)**, responsible for argument parsing and console output, and various **Encryption Engines**, which handle file operations, encryption/decryption and key derivation.

TL;DR
-------------

When Clypher is invoked, the CLI parses the arguments passed to it and calls the appropiate encryption or decryption functions of the specified engine. The engine then:

- Reads the input files into memory.
- Uses a `KDF <https://en.wikipedia.org/wiki/Key_derivation_function>`_ to derive a key from the selected password.
- Encrypts the file contents using said key and an encryption algorithm.
- Writes the output file to disk.
- Repeats until all files are processed.
