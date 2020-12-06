import app


class TestApp:

    def test_add_doc_to_shelf(self):
        shelf_before = len(app.directories['3'])
        app.append_doc_to_shelf('123', '3')
        assert shelf_before + 1 == len(app.directories['3'])

    def test_remove_doc_from_shelf(self):
        docs_before = sum([len(value) for value in app.directories.values()])
        app.remove_doc_from_shelf('11-2')
        assert docs_before - 1 == sum([len(value) for value in app.directories.values()])

    def test_documents_existance(self):
        doc_exist = '2207 876234'
        doc_not_exist = '123'
        assert app.check_document_existance(doc_exist)
        assert not app.check_document_existance(doc_not_exist)
