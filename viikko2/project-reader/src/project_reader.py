from urllib import request
from project import Project
from toml import loads

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        content_dict = loads(content)
        name = content_dict['tool']['poetry']['name']
        license = content_dict['tool']['poetry']['license']
        description = content_dict['tool']['poetry']['description']
        authors = content_dict['tool']['poetry']['authors']
        dependencies = content_dict['tool']['poetry']['dependencies']
        dev_dependencies = content_dict['tool']['poetry']['group']['dev']['dependencies']
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license, authors, dependencies, dev_dependencies)
