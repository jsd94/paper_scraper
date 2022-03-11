from classes import section
from misc import null

abstract = section(
    name = 'abstract',
    start_pattern=r'\n.*(Abstract\n|Summary\n|Abstract:|Summary:|[Aa]\s*[Bb]\s*[Ss]\s*[Tt]\s*[Rr]\s*[Aa]\s*)',
    end_pattern=r'\n.*(Key\s?words|Introduction)(\b.*\b|\s){0,3}\n'
)


abstract.add_layer(r'(?i)A\s*B\s*S\s*T\s*R\s*A\s*C\s*T',r'(?i)(K\s*E\s*Y\s*W\s*O\s*R\s*D\s*S|I\s*N\s*T\s*R\s*O\s*D\s*U\s*C\s*T\s*I\s*O\s*N)',null)

abstract.add_layer(r'',r'(?i)(K\s*E\s*Y\s*W\s*O\s*R\s*D\s*S|I\s*N\s*T\s*R\s*O\s*D\s*U\s*C\s*T\s*I\s*O\s*N)',null)
abstract.add_layer(r'',r'\b\d{4}\b',null)

################################

introduction = section(
    name = 'introduction',
    start_pattern = r'(?i)\n([^A-Za-z]*|[\dI]+.?\s*)(I\s*N\s*T\s*R\s*O\s*D\s*U\s*C\s*T\s*I\s*O\s*N)[^A-Za-z]*\n',
    end_pattern = r'\n([^A-Za-z]*|[\dI]+.?\s*)(P\s*[Rr]\s*[Oo]\s*[Tt]\s*[Oo]\s*[Cc]\s*[Oo]\s*[Ll]|E\s*[Xx]\s*[Pp]\s*[Ee]\s*[Rr]\s*[Ii]\s*[Mm]\s*[Ee]\s*[Nn]\s*[Tt]\s*[Aa]\s*[Ll]|R\s*[Ee]\s*[Ss]\s*[Uu]\s*[Ll]\s*[Tt]\s*[Ss]?|M\s*[Aa]\s*[Tt]\s*[Ee]\s*[Rr]\s*[Ii]\s*[Aa]\s*[Ll]\s*[Ss]|M\s*[Ee]\s*[Tt]\s*[Hh]\s*[Oo]\s*[Dd]\s*[Ss])(\b.*\b|\s){0,3}\n'
)

introduction.add_layer(r'(?i)K\s*E\s*Y\s*W\s*O\s*R\s*D\s*S',r'\n([^A-Za-z]*|[\dI]+.?\s*)(P\s*[Rr]\s*[Oo]\s*[Tt]\s*[Oo]\s*[Cc]\s*[Oo]\s*[Ll]|E\s*[Xx]\s*[Pp]\s*[Ee]\s*[Rr]\s*[Ii]\s*[Mm]\s*[Ee]\s*[Nn]\s*[Tt]\s*[Aa]\s*[Ll]|R\s*[Ee]\s*[Ss]\s*[Uu]\s*[Ll]\s*[Tt]\s*[Ss]?|M\s*[Aa]\s*[Tt]\s*[Ee]\s*[Rr]\s*[Ii]\s*[Aa]\s*[Ll]\s*[Ss]|M\s*[Ee]\s*[Tt]\s*[Hh]\s*[Oo]\s*[Dd]\s*[Ss])(\b.*\b|\s){0,3}\n',null)


introduction.add_layer(r'(?i)A\s*B\s*S\s*T\s*R\s*A\s*C\s*T',r'\n([^A-Za-z]*|[\dI]+.?\s*)(P\s*[Rr]\s*[Oo]\s*[Tt]\s*[Oo]\s*[Cc]\s*[Oo]\s*[Ll]|E\s*[Xx]\s*[Pp]\s*[Ee]\s*[Rr]\s*[Ii]\s*[Mm]\s*[Ee]\s*[Nn]\s*[Tt]\s*[Aa]\s*[Ll]|R\s*[Ee]\s*[Ss]\s*[Uu]\s*[Ll]\s*[Tt]\s*[Ss]?|M\s*[Aa]\s*[Tt]\s*[Ee]\s*[Rr]\s*[Ii]\s*[Aa]\s*[Ll]\s*[Ss]|M\s*[Ee]\s*[Tt]\s*[Hh]\s*[Oo]\s*[Dd]\s*[Ss])(\b.*\b|\s){0,3}\n',null)

introduction.add_layer(r'',r'\n([^A-Za-z]*|[\dI]+.?\s*)(P\s*[Rr]\s*[Oo]\s*[Tt]\s*[Oo]\s*[Cc]\s*[Oo]\s*[Ll]|E\s*[Xx]\s*[Pp]\s*[Ee]\s*[Rr]\s*[Ii]\s*[Mm]\s*[Ee]\s*[Nn]\s*[Tt]\s*[Aa]\s*[Ll]|R\s*[Ee]\s*[Ss]\s*[Uu]\s*[Ll]\s*[Tt]\s*[Ss]?|M\s*[Aa]\s*[Tt]\s*[Ee]\s*[Rr]\s*[Ii]\s*[Aa]\s*[Ll]\s*[Ss]|M\s*[Ee]\s*[Tt]\s*[Hh]\s*[Oo]\s*[Dd]\s*[Ss])(\b.*\b|\s){0,3}\n',null)

introduction.add_layer(r'(?i)\n([^A-Za-z]*|[\dI]+.?\s*)(I\s*N\s*T\s*R\s*O\s*D\s*U\s*C\s*T\s*I\s*O\s*N|K\s*E\s*Y\s*W\s*O\s*R\s*D\s*S|A\s*B\s*S\s*T\s*R\s*A\s*C\s*T)[^A-Za-z]*\n',r'\n([^A-Za-z]*|[\dI]+.?\s*)[A-Z][A-Za-z]{2}[A-Za-z\s]*\n',null)