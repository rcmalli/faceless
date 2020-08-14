from faceless.utils import add_path_suffix


def test_add_path_suffix():
    path = "/tmp/test.mp4"
    assert "/tmp/test_faceless.mp4" == add_path_suffix(path=path)

