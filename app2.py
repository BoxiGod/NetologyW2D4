import requests


class YaApi:
    access_token = ""
    headers = {"Authorization": "OAuth " + access_token}

    def create_folder(self, name):
        create_url = 'https://cloud-api.yandex.net/v1/disk/resources?path=' + '%2F' + name
        create = requests.put(create_url, headers=self.headers)
        return create

    def delete_folder(self, name):
        create_url = 'https://cloud-api.yandex.net/v1/disk/resources?path=' + '%2F' + name
        create = requests.delete(create_url, headers=self.headers)
        return create


if __name__ == '__main__':
    uploader = YaApi()
    result = uploader.create_folder('folder')
    print(result.status_code)
