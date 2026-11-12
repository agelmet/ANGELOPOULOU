#!/usr/bin/env python3
"""Build index.html for Μαρία Αγγελοπούλου (agelmet/ANGELOPOULOU).
Skeleton (rolled 12 Nov 2026): hero = split, text | portrait in a round «clock mirror» · nav = top bar ·
areas = list + sticky panel (accordion on phones) · proof = big single-quote rotation · contact = full band ·
FAQ = two-column, sticky side with crisis lines · signature = «Ο φαύλος κύκλος της αποφυγής» (from her own post)
· opening = clock hand sweeps the page open (conic mask) — new type."""
import json, html, os, re
S = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(S, '..', 'site')
rd = lambda p: open(os.path.join(S, p), encoding='utf-8').read()
esc = lambda s: html.escape(s, quote=True)

GREV = 'https://www.google.com/maps/place/data=!4m3!3m2!1s0x14a1bd2f2581c495:0x4a74bbb48daa151c!9m1!1b1'
GMAP = 'https://www.google.com/maps?cid=5365119440250344732'
PHONE = '+306945152180'

AREAS = [
 dict(t='Άγχος & κρίσεις πανικού', te='Anxiety & panic attacks',
      d='Όταν η ανησυχία δεν σταματά ή όταν το σώμα «σημαίνει συναγερμό» χωρίς πραγματικό κίνδυνο. Μαθαίνουμε πώς λειτουργεί το άγχος, πώς διαφέρει μια κρίση πανικού από μια κρίση άγχους και πώς να ανταποκρινόμαστε διαφορετικά στα σωματικά συμπτώματα.',
      de='When worry will not stop, or when the body «sounds the alarm» with no real danger. We learn how anxiety works, how a panic attack differs from an anxiety attack, and how to respond differently to the physical symptoms.'),
 dict(t='Φοβίες', te='Phobies',
      d='Όταν ο φόβος για μια κατάσταση, ένα μέρος ή ένα ερέθισμα περιορίζει την καθημερινότητα. Με σταδιακή και ασφαλή προσέγγιση, με τον δικό σας ρυθμό, ο φόβος χάνει σιγά σιγά τη δύναμή του.',
      de='When fear of a situation, a place or a trigger limits everyday life. With a gradual and safe approach, at your own pace, the fear slowly loses its power.'),
 dict(t='Κατάθλιψη', te='Depression',
      d='Η κατάθλιψη δεν είναι απλώς μια κακή διάθεση ή μια δύσκολη μέρα. Δουλεύουμε με τις σκέψεις που τη συντηρούν και με μικρά, σταθερά βήματα στην καθημερινότητα, ώστε να επιστρέψουν η ενέργεια και το ενδιαφέρον.',
      de='Depression is not simply a bad mood or a difficult day. We work with the thoughts that keep it going and with small, steady steps in everyday life, so that energy and interest can return.'),
 dict(t='Ιδεοψυχαναγκαστική διαταραχή (ΙΨΔ)', te='Obsessive-compulsive disorder (OCD)',
      d='Επίμονες, ανεπιθύμητες σκέψεις (ιδεοληψίες) και επαναλαμβανόμενες πράξεις που μοιάζουν να τις «ηρεμούν» (καταναγκασμοί) και καταναλώνουν χρόνο και ενέργεια. Μαθαίνουμε να σπάμε σταδιακά αυτόν τον κύκλο.',
      de='Persistent, unwanted thoughts (obsessions) and repeated actions that seem to «calm» them (compulsions), taking up time and energy. We learn, step by step, to break this cycle.'),
 dict(t='Μετατραυματικό στρες', te='Post-traumatic stress',
      d='Όταν μια δύσκολη εμπειρία συνεχίζει να επιστρέφει με αναμνήσεις, ένταση ή αποφυγή. Σε ένα ασφαλές πλαίσιο δουλεύουμε ώστε η εμπειρία να πάρει τη θέση της στο παρελθόν.',
      de='When a difficult experience keeps coming back through memories, tension or avoidance. In a safe setting we work so that the experience can take its place in the past.'),
 dict(t='Άγχος υγείας & ψυχοσωματικά', te='Health anxiety & psychosomatic symptoms',
      d='Όταν κάθε φυσιολογική σωματική αίσθηση μοιάζει με σημάδι σοβαρής ασθένειας, και ο έλεγχος του σώματος ή η αναζήτηση επιβεβαίωσης δεν φέρνουν ηρεμία για πολύ. Μαθαίνουμε να ερμηνεύουμε διαφορετικά τα μηνύματα του σώματος.',
      de='When every normal bodily sensation feels like a sign of serious illness, and checking the body or seeking reassurance never brings calm for long. We learn to read the body’s signals differently.'),
 dict(t='Διαπροσωπικές σχέσεις', te='Relationships',
      d='Δυσκολίες στις σχέσεις με τον σύντροφο, την οικογένεια, τους φίλους ή στη δουλειά. Εξετάζουμε μοτίβα επικοινωνίας και σκέψης και αναζητούμε πιο λειτουργικούς τρόπους σύνδεσης.',
      de='Difficulties in relationships with a partner, family, friends or at work. We look at patterns of communication and thinking and look for more helpful ways to connect.'),
 dict(t='Διαχείριση πένθους', te='Grief',
      d='Η απώλεια ενός ανθρώπου ή μιας σημαντικής πτυχής της ζωής φέρνει πόνο που δεν ακολουθεί κανόνες. Η θεραπεία προσφέρει χώρο να ειπωθούν όσα δυσκολεύουν και να βρεθεί ο δικός σας τρόπος να συνεχίσετε.',
      de='Losing a person or an important part of life brings a pain that follows no rules. Therapy offers room to say what is hard and to find your own way to carry on.'),
 dict(t='Αυτοεκτίμηση & προσωπική ανάπτυξη', te='Self-esteem & personal growth',
      d='Όταν η εσωτερική κριτική φωνή είναι πιο δυνατή από όλες. Δουλεύουμε με την αυτοεικόνα, τις πεποιθήσεις για τον εαυτό και με όσα έχουν πραγματικά αξία για εσάς.',
      de='When the inner critical voice is louder than any other. We work on self-image, beliefs about yourself and on what truly matters to you.'),
]
AREAS[1]['te'] = 'Phobias'

# the avoidance cycle = her own Instagram post «Φαύλος κύκλος της αποφυγής»
CYC = {
 'loop': dict(x='Η αποφυγή φέρνει ανακούφιση — και έτσι ο εγκέφαλος μαθαίνει ότι ο κίνδυνος ήταν πραγματικός. Την επόμενη φορά το άγχος έρχεται πιο γρήγορα.',
              xe='Avoidance brings relief — and so the brain learns that the danger was real. Next time, the anxiety comes faster.',
   n=[dict(l='Σκέψη', le='Thought', t='«Αν μπω στο μετρό, θα πάθω κρίση πανικού και θα λιποθυμήσω»', te='«If I get on the metro, I’ll have a panic attack and faint»'),
      dict(l='Συναίσθημα', le='Feeling', t='Άγχος — ταχυκαρδία, εφίδρωση, τρέμουλο', te='Anxiety — racing heart, sweating, trembling'),
      dict(l='Συμπεριφορά', le='Behaviour', t='Δεν μπαίνω στο μετρό, πάω με τα πόδια', te='I don’t take the metro, I walk'),
      dict(l='Βραχυπρόθεσμο όφελος', le='Short-term gain', t='Προσωρινή ανακούφιση', te='Temporary relief'),
      dict(l='Μακροπρόθεσμο κόστος', le='Long-term cost', t='Το άγχος διαιωνίζεται και η σκέψη «επιβεβαιώνεται»', te='The anxiety lasts and the thought is «confirmed»')]),
 'open': dict(x='Στη θεραπεία εξετάζουμε τη σκέψη και προσεγγίζουμε σταδιακά, με σχέδιο, όσα αποφεύγουμε. Ο κύκλος ανοίγει — και γίνεται δρόμος.',
              xe='In therapy we examine the thought and approach what we avoid gradually, with a plan. The cycle opens — and becomes a path.',
   n=[dict(l='Σκέψη', le='Thought', t='«Πόσο πιθανό είναι πραγματικά; Τι άλλο θα μπορούσε να συμβεί;»', te='«How likely is it, really? What else could happen?»'),
      dict(l='Συναίσθημα', le='Feeling', t='Το άγχος ανεβαίνει — και, αν μείνω, πέφτει μόνο του', te='The anxiety rises — and, if I stay, it falls on its own'),
      dict(l='Συμπεριφορά', le='Behaviour', t='Μπαίνω σταδιακά, με μικρά βήματα', te='I get on gradually, in small steps'),
      dict(l='Εμπειρία', le='Experience', t='Αυτό που φοβόμουν δεν συνέβη', te='What I feared did not happen'),
      dict(l='Νέα μάθηση', le='New learning', t='Η σκέψη χάνει τη δύναμή της', te='The thought loses its power')]),
}
OPEN_D = 'M30 600 C 70 560 70 540 84 528 S 150 450 186 414 S 260 330 300 300 S 370 230 408 186 S 470 110 504 78 S 548 40 572 46'

REVIEWS = [
 ('Ζενια Μπουτρη', 'πριν από 2 μήνες', 'Εξαιρετική επαγγελματίας και πάνω απ’ όλα ένας άνθρωπος που σε κάνει να νιώθεις ασφάλεια και εμπιστοσύνη από την πρώτη στιγμή. Με ακούει πραγματικά, χωρίς κριτική, και με βοηθά να βλέπω τα πράγματα πιο καθαρά και να κατανοώ καλύτερα τον εαυτό μου. Τη συστήνω ανεπιφύλακτα σε όποιον αναζητά έναν άνθρωπο με γνώση, ενσυναίσθηση και πραγματικό ενδιαφέρον.'),
 ('Myrsini Theodosiadou', 'πριν από έναν μήνα', 'Δεν περίμενα ότι θα υπάρξει κάποιος που θα με ακούσει τόσο πολύ και τόσο καθαρά, όσο η Μαρία. Σε ευχαριστώ πολύ!'),
 ('Stella Kapsimali', 'πριν από 2 μήνες', 'Εξαιρετική επαγγελματίας, με ενσυναίσθηση, κατανόηση και πραγματικό ενδιαφέρον για τον άνθρωπο. Δημιουργεί ένα ασφαλές και άνετο περιβάλλον, όπου μπορείς να εκφραστείς ελεύθερα χωρίς να νιώθεις ότι κρίνεσαι. Τη συστήνω ανεπιφύλακτα!'),
 ('Manos Zar', 'πριν από 2 μήνες', 'Με βοήθησε να ανοιχτώ σε εκείνη και να νιώσω εμπιστοσύνη από την πρώτη στιγμή. Με βοήθησε να βάλω τη ζωή μου σε μια σειρά και να κάνω μια νέα αρχή έχοντας πλέον εμπιστοσύνη στον εαυτό μου. Κ. Μαρία σας ευχαριστώ πολύ για όλα!!!'),
 ('γιαννης αλεξιου', 'πριν από έναν μήνα', 'Η Μαρία με έκανε να νιώσω άνετα και να μιλήσω για όσα με απασχολούν. Πάντα με ακούει με προσοχή και ενδιαφέρον. Φαίνεται ότι νοιάζεται πραγματικά και με βοήθησε πολύ. Την ευχαριστώ πολύ!'),
 ('Giorgos Stamatakis', 'πριν από 2 μήνες', 'Η Μαρία είναι ένας εξαιρετικός άνθρωπος, που καταφέρνει να δημιουργεί ένα πολύ ζεστό κλίμα εμπνέοντας ασφάλεια και κατανόηση. Είναι καταρτισμένη επαγγελματίας, ενδιαφέρεται πραγματικά να βοηθάει και για το λόγο αυτό τη συστήνω ανεπιφύλακτα!'),
 ('Εύη Μυλωνά', 'πριν από 3 μήνες', 'Εξαιρετική επαγγελματίας με πραγματικό ενδιαφέρον για τον άνθρωπο. Δημιουργεί από την πρώτη στιγμή ένα ζεστό, ασφαλές και υποστηρικτικό περιβάλλον όπου μπορείς να εκφραστείς ελεύθερα. Τη συστήνω ανεπιφύλακτα σε όποιον αναζητά ουσιαστική ψυχολογική υποστήριξη.'),
 ('Σωτηρης Φ', 'πριν από 2 μήνες', 'Εξαιρετική επαγγελματίας, με δεξιότητες και ενσυναίσθηση που ξεχωρίζει! Πάντα συνεπής, επικοινωνιακή και πρωτίστως καθησυχαστική. Την συστήνω ανεπιφύλακτα!'),
 ('Fanis Karamplias', 'πριν από 2 μήνες', 'Πολύ αξιόλογη επαγγελματίας, προσιτή και με πραγματική διάθεση να ακούσει και να βοηθήσει. Τη συστήνω ανεπιφύλακτα!'),
]

FAQ = [
 ('Πώς γίνεται μια online συνεδρία;', 'How does an online session work?',
  'Μέσω Microsoft Teams, από υπολογιστή, tablet ή κινητό. Χρειάζεστε μόνο σύνδεση στο ίντερνετ και έναν ήσυχο χώρο όπου μπορείτε να μιλήσετε ελεύθερα.',
  'Through Microsoft Teams, from a computer, tablet or phone. All you need is an internet connection and a quiet place where you can speak freely.'),
 ('Πώς κλείνω ραντεβού;', 'How do I book an appointment?',
  'Τηλεφωνικά ή με μήνυμα στο 694 515 2180, Δευτέρα έως Παρασκευή, 09:00–21:00. Αν δεν απαντήσω αμέσως, θα σας καλέσω πίσω.',
  'By phone or text on 694 515 2180, Monday to Friday, 09:00–21:00. If I can’t answer straight away, I will call you back.'),
 ('Με ποιους δουλεύετε;', 'Who do you work with?',
  'Με ενήλικες, σε ατομικές συνεδρίες. Ενδεικτικά: άγχος και κρίσεις πανικού, φοβίες, κατάθλιψη, ιδεοψυχαναγκαστική διαταραχή, μετατραυματικό στρες, άγχος υγείας, σχέσεις, πένθος και αυτοεκτίμηση.',
  'With adults, in individual sessions. For example: anxiety and panic attacks, phobias, depression, OCD, post-traumatic stress, health anxiety, relationships, grief and self-esteem.'),
 ('Τι είναι η Γνωσιακή Συμπεριφορική Θεραπεία (CBT);', 'What is Cognitive Behavioural Therapy (CBT)?',
  'Μια επιστημονικά τεκμηριωμένη μορφή ψυχοθεραπείας που εξετάζει πώς συνδέονται οι σκέψεις, τα συναισθήματα και οι συμπεριφορές μας, και βοηθά να αναπτύξουμε πιο λειτουργικούς τρόπους αντιμετώπισης.',
  'An evidence-based form of psychotherapy that looks at how our thoughts, feelings and behaviours are linked, and helps us develop more helpful ways of coping.'),
 ('Τι είναι η Θεραπεία Αποδοχής και Δέσμευσης (ACT);', 'What is Acceptance and Commitment Therapy (ACT)?',
  'Μια προσέγγιση που εστιάζει στην ψυχολογική ευελιξία, στην ενσυνειδητότητα και σε μια ζωή με βάση τις αξίες μας: να κάνουμε χώρο στις δύσκολες σκέψεις και να κινούμαστε προς ό,τι έχει σημασία για εμάς.',
  'An approach focused on psychological flexibility, mindfulness and values-based living: making room for difficult thoughts and moving towards what matters to us.'),
 ('Είναι εμπιστευτικές οι συνεδρίες;', 'Are sessions confidential?',
  'Ναι. Ό,τι συζητάμε καλύπτεται από το επαγγελματικό απόρρητο του ψυχολόγου.',
  'Yes. Everything we discuss is covered by the psychologist’s professional confidentiality.'),
 ('Πώς γίνεται η πληρωμή;', 'How do I pay?',
  'Με κατάθεση σε τραπεζικό λογαριασμό ή με κάρτα.',
  'By bank transfer or by card.'),
 ('Μπορώ να συνδεθώ από το εξωτερικό;', 'Can I join from abroad?',
  'Ναι. Οι συνεδρίες γίνονται online, οπότε μπορείτε να συνδεθείτε από οπουδήποτε στην Ελλάδα ή στο εξωτερικό.',
  'Yes. Sessions are online, so you can join from anywhere in Greece or abroad.'),
]

DAYS = [('Δευτέρα', 'Monday', '09:00 – 21:00', '09:00 – 21:00'), ('Τρίτη', 'Tuesday', '09:00 – 21:00', '09:00 – 21:00'),
        ('Τετάρτη', 'Wednesday', '09:00 – 21:00', '09:00 – 21:00'), ('Πέμπτη', 'Thursday', '09:00 – 21:00', '09:00 – 21:00'),
        ('Παρασκευή', 'Friday', '09:00 – 21:00', '09:00 – 21:00'), ('Σάββατο', 'Saturday', 'Κλειστά', 'Closed'), ('Κυριακή', 'Sunday', 'Κλειστά', 'Closed')]

def areas_html():
    o = []
    for i, a in enumerate(AREAS):
        o.append(f'<li><button class="a-btn" type="button" role="tab" id="ab{i}" aria-selected="{"true" if i == 0 else "false"}" aria-expanded="false" aria-controls="apanel"><span class="dot" aria-hidden="true"></span><span data-en="{esc(a["te"])}">{esc(a["t"])}</span><span class="ar" aria-hidden="true">→</span></button>'
                 f'<div class="a-acc"><div><p data-en="{esc(a["de"])}">{esc(a["d"])}</p></div></div></li>')
    return ''.join(o)

def nodes_html():
    L = CYC['loop']['n']
    return ''.join(f'<div class="node"><div class="cd"><span class="lb">{esc(n["l"])}</span><span class="tx">{esc(n["t"])}</span></div></div>' for n in L)

def reviews_html():
    o = []
    for i, (n, w, t) in enumerate(REVIEWS):
        o.append(f'<figure class="q{" on" if i == 0 else ""}"><blockquote lang="el">«{esc(t)}»</blockquote>'
                 f'<figcaption class="who"><span class="av" aria-hidden="true">{esc(n[0].upper())}</span><span>{esc(n)}<small><span class="st" aria-hidden="true">★★★★★</span> Google · {esc(w)}</small></span></figcaption></figure>')
    return ''.join(o)

def faq_html():
    return ''.join(f'<details class="qa rv"{" open" if i == 0 else ""}><summary><span data-en="{esc(qe)}">{esc(q)}</span><i aria-hidden="true"></i></summary><div class="an"><p data-en="{esc(ae)}">{esc(a)}</p></div></details>'
                   for i, (q, qe, a, ae) in enumerate(FAQ))

def hours_html():
    return ''.join(f'<tr><td data-en="{e}">{g}</td><td data-en="{he}">{h}</td></tr>' for g, e, h, he in DAYS)

def ticks():
    import math
    o = []
    for i in range(60):
        a = math.radians(i * 6); big = i % 5 == 0
        r1, r2 = 92.5, (88 if big else 90.5)
        o.append(f'<line class="tk{" big" if big else ""}" x1="{100+r1*math.sin(a):.2f}" y1="{100-r1*math.cos(a):.2f}" x2="{100+r2*math.sin(a):.2f}" y2="{100-r2*math.cos(a):.2f}"/>')
    return ''.join(o)

STARS = '<svg viewBox="0 0 24 24" aria-hidden="true"><use href="#star"/></svg>' * 5

LD = {"@context": "https://schema.org", "@graph": [
  {"@type": "MedicalBusiness", "@id": "#practice", "name": "Μαρία Αγγελοπούλου - MSc Ψυχολόγος, Ψυχοθεραπεύτρια",
   "alternateName": ["Maria Angelopoulou - Psychologist, Psychotherapist", "Μαρία Αγγελοπούλου Ψυχολόγος"],
   "description": "Ψυχολόγος – ψυχοθεραπεύτρια με άδεια άσκησης επαγγέλματος (424449/2023). Ατομική online ψυχοθεραπεία ενηλίκων με Γνωσιακή Συμπεριφορική Θεραπεία (CBT) και Θεραπεία Αποδοχής και Δέσμευσης (ACT). Έδρα Βύρωνας Αττικής.",
   "url": "./", "telephone": PHONE, "image": "assets/img/maria-angelopoulou-psychologos-psychotherapeftria-1040.webp", "logo": "assets/icons/icon-512.png",
   "priceRange": "€€", "medicalSpecialty": "Psychiatric",
   "address": {"@type": "PostalAddress", "addressLocality": "Βύρωνας", "postalCode": "16231", "addressRegion": "Αττική", "addressCountry": "GR"},
   "areaServed": [{"@type": "Country", "name": "Ελλάδα"}, {"@type": "City", "name": "Αθήνα"}],
   "hasMap": GMAP,
   "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "21:00"}],
   "paymentAccepted": "Bank transfer, Credit card",
   "availableLanguage": ["el", "en", "fr"],
   "knowsAbout": ["Ψυχοθεραπεία", "Online ψυχοθεραπεία", "Γνωσιακή Συμπεριφορική Θεραπεία (CBT)", "Θεραπεία Αποδοχής και Δέσμευσης (ACT)", "Άγχος", "Κρίσεις πανικού", "Φοβίες", "Κατάθλιψη", "Ιδεοψυχαναγκαστική διαταραχή", "Μετατραυματικό στρες", "Άγχος υγείας", "Διαχείριση πένθους", "Αυτοεκτίμηση"],
   "aggregateRating": {"@type": "AggregateRating", "ratingValue": "5.0", "reviewCount": "14", "bestRating": "5"},
   "sameAs": [GMAP, "https://www.instagram.com/angelopouloumaria.psy/", "https://www.linkedin.com/in/maria-angelopoulou00", "https://www.melapus.com/el/therapists/aggelopoyloy-maria1", "https://www.xo.gr/profile/profile-911757093/el/"],
   "founder": {"@id": "#maria"}},
  {"@type": "Person", "@id": "#maria", "name": "Μαρία Αγγελοπούλου", "alternateName": ["Maria Angelopoulou", "Μαρία Αγγελοπουλου"],
   "jobTitle": "Ψυχολόγος – Ψυχοθεραπεύτρια", "image": "assets/img/maria-angelopoulou-psychologos-psychotherapeftria-1040.webp", "telephone": PHONE,
   "worksFor": {"@id": "#practice"}, "knowsLanguage": ["el", "en", "fr"],
   "alumniOf": {"@type": "CollegeOrUniversity", "name": "Εθνικό και Καποδιστριακό Πανεπιστήμιο Αθηνών"},
   "hasCredential": [{"@type": "EducationalOccupationalCredential", "credentialCategory": "license", "name": "Άδεια άσκησης επαγγέλματος ψυχολόγου 424449/06-04-2023", "recognizedBy": {"@type": "GovernmentOrganization", "name": "Ελληνική Δημοκρατία"}},
                     {"@type": "EducationalOccupationalCredential", "credentialCategory": "degree", "name": "Πτυχίο Ψυχολογίας, ΕΚΠΑ (2018–2022)"}],
   "knowsAbout": ["Γνωσιακή Συμπεριφορική Θεραπεία (CBT)", "Θεραπεία Αποδοχής και Δέσμευσης (ACT)", "Κλινική ψυχοπαθολογία"],
   "sameAs": ["https://www.instagram.com/angelopouloumaria.psy/", "https://www.linkedin.com/in/maria-angelopoulou00"]},
  {"@type": "WebSite", "name": "Μαρία Αγγελοπούλου – Ψυχολόγος, Ψυχοθεραπεύτρια", "alternateName": ["Maria Angelopoulou Psychologist"], "url": "./", "inLanguage": "el"},
  {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, _, a, _ in FAQ]},
]}

TITLE = 'Μαρία Αγγελοπούλου | Ψυχολόγος – Ψυχοθεραπεύτρια Online, Αθήνα'
DESC = 'Μαρία Αγγελοπούλου, ψυχολόγος – ψυχοθεραπεύτρια (CBT & ACT). Online ατομική ψυχοθεραπεία ενηλίκων για άγχος, πανικό, κατάθλιψη, ΙΨΔ. Βύρωνας, Αθήνα · 694 515 2180.'

def fonts_css():
    G = 'U+0370-0377,U+037A-037F,U+0384-038A,U+038C,U+038E-03A1,U+03A3-03FF'
    GX = 'U+1F00-1FFF'
    LA = 'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD'
    o = []
    for fam, f, w in [('GFS Didot', 'gfs-didot', 400), ('Commissioner', 'commissioner', 400), ('Commissioner', 'commissioner', 600)]:
        for sub, rng in [('greek', G), ('latin', LA)]:
            o.append(f"@font-face{{font-family:'{fam}';font-style:normal;font-display:swap;font-weight:{w};src:url(assets/fonts/{f}-{sub}-{w}-normal.woff2) format('woff2');unicode-range:{rng}}}")
    return '\n'.join(o)

def build():
    mark = rd('mark.d').strip()
    body = rd('body.html')
    rep = {'MARK': mark, 'GREV': GREV, 'TICKS': ticks(), 'AREAS': areas_html(), 'NODES': nodes_html(), 'OPEN': OPEN_D,
           'REVIEWS': reviews_html(), 'FAQ': faq_html(), 'HOURS': hours_html(), 'STARS': STARS}
    for k, v in rep.items(): body = body.replace('{{' + k + '}}', v)
    assert '{{' not in body, re.findall(r'\{\{\w+\}\}', body)
    js = rd('script.js').replace('{{AREAS_JSON}}', json.dumps(AREAS, ensure_ascii=False)).replace('{{CYC_JSON}}', json.dumps(CYC, ensure_ascii=False))
    css = rd('style.css')
    page = f'''<!doctype html>
<html lang="el">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(TITLE)}</title>
<meta name="description" content="{esc(DESC)}">
<meta name="theme-color" content="#F7F2EC">
<meta name="color-scheme" content="light only">
<meta property="og:type" content="website">
<meta property="og:locale" content="el_GR">
<meta property="og:locale:alternate" content="en_GB">
<meta property="og:title" content="{esc(TITLE)}">
<meta property="og:description" content="{esc(DESC)}">
<meta property="og:image" content="assets/img/og.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Μαρία Αγγελοπούλου, ψυχολόγος – ψυχοθεραπεύτρια">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="assets/fonts/gfs-didot-greek-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/commissioner-greek-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<style id="advon-fonts">{fonts_css()}</style>
<script>document.documentElement.classList.add('js')</script>
<style>{css}</style>
<script type="application/ld+json">{json.dumps(LD, ensure_ascii=False)}</script>
</head>
<body>
{body}
<script>{js}</script>
</body>
</html>
'''
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(page)
    for f, c in [('.nojekyll', ''), ('robots.txt', 'User-agent: *\nAllow: /\n'), ('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n</urlset>\n')]:
        p = os.path.join(OUT, f)
        if not os.path.exists(p): open(p, 'w').write(c)
    print('index.html', len(page) // 1024, 'KB')

if __name__ == '__main__':
    build()
