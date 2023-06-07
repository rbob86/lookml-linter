import glob
from typing import List, Union
import lkml
import os


class LookMlProjectParser:
    root_file_path = './'

    def __init__(self, filepaths: Union[List[str], None] = None) -> None:
        if os.path.isdir(LookMlProjectParser.root_file_path):
            if filepaths:
                lkml_filepaths = list(filter(lambda file_path: file_path.endswith('.lkml'), filepaths))
            else:
                lkml_filepaths = [f for f in glob.glob(
                    LookMlProjectParser.root_file_path + '**/*.lkml', recursive=True)]
        else:
            raise IOError('Directory does not exist: %s' %
                          LookMlProjectParser.root_file_path)
        self.__lkml_filepaths = []
        self.__not_parsed_lookml_files = {}
        self.__parsed_lookml_files = {}
        for filepath in lkml_filepaths:
            if not os.path.exists(filepath):
                raise IOError('File does not exist: %s' % filepath)
            self.__lkml_filepaths.append(filepath)
            with open(filepath, 'r') as file:
                try:
                    lookml = lkml.load(file)
                    if lookml:
                        self.__parsed_lookml_files[filepath] = lookml
                except SyntaxError as e:
                    self.__not_parsed_lookml_files[filepath] = str(e)

    @property
    def raw_files(self):
        result = {}
        for filepath in self.parsed_lookml_files.keys():
            with open(filepath, 'r') as file:
                result[filepath] = file.readlines()
        return result

    @property
    def parsed_lookml_files(self):
        return self.__parsed_lookml_files

    @property
    def not_parsed_lookml_files(self):
        return self.__not_parsed_lookml_files

    @property
    def lkml_filepaths(self):
        return self.__lkml_filepaths
