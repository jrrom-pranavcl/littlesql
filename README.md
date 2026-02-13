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

```

```

## Syntax:

### Displaying expressions

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

```sql
DROP DATABASE name;
```

```
Database name successfully dropped.
```

### Displaying all the databases

```sql
SHOW DATABASES;
```

```
name
```

### Selecting a database

```sql
USE name;
```

```
Database name successfully selected.
```

### Creating a table
