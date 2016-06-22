import os
import sys
import site

site.addsitedir('~/.virtualenvs/sillysentence/local/lib/python2.7/site-packages')
parent_dir = os.path.join(os.path.dirname(__file__))
sys.path.append(parent_dir)

# Activate your virtual env
try:
    activate_env = os.path.expanduser("/home/jim/.virtualenvs/sillysentence/bin/activate_this.py")
    execfile(activate_env, dict(__file__=activate_env))
except IOError:
    pass


from sillysentence import app as application
