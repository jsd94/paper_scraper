import re
import fitz
from misc import null,is_quality
import pandas as pd

class paper(object):
    def __init__(self,path_to_pdf):
        self.path = path_to_pdf
        self.citation,self.short_id,self.year = self.get_paper_id()
        self.text = self.get_text()
    
    def __repr__(self):
        return 'A paper object for %s' %self.citation
    
    def get_paper_id(self):
        path = self.path
        filename = path.split('/')[-1]
        citation = '.'.join(filename.split('.')[:-1])
        year = re.search('\d{4}',citation).group(0)
        short_id = citation.split(' ')[0]+' '+year
        return citation,short_id,int(year)
    
    def get_text(self):
        text = ''
        with fitz.open(self.path) as infile:
            for page in infile:
                text+= page.getText()
        
        self.pass_qa = is_quality(text)
        if not self.pass_qa:
            return 'Error: Text extraction failed.'
        else:
            return text
    
    def get_section(self,section):
        attr = section.name
        text = self.text
        for i in range(len(section.start_patterns)):
            try:
                text = section.preprocess_steps[i](text)
                start_match = section.start_patterns[i].search(text)
                start = start_match.start()
                start_groups = ''.join([a for a in start_match.groups() if a])
                end_match = section.end_patterns[i].search(text[start:])
                end_groups = ''.join([a for a in end_match.groups() if a])
                end = end_match.start()+start
                break
            except:
                continue
        try:       
            text = text[start:end]
            setattr(self,attr+'_captured',True)
        except:
            text = 'Error: Section could not be captured'
            setattr(self,attr,text)
            setattr(self,attr+'_captured',False)
            return
        setattr(self,attr,text)
        setattr(self,
                attr+'_start_match',
                'pattern: '+section.start_patterns[i].pattern+'\nmatched: '+start_groups)
        setattr(self,
                attr+'_end_match',
                'pattern: '+section.end_patterns[i].pattern+'\nmatched: '+end_groups)
        setattr(self,
                attr+'_used_preprocess_step',
                section.preprocess_steps[i])
        
    def add_dataset(self,name,columns):
        setattr(self,name+'_df',pd.DataFrame(columns=columns))

class section(object):
    def __init__(self,name,start_pattern,end_pattern,preprocess_steps=null):
        self.start_patterns = [re.compile(start_pattern)]
        self.end_patterns = [re.compile(end_pattern)]
        self.name = name
        self.preprocess_steps = [null]
    def __repr__(self):
        return 'A section object for the %s'%self.name
    
    def add_layer(self,start_pattern,end_pattern,preprocess_step):
        self.start_patterns.append(re.compile(start_pattern))
        self.end_patterns.append(re.compile(end_pattern))
        self.preprocess_steps.append(preprocess_step)