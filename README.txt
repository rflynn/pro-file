

Pro-File
-------------------------------------------------------------------------------

Statistical profiling of commonly-available personal information.

For example, a given first name may suggest gender, age and ethnicity.
These suggestions then suggest yet more things such as education level,
interests, BMI, height, etc.

We can't possibly know everything about someone from a name and an IP address,
but this sort of information _can_ give us a starting point for customization
of an online experience which can ultimately result in a happier customer.

We'll construct a database using accurate publicly-available census, genealogical 
and other data and and then cross-reference an incomplete set of information and
return a set of statistical speculations.

Requirements:
	apt-get install sqlite3 unzip python python3

Use:

	Currently a collection of non-integrated libraries with script front-ends.

	in data/
		./givenname.py "my first name"
		./surname.py "my last name"

