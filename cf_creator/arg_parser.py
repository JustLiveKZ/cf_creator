from argparse import ArgumentParser
from . import settings

parser = ArgumentParser(prog='cf_creator')

parser.add_argument(
    'path',
    help='Path to the project',
)

parser.add_argument(
    '--name', '-n',
    help='Name of the project, defaults to last section of path',
)

parser.add_argument(
    '--repository-url', '-r',
    default=settings.REPOSITORY_URL,
    help='Repository URL (git) with JHelper template',
)

parser.add_argument(
    '--do-not-open', '-do',
    action='store_true',
    help='Do not open CLion right after cloning project',
)
