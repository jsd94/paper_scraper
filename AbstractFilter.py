from functions import *
from regexes import *


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
    'Quant. solubility':{'Includes':[solubility,number,improvement],
                        'Excludes':[]},
    'Quant. titer':{'Includes':[expression,number,improvement],
                   'Excludes':[]}
}

### FUNCTION CALL
filter_abstracts(txtfile='romel.txt',criteria_dct=criteria_dct,outfile='test.xlsx')
