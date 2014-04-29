
SQLITE = sqlite3
DB = names.sqlite3

all: db report

db:
	[ -e popclockest.txt ] || curl -O http://www.census.gov/population/estimates/nation/popclockest.txt
	./population-us.py | $(SQLITE) $(DB)
	./life-table-us.py | $(SQLITE) $(DB)
	./givenname-birthyear-us.py
	./surname-origin.py
	./surname-ethnicity-us.py

report:
	./names-dob.py > names-dob.html

clean:
	$(RM) $(DB)

