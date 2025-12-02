files = [
    {
        "srcfolder": "netflix_directors",
        "src_targetfolder": "netflix_directors"
    },
    {
        "srcfolder": "netflix_cast",
        "src_targetfolder": "netflix_cast"
    },
    {
        "srcfolder": "netflix_category",
        "src_targetfolder": "netflix_category"
    },
    {
        "srcfolder": "netflix_countries",
        "src_targetfolder": "netflix_countries"
    },
    {
        "srcfolder": "netflix_titles",
        "src_targetfolder": "netflix_titles"
    }
]


dbutils.jobs.taskValues.set(key = "files", value = files)

