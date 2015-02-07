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
STATE_GDP = "What was the real GDP by state in {year}?"
STATE_PC_GDP = "What was the per capita GDP by state in {year}?"
STATE_GDP_RANGE = "What was the real GDP by county from {start_year} to " \
                  "{end_year}?"

COUNTY_TPI = "What was total personal income by county in {year}?"
STATE_TPI = "What was the total personal income by state in {year}?"

STATE_PCPI = "What was the per-capita personal income by state in {year}?"
COUNTY_PCPI = "What was the per-capita personal income by county in {year}?"


PATTERNS = frozenset([COUNTY_TPI, STATE_GDP, STATE_TPI, STATE_PCPI,
                      COUNTY_PCPI, STATE_PC_GDP])
