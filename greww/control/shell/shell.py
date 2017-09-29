# execute shell command lines
from greww.utils.exceptions import MissingCommand
from greww.utils.str_bin import convert_bin_to_str as cbts
import subprocess
import os

def _cbtr(ln):
    r = []
    for i in ln.split(b'\n'):
        if i:
            r += [cbts(i)]
    return r

def _simple_execution(cmd):
    """
    Shell simple execution
    Return only exit status (0 : Good)
    """
    return os.system(cmd)

def _subprocess_call_with_communicate(cmd, r=False):
    """
    Shell controlled execution
    Cant output shell logs, and errors
    errors empty : Good
    """
    c = cmd.split(' ')
    p = subprocess.Popen(c, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if r:
        return _cbtr(stdout), _cbtr(stderr)

#NOTE: to understand this part take a look at
# https://stackoverflow.com/questions/17904231/handling-tcpdump-output-in-python

def _catch_shell_stream(cmd,
                        verbose=False,
                        stdout=False,
                        urlout=False,
                        runtime_limit=None,
                        deadline_limit=None,
                        iterations_limit=None,
                        raise_repetition_limit=None):
    """
    Catch shell stream
    Commands like 'tcpdump' and 'top' need more tricky way to catch all logs and redirect them

    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = []
    while True:
        line = p.stdout.readline()
        stdout.append(line)
        if verbose:
            print(line)
        if line == '' and p.poll() != None:
            break
    return ''.join(stdout)
    """
    pass

class Shell(object):
    """
    Shell execution and envirenement
    """
    @staticmethod
    def execute(cmd, output=False, errors=False, subprocess=False):
        if subprocess or output:
            s = _subprocess_call_with_communicate(cmd, 1)
            if output:
                res = [s[0]]
                if errors:
                    res += [s[1]]
                return res
        else:
            return _simple_execution(cmd)

    @staticmethod
    def check_output(cmd, subprocess=False):
        if subprocess:
            return not _subprocess_call_with_communicate(cmd, 1)[1]
        else:
            return _simple_execution(cmd) == 0

    @staticmethod
    def _execute(cmd):
        return _subprocess_call_with_communicate(cmd, 1)

    @staticmethod
    def catch_stream():
        _catch_shell_stream(1)
        pass
