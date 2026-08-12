"""Smoke tests for pydump."""

import pytest
from pydump import configure, dump, dd, render_text


def test_render_text_dict():
    text = render_text({'tags': ['python', 'debug']}, color=False)
    assert 'dict:1' in text
    assert 'list:2' in text
    assert '=>' in text
    assert '▶' not in text
    assert '▼' not in text
    assert 'python' in text
    assert 'debug' in text


def test_render_text_fully_expanded():
    text = render_text({
        'id': 1,
        'tags': ['a', 'b', 'c'],
    }, color=False)
    assert '"tags" => list:3 [' in text
    assert '0 => "a"' in text or '0 =>' in text and '"a"' in text
    assert '[▶]' not in text


def test_render_text_scalar_tip():
    configure(project_root='.')
    text = render_text('Post not found', color=False)
    assert 'Post not found' in text
    assert '//' in text


def test_dump_stderr(capsys):
    dump('hello')
    err = capsys.readouterr().err
    assert 'hello' in err


def test_dd_exits():
    with pytest.raises(SystemExit) as ei:
        dd({'a': 1})
    assert ei.value.code == 1


def test_builtins_helpers():
    import builtins

    assert builtins.dd is dd
    assert builtins.dump is dump
    dump('via-builtin')
    with pytest.raises(SystemExit):
        dd('via-builtin')


def test_tip_on_header_not_after_close():
    text = render_text({'a': 1, 'b': 2}, color=False, source='demo.py:1')
    first, _, rest = text.partition('\n')
    assert first.startswith('dict:2 [')
    assert '// demo.py:1' in first
    assert rest.rstrip().endswith(']')
    assert '// demo.py:1' not in rest


def test_inspect_function_has_details():
    from pydump import inspect_value

    def greet(name: str) -> str:
        return name

    node = inspect_value(greet)
    assert node.kind == 'object'
    assert node.label == 'function'
    keys = {k for k, _ in node.children}
    assert 'attr:name' in keys
    assert 'attr:signature' in keys


def test_inspect_class_has_details():
    from pydump import inspect_value

    class Widget:
        kind = 'demo'

    node = inspect_value(Widget)
    assert node.kind == 'object'
    assert node.label == 'Widget (class)'
    assert node.children


def test_call_arg_names_from_source():
    from pydump.core import _call_arg_names

    assert _call_arg_names('dd(connection)') == ['connection']
    assert _call_arg_names('    dd(connection)') == ['connection']
    assert _call_arg_names('dd(a, b)') == ['a', 'b']
    assert _call_arg_names('dd(foo.bar)') == ['foo.bar']


def test_describe_value():
    from pydump import describe_value, value_kind

    class Widget:
        pass

    assert value_kind(Widget) == 'class'
    assert value_kind(Widget()) == 'object'
    assert describe_value(Widget(), name='connection') == (
        '$connection · object · test_describe_value.<locals>.Widget'
    )


def test_inspect_value_respects_max_depth():
    from pydump import inspect_value

    value = {'l1': {'l2': {'l3': {'l4': 'deep'}}}}

    def has_truncated(node) -> bool:
        if node.kind == 'truncated':
            return True
        return any(has_truncated(child) for _, child in node.children)

    shallow = inspect_value(value, max_depth=2)
    assert has_truncated(shallow)

    deep = inspect_value(value, max_depth=10)
    assert not has_truncated(deep)


def test_inspect_sqlalchemy_result_bounded():
    sqlalchemy = pytest.importorskip('sqlalchemy')
    from pydump import inspect_value, render_text
    import signal

    engine = sqlalchemy.create_engine('sqlite:///:memory:')
    with engine.connect() as conn:
        result = conn.execute(sqlalchemy.text('SELECT 1'))

        def count_nodes(node) -> int:
            return 1 + sum(count_nodes(child) for _, child in node.children)

        node = inspect_value(result)
        assert count_nodes(node) < 500

        def timeout(*_args):
            raise TimeoutError('render_text hung')

        signal.signal(signal.SIGALRM, timeout)
        signal.alarm(3)
        try:
            text = render_text(result, color=False)
        finally:
            signal.alarm(0)
        assert len(text) < 200_000
