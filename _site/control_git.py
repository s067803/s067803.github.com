import os

_add_all = "git add ."

COMMITMESSAGE = raw_input("commit message: ")

_commit = "git commit -m" + COMMITMESSAGE
# _add = "git remote add origin https://github.com/s067803/code.git"
_push = "git push -u origin master"

os.system(_add_all)
os.system(_commit)
# os.system(_add)
os.system(_push)
