"""
contains `PATTERNS`, defining strings that this module may respond to

Wrap "blanks" in {braces}

The content inside the braces dictate the type of object being entered.  This content should be lowercase, underscore_separated.

e.g. 
PATTERNS = frozenset([
    "is {person} a {thing}?",
    "is {person} a {thing} in {place}?",
])


"""
COUNTY_GDP = "What was the real GDP by county in {year}?"
STATE_GDP = "What was the real GDP by state in {year}?"
COUNTY_GDP_RANGE = "What was the real GDP by county from {start_year} to " \
                   "{end_year}?"
STATE_GDP_RANGE = "What was the real GDP by county from {start_year} to " \
                  "{end_year}?"

COUNTY_PERSONAL_INCOME = "What was personal income by county in {year}?"
STATE_PERSONAL_INCOME = "What was the real GDP by state in {year}?"


PATTERNS = frozenset([COUNTY_PERSONAL_INCOME, COUNTY_GDP, STATE_GDP,
                      COUNTY_GDP_RANGE, STATE_GDP_RANGE, STATE_PERSONAL_INCOME])
