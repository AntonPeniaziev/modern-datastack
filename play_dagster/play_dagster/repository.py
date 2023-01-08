from dagster import load_assets_from_package_module, repository

from play_dagster import assets


@repository
def play_dagster():
    return [load_assets_from_package_module(assets)]
