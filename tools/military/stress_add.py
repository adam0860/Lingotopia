import sys
V="аеёиоуыэюя"
def mk(spec, out='stress_lex.txt'):
    res=[]
    for it in spec.replace("\n","|").split("|"):
        it=it.strip()
        if not it: continue
        w,n=it.rsplit(None,1); n=int(n); c=0; r=""
        for ch in w:
            r+=ch
            if ch in V:
                c+=1
                if c==n: r+="'"
        assert "'" in r,(w,n)
        res.append(r)
    open(out,'a',encoding='utf-8').write(" ".join(res)+"\n")
if __name__=="__main__":
    mk(sys.stdin.read())
