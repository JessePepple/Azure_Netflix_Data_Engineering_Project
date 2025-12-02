import dlt

lookup_tables = {
    "rule1" : "show_id is NOT NULL"
}

@dlt.table(
    name = "gold_netflixdirectors"
)
@dlt.expect_all_or_drop(lookup_tables)
def gold_netflixdirectors():
    df = spark.readStream.format("delta").load("abfss://silver@netflixdatalakejess.dfs.core.windows.net/netflix_directors")
    return df


@dlt.table(
    name = "gold_netflixcast"
)
@dlt.expect_all_or_drop(lookup_tables)
def gold_netflixcast():
    df = spark.readStream.format("delta").load("abfss://silver@netflixdatalakejess.dfs.core.windows.net/netflix_cast")
    return df
    

@dlt.table(
    name = "gold_netflixcategory"
)
@dlt.expect_all_or_drop(lookup_tables)
def gold_netflixcategory():
    df = spark.readStream.format("delta").load("abfss://silver@netflixdatalakejess.dfs.core.windows.net/netflix_category")
    return df


@dlt.table(
    name = "gold_netflixcountries"
)
@dlt.expect_all_or_drop(lookup_tables)
def gold_netflixcountries():
    df = spark.readStream.format("delta").load("abfss://silver@netflixdatalakejess.dfs.core.windows.net/netflix_countries")
    return df



@dlt.table(
    name = "gold_stg_netflixtitles"
)
@dlt.expect_all_or_drop(lookup_tables)
def gold_stg_netflixdirectors():
    df = spark.readStream.format("delta").load("abfss://silver@netflixdatalakejess.dfs.core.windows.net/netflix_titles")
    return df




@dlt.view
def gold_trans_netflixtitles():
    df = spark.readStream.table("LIVE.gold_stg_netflixtitles")
    df = df.withColumn("date_added", col("date_added").cast("date"))
    return df


master_rules = {
    "rule1" : "show_id is NOT NULL",
    "rule 2" : "date_added is NOT NULL"
}


@dlt.table
@dlt.expect_all_or_drop(master_rules)
def gold_netflixtitles():
    df = spark.readStream.table("LIVE.gold_trans_netflixtitles")
    return df


