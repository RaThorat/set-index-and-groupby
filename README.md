# set-index-and-groupby
## A better way to summerize a table information in pandas
This script answers: Is there a better way to summerize a table information instead of using iloc and append method with nested loops in pandas?

https://stackoverflow.com/questions/74335925/is-there-a-better-way-to-summerize-a-table-information-instead-of-using-iloc-and

https://medium.com/@rn755947/a-better-way-to-summerize-a-table-information-in-pandas-8d243a9d31d

## Chat_GPT's response to the answer file

This code creates a pandas DataFrame from a dictionary of data and then reshapes it to show a list of disciplines for each application number.

There are a couple of things I would suggest to improve the code:

The variable out is a DataFrame, so it is more conventional to call the .to_csv() method to write it to a csv file, instead of using the print() function to display it.

The All_Discipline_count field in the output will always be the same as the number of disciplines in the Discipline_list field. It would be better to remove it as it's not adding any value.
