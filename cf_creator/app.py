import os


class App:
    def __init__(self, args):
        self.args = args
        if self.args.name is None:
            self.args.name = self.args.path.split('/')[-1]

    def _clone(self):
        os.system('git clone {} {}'.format(self.args.repository_url, self.args.path))

    def _remove_git(self):
        os.system('cd {} && rm -rf .git'.format(self.args.path))

    def _replace_name(self):
        cmakelists = os.path.join(self.args.path, 'CMakeLists.txt')
        with open(cmakelists) as f:
            content = f.read()
        with open(cmakelists, 'w') as f:
            f.write(content.replace('%ProjectName%', self.args.name))

    def _open(self):
        os.system('clion {}'.format(self.args.path))

    def run(self):
        self._clone()
        self._remove_git()
        self._replace_name()
        if not self.args.do_not_open:
            self._open()
