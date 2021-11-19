OUTPUTS = $(sort $(wildcard outputs/*.txt))
QUESTIONS = $(patsubst outputs/%.txt,%,$(OUTPUTS))
MAKEFILE_PATH = /Users/sanguiseong/Library/Containers/com.softwareambience.Unclutter/Data/Library/Application Support/Unclutter/FileStorage/ASU 복사본/2021 Fall Semester/CSE412/midterm-phase2
ROOT = $(MAKEFILE_PATH)

all: path $(QUESTIONS)
	rm -rf tmp

%: queries/%.sql
	@echo "checking $@; correct if nothing below ----"
	@psql -A -t -d $(USER) -q -f $< 1> tmp/$@.txt
	@diff outputs/$@.txt tmp/$@.txt || echo "$@ is wrong"; exit 0
	@echo ""

path:
	@mkdir -p tmp

setup_data:
	@echo "creating tables"
	psql -d $(USER) -q -f setup_data/create_tables.sql
	@echo "importing data"
	psql -d $(USER) -q -c "COPY waiter FROM '$(ROOT)/resturant_data/waiter.csv' DELIMITER ',' CSV HEADER;
	psql -d $(USER) -q -c "COPY customer FROM '$(ROOT)/resturant_data/customer.csv' DELIMITER ',' CSV;"
	psql -d $(USER) -q -c "COPY manager FROM '$(ROOT)/resturant_data/manager.csv' DELIMITER ',' CSV;"
	psql -d $(USER) -q -c "COPY chef FROM '$(ROOT)/resturant_data/chef.csv' DELIMITER ',' CSV;"
	psql -d $(USER) -q -c "COPY dish FROM '$(ROOT)/resturant_data/dish.csv' DELIMITER ',' CSV;"
	psql -d $(USER) -q -c "COPY supplier FROM '$(ROOT)/resturant_data/supplier.csv' DELIMITER ',' CSV;"
	psql -d $(USER) -q -c "COPY ingredient FROM '$(ROOT)/resturant_data/ingredient.csv' DELIMITER ',' CSV;"
	@echo "test, count distinct business categories, the result should be 20"
	psql -d $(USER) -q -c "SELECT count(distinct(city)) FROM supplier;"


clean_data:
	psql -d $(USER) -q -f setup_data/drop_tables.sql


.PHONY: setup_postgres

