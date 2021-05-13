# DGC_Validation
This Repository contains the source code to validate the Digital Green Certificate issued in the European Union.

## Glossary
DGC ... Digital Green Certificate
EU ... European Union
## Getting started

1. create an environment using Python 3.7
2. run 
    ```{bash}
    $ pip install -r requirements.txt
    ```
    in your terminal.
3. after installation run the code via
    ```{bash}
    $ uvicorn app.main:app --reload
    ```
4. Test the API 
    Test case: https://app.wien.gv.at/validierung?id=VUQ4SllIL1pxK0VVU0ZJOElqVUljbDU3QkJGMll2NHdvY0VFVkZNU3h6aG5GNmZPQTU1SUVOK0V2eVhRNEhxeQ

    - test the API via terminal
        Open a new terminal and copy
        
        ```{bash}
        curl -X 'GET' \
        'http://127.0.0.1:8000/verification/?qr_url=VUQ4SllIL1pxK0VVU0ZJOElqVUljbDU3QkJGMll2NHdvY0VFVkZNU3h6aG5GNmZPQTU1SUVOK0V2eVhRNEhxeQ&audit_trail=true&apikey=abcd' \
        -H 'accept: application/json'
        ```
        you should receive following output: 

        `[["S.","T.","1998","13.04.2021 12:38","26.04.2021 21:46","City of Vienna","VUQ4SllIL1pxK0VVU0ZJOElqVUljbDU3QkJGMll2NHdvY0VFVkZNU3h6aG5GNmZPQTU1SUVOK0V2eVhRNEhxeQ","Sebastians-MacBook-Pro.local"]]`

    - test the API via UI
        - Open in the browser: _http://127.0.0.1:8000/docs_ to test the API
        - Click **"get"** and **"Try it out"**
        
        | Name          | Description          |
        | ------------- |:-------------:| 
        | qr_url| VUQ4SllIL1pxK0VVU0ZJOElqVUljbDU3QkJGMll2NHdvY0VFVkZNU3h6aG5GNmZPQTU1SUVOK0V2eVhRNEhxeQ | 
        | audit_trail      | true      |   
        | apikey | abcd      |

        - you should see following response in Code 200
        ```{Python}
        [
            [
                "S.",
                "T.",
                "1998",
                "13.04.2021 12:38",
                "26.04.2021 21:44",
                "City of Vienna",
                "VUQ4SllIL1pxK0VVU0ZJOElqVUljbDU3QkJGMll2NHdvY0VFVkZNU3h6aG5GNmZPQTU1SUVOK0V2eVhRNEhxeQ",
                "Sebastians-MacBook-Pro.local"
            ]
        ]
        ```
## packaging

create function.zip:

```{}
cd venv/lib/python3.7/site-packages/
zip -r9 ../../../../function.zip .
cd ../../../../
zip -g ./function.zip -r app
```



## References

- [Proposal of DGC](https://ec.europa.eu/commission/presscorner/detail/en/ip_21_1181)
- [Official proposal document](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52021PC0130)
