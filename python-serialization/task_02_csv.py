#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(filename):
    try:
        data_list = []

        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data_list.append(row)

        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data_list, f)

        return True

    except Exception:
        return False
