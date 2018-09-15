from click.testing import CliRunner
from tempfile import TemporaryDirectory
from pathlib import Path
import os
import contextlib

from solid_toolbox.commands import run


@contextlib.contextmanager
def change_dir(new_loc):
    current = os.getcwd()
    os.chdir(new_loc)
    try:
        yield
    finally:
        os.chdir(current)


def test_new_absolute_path():
    with TemporaryDirectory() as folder, change_dir(folder):
        assert_project_gen_is_ok(Path(folder) / 'test')


def test_new_relative_path():
    with TemporaryDirectory() as folder, change_dir(folder):
        assert_project_gen_is_ok(Path('test'))


def assert_project_gen_is_ok(root):
    name = root.name

    generated_folder = root / 'generated'
    python_script = root / f'{name}.py'
    scad_output = generated_folder / f'{name}.scad'

    result = CliRunner().invoke(run, ['new', str(root)])
    assert result.exit_code == 0
    assert result.output == ''

    assert generated_folder.exists() and generated_folder.is_dir()
    assert python_script.exists() and python_script.is_file()

    with change_dir(root):
        exec(Path(f'{name}.py').read_text(), {'__name__': '__main__'})

    assert scad_output.exists()
