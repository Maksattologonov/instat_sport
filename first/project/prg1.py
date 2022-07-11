import sys

from decouple import config

sys.path.insert(0, config("BASE_PATH"))

from first.moduleA import Say

Say.say_hallo()
