import functools
from os import path, listdir
from pathlib import Path
from typing import List


class RuleNames:
    rules_dir = path.dirname(__file__) + '/rules'

    @staticmethod
    @functools.lru_cache
    def get() -> List[str]:
        dir = RuleNames.rules_dir
        return [Path(f).stem for f in listdir(
                dir) if path.isfile(path.join(dir, f)) and f != '__init__.py']
