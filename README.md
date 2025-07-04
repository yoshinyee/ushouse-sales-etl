##  US House Sales Data ETL Project

This project demonstrates a simple **ETL (Extract, Transform, Load)** pipeline using Python and SQLite. It processes raw house sales data from a CSV file, cleans and transforms the data, calculates city and property-type level statistics, and stores everything into a local SQLite database for further analysis or reporting.

---

##  Tech Stack

- **Python 3.10+**
- **Pandas** – data manipulation and cleaning
- **SQLite** – lightweight relational database
- **SQLAlchemy** – database engine
- **sqlite3** – native SQLite interface for data verification

---

##  Project Structure

```
house-sales-etl/
├── data/
│   └── us_house_Sales_data.csv       # Raw input data
├── output/
│   └── ushouse.db                    # Output SQLite database
│   └── house_sales.csv               # Output after Data Cleaning for Power Bi project
│   └── ushouse.pbix                  # Power Bi Project
├── src/
│   └── main.py                       # Main ETL script
├── requirements.txt                  # Python dependencies
├── README.md                         # Project documentation
├── Licence                          
└── .gitignore


```

---

##  ETL Process Overview

###  Extract
- Loads raw CSV file containing U.S. house sales data.

###  Transform
- Cleans price values (removes `$` and commas)
- Extracts numeric values from fields like `"3 bds"`, `"2 ba"`, `"1200 sqft"`
- Converts `Price`, `Bedrooms`, `Bathrooms`, `Area (Sqft)`, `Lot Size` to integer types
- Groups data by `City` and `Property Type` to calculate average price
- Filters `For Sale` listings and calculates their average price by `City` and `Property Type`

###  Load
- Saves cleaned data to `house_sales` table
- Saves city and property type average prices to `city_avg_price`
- Saves average prices of listings marked `For Sale` to `forsale_avg_price`

---

##  Sample Output

```text
 Tables in the database:
 - house_sales
 - city_avg_price
 - forsale_avg_price

   City   |  Property Type  |  Price
----------|-----------------|---------
Austin    | Single Family   | 458231
Fresno    | Townhouse       | 389724
Miami     | Condo           | 659301
...
```

---

##  How to Run This Project

### 1. Clone the repository

```bash
git clone https://github.com/yoshinyee/ushouse-sales-etl.git
cd ushouse-sales-etl
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your CSV file  
Data source: **Kaggle**

Place your raw data file inside the `data/` folder and name it:

```
us_house_Sales_data.csv
```

### 4. Run the ETL script

```bash
python src/main.py
```

## 5. Verify the output

You can open `output/ushouse.db` using any SQLite client such as [DB Browser for SQLite](https://sqlitebrowser.org).

You will find:
- `house_sales` — cleaned full dataset
- `city_avg_price` — average prices by city and property type
- `forsale_avg_price` — average prices for listings marked as "For Sale"

---

##  Requirements

- Python 3.10+
- pandas
- sqlalchemy

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---
## Power BI Integration

You can import output/house_sales.csv into Power BI for interactive visualizations.
The ushouse.pbix file (if included) provides a sample dashboard with:

-Status count breakdown

-Average price by State

-Average Area (sqft) by property type and city

![image](https://github.com/user-attachments/assets/e783bc7c-0631-4b77-84c9-1b40d2936336)

##  Author Notes

This project is a self-learning initiative:
- Data sourced from **Kaggle** with link : https://www.kaggle.com/datasets/abdulwadood11220/usa-house-sales-data 
- Data cleaning and transformation with **Pandas**
- Full ETL pipeline using **Python**
- Relational storage using **SQLite**
- Verified queries with **sqlite3**
- Data Visualization with **Power BI**

---

## 📃 License

MIT License © 2025


