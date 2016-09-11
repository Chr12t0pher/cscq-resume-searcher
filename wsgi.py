#!/home/cscq/venv/bin/python
import sys

sys.path.insert(0, "/home/cscq/venv/lib/python3.4/site-packages/")
sys.path.insert(0, "/home/cscq/")

from app import app as application

if __name__ == "__main__":
	application.run()
