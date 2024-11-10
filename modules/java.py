from os import system

def java(target: str, path: str) -> None:
    if path != "":
        system(f"javac {target} -d {path}")
        system(f"java {target}")
    else:
        system(f"java {target}")

if __name__ == "__main__":
    print("Please run it with main.py")