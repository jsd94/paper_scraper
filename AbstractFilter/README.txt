The scripts in this folder enable advanced filtering of abstracts from a PubMed search, to narrow down on papers that match certain inclusion and exclusion criteria.

Basic usage:
	- Install the latest version of python 3
	- Install numpy and pandas
	- Run a PubMed search for anything you want
	- Save the search output using the "Abstract" format option and save it to a .txt file in this folder
	- Edit AbstractFilter.py in the following ways:
		- 1) Where it says "### DEFINE CRITERIA", update the variable called criteria_dct
			- 1.1) For every inclusion/exclusion variable you have, give it a name (e.g., 'Quant. titer', if we're looking for papers that report a quantitative measure of protein titer)
			- 1.2) For that variable, add inclusion criteria in a list (i.e. inside the [] brackets) after where it says 'Includes'. The way this works is that the inclusion criteria can be 				either strings (words inside quotes, like 'this' or "this") or regular expressions (basically, special programming tools that can match variable patterns instead of 					specific words). It's much more powerful if you use regular expressions, but they can be tricky to write. I've provided a small library of predefined regexes in the file 				regexes.py in this folder, given them descriptive names, and grouped them into categories. Check that file and try using some of the regexes in it for your filtering. If 				you use regexes, the program will check if any one sentence in the abstract matches all the regex patterns you put in the brackets for 'Includes': [] in criteria_dct. If 				you use strings, it will be the same except the sentence will have to include an *exact* match for each string. You can mix and match as many regexes and strings as you 				want.
			 - 1.3) For the same variable, add the exclusion criteria in exactly the same way as for the inclusion criteria. The program will now look through all the 				sentences that matched all the inclusion criteria for a given variable, check to see whether each sentence matches any of the exclusion criteria, and throw it out if it 				does. Whatever sentences you're left with are matches and make the paper either a "hit" or a "miss" for that variable.
			 - (You can leave either Excludes blank (just the []) if you want. But you have to have at least one pattern/string for each 'Includes':[] or it won't work.
		- 2) Where it says "### FUNCTION CALL"
			- 2.1) Change the txtfile parameter to the name of your PubMed abstracts file
			- 2.2) Change the outfile parameter to the name you want to give your output file
	- Run AbstractFilter.py
	- The output is sent to an excel file with the name you specified in the outfile parameter
		- Each row is an abstract from the search results
		- There's a column for the paper title, the DOI, the abstract/pubmed search result, and then columns for each inclusion/exclusion criterion you specified
		- In the criteria columns, 1 means the abstract matched the criterion 0 means it did not
		
		

Advanced usage:
	- This can be also filter entire papers, return matching sentences, etc. Ask me if you want that.
	- You can write your own additional regexes and add them to regexes.py or ask me for help.
