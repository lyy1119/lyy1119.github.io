default: gitPush recentPost gitPush

gitPush:
	git add .
	git commit -m "write exp"
	git push origin main

recentPost:
	python genRecent.py