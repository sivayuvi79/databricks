# Databricks notebook source
from myfunctions import *

tableName   = "diamonds"
dbName      = "default"
columnName  = "clarity"
columnValue = "VVS2"

# If the table exists in the specified database...
if tableExists(tableName, dbName):

  df = spark.sql(f"SELECT * FROM {dbName}.{tableName}")

  # And the specified column exists in that table...
  if columnExists(df, columnName):
    # Then report the number of rows for the specified value in that column.
    numRows = numRowsInColumnForValue(df, columnName, columnValue)

    print(f"There are {numRows} rows in '{tableName}' where '{columnName}' equals '{columnValue}'.")
  else:
    print(f"Column '{columnName}' does not exist in table '{tableName}' in schema (database) '{dbName}'.")
else:
  print(f"Table '{tableName}' does not exist in schema (database) '{dbName}'.") 

# COMMAND ----------

# MAGIC %pip install pytest

# COMMAND ----------

import pytest
import os
import sys

repo_name = "databricks"

# Get the path to this notebook, for example "/Workspace/Repos/{username}/{repo-name}".
notebook_path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()

# Get the repo's root directory name.
repo_root = os.path.dirname(os.path.dirname(notebook_path))

# Prepare to run pytest from the repo.
os.chdir(f"/Workspace/{repo_root}/{repo_name}")
print(os.getcwd())

# Skip writing pyc files on a readonly filesystem.
sys.dont_write_bytecode = True

# Run pytest.
retcode = pytest.main([".", "-v", "-p", "no:cacheprovider"])

# Fail the cell execution if there are any test failures.
assert retcode == 0, "The pytest invocation failed. See the log for details."
