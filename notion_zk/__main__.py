import sys

from notion_zk.commands import create, delete, open


def main():
    try:
        command = sys.argv[1]
    except IndexError:
        command = 'create'

    if command == 'create':
        create()
    if command == 'delete':
        delete()
    if command == 'open':
        open()


if __name__ == '__main__':
    main()
