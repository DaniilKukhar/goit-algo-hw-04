import argparse
import shutil
from pathlib import Path


def copy_and_sort_files(source_dir: Path, destination_dir: Path):

    try:
        for item in source_dir.iterdir():

            # Якщо це директорія — рекурсія
            if item.is_dir():
                copy_and_sort_files(item, destination_dir)

            # Якщо це файл — копіюємо
            elif item.is_file():

                # Отримуємо розширення
                extension = item.suffix[1:] if item.suffix else "no_extension"

                # Створюємо папку під тип файлу
                target_folder = destination_dir / extension
                target_folder.mkdir(parents=True, exist_ok=True)

                # Шлях копії файлу
                target_file = target_folder / item.name

                # Копіювання файлу
                shutil.copy2(item, target_file)

                print(f"Скопійовано: {item} -> {target_file}")

    except PermissionError:
        print(f"Немає доступу: {source_dir}")

    except Exception as error:
        print(f"Помилка в {source_dir}: {error}")


def main():

    parser = argparse.ArgumentParser(
        description="Рекурсивне сортування файлів за розширенням"
    )

    parser.add_argument("source", help="Вихідна директорія")

    parser.add_argument(
        "destination",
        nargs="?",
        default="dist",
        help="Директорія призначення"
    )

    args = parser.parse_args()

    source_path = Path(args.source)
    destination_path = Path(args.destination)

    # Перевірка source
    if not source_path.exists():
        print("Вихідна директорія не існує")
        return

    destination_path.mkdir(parents=True, exist_ok=True)

    # Запуск рекурсії
    copy_and_sort_files(source_path, destination_path)

    print("\nГотово: всі файли скопійовано і відсортовано")


if __name__ == "__main__":
    main()