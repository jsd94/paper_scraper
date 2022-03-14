def remove_newlines(text):
    text = text.replace('\n-','')
    text = text.replace('-\n','')
    text = text.replace('\n',' ')
    return text

def decimal_replace(matchobj):
    if matchobj.group(2)=='.':
        return matchobj.group(1)+'/POINT/'+matchobj.group(3)
    
def dot_replace(matchobj):
    if matchobj.group(2)=='.':
        if matchobj.group(3):
            return matchobj.group(1)+'/DOT/'+matchobj.group(3)
        else:
            return matchobj.group(1)+'/DOT/'

def split_to_sentences(text):
    sentence_pattern = re.compile(r'[^.!?]*[.!?]')
    decimal_number = re.compile(r'(\d+)(\.)(\d+)')
    abbreviation_dot = re.compile(r'([A-Z])(\.)(\s[a-z])?')
    text = remove_newlines(text)
    text = decimal_number.sub(decimal_replace,text)
    text = abbreviation_dot.sub(dot_replace,text)
    sentences = sentence_pattern.findall(text)
    sentences = [a.replace('/DOT/','.') for a in sentences]
    sentences = [a.replace('/POINT/','.') for a in sentences]
    return sentences

def split_to_lines(text):
    text = text.split('\n')
    return text

def unique(lst):
    unique = []
    cp = lst.copy()
    for a in lst:
        cp.remove(a)
        if a not in cp:
            unique.append(a)
    return unique

def contigs(lst_of_ints):
    lst = sorted(unique(lst_of_ints))
    contigs = []
    temp = []
    for a in lst:
        if temp == []:
            temp = [a]
        if a+1 in lst:
            temp.append(a+1)
        else:
            contigs.append(temp)
            temp = []
    return contigs

def narrow(text,include,exclude,chunk='sentence',n_neighbor_chunks=0):
    if not isinstance(include,list):
        include = [include]
    if not isinstance(exclude,list):
        exclude = [exclude]
    if chunk == 'sentence':
        text = split_to_sentences(text)
    elif chunk == 'line':
        text = split_to_lines(text)
    
    out_indices = []
    out = []
    indices = range(len(text))
    for i in indices:
        missing_includes = True
        has_excludes = True
        chunk = text[i]
        for pattern in include:
            if not pattern.search(chunk):
                break
        else:
            missing_includes = False
        for pattern in exclude:
            if pattern.search(chunk):
                break
        else:
            has_excludes = False
        if not missing_includes and not has_excludes:
            out_indices.append(i)
            j=0
            while j < n_neighbor_chunks:
                j+=1
                if i+j in indices:
                    out_indices.append(i+j)
            j=0
            while j < n_neighbor_chunks:
                j+=1
                if i-j in indices:
                    out_indices.append(i-j)
            
    contig_indices = contigs(out_indices)
    for lst in contig_indices:
        sent = ''.join([text[a] for a in lst])
        out.append(sent)
    return out
