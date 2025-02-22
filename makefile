all:
	python genRecent.py
	git add .
	git commit -m "write exp"
	git push origin main