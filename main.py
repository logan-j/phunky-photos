#!/usr/bin/env python3
import argparse
from src.backend import Backend
from src.printer import Printer


def main():
    parser = argparse.ArgumentParser(description='Display photo album information.')
    parser.add_argument('album_id', type=int, nargs=1, help='id of the album to display')
    args = parser.parse_args()
    backend = Backend()
    photos = backend.get_photo_album(args.album_id)
    for photo in photos:
        print(Printer.display(photo))


if __name__ == "__main__":
    main()
