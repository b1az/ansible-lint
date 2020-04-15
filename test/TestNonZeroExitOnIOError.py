import pytest
from ansiblelint import RulesCollection


@pytest.mark.xfail(raises=IOError)
def test_running_nonexistent_file_raises_ioerror():
    RulesCollection().run({"path": "no_such_playbook"})
