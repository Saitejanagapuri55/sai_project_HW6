import pytest
from app import App

@pytest.fixture
def app_instance():
    return App()

def test_environment_variables_loaded(app_instance):
    assert app_instance.get_environment_variable('ENVIRONMENT') == 'PRODUCTION'

def test_plugin_loading(app_instance):
    app_instance.load_plugins()
    assert 'greet' in app_instance.command_handler.commands
