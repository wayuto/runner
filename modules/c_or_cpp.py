from os import system
from config import *


def c_or_cpp (target: str, output_path: str, compiler: str) -> None:
    if output_path != "":
        if output_path[0] in "./":
            system(f"{compiler} {target} -o {output_path}")
            system(f"{output_path}")
        else:
            system(f"{compiler} {target} -o {output_path}")
            system(f"./{output_path}")
    else:
        system(f"{compiler} {target} -o ./{DEFAULT_C_OUTPUT_NAME}")
        # Run the output file, and delete it if DELETE in config is True
        system(f"./{DEFAULT_C_OUTPUT_NAME} {(lambda : f'&& rm -rf ./{DEFAULT_C_OUTPUT_NAME}' if DELETE else '')()}")

if __name__ == '__main__':
    print("Please run it with main.py")