import pytest
import filecmp
import os
import sys
import shutil
from time import sleep
from creator.creator import Creator


def test_compare_files():
    c = Creator('default_k8s_parameters.yaml')
    c.load_parameter_file()
    c.validate_objects()
    c.k8s_create_manifest()

    sleep(3)

    cwd = os.getcwd()

    new_service_config = cwd + '/tzankoswebpage/k8s/service.yaml'
    test_service_config = cwd + '/test_service_config.yaml'
    assert filecmp.cmp(new_service_config, test_service_config, shallow=False)