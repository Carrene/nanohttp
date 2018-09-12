from bddrest import status, response, given

from nanohttp import Application, Controller, action, html, json, text, \
    xml, binary
from nanohttp.tests.helpers import Given, when

app_init_calls = 0
begin_response_calls = 0
begin_request_calls = 0
end_response_calls = 0

def test_application_hooks():
    class Root(Controller):
        @action
        def index(self):
            yield 'Index'

    class TestApp(Application):
        def app_init(self):
            global app_init_calls
            app_init_calls += 1

        def begin_request(self):
            global begin_request_calls
            begin_request_calls += 1

        def begin_response(self):
            global begin_response_calls
            begin_response_calls += 1

        def end_response(self):
            global end_response_calls
            end_response_calls += 1

    with Given(TestApp(Root())):
        assert status == 200
        assert app_init_calls == 1
        assert begin_response_calls == 1
        assert begin_request_calls == 1
        assert end_response_calls == 1

        when()
        assert status == 200
        assert app_init_calls == 1
        assert begin_response_calls == 2
        assert begin_request_calls == 2
        assert end_response_calls == 2
