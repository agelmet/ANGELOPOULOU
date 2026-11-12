#!/bin/bash
# ANGELOPOULOU — cloud pipeline. Edit src/, then: bash make.sh
set -e
A=/home/claude/ac/.advon; S=/home/claude/ma/site; cd /home/claude/ma
python3 src/build.py
python3 -I $A/privacy/privacy_fix.py apply $S >/dev/null
sed -i 's/is Maria Angelopoylou, 16231, Βύρωνας/is Maria Angelopoulou, Vyronas 16231, Attica/; s/είναι Μαρία Αγγελοπούλου, 16231, Βύρωνας/είναι η Μαρία Αγγελοπούλου, Βύρωνας 16231, Αττική/' $S/privacy.html
python3 -I $A/seo_live.py fix $S | tail -1
(cd $S && python3 -I $A/favicon.py make $S assets/img/maria-angelopoulou-logo-icon.svg --tile "#6B2129" | head -1)
python3 -I $A/seo_rank.py en $S | tail -1
python3 -I $A/ai_seo.py fix $S | tail -1
