
table.txt: emojilib/emojis.json
	python3 make_table.py

install: table.txt
	sudo ibus-table-createdb -n /usr/share/ibus-table/tables/emoji-eng.db -s table.txt
	sudo cp Emojione_1F600.svg /usr/share/ibus-table/icons
	ibus-daemon -drx

clean:
	rm table.txt

uninstall:
	sudo rm /usr/share/ibus-table/tables/emoji-eng.db
	sudo rm /usr/share/ibus-table/icons/Emojione_1F600.svg 


