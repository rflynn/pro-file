
Goal: Data mine commonly available personal information.
See how much we learn or reasonably guess.
For example, a given name may suggest gender, maybe ethnicity, maybe age,
maybe religion, maybe financial situation.
Research and determine possible useful correlations.

We'll construct a database using publicly-available census data and other sources...

Retain flexibility; all answers should allow multiple pieces of data.
No answer should be considered perfect or complete, only a best guess.

We should be able to take information present into account, but not require anything in particular.

Name (Given, Surname)
	(Name → Psuedonym) i.e. Fake name
	(Name → Age)
	(Name → Ethnicity)
	(Name → Location)
Username
	(Username → Name)
	(Username → DOB)
	(Username → Interests)
	(Username → Membership on other sites)
Email (Username, Domain)
Location
	(Location → Political affiliation)
DOB (Day, Month, Year)
Gender
Ethnicity
	(Ethnicity → Finances)
Education
	Level
	Location
Finances
	Home Ownership
Health
Political affiliation
Any written material
	(Writing → Education level)
	(Writing → Gender)

List of names
List of countries
List of languages
List of ethnicities

-----------------------------------------------------------------------------

API

Ideally, we should be able to provide a partial profile and receive back
a set of "clues" and percentages about this person. For example, given 
the first name "Ryan" we should get back "there is a 90% chance this person is under 40"

-----------------------------------------------------------------------------

Sources:
	"Profiles of General Demographic Characteristics, 2000 Census of Population and Housing, United States" U.S. Department of Commerce Donald L. Evans, Secretary
		<URL: http://www2.census.gov/census_2000/datasets/demographic_profile/0_National_Summary/2khus.pdf>
	http://www.ssa.gov/oact/babynames/limits.html
		http://www.ssa.gov/oact/babynames/names.zip
	http://www2.census.gov/census_2000/datasets/

