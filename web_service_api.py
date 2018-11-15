from app_settings import DEBUG
import requests
import json


class WebServiceAPIException(Exception):
    def __init__(self, err_code, err_msg):
        self.err_code = err_code
        self.err_msg = err_msg


class WebServiceAPI(object):
    def __init__(self):
        return

    def get_access_token(self):
        raise NotImplementedError

    def refresh_access_token(self):
        raise NotImplementedError

    def get_suite_access_token(self):
        raise NotImplementedError

    def refresh_suite_access_token(self):
        raise NotImplementedError

    def get_provider_access_token(self):
        raise NotImplementedError

    def refresh_provider_access_token(self):
        raise NotImplementedError

    def http_call(self, url_type, args=None):
        short_url = url_type[0]
        method = url_type[1]
        response = {}
        for retry_cnt in range(0, 3):
            if 'POST' == method:
                url = self.__make_url(short_url)
                response = self.__http_post(url, args)
            elif 'GET' == method:
                url = self.__make_url(short_url)
                url = self.__append_args(url, args)
                response = self.__http_get(url)
            else:
                raise WebServiceAPIException(-1, 'unknown method type')

            # check if token expired
            if self.__token_expired(response.get('errcode')):
                self.__refresh_token(short_url)
                retry_cnt += 1
                continue
            else:
                break

        return self.__check_response(response)

    @staticmethod
    def __append_args(url, args) :
        if args is None:
            return url

        for key, value in args.items():
            if '?' in url:
                url += ('&' + key + '=' + value)
            else:
                url += ('?' + key + '=' + value)

        return url

    @staticmethod
    def __make_url(short_url) :
        base = "https://qyapi.weixin.qq.com"
        if short_url[0] == '/' :
            return base + short_url
        else:
            return base + '/' + short_url

    def __append_token(self, url):
        if 'SUITE_ACCESS_TOKEN' in url :
            return url.replace('SUITE_ACCESS_TOKEN', self.get_suite_access_token())
        elif 'PROVIDER_ACCESS_TOKEN' in url :
            return url.replace('PROVIDER_ACCESS_TOKEN', self.get_provider_access_token())
        elif 'ACCESS_TOKEN' in url :
            return url.replace('ACCESS_TOKEN', self.get_access_token())
        else:
            return url

    def __http_post(self, url, args) :
        real_url = self.__append_token(url)

        if DEBUG is True:
            print(real_url, args)

        return requests.post(real_url, data=json.dumps(args, ensure_ascii=False).encode('utf-8')).json()

    def __http_get(self, url):
        real_url = self.__append_token(url)

        if DEBUG is True : 
            print(real_url)

        return requests.get(real_url).json()

    def __post_file(self, url, media_file):
        return requests.post(url, file=media_file).json()

    @staticmethod
    def __check_response(response):
        err_code = response.get('errcode')
        err_msg = response.get('errmsg')
        if err_code is 0:
            return response 
        else:
            raise WebServiceAPIException(err_code, err_msg)

    @staticmethod
    def __token_expired(err_code) :
        if err_code == 40014 or err_code == 42001 or err_code == 42007 or err_code == 42009:
            return True
        else:
            return False

    def __refresh_token(self, url):
        if 'SUITE_ACCESS_TOKEN' in url:
            self.refresh_suite_access_token()
        elif 'PROVIDER_ACCESS_TOKEN' in url:
            self.refresh_provider_access_token()
        elif 'ACCESS_TOKEN' in url:
            self.refresh_access_token()
