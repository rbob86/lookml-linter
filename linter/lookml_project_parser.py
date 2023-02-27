import glob
from typing import List, Union
import lkml
import os


class LookMlProjectParser:
    root_file_path = './'

    def __init__(self, filepaths: Union[List[str], None] = None) -> None:
        if os.path.isdir(LookMlProjectParser.root_file_path):
            print('1 ========================')
            print(filepaths)
            print('========================')
            if filepaths:
                lkml_filepaths = list(filter(lambda filepath: filepath.endswith('.lkml'), filepaths))
            else:
                lkml_filepaths = [f for f in glob.glob(
                    LookMlProjectParser.root_file_path + '**/*.lkml', recursive=True)]
            print('2 ========================')
            print(lkml_filepaths)
            print('========================')
        else:
            raise IOError('Directory does not exist: %s' %
                          LookMlProjectParser.root_file_path)
        self.unparsable_lookml_files = []
        self.parsed_lookml_files = {}
        for filepath in lkml_filepaths:
            if not os.path.exists(filepath):
                raise IOError('File does not exist: %s' % filepath)
            with open(filepath, 'r') as file:
                try:
                    self.parsed_lookml_files[filepath] = lkml.load(file)
                except SyntaxError:
                    self.unparsable_lookml_files.append(filepath)

    def get_unparsable_lkml_files(self) -> None:
        if len(self.unparsable_lookml_files) > 0:
            return self.unparsable_lookml_files
        return None

    def get_parsed_lookml_files(self) -> None:
        if len(self.parsed_lookml_files) > 0:
            return self.parsed_lookml_files
        return None
