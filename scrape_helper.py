# Functions to help with our web scraping
import pandas as pd

def tableToDataFrame(table):
    # Process header row, building up a data frame with the sepcified columns
    col_names = ['Index']    # the first col is always the index
    row = table.find('tr')  # get the first row ( the header row)
    columns = row.find_all(['td', 'th']) # find all the columns in this row
    for column in columns:  # go through all the columns
        text = column.find(text=True)   # get the text from the column - this is the column name
        text = text.strip()
        col_names.append(text)  # add the column name to the list of column names
    df = pd.DataFrame(columns=col_names) # create a Pandas dataframe with the same column structure
    
    row_index = 0
    first_row = True

    # Find all the rows in the table. Rows are 'tr' elements within the table
    for row in table.find_all('tr'):
        #skip the first row, which is the header which we have already processed
        if first_row:
            first_row = False
            continue
        
        # Create a new row in the DataFrame
        df.loc[row_index] = ''
        
        # Find all the columns in this row. Columns are in 'td' elements within the row
        columns = row.find_all(['td','th'])
        
        # Iterate through the columns
        column_index = 1
        for column in columns:
            # Pull out all the text from the column
            text = "".join(column.findAll(text=True,recursive='True')).strip()
            # text = column.find(text = true)
            # text = text.strip()
            
            # set the value in the DataTable cell
            df.iat[row_index, column_index] = text

            column_index += 1
        row_index += 1
    return df