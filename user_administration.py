import argparse
from models import User
from connection import get_connection
parser = argparse.ArgumentParser()
parser.add_argument('-u', "--username", help="")
parser.add_argument('-p', "--password", help="")
parser.add_argument('-e',"--edit", help="")
parser.add_argument('-d', "--delete", help="")
args = parser.parse_args()


print(args.username)
print(args.password)
print(args.edit)
print(args.delete)

def create_user():
    print("CREATING NEW USER")


if args.username and args.password and not args.edit and not args.delete:
    connection = get_connection()
    cursor = connection.cursor()
    u = User()
    # u.set_password( args.password)
    u.username = args.username
    u.save(cursor)
    connection.close()