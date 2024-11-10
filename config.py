# Just an empty value, you can modify it to any
DEFAULT = ""
# Default command to run .sh/.bat/.cmd
DEFAULT_SHELL: str = "sh"
DEFAULT_CMD: str = "cmd"
# Default name of C/C++ output files
DEFAULT_C_OUTPUT_NAME: str = "a.out"
# Default PHP running port
DEFAULT_PORT: int = 8000
# Default C/C++ compiler
C_COMPILER: str = "gcc"
CPP_COMPILER: str = "g++"
# Used in module/c_or_cpp and module/java, decide if delete the default output file when it ran
DELETE: bool = True
