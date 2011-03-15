
Pro-File
-------------------------------------------------------------------------------

Goal: statistical profiling of commonly-available personal information.
For example, a given first name may suggest gender, age and cultural information
such as ethnicity and religion. These suggestions then suggest yet more things.

We can't possibly know everything about someone from a name and an IP address,
but this sort of information *can* give us a starting point for subtle
customization of someone's online experience which can ultimately result in a
happier customer.

We'll construct a database using accurate publicly-available census data and
other sources, and then, given an incomplete set of information we'll return a
set of statistical speculations.

In:
	Given name
	Family name
	IP address
	Email address
	Member profile

Out:
	Personal characteristics:
		Gender
		Age
		Location
	Cultural:
		Ethnicity
		Religious affiliation
	Society:
		Education level
		Political affiliation
		Marital status

Requirements: python3, sqlite3

