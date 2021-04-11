import os, re

path = "/proc/self/cgroup"

def is_docker():
  if not os.path.isfile(path): return False
  with open(path) as f:
    for line in f:
      if re.match("\d+:[\w=]+:/docker(-[ce]e)?/\w+", line):
        return True
    return False