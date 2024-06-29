# data-individual-project

This project demonstrates the creation of a star schema data warehouse to track video starts over time using raw data.

## Data Source

The data includes columns for DateTime, VideoTitle, and events. I will filter the data to include only rows where the event contains "206", indicating a video start.

## Star Schema Design

The star schema consists of the following tables:

- **Fact Table**: FactVideoStart
- **Dimension Tables**: DimDate, DimPlatform, DimSite, DimVideo

![Star Schema](images/data_schema.png)

## Steps to Create the Data Warehouse

1. Filter raw data to include only relevant events.
2. Create dimension tables.
3. Populate dimension tables with unique values.
4. Create and populate the fact table with references to the dimension tables.

## How to Run the SQL Scripts

1. Clone the repository.
2. Import the raw data from `raw_data/raw_data.csv`.
3. Execute the SQL scripts in the following order:
    - `sql_scripts/create_tables.sql`
    - `sql_scripts/insert_data.sql`
    - `sql_scripts/queries.sql`

## License

This project is licensed under the MIT License.
