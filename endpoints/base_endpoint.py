class BaseEndpoint:
    response = None
    data = None

    def check_response_is_200(self):
        assert self.response.status_code == 200

    def check_response_is_400(self):
        assert self.response.status_code == 400

    def check_response_is_500(self):
        assert self.response.status_code == 500
