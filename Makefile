default: build

build:
	find . -name Makefile -not -path "./Makefile" -exec sh -c 'make build -C "$$(dirname {})"' \;

serve:
	marp -s .
