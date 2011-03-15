
all:
	$(MAKE) -C doc
	$(MAKE) -C data

clean:
	$(MAKE) -C doc clean
	$(MAKE) -C data clean

