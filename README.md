# Search images demo

## Api
### /api/v1/sizing
#### methods
    POST
#### PARAM
||||
|-|-|-|
|Vectors|int|>0|
|Dimensions|int|(0,16384]|
|Data|str|float/bytes|
|Index|str|FLAT/IVFFLAT/IVFSQ8/IVFSQ8H|
|Single|bool|True/False|
|[Cluster]|int|>0|



## how to use

    python3 src/app.py
