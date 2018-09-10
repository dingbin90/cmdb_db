import requests
import copy

SALT_API = {
    "url":"http://172.17.1.199:8000",
    'user':'saltapi',
    'password':"password"
}
class SaltApi(object):
    def __init__(self):
        self._user = SALT_API['user']
        self._passwd = SALT_API['password']
        self.url = SALT_API['url']
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        self._base_data = dict(
            username = self._user,
            password = self._passwd,
            eauth = 'pam'
        )

        self._token = self.get_token()


    def get_token(self):
        params = copy.deepcopy(self._base_data)
        ret = requests.post(url=self.url+'/login',verify=False, headers=self.headers, json=params)
        ret_json = ret.json()
        token = ret_json['return'][0]['token']
        return token



    def _post(self,**kwargs):
        headers_token = {'X-Auth-Token': self._token}
        headers_token.update(self.headers)
        ret = requests.post(url=self.url, verify=False, headers=headers_token, **kwargs)
        ret_code,ret_data = ret.status_code,ret.json()
        return (ret_code,ret_data)

    def run(self, params):
        """ remote common interface, you need custom data dict
            for example:
                params = {
                    'client': 'local',
                    'fun': 'grains.item',
                    'tgt': '*',
                    'arg': ('os', 'id', 'host' ),
                    'kwargs': {},
                    'expr_form': 'glob',
                    'timeout': 60
                }
         """
        r = self._post(json=params)
        return r[1]['return'][0]




if __name__ == "__main__":
    data = {
            'client':'local',
            'fun':'cmd.run',
            'tgt':'*',
          #  'arg':('os','id','host'),
            'arg':('date'),
            'kwarg':{},
            'expr_form':'glob',
            'timeout':60
        }
    obj = SaltApi()
    ret = obj.run(data)
    print(ret)




















