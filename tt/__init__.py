__version__ = '0.1.0'
import auth
from sys import argv
from actions import dm, post, read, chat
api = auth.run()
    
if argv[1] == 'read':
    read(argv, api)
elif argv[1] == 'post':
    post(argv, api)
elif argv[1] == 'dm':
    dm(argv, api)
elif argv[1] == 'chat':
    chat(argv, api)
else:
    print("Wrong!")