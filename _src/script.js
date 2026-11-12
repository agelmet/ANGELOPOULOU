(function(){
var D=document,H=D.documentElement,W=window;
var RM=matchMedia('(prefers-reduced-motion:reduce)').matches;
var $=function(s,r){return (r||D).querySelector(s)},$$=function(s,r){return [].slice.call((r||D).querySelectorAll(s))};
var META={el:{t:D.title,d:($('meta[name="description"]')||{}).content||''},en:{t:'Maria Angelopoulou | Psychologist – Psychotherapist, CBT & ACT, Online',d:'Maria Angelopoulou, licensed psychologist and psychotherapist (CBT & ACT). Individual online psychotherapy for adults — anxiety, panic, depression, OCD. Based in Vyronas, Athens. Call 694 515 2180.'}};
var LANG='el';

/* ---------- language ---------- */
var ATTR={'data-en-alt':'alt','data-en-aria':'aria-label','data-en-title':'title'};
function setLang(l){
  if(l===LANG)return;LANG=l;H.lang=l;
  $$('[data-en]').forEach(function(e){if(e.dataset.el==null)e.dataset.el=e.innerHTML;e.innerHTML=l==='en'?e.dataset.en:e.dataset.el});
  Object.keys(ATTR).forEach(function(k){$$('['+k+']').forEach(function(e){var a=ATTR[k],s='data-el-'+a;if(!e.hasAttribute(s))e.setAttribute(s,e.getAttribute(a)||'');e.setAttribute(a,l==='en'?e.getAttribute(k):e.getAttribute(s))})});
  D.title=META[l].t;var md=$('meta[name="description"]');if(md)md.content=META[l].d;
  $$('.lg').forEach(function(b){var on=b.dataset.l===l;b.classList.toggle('on',on);b.setAttribute('aria-pressed',on)});
  try{localStorage.setItem('ma-lang',l)}catch(e){}
  $$('.lc').forEach(function(h){delete h.dataset.lc;split(h);h.classList.add('in')});
  qSplit();areaShow(cur,true);cycText();hoursNow();
}
$$('.lg').forEach(function(b){b.addEventListener('click',function(){setLang(b.dataset.l)})});

/* ---------- letter cascade on section headings ---------- */
function split(h){if(h.dataset.lc)return;h.dataset.lc=1;h.setAttribute('aria-label',h.textContent.replace(/\s+/g,' ').trim());var i=0;
  (function walk(n){[].slice.call(n.childNodes).forEach(function(c){
    if(c.nodeType===3){var f=D.createDocumentFragment();c.textContent.split(/(\s+)/).forEach(function(w){if(!w)return;if(/^\s+$/.test(w)){f.appendChild(D.createTextNode(' '));return}
      var ws=D.createElement('span');ws.className='lc-w';ws.setAttribute('aria-hidden','true');Array.from(w).forEach(function(ch){var s=D.createElement('span');s.className='lc-c';s.style.setProperty('--i',i++);s.textContent=ch;ws.appendChild(s)});f.appendChild(ws)});c.replaceWith(f)}
    else if(c.nodeType===1&&c.tagName!=='BR')walk(c)})})(h)}

/* ---------- reveal ---------- */
var io=('IntersectionObserver' in W)&&!RM?new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -8% 0px',threshold:.04}):null;
function watch(sel){$$(sel).forEach(function(e){io?io.observe(e):e.classList.add('in')})}
if(!RM)$$('.lc').forEach(split);
watch('.rv,.lc,.proof,.logo-card,.ap,.extras,.g-card');

/* ---------- intro: the clock hand sweeps the page open ---------- */
var intro=$('#intro'),hero=$('.hero');
function heroGo(){hero.classList.add('go')}
var seen=false;try{seen=sessionStorage.getItem('ma-intro')}catch(e){}
if(!intro||RM||seen||D.hidden){if(intro)intro.remove();heroGo()}
else{try{sessionStorage.setItem('ma-intro',1)}catch(e){}
  var done=function(){if(intro.parentNode)intro.remove()};
  setTimeout(function(){intro.classList.add('go');setTimeout(heroGo,380)},1150);
  intro.addEventListener('animationend',function(e){if(e.animationName==='sweepOpen')done()});
  setTimeout(function(){done();heroGo()},3400)}

/* ---------- header, progress, bars ---------- */
var hd=$('#hd'),prog=$('#prog'),mbar=$('#mbar'),tt=$('#totop'),ticking=false;
function onScroll(){ticking=false;var y=scrollY,h=D.documentElement.scrollHeight-innerHeight,p=h>0?y/h:0;
  hd.classList.toggle('solid',y>30);H.classList.toggle('scrolled',y>60);
  prog.style.setProperty('--p',p.toFixed(4));tt.style.setProperty('--p',p.toFixed(4));tt.classList.toggle('on',y>innerHeight*1.2);
  mbar.classList.toggle('on',y>innerHeight*.55);
  steps();cvFill();ctLine();quoteLight();aboutLight();}
addEventListener('scroll',function(){if(!ticking){ticking=true;requestAnimationFrame(onScroll)}},{passive:true});
addEventListener('resize',function(){stBuild();onScroll()});
tt.addEventListener('click',function(){scrollTo({top:0,behavior:RM?'auto':'smooth'})});

/* ---------- mobile menu ---------- */
var bg=$('.burger'),mn=$('#mnav');
function menu(o){H.classList.toggle('menu-open',o);bg.setAttribute('aria-expanded',o);D.body.style.overflow=o?'hidden':''}
bg.addEventListener('click',function(){menu(!H.classList.contains('menu-open'))});
$('.mnav-x').addEventListener('click',function(){menu(false)});
$$('a',mn).forEach(function(a){a.addEventListener('click',function(){menu(false)})});
addEventListener('keydown',function(e){if(e.key==='Escape')menu(false)});

/* ---------- active nav ---------- */
var navA=$$('.nav a');
if(io){var so=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){navA.forEach(function(a){a.classList.toggle('on',a.getAttribute('href')==='#'+e.target.id)})}})},{rootMargin:'-45% 0px -50% 0px'});
  navA.forEach(function(a){var s=$(a.getAttribute('href'));if(s)so.observe(s)})}

/* ---------- about: paragraphs come into ink at the reading line ---------- */
var pps=$$('.about .pp');
function aboutLight(){var line=innerHeight*.72;pps.forEach(function(p){if(p.getBoundingClientRect().top<line)p.classList.add('lit')})}
if(RM)pps.forEach(function(p){p.classList.add('lit')});

/* ---------- areas ---------- */
var AREAS={{AREAS_JSON}};
var cur=0,ap=$('#apanel'),btns=$$('.a-btn'),mob=matchMedia('(max-width:900px)');
function areaShow(i,quiet){cur=i;var a=AREAS[i],en=LANG==='en';
  btns.forEach(function(b,k){b.setAttribute('aria-selected',k===i)});
  var fill=function(){$('#anum').textContent=(en?'Topic ':'Θέμα ')+(i+1)+' / '+AREAS.length;$('#ah').textContent=en?a.te:a.t;$('#ap').textContent=en?a.de:a.d};
  if(quiet||RM){fill();return}ap.classList.add('sw');setTimeout(function(){fill();ap.classList.remove('sw')},220)}
btns.forEach(function(b,i){b.addEventListener('click',function(){
  if(mob.matches){var li=b.parentNode,o=!li.classList.contains('open');$$('.a-list li').forEach(function(x){x.classList.remove('open');$('.a-btn',x).setAttribute('aria-expanded','false')});li.classList.toggle('open',o);b.setAttribute('aria-expanded',o)}
  areaShow(i)});
  b.addEventListener('mouseenter',function(){if(!mob.matches&&matchMedia('(hover:hover)').matches)areaShow(i)})});
areaShow(0,true);

/* ---------- signature: the avoidance cycle ---------- */
var CYC={{CYC_JSON}};
var stg=$('#stage'),nodes=$$('.node',stg),mode='loop',ctl=$('.cyc-ctl'),pill=$('.pill',ctl),cb=$$('button',ctl);
var LOOP=[[50,10],[88,38],[73,84],[27,84],[12,38]],OPEN=[[14,88],[31,69],[50,50],[68,31],[84,13]];
function place(){var P=mode==='open'?OPEN:LOOP;nodes.forEach(function(n,i){n.style.setProperty('--x',P[i][0]+'%');n.style.setProperty('--y',P[i][1]+'%')})}
function cycText(){var en=LANG==='en',M=CYC[mode];nodes.forEach(function(n,i){$('.lb',n).textContent=en?M.n[i].le:M.n[i].l;$('.tx',n).textContent=en?M.n[i].te:M.n[i].t});$('#cexp').textContent=en?M.xe:M.x}
function pillPos(){var b=cb[mode==='open'?1:0];pill.style.width=b.offsetWidth+'px';pill.style.transform='translateX('+(b.offsetLeft-5)+'px)'}
function setMode(m){mode=m;stg.classList.toggle('open',m==='open');cb.forEach(function(b){b.setAttribute('aria-pressed',b.dataset.m===m)});pillPos();place();
  var ex=$('#cexp');if(RM){cycText();return}ex.style.opacity=0;setTimeout(function(){cycText();ex.style.opacity=1},250);runT=0}
cb.forEach(function(b){b.addEventListener('click',function(){setMode(b.dataset.m);userSet=true})});
place();cycText();setTimeout(pillPos,60);addEventListener('load',pillPos);
var run=$('.run',stg),cP=$('.ring .c',stg),oP=$('.ring .o',stg),runT=0,onStage=false,userSet=false,last=0,autoT=0;
function frame(t){if(!onStage){last=0;return}var dt=last?Math.min(t-last,60):16;last=t;
  runT=(runT+dt/(mode==='open'?5200:6400))%1;var p=mode==='open'?oP:cP,L=p.getTotalLength(),pt=p.getPointAtLength(L*runT);
  run.setAttribute('cx',pt.x);run.setAttribute('cy',pt.y);
  var k=mode==='open'?Math.min(4,Math.floor(runT*5)):Math.floor(((runT+.1)%1)*5);nodes.forEach(function(n,i){n.classList.toggle('hot',i===k)});
  if(!userSet){autoT+=dt;if(autoT>9000){autoT=0;setMode(mode==='open'?'loop':'open')}}
  requestAnimationFrame(frame)}
if(io&&!RM){new IntersectionObserver(function(es){es.forEach(function(e){onStage=e.isIntersecting;if(onStage){stg.classList.add('in');requestAnimationFrame(frame)}})},{threshold:.25}).observe(stg)}else stg.classList.add('in');

/* ---------- approach quote lights word by word ---------- */
var qp=$('#quote p');
function qSplit(){var t=qp.textContent;qp.innerHTML=t.split(' ').map(function(w){return '<span class="wd">'+w+'</span>'}).join(' ')}
qSplit();
function quoteLight(){var r=qp.getBoundingClientRect(),ws=$$('.wd',qp),f=RM?1:Math.min(1,Math.max(0,(innerHeight*.85-r.top)/(innerHeight*.45)));ws.forEach(function(w,i){w.classList.toggle('on',i<f*ws.length+.01)})}

/* ---------- steps: a line drawn with the scroll ---------- */
var stw=$('#stw'),stl=$('#stl'),sBg=$('.bg',stl),sFg=$('.fg',stl),sN=$$('.st-list .n'),sLen=0;
function stBuild(){var R=stw.getBoundingClientRect(),pts=sN.map(function(n){var b=n.getBoundingClientRect();return [b.left-R.left+b.width/2,b.top-R.top+b.height/2]});
  stl.setAttribute('viewBox','0 0 '+R.width+' '+R.height);stl.setAttribute('width',R.width);stl.setAttribute('height',R.height);
  var d='M'+pts[0][0]+' '+pts[0][1];for(var i=1;i<pts.length;i++){var a=pts[i-1],b=pts[i],mx=(a[0]+b[0])/2,vert=Math.abs(b[1]-a[1])>Math.abs(b[0]-a[0]);
    d+=vert?' C'+(a[0]-40)+' '+((a[1]+b[1])/2)+' '+(b[0]+40)+' '+((a[1]+b[1])/2)+' '+b[0]+' '+b[1]:' C'+mx+' '+(a[1]-46)+' '+mx+' '+(b[1]+46)+' '+b[0]+' '+b[1]}
  sBg.setAttribute('d',d);sFg.setAttribute('d',d);sLen=sFg.getTotalLength();sFg.style.strokeDasharray=sLen;steps()}
function steps(){if(!sLen)return;var r=stw.getBoundingClientRect(),f=RM?1:Math.min(1,Math.max(0,(innerHeight*.8-r.top)/(r.height+innerHeight*.25)));
  sFg.style.strokeDashoffset=sLen*(1-f);sN.forEach(function(n,i){n.parentNode.classList.toggle('on',f>=(i/(sN.length-1))*.94)})}
stBuild();

/* ---------- CV lines fill with the scroll ---------- */
var tls=$$('.tl');
function cvFill(){tls.forEach(function(t){var r=t.getBoundingClientRect(),f=RM?1:Math.min(1,Math.max(0,(innerHeight*.75-r.top)/r.height));t.style.setProperty('--p',f.toFixed(3));
  $$('.it',t).forEach(function(it){it.classList.toggle('on',it.getBoundingClientRect().top<innerHeight*.75||RM)})})}

/* ---------- contact: her line draws itself ---------- */
var ct=$('.ct'),ctl2=$('.ct .bgline .lc-m');
function ctLine(){var r=ct.getBoundingClientRect(),f=RM?1:Math.min(1,Math.max(0,(innerHeight-r.top)/(innerHeight*.9)));ctl2.style.setProperty('--p',f.toFixed(3))}

/* ---------- reviews: one big quote at a time ---------- */
var rq=$('#rq'),qs=$$('.q',rq),dots=$('#rqd'),qi=0,qt=null,qpause=false,DUR=7500;
qs.forEach(function(q,i){var b=D.createElement('button');b.type='button';b.setAttribute('aria-label',(i+1)+' / '+qs.length);b.innerHTML='<i></i>';b.addEventListener('click',function(){qShow(i)});dots.appendChild(b)});
var db=$$('button',dots);
function qShow(i){qi=(i+qs.length)%qs.length;qs.forEach(function(q,k){q.classList.toggle('on',k===qi);q.setAttribute('aria-hidden',k!==qi)});
  db.forEach(function(b,k){b.classList.toggle('done',k<qi);b.classList.remove('on');if(k===qi){void b.offsetWidth;b.classList.add('on')}});
  clearTimeout(qt);if(!RM&&!qpause&&revOn)qt=setTimeout(function(){qShow(qi+1)},DUR)}
dots.style.setProperty('--dur',DUR+'ms');
$$('.rq-arrows button').forEach(function(b){b.addEventListener('click',function(){qShow(qi+ +b.dataset.d)})});
var nav=$('#rqn');[rq,nav].forEach(function(el){el.addEventListener('mouseenter',function(){qpause=true;nav.classList.add('paused');clearTimeout(qt)});el.addEventListener('mouseleave',function(){qpause=false;nav.classList.remove('paused');qShow(qi)})});
var sx=null;rq.addEventListener('touchstart',function(e){sx=e.touches[0].clientX},{passive:true});rq.addEventListener('touchend',function(e){if(sx==null)return;var dx=e.changedTouches[0].clientX-sx;if(Math.abs(dx)>40)qShow(qi+(dx<0?1:-1));sx=null});
var revOn=false;if(io){new IntersectionObserver(function(es){revOn=es[0].isIntersecting;if(revOn)qShow(qi);else clearTimeout(qt)},{threshold:.3}).observe(rq)}
qShow(0);
var gs=$('.g-card .stars');if(io){new IntersectionObserver(function(es){if(es[0].isIntersecting)gs.classList.add('lit')},{threshold:.5}).observe(gs)}else gs.classList.add('lit');

/* ---------- hours: open now (Athens time) ---------- */
function hoursNow(){var n=$('#now');try{var f=new Intl.DateTimeFormat('en-GB',{timeZone:'Europe/Athens',weekday:'short',hour:'2-digit',minute:'2-digit',hour12:false}).formatToParts(new Date()),o={};f.forEach(function(p){o[p.type]=p.value});
  var wd=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'].indexOf(o.weekday),m=+o.hour*60+ +o.minute,open=wd<5&&m>=540&&m<1260,en=LANG==='en';
  $$('#hrs tr').forEach(function(tr,i){tr.classList.toggle('today',i===wd)});
  n.classList.toggle('off',!open);$('span',n).textContent=open?(en?'Available now · until 21:00':'Διαθέσιμη τώρα · έως τις 21:00'):(en?'Outside hours · leave a message':'Εκτός ωραρίου · αφήστε μήνυμα')}catch(e){n.style.display='none'}}
hoursNow();setInterval(hoursNow,60000);
$('#yr').textContent=new Date().getFullYear();

/* ---------- start ---------- */
var saved=null;try{saved=localStorage.getItem('ma-lang')}catch(e){}
if(saved==='en')setLang('en');
onScroll();
})();
