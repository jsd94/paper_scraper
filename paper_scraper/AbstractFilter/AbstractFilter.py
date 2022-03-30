from paper_scraper.AbstractFilter import functions
from paper_scraper import regexes as reg


### DEFINE CRITERIA

##criteria_dct = {
  ##  'Name of 1st criterion':{'Includes':[keywords/patterns],
    ##                    'Excludes':[]},
    ##'Name of 2nd criterion':{'Includes':[keywords/patterns],
      ##             'Excludes':[]}
    ## . . .
    ## . . .
## }

criteria_dct = {
    'Quant. solubility':{'Includes':[reg.solubility,reg.number,reg.improvement],
                        'Excludes':[]},
    'Quant. titer':{'Includes':[reg.expression,reg.number,reg.improvement],
                   'Excludes':[]}
}

### FUNCTION CALL
functions.filter_abstracts(txtfile='romel.txt',criteria_dct=criteria_dct,outfile='test.xlsx')
