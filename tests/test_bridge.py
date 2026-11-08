from unfold_mcp import server

import hybridforgelab_unfold_mcp as bridge


def test_main_prints_the_notice_on_stderr_and_runs_the_bytestay_server(monkeypatch, capsys):
    calls = []
    monkeypatch.setattr(server, "main", lambda: calls.append("run"))
    bridge.main()
    out, err = capsys.readouterr()
    assert calls == ["run"]
    assert out == ""
    assert "bytestay-unfold-mcp" in err and "uvx --from bytestay-unfold-mcp unfold-mcp" in err
    assert err.count("\n") == 1
