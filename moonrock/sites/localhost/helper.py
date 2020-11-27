"""
Constants and methods used in testing
"""

class Colors():
    WHITE = 'rgba(255, 255, 255, 1)'
    RED_ERROR = 'rgba(220, 53, 69, 1)'


users = {
 'valid_user': {'first_name':'Shinji',
                'last_name': 'Ikari',
                'user_name': 'sikari',
                'address1': '123 Main St.',
                'country': 'United States',
                'state': 'California',
                'zip': '12345',
                'name_on_card': 'John Galt',
                'number_on_card': '1111111111111',
                'cvv': '111'},
 'user_wo_username':{
                'first_name':'Shinji',
                'last_name': 'Ikari',
                'address1': '123 Main St.',
                'country': 'United States',
                'state': 'California',
                'zip': '12345',
                'name_on_card': 'John Galt',
                'number_on_card': '1111111111111',
                'cvv': '111'
 },
 'user_invalid_cc':{
                'first_name':'Shinji',
                'last_name': 'Ikari',
                'user_name': 'sikari',
                'address1': '123 Main St.',
                'country': 'United States',
                'state': 'California',
                'zip': '12345',
                'name_on_card': 'John Galt',
                'number_on_card': '4671100111123',
                'cvv': '111'
 }, 
}
