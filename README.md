# mini-CSVQL

A small SQL interpreter to interact with CSV files.

## Features:

- Case insensitive
- REPL and server frontend
- Supported commands:
  - `DROP`
  - `INSERT`
  - `PRINT`
  - `SELECT`
  - `SHOW`
  - `UPDATE`
  - `USE`

## Multiline REPL:

```sql
> DROP DATABASE company;
Database company successfully dropped.
> CREATE DATABASE company;
Database company successfully created.
> use company;
Database company successfully selected.
> CREATE TABLE employees (\
    id INT,\
    name STRING,\
    salary FLOAT);
Table employees successfully created
```

## Syntax:

### Displaying expressions

Used mostly for debugging.

```sql
PRINT 355 / 113;
```

```
3.1415929203539825
```

### Database creation

In mini-CSVQL, databases are just directories with a `database.json` file. To create a database, you must use the `CREATE DATABASE` command.

```sql
CREATE DATABASE name;
```

```
Database name successfully created.
```

### Database deletion

This command will delete the directory and everything inside it.

```sql
DROP DATABASE name;
```

```
Database name successfully dropped.
```

### Displaying all the databases

Shows all the database directories that can be selected in the working directory where the command was ran.

```sql
SHOW DATABASES;
```

```
name
```

### Selecting a database

In order to perform table operations we must select a database.

```sql
USE name;
```

```
Database name successfully selected.
```

### Table creation

Note: a database must be selected with `USE` before proceeding.

```sql
CREATE TABLE employees (\
    id INT,\
    name STRING,\
    salary FLOAT);
```

```
Table employees successfully created.
```

### Table deletion

```sql
DROP TABLE name;
```

```
Table successfully dropped.
```
