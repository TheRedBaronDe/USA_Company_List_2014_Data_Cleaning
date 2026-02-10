import pandas as pd # import pandas to manipulate data and clean it so it can be imported into pgAdmin 4

file_path = r"C:\\Users\\User\\Documents\\PostgreSQL\\TWO_CENTURIES_OF_UM_RACES.csv"

df = pd.read_csv(
    file_path,
    engine="python", # forces Pandas to read the CSV file as a Python based parser
    sep=",", # separates each column with a comma
    quotechar='"', # tells Pandas that double quotes means strings/text, meaning that any commas inside double quotes should be treated as text as well
    escapechar='\\', # defines how to deal with escaped characters
    on_bad_lines='skip', # extremely important, tells Pandas to skip any row that cannot be parsed
    encoding='utf-8' # defines an enconding that supports international characters and prevents breaking/corruption
)

for col in df.select_dtypes(include='object').columns: # selects TEXT columns
    df[col] = (
        df[col]
        .astype(str) # converts to string
        .str.replace('"', '', regex=False) # removes double quotes inside the strings
        .str.replace("'", '', regex=False) # removes singular quotes inside the strings
    )

df.to_csv(
    r"C:\\Users\\User\\Documents\\PostgreSQL\\TWO_CENTURIES_OF_UM_RACES_CLEAN.csv", # saves the cleaned dataset so it can be imported into pgAdmin 4
    index=False # prevents Pandas from writing extra columns
    encoding='utf-8' # applies an international character encoding
)

print(len(df)) # prints the number of loaded rows, allowing you to verify lost rows and compare its size to the expectedd value of the full dataset
