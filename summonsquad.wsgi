import sys
sys.path.insert(0, '/var/www/html')

from App import app as application

if __name__ == "__main__":
    application.run()
