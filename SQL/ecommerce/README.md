# E-commerce SQL Analysis
This project demonstrates SQL data analysis on a mock e-commerce dataset. The goal is to showcase the ability to write and run SQL queries using SQLite database and Python for exploratory data analysis including visualization.


## Project Overview
- Simulated e-commerce datasets for users, products, orders, and payments using Python
- Stored data in an SQLite database
- Performed SQL queries to analyze revenue by product category and revenue over time (sqlite3)
- Visualized results using Python libraries (pandas, seaborn, and matplotlib)


## Folder Structure
```
ecommerce-sql-analysis/
├── data/               #Simulate datasets and save as CSV files (users, products, orders, payments)
├── sql/                #Create SQL database and write SQL queries using Python sqlite3
└── README.md           #Project summary and instructions
```


## Tools and Key Skills
- Tools: SQLite, Jupyter Notebook, Python (pandas, numpy, faker, matplotlib, seaborn, sqlite3)
- SQL: joins, aggregations, filtering, grouping, ordering, date functions
- Python: data manipulation, interaction with SQLite using sqlite3, visualization


## Steps to Replicate or Extend the Analysis
1. Load the CSV data files located in the `data/` folder, or simulate your own data following Jupyter Notebook `simulate_data.ipynb` in the `data/` folder (maintain the same data structure)
2. Use the Jupyter notebook `01_create_db.ipynb` in the `sql/` folder to create the SQLite database
3. Run SQL queries from the Jupyter notebook `02_sql_queries.ipynb` in the `sql/` folder or write your own queries using Python's sqlite3 library
4. Explore visualizations using matplotlib and seaborn


## Contact
If you would like to collaborate or provide feedback, please contact me on www.linkedin.com/in/yumiko-siegfried-95b61a232
