Search.setIndex({"docnames": ["concrete-implementations/fernetengine", "index", "inner-workings/cli", "inner-workings/encryptors", "inner-workings/engines", "inner-workings/filehandlers", "inner-workings/logging", "inner-workings/tldr", "intro/introduction"], "filenames": ["concrete-implementations/fernetengine.rst", "index.rst", "inner-workings/cli.rst", "inner-workings/encryptors.rst", "inner-workings/engines.rst", "inner-workings/filehandlers.rst", "inner-workings/logging.rst", "inner-workings/tldr.rst", "intro/introduction.rst"], "titles": ["The FernetEngine", "Welcome to Clypher\u2019s documentation!", "The CLI", "Encryptors", "Engines", "File Handlers", "Logging", "How Clypher Works", "Introduction to Clypher"], "terms": {"i": [0, 2, 4, 5, 6, 7, 8], "default": [0, 2, 5, 6, 8], "engin": [0, 1, 2, 3, 5, 7], "ship": 0, "clypher": [0, 2, 3, 4, 5, 6], "It": [0, 3, 8], "us": [0, 2, 3, 4, 6, 7, 8], "fernet": [0, 2, 4, 8], "implement": [0, 2, 3, 4, 5], "found": [0, 2, 3, 4, 5, 6], "cryptographi": 0, "packag": [0, 6, 8], "As": [0, 3, 5, 8], "previous": 0, "state": 0, "base": [0, 4, 5], "around": 0, "symmetr": 0, "encrypt": [0, 1, 3, 4, 7, 8], "scrypt": 0, "deriv": [0, 3, 7], "kei": [0, 3, 4, 7], "from": [0, 4, 5, 6, 7, 8], "password": [0, 1, 2, 3, 4, 7], "specifi": [0, 1, 2, 7], "user": [0, 2, 3, 4], "everi": [0, 5, 8], "time": [0, 8], "method": [0, 2, 4, 5], "call": [0, 2, 4, 6, 7, 8], "new": [0, 1, 8], "16": 0, "byte": [0, 3, 4, 5], "long": [0, 8], "salt": [0, 3], "come": [0, 5], "o": 0, "urandom": 0, "thi": [0, 2, 4, 5, 6, 8], "instanti": [0, 3, 4, 6], "instanc": [0, 2, 4], "gener": [0, 3], "slow": 0, "should": [0, 3, 4, 8], "prevent": 0, "multipl": [0, 8], "file": [0, 1, 2, 4, 6, 7], "share": 0, "same": [0, 8], "when": [0, 2, 4, 6, 7, 8], "save": [0, 8], "append": 0, "start": [0, 1, 4], "result": [0, 4], "necessari": [0, 2], "allow": [0, 4, 6, 8], "decrypt": [0, 1, 3, 4, 7, 8], "differ": [0, 3, 4, 5, 8], "even": 0, "correct": 0, "store": [0, 6, 8], "read": [0, 2, 4, 5, 7], "input": [0, 1, 4, 5, 7], "handler": [0, 1, 4], "extens": 0, "ani": [0, 3, 4, 5, 6, 8], "remov": 0, "them": [0, 4, 5, 8], "introduct": 1, "get": 1, "instal": [1, 4], "cli": [1, 4, 5, 7], "usag": 1, "recurs": [1, 5], "ad": [1, 4], "an": [1, 2, 5, 7], "output": [1, 4, 5, 7], "directori": [1, 4, 5, 6], "overwrit": [1, 4, 5], "how": [1, 2, 5], "tl": 1, "dr": 1, "The": [1, 7], "consolemanag": 1, "progressmanag": 1, "baseengin": 1, "class": [1, 2], "plaintext_password": [1, 4], "infil": [1, 4], "force_ow": [1, 4, 5], "start_encrypt": [1, 4], "start_decrypt": [1, 4], "oper": [1, 3, 5, 7], "import": [1, 2, 6], "creat": [1, 2, 3, 6, 8], "basefilehandl": 1, "file_list": [1, 5], "out": [1, 5, 8], "list_fil": [1, 5], "request": [1, 4, 5], "write": [1, 4, 5, 7, 8], "encryptor": [1, 4], "baseencryptor": 1, "log": 1, "get_logger_or_debug": 1, "function": [1, 2, 3, 4, 7], "fernetengin": [1, 4, 8], "fernetencryptor": 1, "filehandl": [1, 4], "command": [2, 4, 7, 8], "line": [2, 4, 7, 8], "interfac": [2, 3, 5, 7, 8], "power": 2, "typer": 2, "rich": 2, "provid": [2, 3, 4, 5], "veri": [2, 3], "simpl": [2, 3, 4, 5, 8], "api": [2, 4], "manag": [2, 5], "argument": [2, 4, 6, 7, 8], "print": 2, "consol": [2, 4, 7], "app": [2, 6], "invok": [2, 7], "associ": 2, "both": [2, 4, 8], "enc": [2, 4, 8], "dec": [2, 8], "pass": [2, 4, 7, 8], "program": [2, 4, 8], "If": [2, 4, 5, 6, 8], "option": [2, 4, 5, 8], "ask": [2, 8], "onc": [2, 4, 8], "set": [2, 4, 6], "try": 2, "need": [2, 3, 4], "process": [2, 5, 7, 8], "explicitli": 2, "succe": [2, 4], "all": [2, 3, 4, 5, 7, 8], "ar": [2, 3, 6, 7, 8], "deem": 2, "bunch": 2, "static": 2, "common": [2, 3, 5], "messag": [2, 4, 6], "warn": 2, "error": [2, 8], "success": 2, "etc": 2, "src": [2, 3, 4, 5, 6], "py": [2, 3, 4, 5, 6], "thin": 2, "wrapper": 2, "To": [2, 6, 8], "displai": [2, 8], "progress": 2, "bar": 2, "": [2, 6, 8], "simplifi": 2, "its": [2, 4, 5], "singl": [2, 8], "step": [2, 4], "which": [2, 4, 5, 6, 7], "advanc": 2, "depend": 2, "mani": [2, 8], "left": 2, "actual": [2, 4, 8], "being": [2, 4], "work": [2, 4, 5, 8], "noth": 2, "describ": 2, "page": 2, "final": 2, "probabl": 2, "chang": 2, "futur": [2, 5], "along": [3, 4, 5, 8], "other": [3, 8], "behaviour": [3, 6], "algorithm": [3, 7], "thei": [3, 4, 5, 8], "design": [3, 4], "suppos": 3, "manual": 3, "base_encryptor": 3, "concret": [3, 4, 5], "paramet": [3, 4, 5], "plaintext": [3, 4], "abstract": [3, 4, 5], "given": [3, 5], "data": 3, "must": [3, 4, 5], "subclass": [3, 4, 5], "most": 3, "core": 4, "act": 4, "mediat": 4, "between": 4, "base_engin": 4, "arg": 4, "kwarg": 4, "A": [4, 5], "str": [4, 6], "list": [4, 5, 8], "path": [4, 5], "bool": [4, 5], "forc": [4, 5, 8], "alreadi": [4, 8], "exist": [4, 5, 8], "defin": 4, "attribut": 4, "might": [4, 5, 6], "requir": 4, "you": [4, 5, 8], "outlin": 4, "abov": 4, "execut": 4, "follow": [4, 8], "three": 4, "pop": 4, "queue": 4, "return": [4, 5, 6], "send": 4, "back": 4, "prepar": 4, "next": [4, 5], "occasion": 4, "wa": 4, "enabl": 4, "easi": 4, "integr": 4, "nearli": 4, "drag": 4, "drop": 4, "experi": 4, "becaus": 4, "choos": 4, "runtim": 4, "avail": [4, 8], "potenti": 4, "lot": 4, "unnecesari": 4, "code": 4, "load": 4, "fly": 4, "system": [4, 8], "help": [4, 8], "mitig": 4, "modul": [4, 6], "hous": 4, "installed_engin": 4, "constant": 4, "locat": [4, 8], "__init__": 4, "here": 4, "quick": 4, "look": [4, 8], "content": [4, 7], "fernet_engin": 4, "dictionari": 4, "repres": 4, "name": [4, 5, 6, 8], "valu": 4, "pars": [4, 7], "import_engin": 4, "import_handl": 4, "up": [4, 5], "engine_list": 4, "correspond": 4, "sent": 4, "importlib": 4, "tri": 4, "getattr": 4, "made": 4, "someth": 4, "fail": [4, 8], "miss": 4, "doesn": [4, 5], "t": [4, 5], "suppli": 4, "rais": [4, 5], "appropi": [4, 7], "except": 4, "exit": 4, "ve": [4, 8], "your": 4, "entri": [4, 5], "new_engin": 4, "newengin": 4, "valid": [4, 5], "python": [4, 6, 8], "otherwis": 4, "also": [4, 5], "cannot": [4, 8], "have": 4, "word": 4, "separ": 4, "whitespac": 4, "interpret": [4, 5], "can": [4, 5, 6, 8], "via": [4, 8], "python3": [4, 8], "m": [4, 8], "foo": [4, 5, 8], "txt": [4, 8], "impli": 5, "deal": 5, "structur": [5, 8], "file_handl": 5, "base_filehandl": 5, "output_dir": 5, "none": 5, "force_overwrit": 5, "fals": [5, 6], "resolv": 5, "convert": 5, "absolut": 5, "walk": [5, 8], "abl": 5, "rel": 5, "current": [5, 8], "dir": 5, "true": [5, 6], "filenotfounderror": 5, "valueerror": 5, "type": 5, "while": 5, "uncertain": 5, "whether": 5, "version": [5, 8], "continu": 5, "wai": 5, "right": 5, "now": 5, "subclassess": 5, "consid": 5, "onli": [5, 8], "convent": 5, "achiev": 5, "complet": [5, 6], "add": 6, "support": [6, 8], "first": [6, 8], "run": [6, 8], "folder": 6, "logfil": 6, "rotatingfilehandl": 6, "split": 6, "4kb": 6, "chunk": 6, "config": 6, "logging_config": 6, "logger_config": 6, "easier": 6, "debug": 6, "logger": 6, "mark": 6, "higher": 6, "howev": [6, 8], "level": 6, "inform": [6, 8], "dai": 6, "so": [6, 8], "info": 6, "check": [6, 8], "clypher_debug": 6, "environ": 6, "flag": 6, "normal": 6, "top": 6, "want": [6, 8], "__name__": 6, "consist": 7, "two": 7, "main": 7, "compon": 7, "respons": 7, "variou": 7, "handl": 7, "memori": 7, "kdf": 7, "select": 7, "said": [7, 8], "disk": 7, "repeat": 7, "until": 7, "small": 8, "project": 8, "intend": 8, "littl": 8, "person": 8, "secur": 8, "solut": 8, "re": 8, "sensit": 8, "util": 8, "veracrypt": 8, "guarante": 8, "low": 8, "applic": 8, "pip": 8, "altern": 8, "edit": 8, "mode": 8, "e": 8, "navig": 8, "root": 8, "where": 8, "proyect": 8, "toml": 8, "everyth": 8, "went": 8, "well": 8, "v": 8, "0": 8, "4": 8, "doe": 8, "succeed": 8, "interact": 8, "wide": 8, "just": 8, "termin": 8, "short": 8, "descript": 8, "each": 8, "one": 8, "more": 8, "about": 8, "detail": 8, "take": 8, "after": 8, "baz": 8, "By": 8, "ignor": 8, "duplic": 8, "caution": 8, "recommend": 8, "place": 8, "sourc": 8, "overrid": 8, "simpli": 8, "desir": 8, "subfold": 8, "lack": 8, "privileg": 8, "enter": 8, "befor": 8, "supersecretpassword1234": 8, "There": 8, "few": 8, "thing": 8, "keep": 8, "mind": 8, "either": 8, "prompt": 8, "appli": 8, "enforc": 8, "specif": 8, "format": 8, "charact": 8, "printabl": 8, "ascii": 8, "throw": 8, "conflict": 8, "fo": 8, "learn": 8, "document": 8}, "objects": {"encryptors.base_encryptor": [[3, 0, 1, "", "BaseEncryptor"]], "encryptors.base_encryptor.BaseEncryptor": [[3, 1, 1, "", "decrypt"], [3, 1, 1, "", "encrypt"], [3, 2, 1, "", "password"]], "engines.base_engine": [[4, 0, 1, "", "BaseEngine"]], "engines.base_engine.BaseEngine": [[4, 2, 1, "", "force_ow"], [4, 2, 1, "", "infiles"], [4, 2, 1, "", "output"], [4, 2, 1, "", "plaintext_password"], [4, 1, 1, "", "start_decryption"], [4, 1, 1, "", "start_encryption"]], "file_handlers.base_filehandler": [[5, 0, 1, "", "BaseFileHandler"]], "file_handlers.base_filehandler.BaseFileHandler": [[5, 2, 1, "", "file_list"], [5, 2, 1, "", "force_ow"], [5, 1, 1, "", "list_files"], [5, 2, 1, "", "out"], [5, 1, 1, "", "request"], [5, 1, 1, "", "write"]]}, "objtypes": {"0": "py:class", "1": "py:method", "2": "py:attribute"}, "objnames": {"0": ["py", "class", "Python class"], "1": ["py", "method", "Python method"], "2": ["py", "attribute", "Python attribute"]}, "titleterms": {"The": [0, 2, 3, 4, 5, 6], "fernetengin": 0, "fernetencryptor": 0, "filehandl": 0, "welcom": 1, "clypher": [1, 7, 8], "": 1, "document": 1, "quick": 1, "summari": 1, "inner": 1, "work": [1, 7], "concret": 1, "implement": 1, "cli": [2, 8], "consolemanag": 2, "progressmanag": 2, "encryptor": 3, "baseencryptor": 3, "class": [3, 4, 5], "engin": [4, 8], "baseengin": 4, "how": [4, 7], "an": [4, 8], "oper": 4, "get": [4, 8], "import": 4, "creat": 4, "new": [4, 5], "file": [5, 8], "handler": 5, "basefilehandl": 5, "ad": [5, 8], "log": 6, "get_logger_or_debug": 6, "function": 6, "tl": 7, "dr": 7, "introduct": 8, "start": 8, "instal": 8, "usag": 8, "specifi": 8, "input": 8, "recurs": 8, "output": 8, "directori": 8, "password": 8, "overwrit": 8}, "envversion": {"sphinx.domains.c": 3, "sphinx.domains.changeset": 1, "sphinx.domains.citation": 1, "sphinx.domains.cpp": 9, "sphinx.domains.index": 1, "sphinx.domains.javascript": 3, "sphinx.domains.math": 2, "sphinx.domains.python": 4, "sphinx.domains.rst": 2, "sphinx.domains.std": 2, "sphinx": 60}, "alltitles": {"The FernetEngine": [[0, "the-fernetengine"]], "The FernetEncryptor": [[0, "the-fernetencryptor"]], "The FileHandler": [[0, "the-filehandler"]], "Welcome to Clypher\u2019s documentation!": [[1, "welcome-to-clypher-s-documentation"]], "Quick Summary": [[1, null]], "Inner Workings": [[1, null]], "Concrete Implementations": [[1, null]], "The CLI": [[2, "the-cli"]], "The ConsoleManager": [[2, "the-consolemanager"]], "The ProgressManager": [[2, "the-progressmanager"]], "Encryptors": [[3, "encryptors"]], "The BaseEncryptor class": [[3, "the-baseencryptor-class"]], "Engines": [[4, "engines"]], "The BaseEngine class": [[4, "the-baseengine-class"]], "How an Engine operates": [[4, "how-an-engine-operates"]], "How Engines get imported": [[4, "how-engines-get-imported"]], "Creating new engines": [[4, "creating-new-engines"]], "File Handlers": [[5, "file-handlers"]], "The BaseFileHandler class": [[5, "the-basefilehandler-class"]], "Adding new File Handlers": [[5, "adding-new-file-handlers"]], "Logging": [[6, "logging"]], "The get_logger_or_debug() function": [[6, "the-get-logger-or-debug-function"]], "How Clypher Works": [[7, "how-clypher-works"]], "TL;DR": [[7, "tl-dr"]], "Introduction to Clypher": [[8, "introduction-to-clypher"]], "Getting Started": [[8, "getting-started"]], "Installation": [[8, "installation"]], "CLI Usage": [[8, "cli-usage"]], "Specifying input files": [[8, "specifying-input-files"]], "Recursively adding input files": [[8, "recursively-adding-input-files"]], "Specifying an output directory": [[8, "specifying-an-output-directory"]], "Specifying a password": [[8, "specifying-a-password"]], "Overwriting files": [[8, "overwriting-files"]], "Specifying an engine": [[8, "specifying-an-engine"]]}, "indexentries": {"baseencryptor (class in encryptors.base_encryptor)": [[3, "encryptors.base_encryptor.BaseEncryptor"]], "decrypt() (encryptors.base_encryptor.baseencryptor method)": [[3, "encryptors.base_encryptor.BaseEncryptor.decrypt"]], "encrypt() (encryptors.base_encryptor.baseencryptor method)": [[3, "encryptors.base_encryptor.BaseEncryptor.encrypt"]], "password (encryptors.base_encryptor.baseencryptor attribute)": [[3, "encryptors.base_encryptor.BaseEncryptor.password"]], "baseengine (class in engines.base_engine)": [[4, "engines.base_engine.BaseEngine"]], "force_ow (engines.base_engine.baseengine attribute)": [[4, "engines.base_engine.BaseEngine.force_ow"]], "infiles (engines.base_engine.baseengine attribute)": [[4, "engines.base_engine.BaseEngine.infiles"]], "output (engines.base_engine.baseengine attribute)": [[4, "engines.base_engine.BaseEngine.output"]], "plaintext_password (engines.base_engine.baseengine attribute)": [[4, "engines.base_engine.BaseEngine.plaintext_password"]], "start_decryption() (engines.base_engine.baseengine method)": [[4, "engines.base_engine.BaseEngine.start_decryption"]], "start_encryption() (engines.base_engine.baseengine method)": [[4, "engines.base_engine.BaseEngine.start_encryption"]], "basefilehandler (class in file_handlers.base_filehandler)": [[5, "file_handlers.base_filehandler.BaseFileHandler"]], "file_list (file_handlers.base_filehandler.basefilehandler attribute)": [[5, "file_handlers.base_filehandler.BaseFileHandler.file_list"]], "force_ow (file_handlers.base_filehandler.basefilehandler attribute)": [[5, "file_handlers.base_filehandler.BaseFileHandler.force_ow"]], "list_files() (file_handlers.base_filehandler.basefilehandler method)": [[5, "file_handlers.base_filehandler.BaseFileHandler.list_files"]], "out (file_handlers.base_filehandler.basefilehandler attribute)": [[5, "file_handlers.base_filehandler.BaseFileHandler.out"]], "request() (file_handlers.base_filehandler.basefilehandler method)": [[5, "file_handlers.base_filehandler.BaseFileHandler.request"]], "write() (file_handlers.base_filehandler.basefilehandler method)": [[5, "file_handlers.base_filehandler.BaseFileHandler.write"]]}})