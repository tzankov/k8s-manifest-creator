import pytest
import filecmp
import os
import sys
from creator.creator import Creator


class TestClass:
    def compare_files(self):
        c = Creator('default_k8s_parameters.yaml')
        c.load_parameter_file()
        c.validate_objects()
        c.k8s_create_manifest()

        cwd = os.getcwd()

        new_service_config = cwd + '/tzankoswebpage/service.yaml'
        test_service_config = cwd + 'test_service_config.yaml'
        assert filecmp.cmp(new_service_config, test_service_config, shallow=False)

