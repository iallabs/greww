import argparse
import os
import subprocess
import shutil
import tempfile
import platform
from distutils.dir_util import copy_tree


def get_project_name(url):
    parts = url.split("/")
    name = parts[-1]
    if name.endswith(".git"):
        name = name[:-4]
    return name


def get_arch():
    arch = platform.machine()
    if arch == 'x86_64':
        arch = 'amd64'
    return arch


def get_maintainer():
    return subprocess.check_output([
        'git', '--no-pager', 'show', '-s', '--format="%aN <%aE>"'
    ]).decode().strip()


def get_version():
    return subprocess.check_output([
        'git', '--no-pager', 'show', '-s', '--format=%at'
    ]).decode().strip()


def git_clone(url, to):
    subprocess.call(['git', 'clone', url, to])


def get_description(project):
    if not os.path.exists("README.md"):
        return project, ""
    with open("README.md") as f:
        sd = f.readline(60).strip()
        ld = f.read().strip()
        lines = ld.split("\n")
        nlines = []
        for line in lines:
            l = line.strip()
            if l == "":
                l = "."
            nlines.append(" " + l)
        return sd, "\n".join(nlines)


def go_build(project):
    subprocess.call(["go", "get", "-v", "."])
    subprocess.call(["go", "build", "-v", "-o", project, "."])


def pack(root):
    subprocess.call(["dpkg", "--build", root])


def save_doc(project, mandir):
    if not os.path.exists("README.md"):
        return
    subprocess.call([
        'pandoc', '-s', '-t', 'man', 'README.md', '-o',
        os.path.join(mandir, project + ".1")
    ])


def make_dir_structure(project, version, arch):
    root = project + "-" + version + "_" + arch
    controldir = os.path.join(root, "DEBIAN")
    bindir = os.path.join(root, "usr", "local", "bin")
    mandir = os.path.join(root, "usr", "local", "share", "man", "man1")
    os.makedirs(root)
    os.makedirs(controldir, exist_ok=True)
    os.makedirs(bindir, exist_ok=True)
    os.makedirs(mandir, exist_ok=True)
    return root, controldir, bindir, mandir


def copy_bin(project, bindir):
    shutil.copy(project, os.path.join(bindir, project))


def copy_resources(root):
    if os.path.exists("resources"):
        copy_tree("resources", root)


def save_control(dir, project, version, maintainer, arch, sdesc, ldesc):
    lines = [
        "Package: " + project,
        "Version: " + version,
        "Priority: extra",
        "Maintainer: " + maintainer,
        "Architecture: " + arch,
        "Description: " + sdesc,
        ldesc,
        ""
    ]
    text = "\n".join(lines)
    with open(os.path.join(dir, "control"), "wt") as f:
        f.write(text)


parser = argparse.ArgumentParser("Build package from golang GIT")
parser.add_argument("url", nargs=1)
parser.add_argument("--tmp", action='store', help="Temporary directory")
args = parser.parse_args()

url = args.url[0]
project = get_project_name(url)
dirpath = tempfile.mkdtemp(prefix="packet_", suffix="_" + project, dir=args.tmp)
git_clone(url, dirpath)
workdir = os.getcwd()
os.chdir(dirpath)
maintainer = get_maintainer()

arch = get_arch()
version = get_version()
short_description, long_description = get_description(project)

go_build(project)

root, control, bin, man = make_dir_structure(project, version, arch)
save_doc(project, man)
copy_bin(project, bin)
save_control(control, project, version, maintainer, arch, short_description, long_description)
copy_resources(root)
pack(root)

shutil.copy(root + ".deb", os.path.join(workdir, root + ".deb"))

os.chdir(workdir)
shutil.rmtree(dirpath)
