
import requests
import json
import cmd


class CarousellTestShell(cmd.Cmd):
    # All paramete
    base_url = "https://stage.carousell.io"
    headers = {
        'authorization': "Token 369e52be163522b9f4bb5ee27786d90112220fa4",
        'platform': "ios",
        }
    # ALL Endpoints
    login_endpoint = "/api/2.0/login/"
    create_711 = "/api/3.1/listings/"
    fd = open("OUT.PNG", "rb")


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

    def do_create_711(self, args):
        try:
            title = args.split()
            print title
            data = { 
                "mailing": "false",
                "meetup":"false",
                "shipping_tw_711":"true",
                "title":title,
                "price":117.0,
                "condition":1,
                "collection_id":1113,
                "size": "WOMEN_BOTTOMS_FREESIZE",
                }
            files = {
                    "photo_0": self.fd
                }

            self.__post(self.create_711, data=data,files=files,headers=self.headers)

        except:
            print 'example: create_711  <<title>>'



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

    def __post(self, endpoint, data,files,headers):
        '''
        private method: this is a common method
        for post request

        '''
        res = requests.post(
            self.base_url + endpoint,
            data=data,
            files=files,
            headers=headers
        )
        json_text = res.text
        jsonstr = json.loads(json_text)
        return jsonstr
    def do_exit(self,*args):
        return True

if __name__ == '__main__':
    CarousellTestShell().cmdloop()
