"""pydump — structured dump and die for the terminal."""

from pydump.api import configure, dd, dump, install_helpers, render_text
from pydump.core import DumpNode, inspect_value, set_project_root
from pydump.core import (
    caller_arg_names,
    caller_frame,
    describe_value,
    format_dump_tip,
    value_kind,
    value_type_name,
)

__all__ = [
    'dd',
    'dump',
    'configure',
    'render_text',
    'install_helpers',
    'DumpNode',
    'inspect_value',
    'set_project_root',
    'caller_frame',
    'caller_arg_names',
    'describe_value',
    'format_dump_tip',
    'value_kind',
    'value_type_name',
]
__version__ = '0.2.4'

# Laravel-style: ``dd()`` / ``dump()`` without per-file import after ``import pydump``.
install_helpers()
