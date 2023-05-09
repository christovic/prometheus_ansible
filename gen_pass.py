# Modified code from here: https://prometheus.io/docs/guides/basic-auth/

import getpass
import bcrypt
import re

password = getpass.getpass("password: ")
hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
yamlvars = open('vars.yaml').read()
x = re.sub("prom_password:.+\n", f"prom_password: {password}\n", yamlvars)
x = re.sub("prom_hashed_password:.+\n", f"prom_hashed_password: {hashed_password.decode()}\n", x)

open('vars.yaml', 'w').write(x)