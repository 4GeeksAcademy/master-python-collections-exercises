def sort_records(records):
    return sorted(tuple(record.split(",")) for record in records)


# Try your function with different values
print(sort_records(['Tom,19,80', 'John,20,90', 'Jony,17,91', 'Jony,17,93', 'Jason,21,85']))
