import re, sys
src = open(sys.argv[1]).read()
K = 96/400
OX = -4191.348718 + 530.015385  # outer + inner group translate

def mat(a,b,c,d,e,f): return (a,b,c,d,e,f)
def mul(m, n):  # m then applied after n: m*n
    a,b,c,d,e,f = m; A,B,C,D,E,F = n
    return (a*A+c*B, b*A+d*B, a*C+c*D, b*C+d*D, a*E+c*F+e, b*E+d*F+f)
base = mul(mat(K,0,0,K,0,0), mat(1,0,0,1,OX,0))

def fmt(v):
    s = f"{v:.2f}".rstrip('0').rstrip('.')
    return "0" if s in ("-0","") else s

def bake(d, m):
    a,b,c,dd,e,f = m
    out=[]
    for cmd, args in re.findall(r'([MCLZ])([^MCLZ]*)', d):
        nums=[float(x) for x in re.findall(r'-?[\d.]+', args)]
        pts=[]
        for i in range(0,len(nums),2):
            x,y=nums[i],nums[i+1]
            pts.append(f"{fmt(a*x+c*y+e)},{fmt(b*x+dd*y+f)}")
        out.append(cmd+" ".join(pts))
    return "".join(out)

paths=[]; seen=set()
for tr, d in re.findall(r'<g transform="matrix\(([^)]*)\)">\s*<path d="([^"]+)"', src):
    if tr in seen: continue  # first pill is duplicated in the export
    seen.add(tr)
    m = mul(base, tuple(float(x) for x in tr.split(',')))
    paths.append(f'<path d="{bake(d,m)}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>')
gear = re.findall(r'</g>\s*<path d="([^"]+)"', src)[-1]
paths.append(f'<path d="{bake(gear,base)}" fill="currentColor" fill-rule="evenodd" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>')
print('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 96">'+"".join(paths)+'</svg>')