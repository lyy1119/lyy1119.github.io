default: commit recentPost push

commit:
	git add .
	git commit -m "write exp"

push:
	git add .
	git commit -m "write exp"
	git push origin main

recentPost:
	python genRecent.py