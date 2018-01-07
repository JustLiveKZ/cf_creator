from .arg_parser import parser
from .app import App


def main():
    args = parser.parse_args()
    app = App(args)
    app.run()
    return 0
