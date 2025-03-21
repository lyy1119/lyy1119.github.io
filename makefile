default: commit recentPost push
	echo "https://wiki.lyy19.cn"
commit:
	git add .
	git commit -m "write exp"

push:
	git add .
	git commit -m "write exp"
	git push origin main

recentPost:
	python genRecent.py