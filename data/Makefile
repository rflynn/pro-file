
SQLITE = sqlite3
DB = names.db

db:
	./population-us.py | $(SQLITE) $(DB)
	./life-table-us.py | $(SQLITE) $(DB)
	./surname-us.py | $(SQLITE) $(DB)
	./givenname-birthyear-us.py | $(SQLITE) $(DB)
	./surname-ethnicity-us.py
	./names-dob.py > names-dob.html

clean:
	$(RM) $(DB)

