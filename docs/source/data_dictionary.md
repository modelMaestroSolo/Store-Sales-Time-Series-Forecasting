# DATA DICTIONARY
Contains granular details about each variable. 

## Surface Properties of Dataset 

|          | Number of Instances | Number of Attributes |   Attributes                   | Attribute Types | Contains Missing Values? | Mismatches Btn Data and Metadata File |
|----------|---------------------|----------------------|----------------------|------------------|---------------------------|--------------------------------------------|
| train    |    3000888          |        6             |  'id', 'date', 'store_nbr', 'family', 'sales', 'onpromotion'                    | numerical, categorical |    No         |          No                             |
| test     |     28512           |       5              |  'id', 'date', 'store_nbr', 'family',  'onpromotion'                    | numerical, categorical |    No         |          Yes: 16 days not 15 days       |
| holiday_events| 350           |         6             |  'date', 'type', 'locale', 'locale_name', 'description', 'transferred'                    |  categorical, bool           |    No         |          No                       |
| oil    |     1218                |       2            |    'date', 'dcoilwtico'                 |   numerical               |    Yes        |          No                          |
| stores    |       54              |      5            | 'store_nbr', 'city', 'state', 'type', 'cluster'                     |  categorical              |    No      |            NO                           |
| transactions    |    83488           |  3      | 'date', 'store_nbr', 'transactions'                    |   numerical, categorical  |   No        |             No               |            |



