pyinstaller --onefile driver.spec
copy datamodel\*.xml dist /Y
copy {{cookiecutter.project_slug}}_runtimeconfig.yml dist /Y
