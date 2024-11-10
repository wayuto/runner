# Runner Project

The Runner project is designed to execute various types of files, including C/C++ source code, PHP scripts, shell scripts, and batch files. It provides a simple and unified interface to run these files with appropriate compilers and interpreters.

## Features

- Execute C/C++ files using `gcc` or `g++`.
- Run PHP scripts with your default browser.
- Execute shell and batch scripts.
- Easy to extend and integrate with other tools.
- Run Python script
- Execute Java files using `jdk` 
- More languages developing...

## Getting Started

To get started with the Runner project, follow these steps:

### Prerequisites

- Python 3.10 or higher ([Official Website](https://www.python.org)) *
- GCC and G++ (for C/C++ compilation)
- PHP (for PHP script execution)
- A Unix-like shell (for shell script execution)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/wayuto/runner.git -depth 1
```
2. Navigate to the project directory and make the main file executable:

```bash
cd runner
chmod +x ./main.py
```

3. Install the required dependencies (if any).

### Usage

To run a file, use the following command:

python main.py [path_to_file]


Replace `[path_to_file]` with the path to the file you want to execute.

#### Examples

- To run a C/C++ file:
```bash
./ main.py path/to/source.c [output_path]
```

- To run a PHP script:
```bash
./main.py path/to/index.php [port]
```

- To run a shell script:
```bash
./main.py path/to/script.sh [shell]
```
- To run a Java file:
```bash
./main.py path/to/source.java [output_path]
```
- To run a Python script:
```bash
./main.py path/to/script.py
```

## Configuration

The project uses a `config.py` file to manage configurations. You can set the default compiler, shell, and other settings in this file.