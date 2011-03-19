
SQLITE = sqlite3
DB = names.db

all: db report

db:
	./population-us.py | $(SQLITE) $(DB)
	./life-table-us.py | $(SQLITE) $(DB)
	./givenname-birthyear-us.py | $(SQLITE) $(DB)
	./surname-origin.py
	./surname-ethnicity-us.py

report:
	./names-dob.py > names-dob.html

clean:
	$(RM) $(DB)

