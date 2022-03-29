import os
import textproc
import pandas as pd
import re

context = re.compile(r'(?i)food|industr|biotechnolog|agricultur|reagent|pharm|medic|therap|diagnos|prevent|treat')

##Biological entities
product = re.compile(r'(?i)product|target|crude|\sextract\s|lysate|recombinant|[^h]ase\s|ab\s|antibod|\sIgG\s|immunoglob|[a-z][^e\s]in\s')
species_name = re.compile(r'[^A-Z][^.](\s|\()[A-Z]([a-z]+|\.)\s[a-z]{2}|yeast|[A-Z]{3}(\d+)?(\s\w*\s){0,4}\scell|host')
contaminants = re.compile(r'(?i)contamina|hcp|host\scell\sprotein|chop|unwanted|impurit|\sdna\s|\srna\s|\slps\s|lipopolysaccharide|endotoxin|hmw|lmw|aggregate|high\smolecular\sweight|low\smolecular\sweight')


##Treatments
recovery = re.compile(r'recover|yield|obtain|product')
purity = re.compile(r'(?i)puri|clear[^l\s]|remov|reduc|separat|decreas|selectiv|eliminat')
concentration = re.compile(r'(?i)concentrat.*(factor|times|fold|[^a-z]log[^a-z]|by)')
recycling = re.compile(r'(?i)recyl|recover|reuse|cycles')
operations = re.compile(r'(?i)[^A-Z]heat|precipitat|filt[er]|wash|centrifug|chromatograph|refold|atp[se]|extract|phase.*(separat.*|system)|add(ition|ed|ing)|mix')

##misc.
table = re.compile(r'(?i)\stable\s[\dI]')
theory_model = re.compile(r'(?i)theor|model|equation|predict|[^a-z]fit')

    #note: the doe regex is weird because fitz sometimes reads the "fl" in a word like "influence"
    #as the single character u\FB02 instead of as 'fl'
doe = re.compile(r'(?i)systematic|model|design\sof\sexperiments|[^a-z]doe[^a-z]|\s[^s]\w{0,3}uence|screen')
phase_curve = re.compile(r'(?i)solubility|binodal|phase\s(behavior|curve|data)')

##units
mass_per_volume = re.compile(r'[\s/][\w\(]?[wmg][\s/][\w]?[LvV][^A-Za-z]')
mass = re.compile(r'[\s/][\w\(]?[g][^A-Za-z]')
volume = re.compile(r'[\s/][\w\(]?[\w]?[LvV][^A-Za-z]')
temperature = re.compile(r'[^A-Za-z](C|K|F)\s')
time = re.compile(r'(?i)year|month|week|day|\sh.?\s|hour|hr\.?\s|\smin\.?\s|\ssec\.?\s|\ss\.?\s')
pH = re.compile(r'\spH\s')

##Improvements
best = re.compile(r'(?i)optimal|best|ideal|standard|optimum|\sup\sto\s|final|maxim')
improvement = re.compile(r'(?i)higher|best|better|improve|achieve|up\sto|fold|factor|best|times|[^a-z]log[^a-z]')

##numbers
number = re.compile(r'(?i)[^a-z]\d[^a-z]')
specific_number = re.compile(r'\d+\.\d+|\d\s?%')
percentage = re.compile(r'\d+\.?\d+?\s?%')
percent_sign = re.compile(r'%')

## expression
solubility = re.compile(r'(?i)solub|[^a-z]tag[^a-z]|inclusion\sbod')
expression = re.compile(r'(?i)(titer|titre|express|productiv)')