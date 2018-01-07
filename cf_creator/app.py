import os


class App:
    def __init__(self, args):
        self.args = args

    def _get_path(self):
        if self.args.path is not None:
            return self.args.path
        return self.args.name

    def _clone(self):
        os.system('git clone {} {}'.format(self.args.repository_url, self._get_path()))

    def _remove_git(self):
        os.system('cd {} && rm -rf .git'.format(self._get_path()))

    def _replace_name(self):
        cmakelists = os.path.join(self._get_path(), 'CMakeLists.txt')
        with open(cmakelists) as f:
            content = f.read()
        with open(cmakelists, 'w') as f:
            f.write(content.replace('%ProjectName%', self.args.name))

    def run(self):
        self._clone()
        self._remove_git()
        self._replace_name()
