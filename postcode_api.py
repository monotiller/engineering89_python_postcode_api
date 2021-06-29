# # We already touched base on API using requests
# import requests
#
# check_response_postcode = requests.get("https://api.postcodes.io/postcodes/ct66hj")
#
# # # First iteration
# # if check_response_postcode == 200:
# #     print(f"The postcode is valid and returned with status code {check_response_postcode.status_code}")
# # else:
# #     print(f"Ooops, something went wrong. {check_response_postcode.status_code}, try again")
# #
# # # Second iteration
# if check_response_postcode:
#     print(f"Success with status code {check_response_postcode.status_code}")
# else:
#     print("Unavailable")
#
# # Research how requests is doing that behind the scenes
#
# # Third iteration
# # print(type(check_response_postcode.headers))
# #
# # # Let's see how we can parse or get the data from dict
# # print(check_response_postcode.json()) # json() converts that datat for us
#
# # Let's store this data in to a variale
# response_dict = check_response_postcode.json()
# # print(type(response_dict)) #  Let's check the data type now to ensure we could utilise this data
#
# result_dict = response_dict['result']
# # print(response_dict)
#
# for key in response_dict.keys():
#     print(f"The name of the key is {key} and the value inside is {result_dict[key]}")
#
# # Prompt the user to enter the postcode
# # Validate the postcode
# # Present the location back to the user with required message
# # Apply OOP

import requests

def check_response(postcode):
    return requests.get(f"https://api.postcodes.io/postcodes/{postcode}")

def check_response_code(postcode):
    return requests.get(f"https://api.postcodes.io/postcodes/{postcode}").status_code

def check_location(postcode):
    check_response = requests.get(f"https://api.postcodes.io/postcodes/{postcode}")
    response_dict = check_response.json()
    result_dict = response_dict['result']
    return "Lat: " + str(result_dict['latitude']) + " Long: " + str(result_dict['longitude'])

postcode = input("What is your postcode?")
print(check_response(postcode))
print(check_response_code(postcode))
print(check_location(postcode))