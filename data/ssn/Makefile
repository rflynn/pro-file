# vim: set ts=8 noet:

ssn.sqlite3: ssn_area_codes.csv ssn_area_codes.sql
	sqlite3 ssn.sqlite3 < ssn_area_codes.sql

clean:
	rm ssn.sqlite3

.PHONY: clean
