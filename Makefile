compile:
	pyinstaller --onefile -F --add-data "./utils/*:utils" screenpen.pyw

clean:
	rm -rf ./dist ./build