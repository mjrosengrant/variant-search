# Set Up:
```
pip install -r requirements.txt`
python manage.py import_data`
python manage.py runserver`
 ```
 
 
Notes
- For import_data command to work, the file `variant_results.tsv` must be added to the project root directory`.
Download this from `http://clinvitae.invitae.com/download` 
- By default the app is connected to a Postgres instance running on Heroku. Please excuse the hardcoded credentials; In production code that would never happen ;)


# Assignment

Create a genomic variant web application that allows a user to search for genomic variants based on a gene name and display the results in a tabular view.

Features

-------------  

1) A user will enter a gene name and hit a search button which will result in a list of genomic variants for that gene being displayed.  The display of the list of genomic variants will be in a tabular view that allows the user to see the various attributes associated with each genomic variant.

 
2) To assist the user with entering the gene name to search for, provide a type-ahead or auto-suggest feature such that upon typing the first two or more letters of a gene name, a list of gene names that start with those characters is available for the user to choose from. 

 
3) Provide two RESTful endpoints supporting the functionality listed in steps 1 and 2 so that it can be easily consumed by other applications such as command-line apps or reused by the genomic variant web application itself if it is implemented as a single-page app.





