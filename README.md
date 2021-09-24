# CountriesPhoneNumbers
Easy way to validate / check and work with phone

## Usage

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

## Install deps
pip install Flask


## Legend
- country_iso: Alpha 2 Code [https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes]
- country: Country name
- country_code: International country code
- trunk_perfix: A trunk prefix is a digit sequence to be dialed before a telephone number to initiate a telephone call for the purpose of selecting an appropriate telecommunications circuit by which the call is to be routed. [https://en.wikipedia.org/wiki/Trunk_prefix]
- local_lenght: Country local lenght


