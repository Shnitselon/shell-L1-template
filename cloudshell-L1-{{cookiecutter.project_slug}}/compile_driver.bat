pyinstaller --onefile driver.spec
copy datemodel\*.xml dist /Y
copy {{cookiecutter.project_slug}}_runtime_configuration.json dist /Y
