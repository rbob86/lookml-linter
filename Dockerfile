FROM python:3.8-slim-buster

LABEL "com.github.actions.name"="Snazzy-Linter"
LABEL "com.github.actions.description"="Automatic code reviewer for GitHub PRs."
LABEL "com.github.actions.icon"="code"
LABEL "com.github.actions.color"="gray-dark"

LABEL "repository"="https://github.com/rbob86/lookml-linter/tree/main/linter/rules"
LABEL "homepage"="https://github.com/rbob86/lookml-linter"
LABEL "maintainer"="Eric"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .
RUN ls -la

RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
ENV PYTHONPATH /linter
# RUN pip3 install linter/


# RUN python pip install  --upgrade pip
# RUN pip install looker-sdk
# RUN pip install pyyaml
# RUN pip install jsonschema 
# RUN pip install pytest
# RUN pip install lkml



CMD ["python3", "-m", "linter.main", "config.example.yaml"]
