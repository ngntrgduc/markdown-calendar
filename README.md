# markdown-calendar

Generate calendars as markdown tables using Python.

## Usage
```
usage: main.py [-h] [--year YEAR] [--month MONTH] [--whole_year]

options:
  -h, --help            show this help message and exit
  --year YEAR, -y YEAR  Choose the year. Default is the current year.
  --month MONTH, -m MONTH
                        Choose the month. Default is the current month.
  --whole_year, -w      Generate the whole year.
```

## Example

- Generate calendar of `2023/2`: 
```py
python main.py -y 2023 -m 2
```

```
   February 2023
|Mon|Tue|Wed|Thu|Fri|Sat|Sun|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|30|31|1|2|3|4|5|
|6|7|8|9|10|11|12|
|13|14|15|16|17|18|19|
|20|21|22|23|24|25|26|
|27|28|1|2|3|4|5|
```

- Generate calendar of specified year, with specified month:
```py
python main.py -y 2021 -m 1
```

- Generate calendar of whole specified year:
```py
python main.py -y 2021 -w
```

## Rendered in markdown example:
   February 2023
|Mon|Tue|Wed|Thu|Fri|Sat|Sun|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|30|31|1|2|3|4|5|
|6|7|8|9|10|11|12|
|13|14|15|16|17|18|19|
|20|21|22|23|24|25|26|
|27|28|1|2|3|4|5|