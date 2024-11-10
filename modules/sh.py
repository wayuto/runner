from os import system


def sh(target: str, shell: str) -> None:
    if target in "./":
        system(f"{shell} {target}")
    else:
        system(f"{shell} ./{target}")


if __name__ == "__main__":
    print("Please run it with main.py")