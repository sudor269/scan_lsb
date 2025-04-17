import argparse
import os
from pathlib import Path
from PIL import Image
import numpy as np
from colorama import Fore, Style, init
from scipy.stats import chisquare
from art import tprint

init(autoreset=True)

def is_image_file(filename):
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')
    return filename.lower().endswith(image_extensions)


def calculate_chi_squared(observed):
    expected = np.zeros(256, dtype=np.float64)
    for i in range(0, 256, 2):
        if i + 1 >= 256:
            break
        total = observed[i] + observed[i + 1]
        expected_val = total / 2.0
        expected[i] = expected_val
        expected[i + 1] = expected_val

    expected[expected == 0] = 1e-10
    chi2, _ = chisquare(observed, expected)
    return chi2


def analyze_image(image_path):
    try:
        image = Image.open(image_path)
        image = image.convert('RGB')
        pixels = np.array(image)

        channels = [
            pixels[:, :, 0].flatten(),
            pixels[:, :, 1].flatten(),
            pixels[:, :, 2].flatten()
        ]

        chi_results = []
        for channel in channels:
            observed = np.bincount(channel, minlength=256)
            chi2 = calculate_chi_squared(observed)
            chi_results.append(chi2)

        avg_chi = np.mean(chi_results)

        threshold = 340
        is_stego = avg_chi < threshold

        if is_stego:
            print(f"{image_path} {Fore.RED}ОПАСНО! СТЕГО-КОНТЕЙНЕР!")
        else:
            print(f"{image_path} {Fore.GREEN}БЕЗОПАСНО!")

        return avg_chi, is_stego

    except Exception as e:
        print(f"{Fore.RED}Ошибка при анализе {image_path}: {e}")
        raise


def analyze_directory(directory):
    if not os.path.isdir(directory):
        print(f"{Fore.RED}{directory} не является директорией")
        return

    image_files = [f for f in os.listdir(directory) if is_image_file(f)]
    results = {
        'clean': 0,
        'stego': 0,
        'errors': 0,
        'chi_values': []
    }

    if not image_files:
        print(f"{Fore.YELLOW}В директории нет изображений")
        return

    print(f"{Fore.CYAN}\nАнализ директории: {directory}")
    print(f"{Fore.BLUE}Найдено изображений: {len(image_files)}\n")

    for idx, filename in enumerate(image_files, 1):
        full_path = os.path.join(directory, filename)
        print(f"{Fore.WHITE}[{idx}/{len(image_files)}] Анализ: {filename}")
        try:
            chi, stego = analyze_image(full_path)
            results['chi_values'].append(chi)
            if stego:
                results['stego'] += 1
            else:
                results['clean'] += 1
        except:
            results['errors'] += 1

    print(f"\n{Fore.MAGENTA}{'=' * 50}")
    print(f"{Fore.CYAN}Итоговый отчет:")
    print(f"{Fore.GREEN}Чистые: {results['clean']}")
    print(f"{Fore.RED}Стего: {results['stego']}")
    print(f"{Fore.YELLOW}Ошибки: {results['errors']}")

    if results['chi_values']:
        avg_chi = np.mean(results['chi_values'])
        print(f"{Fore.CYAN}Средний χ²: {avg_chi:.1f}")


def main():
    tprint('scan_lsb')

    parser = argparse.ArgumentParser(
        description="Детектор LSB стеганографии с улучшенной точностью",
        epilog="Примеры:\n  scanner.py -f image.jpg\n  scanner.py -d ./photos",
        formatter_class=argparse.RawTextHelpFormatter
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--file', help="Анализ конкретного файла")
    group.add_argument('-d', '--dir', help="Анализ директории")

    args = parser.parse_args()

    try:
        if args.file:
            if not Path(args.file).exists():
                raise FileNotFoundError(f"Файл не найден: {args.file}")
            analyze_image(args.file)
        elif args.dir:
            if not Path(args.dir).is_dir():
                raise NotADirectoryError(f"Директория не найдена: {args.dir}")
            analyze_directory(args.dir)
    except Exception as e:
        print(f"\n{Fore.RED}{'!' * 20} ОШИБКА {'!' * 20}")
        print(f"{str(e)}")
        print(f"{Fore.RED}{'!' * 40}")

if __name__ == "__main__":
    main()