# Runner Project

The Runner project is designed to execute various types of files, including C/C++ source code, PHP scripts, shell scripts, and batch files. It provides a simple and unified interface to run these files with appropriate compilers and interpreters.

## Features

- Execute C/C++ files using `gcc` or `g++`.
- Run PHP scripts with a built-in server.
- Execute shell and batch scripts.
- Easy to extend and integrate with other tools.
- Run Python script
- More languages developing...

## Getting Started

To get started with the Runner project, follow these steps:

### Prerequisites

- Python 3.10 or higher ([Official Website](https://www.python.org))
- GCC and G++ (for C/C++ compilation)
- PHP (for PHP script execution)
- A Unix-like shell (for shell script execution)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/wayuto/runner.git -depth 1
```
2. Navigate to the project directory:

```bash
cd runner
```

3. Install the required dependencies (if any).

### Usage

To run a file, use the following command:

python main.py [path_to_file]


Replace `[path_to_file]` with the path to the file you want to execute.

#### Examples

- To run a C/C++ file:
```bash
python main.py path/to/source.c [output_path]
```

- To run a PHP script:
```bash
python main.py path/to/index.php [port]
```

- To run a shell script:
```bash
python main.py path/to/script.sh [shell]
```

## Configuration

The project uses a `config.py` file to manage configurations. You can set the default compiler, shell, and other settings in this file.

## Contributing

Contributions to the Runner project are welcome. Please ensure you follow the existing code structure and maintain the coding style.
