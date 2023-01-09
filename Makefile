init: 
    pipenv install --dev

format: 
    pipenv run black corteva_api tests

test: 
    pytest tests

coverage: 
    pytest --cov corteva_api --cov-report term-missing tests