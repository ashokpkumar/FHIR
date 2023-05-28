#http://hapi.fhir.org/baseR4/Patient/1231232?_pretty=true

#curl -X 'GET'   'https://hapi.fhir.org/baseR4/Patient?gender=male&given=john'   -H 'accept: application/fhir+json'
'''
https://hapi.fhir.org/baseR4/Patient?
address-city=Ketchum
&address-country=USA
&address-postalcode=98765
&address-state=ID
&birthdate=2020-01-01
&family=Doe
&gender=male
&given=john
&identifier=593274
&language=english
&phone=4450458282
&telecom=%28888%29%20888-8888
'''
"""[_content,
 _id, 
 _lastUpdated, 
 _profile, 
 _security, 
 _source, _tag, 
 _text, active, 
 address, address-city, 
 address-country, 
 address-postalcode, 
 address-state, 
 address-use, birthdate, 
 death-date, deceased, 
 email, family, gender, 
 general-practitioner, 
 given, identifier, 
 language, link, name, 
 organization, 
 phone, phonetic, 
 telecom]"""


from json import dumps

try:
    from urllib import urlencode, unquote
    from urlparse import urlparse, parse_qsl, ParseResult
except ImportError:
    # Python 3 fallback
    from urllib.parse import (
        urlencode, unquote, urlparse, parse_qsl, ParseResult
    )

def add_url_params(url, params):
    url = unquote(url)
    parsed_url = urlparse(url)
    get_args = parsed_url.query
    parsed_get_args = dict(parse_qsl(get_args))
    parsed_get_args.update(params)
    parsed_get_args.update(
        {k: dumps(v) for k, v in parsed_get_args.items()
         if isinstance(v, (bool, dict))}
    )
    encoded_get_args = urlencode(parsed_get_args, doseq=True)
    new_url = ParseResult(
        parsed_url.scheme, parsed_url.netloc, parsed_url.path,
        parsed_url.params, encoded_get_args, parsed_url.fragment
    ).geturl()
    return new_url