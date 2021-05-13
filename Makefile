compileone:
	pyinstaller --onefile -F --add-data "./screenpen/utils/*:utils" screenpen/screenpen.py

clean:
	rm -rf dist build screenpen.egg-info

setup: clean
	python setup.py sdist bdist_wheel 

setuppip: clean
	rm -rf dist build  && python setup.py sdist bdist_wheel && twine upload dist/*

test: clean
	pip uninstall -y screenpen && pip install -e . && python -m screenpen