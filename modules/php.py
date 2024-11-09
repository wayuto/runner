import webbrowser
from time import sleep
import subprocess


def php(target: str, port: int) -> None:
    subprocess.Popen(["php", "-S", f"0.0.0.0:{port}"])
    sleep(2.5)
    webbrowser.open(f"0.0.0.0:{port}/{target}")

if __name__ == "__main__":
    print("Please run it with main.py")