from __future__ import print_function
from date_formats import get_date_formats


if __name__ == "__main__":
    data = get_date_formats()
    year_month_dict = dict(
        (lang_id.split("_")[0], d.get("yMMM")) for (lang_id, d) in data.items()
    )
    year_month_dict = dict(
        (lang_id, value)
        for (lang_id, value)
        in year_month_dict.items() if value and value != "MMM y"
    )
    print(year_month_dict)
