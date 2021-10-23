import os


def test_user(client, capsys):
    res = client.get('/hs')


    captured = capsys.readouterr()

    assert 'error' not in captured.err
    assert b'ok' in res.data
