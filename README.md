# Geospatial-Analysis-of-NexRad-and-GEOS-satellite


## About 
The Storm EVent ImagRy (SEVIR) dataset is a collection of geographically and chronologically aligned images that include meteorological events that were photographed by radar and satellite. <br>
This dataset was produced using freely accessible NOAA datasets, such as those from the GOES-16 geostationary satellite and NEXRAD weather radar data, both of which are accessible on the Registry of Open Data on AWS.<br>
##### We focused on this geospatial data to build a streamlit application for data exploration that leverages publicly available data and makes it easier for data analysts to download and work on.
<br>

Dataset: <br>
* GOES - [https://registry.opendata.aws/noaa-goes/]
* NEXRAD - [https://registry.opendata.aws/noaa-nexrad/]


![sevir_sample](https://user-images.githubusercontent.com/114712818/218191862-49f8f32b-bc77-4e03-ae81-9ebac16b514a.gif)

## Links
* Codelab Documentation - [link](https://codelabs-preview.appspot.com/?file_id=1CwPu13u5ciGguLL0QcZjw2f8TZfOqSlW74EaKc7tRBE/#2)
* GitHub Organization - [link][https://github.com/BigDataIA-Spring2023-Team-12]
---

## Process Flow
1. Web scrap the data from GOES and NEXRAD's AWS bucket publicly available
2. Convert the raw metdata into JSON format
3. Push the collected data into a SQLite database and then on a AWS bucket 
4. Create a Streamlit application with 2 pages each for GOES and NEXRAD
5. Implement the features for  a user to get data in two ways, either directly using the file name or by giving drop down options to select the file path
6. The application should generate a URL which will directly download the required file from the AWS bucket created
7. Plot NEXRAD locations on a map using streamlit
8. Use great-expectations to validate the data
9. Initialize great expectations, and fetch the data from the database and convert it to a csv file for both GOES and NEXRAD
10. Create a new datasource and suite for each of the dataset
11. Edit, add new expectations or delete unecessary expectations from the suite and generate reports
12. Write test cases using Pytest
12. Host the streamlit application on streamlit cloud


<br>

## LEARNINGS/TECH USED
Streamlit<br>
AWS<br>
SQLite<br>
Great-Expectations<br>
Documentation on Codelabs<br>
Pytest<br>
Git (Version Control)



---
## Team Members
1. Harsh Shah - NUID: 002704406 - (shah.harsh7@northeastern.edu)
2. Parva Shah - NUID: 002916822 - (shah.parv@northeastern.edu)
3. Dev Shah - NUID: 002978981 - (shah.devs@northeastern.edu)



## Undertaking

> WE ATTEST THAT WE HAVEN’T USED ANY OTHER STUDENTS’ WORK IN OUR ASSIGNMENT AND ABIDE BY THE POLICIES LISTED IN THE STUDENT HANDBOOK

**Contribution**: 
*   Harsh Shah &emsp; :`33.33%`
*   Parva Shah &emsp; :`33.33%`
*   Dev Shah &emsp;   :`33.33%`


