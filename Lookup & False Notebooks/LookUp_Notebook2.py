dbutils.widgets.text("weekday", "7")

weekday_value = dbutils.widgets.get("weekday")
if weekday_value.isdigit():
    var = int(weekday_value)
else:
    var = weekday_value

dbutils.jobs.taskValues.set(key = "weekoutput", value = var)