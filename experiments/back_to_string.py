import urllib.parse

string = "urn:li:ts_hiring_project:', ['urn:li:ts_contract:', ('454254206', '1042246722')]"
print("string", string)
encoded_string = urllib.parse.quote(str(string), safe='')
print(encoded_string)
print("urn%3Ali%3Ats_hiring_project%3A%28urn%3Ali%3Ats_contract%3A454254206%2C1042246722%29" == encoded_string)

# urn:li:ts_hiring_project:(urn:li:ts_contract:454254206,1042246722)
