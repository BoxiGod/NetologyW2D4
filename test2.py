import app2


class TestApp:

    def test_create_folder(self):
        name = 'folder'
        uploader = app2.YaApi()
        uploader.create_folder(name)
        exist = app2.requests.get('https://cloud-api.yandex.net/v1/disk/resources?path=' + '%2F'
                                  + name, headers=uploader.headers)
        assert exist.status_code == 200

    def test_delete_folder(self):
        name = 'folder'
        uploader = app2.YaApi()
        uploader.delete_folder(name)
        exist = app2.requests.get('https://cloud-api.yandex.net/v1/disk/resources?path=' + '%2F'
                                  + name, headers=uploader.headers)
        assert exist.status_code != 200
