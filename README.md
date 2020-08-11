# json-search
A Vuejs / Flask app that lets you index and full-text search through a specified json file. Uses Whoosh as its search and indexing library.

## Backend
Please see makefile for running instructions.

__Configuration:__

with Poetry:
```
make configure-poetry
```

with pip:
```
make configure-pip
```

__How to run:__

```
make run
```

if without poetry:
```
make run-no-poetry
```

## Frontend
To configure & run:

yarn:
```
yarn && yarn serve
```

npm:
```
npm install && npm run serve
```
