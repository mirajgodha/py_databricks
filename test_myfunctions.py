import pytest
import myfunctions

tableName   = "diamonds"
dbName      = "default"
columnName  = "clarity"
columnValue = "VVS2"

# Does the table exist?
def test_tableExists():
  assert myfunctions.tableExists(tableName, dbName) is True

# Does the column exist?
def test_columnExists():
  assert myfunctions.columnExists(tableName, dbName, columnName) is True

# Is there at least one row for the value in the specified column?
def test_numRowsInColumnForValue():
  assert myfunctions.numRowsInColumnForValue(tableName, dbName, columnName, columnValue) > 0
