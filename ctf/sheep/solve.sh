#/bin/sh
binwalk -D=".*" sheep.jpg
mv _sheep.jpg.extracted/27D77 _sheep.jpg.extracted/flag.png
code _sheep.jpg.extracted/flag.png
