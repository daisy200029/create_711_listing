
import requests
import json
import cmd


class CarousellTestShell(cmd.Cmd):
    # All paramete
    base_url = "https://icetea.carousell.com"
    headers = {'Authorization': ''}

    # ALL Endpoints
    login_endpoint = "/api/2.0/login/"
    bump_endpoint = "/api/2.5/helper/products/bump/"

    def do_get_token(self, args):
        '''
        Description: Get user token
        Example: 
            get_token 001stage stage123
        Flow:
            request  --> 
            token    <--
        '''
        try:
            usr, pwd = args.split()
            self.__login(usr, pwd)
        except:
            print 'login error = example: get_token 001stage, stage123'


    def __login(self, usr, pwd):
        '''
        private method: this is a common method
        for user login action

        '''
        data = {'username': usr, "password": pwd}
        jsonstr = self.__post(self.login_endpoint, data)
        token = jsonstr['token']
        self.headers['Authorization'] = "Token " + token
        print token

    def __get(self, endpoint):
        '''
        private method: this is a common method
        for get request

        '''
        res = requests.get(
            self.base_url + endpoint,
            headers=self.headers,
        )
        json_text = res.text
        jsonstr = json.loads(json_text)
        return jsonstr

    def __post(self, endpoint, data):
        '''
        private method: this is a common method
        for post request

        '''
        res = requests.post(
            self.base_url + endpoint,
            data=data
        )
        json_text = res.text
        jsonstr = json.loads(json_text)
        return jsonstr

if __name__ == '__main__':
    CarousellTestShell().cmdloop()
