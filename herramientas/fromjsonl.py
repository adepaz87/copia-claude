# Extract every Claude_Docs export result (inline or saved file) from a session transcript and decode it.
import json,sys,base64,os,re,glob
tr,outroot=sys.argv[1],sys.argv[2]
def handle(txt):
    i=txt.find('{"verdict"')
    if i<0: return
    try: j=json.loads(txt[i:txt.rfind('}')+1])
    except Exception: return
    d=j.get("data") or {}
    b=d.get("bytes_b64")
    url=(j.get("frame") or {}).get("artifactUrl","")
    if not b or not url: return
    aid=url.rstrip("/").split("/")[-1]
    name=re.sub(r'[\\/:*?"<>|]+','_',d.get("name") or "doc")[:120]
    od=os.path.join(outroot,aid); os.makedirs(od,exist_ok=True)
    open(os.path.join(od,name),"wb").write(base64.b64decode(b))
    print(aid,name,d.get("bytes"))
for line in open(tr):
    try: m=json.loads(line)
    except Exception: continue
    c=(m.get("message") or {}).get("content")
    if not isinstance(c,list): continue
    for part in c:
        if part.get("type")!="tool_result": continue
        cc=part.get("content")
        texts=[cc] if isinstance(cc,str) else [x.get("text","") for x in (cc or []) if isinstance(x,dict)]
        for t in texts:
            handle(t)
            for p in re.findall(r'(/root/\.claude/projects/\S+?/tool-results/mcp-Claude_Docs-export-\d+\.txt)',t):
                if os.path.exists(p): handle(open(p).read())
