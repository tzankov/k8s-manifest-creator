import os
import sys
import yaml
import argparse
from jinja2 import PackageLoader, Environment

class Creator():
    def __init__(self, path: str):
        self.path = path


    def load_parameter_file(self):
        '''
        This function takes in one parameter, path, and returns an object with the contents of said file. File must be in yaml format.
        
        :return: contents of file object
        '''

        with open(self.path) as f:
            try:
                doc = yaml.safe_load(f)
            except yaml.YAMLError as e:
                print(e)
        
        self.doc = doc


    def k8s_create_manifest(self):
        '''
        This function creates the k8s manifests, it takes in object requirements and writes them into templated files under a new directory

        :self.doc: object requirements in yaml format
        :return: None
        '''

        # Create output directory
        directory = os.getcwd() + '/' + self.doc['name'] + '/k8s/'

        try:
            os.makedirs(directory)
        except OSError:
            print (f"Creation of the directory {directory} failed")
        else:
            print (f"Successfully created the directory {directory}")

        # Render files
        file_loader = PackageLoader('creator', 'templates/')
        env = Environment(loader=file_loader)

        for template_name in env.list_templates():
            template = env.get_template(template_name)

            rendered_output = template.render(name=self.doc['name'], hostname=self.doc['hostname'], ingress=self.doc['ingress'], registry=self.doc['registry'])

            output = directory + '/' + template_name
            with open(output, 'w') as f:
                f.write(rendered_output)


    def validate_objects(self):
        '''
        This function takes in the loaded self.document, checks if the entries within it are valid object types
        
        :self.doc: This is the loaded yaml file
        :return: None
        '''

        # define valid object types
        valid_objects = {
            'name': '',
            'type': ['microservice', 'api'],
            'ingress': ['internal-ingress', 'external-ingress'],
            'hostname': '',
            'registry': '',
        }

        # cycle through the entries within the self.doc file, and check if they exist in valid_objects, otherwise, alert and exit
        for key, value in self.doc.items():
            if key in valid_objects:
                if value in self.doc[key]:
                    print(f"Value valid: {value} ***ALL GOOD***")
                else:
                    print(f"Value NOT VALID: {value} ***EXITING***")
                    sys.exit()
            else:
                print(f"Key NOT VALID: {key} Check that your keys are valid! ***EXITING***")
                sys.exit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
                    '-fp', '--file-path',
                    help="Path and file name of parameter to read.",
                    nargs=1,
                    required=False,
                    default='default_k8s_parameters.yaml'
                    )
    args = parser.parse_args() 

    c = Creator(args.file_path)
    c.load_parameter_file()
    c.validate_objects()
    c.k8s_create_manifest()