import requests

LOGIN_URL = 'https://ting.com/account/login'
ACCOUNT_USAGE_URL = 'https://ting.com/json/account/get_account_usage_details'

class Ting():

    def __init__(self):
        self._session = requests.Session()
        self._logged_in = False

    def login(self, email, password):

        form = {
            'email': email,
            'password': password,
            'existing_user_login': 'existing_user_login'
        }

        result = self._session.post(LOGIN_URL, data=form)

        # Did we sucessfully log in?
        login_successful = result.cookies['tingweb_user_logged_in'] == '1'

        if not login_successful:
            raise Exception("Login not indicated as successful.", result)

        self._logged_in = True

    def get_account_usage (self):

        if not self._logged_in:
            raise Exception("You are not logged in")

        acct_usage = self._session.get(ACCOUNT_USAGE_URL)

        return acct_usage.json()

if __name__ == '__main__':
    ting = Ting()

    ting.login('email@email.com', 'password')
    acct_usage = ting.get_account_usage()

    print(acct_usage)
