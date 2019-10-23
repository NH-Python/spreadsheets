# NH Python Group Project Night

### Project Night: Spreadsheets in Python; CSV/Pandas, XLS and Google Sheets
In this all-skill-levels project night we’ll be tackling spreadsheets of all kinds. If you want to interact with spreadsheets in Python, but you’re new to programming or new to Python, we’ll be happy to help you out. Or if you just want to get familiar with one of these libraries come hang out. Alexander Technology Group/ Bank W Holdings is hosting us at their offices (5 Bedford Farms Dr, Bedford, NH 03110) with pizza and drinks provided. Bring your laptop!

### Examples:
#### `csv_pandas.py`

Lorem ipsum

#### `excel.py`

Open `excel.xlsx` to view the "before" state of the file.

From `/spreadsheets` execute:

    python excel.py

This will change the contents and the formatting of the file, including inserting text, numbers, a formula, column autofit and background colors.

#### `sheets.py`
##### Setup
1) In your Google Drive account, create a worksheet titled `NH Python`
1) Follow steps **1 through 4** in the 'Using Signed Credentials' section [of this page](https://gspread.readthedocs.io/en/latest/oauth2.html).  (Step 4 is very important)
1) Rename the downloaded service account json file created above to `client_secret.json` and copy it into the `/spreadsheets` directory.
    
    **IMPORTANT**: _Do not commit this file to git.  `client_secret.json` is already in the `.gitignore` file of this repository; if you use a different name for the json file, the different name should be added to the `.gitignore` file as well_
##### Run
From `/spreadsheets` execute:
    
    python sheets.py

A multiplication table will be generated.  Also, each column and row in the table will be summed via formula.
