from classes import section
from misc import null

abstract = section(
    name = 'abstract',
    start_pattern=r'\n.*(Abstract\n|Summary\n|Abstract:|Summary:|[Aa]\s*[Bb]\s*[Ss]\s*[Tt]\s*[Rr]\s*[Aa]\s*)',
    end_pattern=r'\n.*(Key\s?words|Introduction)(\b.*\b|\s){0,3}\n'
)


abstract.add_layer(r'(?i)a\s*b\s*s\s*t\s*r\s*a\s*c\s*t',r'(?i)(k\s*e\s*y\s*w\s*o\s*r\s*d\s*s|i\s*n\s*t\s*r\s*o\s*d\s*u\s*c\s*t\s*i\s*o\s*n)',null)

#abstract.add_layer(r'(?i)abstract',r'(?i)(key\s?words|introduction)',null)
abstract.add_layer(r'',r'(?i)(k\s*e\s*y\s*w\s*o\s*r\s*d\s*s|i\s*n\s*t\s*r\s*o\s*d\s*u\s*c\s*t\s*i\s*o\s*n)',null)
abstract.add_layer(r'',r'\b\d{4}\b',null)