import json
seed=open(__import__('sys').argv[1] if len(__import__('sys').argv)>1 else 'project_seed.json').read().replace('<','\\u003c')
h=open('src/head.html').read().replace('/*SEED*/',seed)
js=''.join(open('src/'+f).read() for f in ['core.js','views1.js','views2.js','views3.js','views4.js'])
open(__import__('sys').argv[2] if len(__import__('sys').argv)>2 else 'index.html','w').write(h+js)
