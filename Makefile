ROOT_DIR = $(CURDIR)
SOURCE_DIR = $(CURDIR)/src

MANAGER = python $(SOURCE_DIR)/manage.py
VENV_DIR_NAME = venv
VENV = . $(ROOT_DIR)/$(VENV_DIR_NAME)/bin/activate;

.PHONY : static
static:
	$(VENV) $(MANAGER) collectstatic --noinput

.PHONY : init_venv
init_venv:
	if [ ! -e "$(ROOT_DIR)/$(VENV_DIR_NAME)/bin/activate" ] ; then virtualenv -p python3 --clear $(VENV_DIR_NAME); fi

.PHONY : pip
pip:
	$(VENV) pip install -r $(ROOT_DIR)/requirements.txt

.PHONY : test
test:
	$(VENV) $(MANAGER) test

.PHONY : migrate
migrate:
	$(VENV) $(MANAGER) migrate --noinput

.PHONY : makemigrations
makemigrations:
	$(VENV) $(MANAGER) makemigrations --noinput

.PHONY : mm
mm: makemigrations migrate

.PHONY : runserver
runserver:
	$(VENV) $(MANAGER) runserver 127.0.0.1:8000

.PHONY : install
install: init_venv pip migrate static

# Update instance
.PHONY : update
update: pip migrate static