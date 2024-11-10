#!/usr/bin/python
import sys
from os import system
import re

# Default values
from config import *


def main(target: str = "") -> None:
    # Ret the type of target files
    target_type = re.search("([a-zA-Z0-9]+)$", target)
    if target_type is None:
        print(f"runner:\033[91m warning: \033[90mInvalid target type: {target}")
        return

    # Run it according the type
    match target_type.group(1):
        case "c":
            from modules.c_or_cpp import c_or_cpp
            output_path = lambda : sys.argv[2] if len(sys.argv) > 2 else ""
            c_or_cpp(target, output_path(), C_COMPILER)

        case "cpp":
            from modules.c_or_cpp import c_or_cpp
            output_path = lambda : sys.argv[2] if len(sys.argv) > 2 else ""
            c_or_cpp(target, output_path(), CPP_COMPILER)

        case "py":
            # This is the only type have no module, it's so easy that I don't know what can I do.
            system(f"python {target}")

        case "php" | "phtml" | "html":
            from modules.php import php
            # DEFAULT_PORT is defined in config.py
            port = lambda : int(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_PORT
            php(target, port())

        case "sh" | "bat" | "cmd":
            from modules.sh import sh
            from platform import uname

            # Choose the default shell with system
            shell = lambda : (lambda result: sys.argv[2] if len(sys.argv) > 2 else DEFAULT_SHELL)(1) if uname == "Linux" \
                else (lambda result: sys.argv[2] if len(sys.argv) > 2 else DEFAULT_CMD)(1)
            sh(target, shell())

        case "java":
            from modules.java import java
            output_path = lambda: sys.argv[2] if len(sys.argv) > 2 else ""
            java(target, output_path())

        case "version":
            print("1.0.0")

        case "egg":
            from modules.egg import egg
            egg()

        case _:
            # Print the error about unknown type, maybe I don't add it to the project
            print(f"runner:\033[93m warning:\033[0m unknown type: \033[0m{target_type.group(1)}")


if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except IndexError as e:
        # Print the error if no files
        print("runner:\033[91m error: \033[0mno input files")