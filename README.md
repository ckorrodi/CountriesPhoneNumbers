# SMS HELPER
Api to help you with all sms problems related

## Usage
### VALIDATE MOBILE PHONE
[GET] localhost/validate/351-000000000
```
{
  "country": "PORTUGAL",
  "country_code": "+351",
  "country_iso": "PT",
  "local_length": "9",
  "trunk_prefix": null
}
```
#### Legend
- country_iso: Alpha 2 Code [https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes]
- country: Country name
- country_code: International country code
- trunk_perfix: A trunk prefix is a digit sequence to be dialed before a telephone number to initiate a telephone call for the purpose of selecting an appropriate telecommunications circuit by which the call is to be routed. [https://en.wikipedia.org/wiki/Trunk_prefix]
- local_lenght: Country local lenght


### VALIDATE SMS PARTS
[POST] localhost/sms/count
[PAYLOAD]
```
{
    "message":"Teste"
}
```
[RESPONSE]
```
{
    "encoding": "GSM_7BIT",
    "length": 50,
    "messages": 1,
    "per_message": 160,
    "remaining": 110
}
```

#### Legend
- encoding: message encoding
- length: message size
- messages: parts
- per_message: chars per message
- remaining: Remaining char for the current part


## Install deps
pip install Flask





