from unittest import TestCase, mock
from etl_twaren.es_api.index import create_process

mock_ctx = {
    "analy_es_object": "es_object",
    "index_properties": {
        "name": "index_name",
        "body": "index_body"
    },
    "is_created_new_index": None
}


class TestIndex(TestCase):
    @mock.patch("etl_twaren.es_api.index.already_exist")
    def test_index_already_exist(self, already_exist_mock):
        already_exist_mock.return_value = True
        result_ctx = create_process(mock_ctx)

        self.assertFalse(result_ctx["is_created_new_index"])

    @mock.patch("etl_twaren.es_api.index.create")
    @mock.patch("etl_twaren.es_api.index.already_exist")
    def test_create_new_index(self, already_exist_mock, create_mock):
        already_exist_mock.return_value = False

        result_ctx = create_process(mock_ctx)

        # check create call
        create_mock.assert_called_with({
            "es_object": mock_ctx["analy_es_object"],
            "index_properties": mock_ctx["index_properties"]
        })
        self.assertTrue(result_ctx["is_created_new_index"])
