#!/usr/bin/env -S just --working-directory . --justfile

env_name := "venv"

python_dir := if os_family() == "windows" { env_name + "/Scripts" } else { env_name + "/bin" }
python := python_dir + if os_family() == "windows" { "/python.exe" } else { "/python3" }

# List all the available commands
default:
  @just --list

# Install packages in the virtual environment
[private]
package_venv: venv
  {{python}} -m pip install --upgrade pip
  {{python}} -m pip install -r requirements.txt

# Make a new virtual environment
[private]
make_venv:
  python3 -m venv {{env_name}}
  just package_venv

# Make the environment if it does not exit
[private]
@venv:
  [ -d {{env_name}} ] || just make_venv

# Removes the virtual environment
clean:
  rm -rf {{env_name}}

# Upgrades packages and pre-commit
upgrade: venv
  just package_venv
  just pre-commit

# Setup pre-commit hooks
pre_commit: venv
  {{python_dir}}/pre-commit install --install-hooks
