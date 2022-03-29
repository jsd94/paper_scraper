import textproc
import pandas as pd
import re

def parse_pubmed_abstracts(txtfile):
    with open(txtfile,'r') as infile:
        text = infile.read()
    papers = re.split(r'PMID.*\n',text)
    return papers

def filter_abstracts(txtfile,criteria_dct,outfile):
    papers = parse_pubmed_abstracts(txtfile)
    columns = ['Title','doi','entry']+list(criteria_dct.keys())
    df = pd.DataFrame(columns=columns)
    i = 0
    for paper in papers:
        try:
            abst = re.search(r'(?si)\n\n([a-z].*?)\n\n(DOI|PMCID|PMID)',paper).groups()[0]
        except:
            abst = paper
        try:
            title = re.search(r'(?si)\n\n([a-z].*?)\.\n\n',paper).groups()[0].strip()
        except:
            title = ''
        try:
            doi = re.search(r'(doi:.*)\.',paper).groups()[0].strip()
        except:
            doi = ''
        
        df.loc[len(df),['Title','doi','entry']] = [title,doi,abst]
        out_dct = {}
        
        for key in criteria_dct.keys():
            hits = textproc.narrow(abst,criteria_dct[key]['Includes'],criteria_dct[key]['Excludes'])
            if hits != []:
                out_dct[key] = True
            else:
                out_dct[key] = False
    
            df.loc[i,key] = out_dct[key]
        i+=1
    df.to_excel(outfile)
    
