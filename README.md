# compute_canada_sql_demo
Boilerplate code for logging data to a mysql database

## How to run
1. Install mysql connector by running: 
``` bash
pip install mysql-connector-python
``` 

2. Add the correct credentials in credentials.json. You can get a database server on Compute Canada by following these instructions: 
https://docs.computecanada.ca/wiki/Database_servers 

3. Edit the mysql_demo.py file by adding your compute canada username (This is required because CC only allows you to make databases that start with your CC username). 

4. Run the following command to log some data to the database: 

``` bash
parallel python mysql_demo.py --name sweep_test --step-size 1e-2 1e-3 1e-4 1e-5 --b2 0.9 0.99 --b1 0 0.9 0.99 --seed 0 1 2 3 4 5 6 7 8 9  --run ::: {0..239} 
```

The command will run 239 jobs and and store the data in the database. You can look at the data by executing the following commands: 

1. use COMPUTE_CANADA_USERNAME_sweep_test; 
2. select * from runs; 
3. select * from error;
4. select * from predictions; 
