# Runner Project

The Runner project is designed to execute various types of files, including C/C++ source code, PHP scripts, shell scripts, and batch files. It provides a simple and unified interface to run these files with appropriate compilers and interpreters.

## Features

- Execute C/C++ files using `GCC` or `G++`.
- Run PHP scripts with your default browser.
- Execute shell and batch scripts.
- Easy to extend and integrate with other tools.
- Run Python script with `Python Interpreter`
- Execute Java files using `JDK` 
- More languages are developing...

## Getting Started

To get started with the Runner project, follow these steps:

### Prerequisites
#### Requires
- Python 3.10+ ([Official Website](https://www.python.org))
#### Optional (If you need):
- GCC and G++ (for C/C++ compilation)
- PHP (for PHP Script execution)
- A Unix-like shell (for Shell Script execution)
- JDK (for running or compile Java sources)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/wayuto/runner.git --depth 1
```
2. Navigate to the project directory and make the main file executable:

```bash
cd runner
chmod +x ./main.py
```

3. Link the main file to /usr/bin/runner (Optional)<a id="step3"></a>
```bash
ln -s $PWD/main.py /usr/bin/runner
```

4. Install the required dependencies (if any).

### Usage
Replace `[path_to_file]` with the path to the file you want to execute.

`(./main.py|runner)` recommend `runner` if you did [Step 3](#step3)

#### Examples

- To run a C/C++ source:
```bash
(./main.py|runner) path/to/source.c [output_path]
```

- To run a PHP script:
```bash
(./main.py|runner) path/to/index.php [port]
```

- To run a shell script:
```bash
(./main.py|runner) path/to/script.sh [shell]
```
- To run a Java source:
```bash
(./main.py|runner) path/to/source.java [output_path]
```
- To run a Python script:
```bash
(./main.py|runner) path/to/script.py
```

## Configuration

The project uses a `config.py` file to manage configurations. You can set the default compiler, shell, and other settings in this file.

## Contact me
#### Email: wan10910@outlook.com | 4e07910@gmail.com
#### QQ number: 2041966268
#### Wechat ID: wyt10910