This project implemented Unity Catalog in Databricks for secure, centralized data governance, while leveraging Delta Lake and Delta Tables for scalable, efficient storage. The data pipeline followed the Medallion Architecture (Bronze → Silver → Gold), ensuring data quality, reliability, and usability at every stage. The solution utilized Azure Data Factory, Azure Synapse, Azure Data Lake Storage, and Azure Databricks, also finalised with Delta Live Tables as an automated pipeline tool for serving our data in the SQL Data Warehouse for analytics and reporting, with Python and SQL for data transformation and scripting.

## PROJECT OVERVIEW

<img width="1320" height="736" alt="Group 4" src="https://github.com/user-attachments/assets/e4e25ee1-f539-4b3b-afc8-3e6affae184e" />

## Creating And Ingesting Raw Data with ADF
After provisioning the required resources for this project, I created a parameterized, dynamic data pipeline to ingest the five datasets needed for the project. The raw data was then stored in the Bronze container of Azure Data Lake within my resource group.
<img width="1434" height="737" alt="Screenshot 2025-09-15 at 06 11 23" src="https://github.com/user-attachments/assets/84ae5bb1-45a2-4153-83e2-d2399f47a0db" />
<img width="1434" height="737" alt="Screenshot 2025-09-15 at 06 37 13" src="https://github.com/user-attachments/assets/30db468e-6384-447c-aa07-855aee9b725b" />
<img width="1434" height="764" alt="Screenshot 2025-09-15 at 07 25 23" src="https://github.com/user-attachments/assets/fde43d6e-02d2-4858-85e8-d3b3eb1c1c84" />

## PHASE 2 TRANSFORMATION
To begin with Unity Catalog, I created a catalog named netflix_catalog, followed by configuring credentials and external locations mapped to the corresponding container in the data lake. In addition, I built a parameterized jobs pipeline in Databricks to ingest the five data sources required for the project. After ingesting i engaged in transformations of my data, which was very tedious.
<img width="1434" height="764" alt="Screenshot 2025-09-15 at 08 21 55" src="https://github.com/user-attachments/assets/a1ccc843-ae2f-47bf-a982-f1602d283b35" />
<img width="1434" height="764" alt="Screenshot 2025-09-15 at 17 10 02" src="https://github.com/user-attachments/assets/01bd970d-3181-4e60-ab67-d8fd817ed2c6" />
<img width="1434" height="764" alt="Screenshot 2025-09-15 at 17 40 42" src="https://github.com/user-attachments/assets/c8e1d0f9-7e68-44da-b2a1-8b93df8fc31d" />

## SERVING
After the transformation stage, the next step was data serving. I loaded the cleaned data into SQL Data Warehouses for analysis and BI reporting. In this process, I utilized Delta Live Tables (DLT), a declarative framework for building ETL pipelines, which allowed me to validate code and efficiently orchestrate the data pipeline process.
<img width="1434" height="764" alt="Screenshot 2025-09-17 at 13 40 24" src="https://github.com/user-attachments/assets/c6155a34-3f91-4756-a1e0-192b265f333c" />
<img width="1434" height="764" alt="Screenshot 2025-09-17 at 13 40 42" src="https://github.com/user-attachments/assets/f8968bf4-dcbc-4048-98b6-9fa58998793f" />
<img width="1434" height="764" alt="Screenshot 2025-09-17 at 13 44 39" src="https://github.com/user-attachments/assets/8d057287-ead6-4a6f-aa16-a8984c00e2c6" /><img width="1434" height="764" alt="Screenshot 2025-09-17 at 13 49 31" src="https://github.com/user-attachments/assets/8386caef-c34c-4926-becb-8595d1ede639" />

I attempted to load the data, fully aware it would return 0 since there were no new changes, and as expected, it did return 0.

<img width="1434" height="764" alt="Screenshot 2025-09-17 at 13 48 27" src="https://github.com/user-attachments/assets/4fefdec6-4d58-463d-97ab-1f27e3205e3c" />

## SQL WAREHOUSE QUERYING AND BI REPORTING

<img width="1434" height="764" alt="Screenshot 2025-09-17 at 13 56 56" src="https://github.com/user-attachments/assets/d3d86e63-ccc0-4eae-baac-321762ee7d22" />

<img width="1434" height="764" alt="Screenshot 2025-09-17 at 13 57 53" src="https://github.com/user-attachments/assets/a5bde673-2e0f-446c-b750-088fd04b2a6b" />

<img width="1434" height="764" alt="Screenshot 2025-09-17 at 13 56 10" src="https://github.com/user-attachments/assets/6bda1368-3a77-411c-a9fa-47518ea85755" />

## VISUALISATION
<img width="1434" height="764" alt="Screenshot 2025-09-17 at 14 09 10" src="https://github.com/user-attachments/assets/924470c8-b646-4fc3-80e4-9d085d8f24d8" />

## BI REPORTING
Thanks to Databricks Partner Connect, I was able to provide the BI connector to the Data Analyst, enabling them to directly query and visualize the cleaned data in Power BI with ease—without needing to rely on the SQL Data Warehouse. Followed after was loading my data in Synapse Warehouse.

