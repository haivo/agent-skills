# Report template

The success report is produced entirely by `scripts/profile.py` and shown
verbatim. This file only defines how errors are presented.

---

## Error section

Could not profile `{path}`.

```
{the full Error: line from the script}
```

Check that the path is correct and points to a plain .csv file, then run the
command again.
