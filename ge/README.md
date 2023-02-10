# Using great expectations to validate the data scrapped for GOES and Nexrad.
 > [Great Expectations](https://greatexpectations.io/) is the leading tool for validating, documenting, and profiling your data to maintain quality and improve communication between teams


# Process
* __Setting up Great Expectations__ <br>
To setup great expectation package, you'll need python(3.7 or later), pip instll for python packages, git, and a browser to view the validation reports.
Environment Configuration: <br>
1. Create a python environment and activate it
2. Install module `great_expectations`
```bash
pip install great_expectations
```
3. Verify the version
```bash
great_expectations --version
```
4. Initialize at the base dir
```bash
great_expectations init
```
Change working dir to the newly created dir, `great_expectations`
```bash
cd great_expectations
```
5. Configure the data for datasource
Copy the created csv into `great_expectations/data`
Here, the data is being fetched from the our SQLite db `meta_data.db`, which contains 2 tables for each use case : GOES and NEXRAD. 
The data collected is converted into a csv and stored as `goes.csv` and `nexrad.csv`.


* __Connect to Data__ <br>
1. Once the environment is configured, you should be able to connect to a datasource easily. The below command will initialise  new datasource
```bash
great_expectations datasource new
```
2. Follow through the steps on the terminal that will ask you to choose what data would you like to connect to, the processing tool to be used, and the path to the root directory where the data is stored.
3. If connected sucessfuly, a jupyter notebook will open in the browser. You can change the name of your data source and also have file parsing filters. (We have used \.csv to filter out only csv files from the data folder)
 * __Create Expectations__ <br>
1. With the datsource now connected, you can start created expectations to validate your data.
2. Each Expectation is a declarative, machine-verifiable assertion about the expected format, content, or behavior of your data. Great Expectations comes with dozens of built-in Expectations, and it’s possible to develop your own custom Expectations, too.
3. Initialize a new suite -
```bash
great_expectations suite new
```
4. Follow through the prompted questions on the terminal and answer as per your preferences. Once complted, a new juypter notebook will open in the browser.
5. You can go through the ipynb file comment out columns on which you do not want to have expectations run on. Save and run the notebook.
6. A new window will open up with the report of your suit.
7. You can also edit your expectations by opening the `suite_name.json` file in your great_expectations folder.
8. Add, edit or delete uneccessary expectations and run the following commmand-
```bash
great_expectations suite edit suite_name
```
A jupyter notebook will open, run the cell to see your updated report of the expectations.

Create checkpoints to have a track of your expectations reports.
```
great_expectations checkpoint new checkpoint_name
```
Uncomment the last cell of the jupyter notebook and run. 
A new tab will open up the Data Docs and you'll be able to see all your created checkpoints for a particular suite and be able to view the validation reports.

![Screenshot (341)](https://user-images.githubusercontent.com/114712818/218179626-81fa86a7-a9eb-4188-b80e-18c4c2365f5f.png)
![Screenshot (344)](https://user-images.githubusercontent.com/114712818/218179640-ca804d2c-ca3c-4e7b-b7d5-a26bf1df2980.png)
![Screenshot (346)](https://user-images.githubusercontent.com/114712818/218179657-1b688d5f-1b3c-4670-8f7c-c28f176b5bff.png)
![Screenshot (347)](https://user-images.githubusercontent.com/114712818/218179665-d6fb202b-0703-4bd1-8580-c6c0b710cc32.png)
![Screenshot (348)](https://user-images.githubusercontent.com/114712818/218179677-0c4d8cef-0de4-47a5-8401-0f7f1518b3c4.png)