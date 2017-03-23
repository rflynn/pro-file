# vim: set ts=8 noet:

all: venv
	$(MAKE) -C doc
	$(MAKE) -C data

venv: requirements.txt
	test -d venv || { virtualenv -p python3 venv || python3 -m venv venv; }
	venv/bin/pip install --upgrade pip
	venv/bin/pip install -r requirements.txt

clean:
	$(MAKE) -C doc clean
	$(MAKE) -C data clean

distclean: clean
	$(RM) -r venv

