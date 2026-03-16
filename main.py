# main.py - главный файл приложения
from colorama import init, Fore, Style

from config import APP_NAME, VERSION
from utils import farewell, greet

init()


def main():
    print(f"{Fore.CYAN}{APP_NAME} v{VERSION}{Style.RESET_ALL}")
    print(f"\n{Fore.CYAN}{greet('мир')}{Style.RESET_ALL}")
    print(f"\n{Fore.MAGENTA}{farewell('мир')}{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
