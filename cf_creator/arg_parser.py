from argparse import ArgumentParser
from . import settings

parser = ArgumentParser(prog='cf_creator')

parser.add_argument(
    'name',
    help='Name of the new project',
)

parser.add_argument(
    '--path', '-p',
    help='Path to folder',
)

parser.add_argument(
    '--repository-url', '-r',
    default=settings.REPOSITORY_URL,
    help='Repository URL (git) with JHelper template',
)

parser.add_argument(
    '--open', '-o',
    action='store_true',
    help='Is selected opens CLion right after cloning project',
)
