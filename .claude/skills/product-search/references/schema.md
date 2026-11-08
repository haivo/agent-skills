# products table

Created by `_ensure_seeded()` in `simple_agent.py` if it does not exist.

| Column   | Type    | Notes                     |
|----------|---------|---------------------------|
| id       | SERIAL  | primary key               |
| name     | TEXT    | product name, not null    |
| category | TEXT    | not null                  |
| price    | NUMERIC | not null                  |

Search query used by the tool:

```sql
SELECT name, category, price FROM products
WHERE name ILIKE '%<keyword>%' OR category ILIKE '%<keyword>%'
```

## Seed data (inserted only when the table is empty)

| name                | category    | price  |
|---------------------|-------------|--------|
| Wireless Mouse      | Electronics | 19.99  |
| Mechanical Keyboard | Electronics | 79.99  |
| Standing Desk       | Furniture   | 249.00 |
| Office Chair        | Furniture   | 149.50 |
| USB-C Hub           | Electronics | 24.99  |
| Desk Lamp           | Furniture   | 34.95  |
