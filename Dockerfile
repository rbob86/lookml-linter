FROM python:3.8-slim-buster

LABEL "com.github.actions.name"="Snazzy-Linter"
LABEL "com.github.actions.description"="Automatic code reviewer for GitHub PRs."
LABEL "com.github.actions.icon"="code"
LABEL "com.github.actions.color"="gray-dark"

LABEL "repository"="https://github.com/rbob86/lookml-linter/tree/main/linter/rules"
LABEL "homepage"="https://github.com/rbob86/lookml-linter"
LABEL "maintainer"="Eric"

COPY . .

RUN python3 -m pip3 install --upgrade pip3
RUN pip3 install -r requirements.txt
RUN pip3 install .

# RUN python pip install  --upgrade pip
# RUN pip install looker-sdk
# RUN pip install pyyaml
# RUN pip install jsonschema 
# RUN pip install pytest
# RUN pip install lkml


RUN ls -la

CMD ["python3", "-m", "linter.main", "config.example.yaml"]
