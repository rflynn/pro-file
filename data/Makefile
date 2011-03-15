
SQLITE = sqlite3
DB = names.db

db: population life_table surname givenname report

population:
	./population-us.py | $(SQLITE) $(DB)

life_table:
	./life-table-us.py | $(SQLITE) $(DB)

surname:
	./surname-us.py | $(SQLITE) $(DB)

givenname:
	./givenname-birthyear-us.py | $(SQLITE) $(DB)

report:
	./names-dob.py > names-dob.html

clean:
	$(RM) $(DB)

