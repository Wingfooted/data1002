# this is the project for data1002
Assignment 1. 

main.py processes the market data and returns the market_data.csv file. 

Data was sourced from www.dolthub.com

https://www.dolthub.com/repositories/post-no-preference/stocks/query/master?active=Tables&q=SELECT+*%0AFROM+%60ohlcv%60%3B

Dolthub is a gitstyle tool for uploading databases. post-no-preference/stocks is a dataset containing trading information for US stocks. Information contained is open hgih low close volume for each day.
On the top right corner under options was an option to download the resulting table from the below SQL as a csv file
This CSV file was then processed by main.py and turned into market data

SQL:

SELECT * FROM ohlcv;
