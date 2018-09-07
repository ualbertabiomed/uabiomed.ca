SRC=src
ASSETS=assets
CSS=$(ASSETS)/css
SASS=$(ASSETS)/sass
BIN=bin
website: index.html team.html join.html events.html sponsors.html docs.html
	mkdir -p $(BIN)
	sass $(SASS)/main.scss $(CSS)/main.css
	cp -r assets/ bin/
	cp -r images/ bin/

clean:
	rm -r $(BIN)

%.html: $(SRC)/%.htm $(SRC)/foot.htm $(SRC)/head.htm
	@echo "making index.html"
	mkdir -p $(BIN)
	cat $(SRC)/head.htm > $(BIN)/$@
	cat $< >> $(BIN)/$@
	cat $(SRC)/foot.htm >> $(BIN)/$@

$(SRC)/%:
	echo "making $%"

