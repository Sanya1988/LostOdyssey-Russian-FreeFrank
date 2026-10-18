"""Validate and reproducibly package this data-only release; Python standard library only.

Licensing of this newly authored tool is pending the owner's publication decision;
see LICENSE.md. No FreeFrank source code or private converter is incorporated.
"""
import argparse
import csv
import hashlib
import json
import pathlib
import re
import struct
import zipfile

ROOT=pathlib.Path(__file__).resolve().parents[1]
BASE=ROOT/'package'
ADDON=ROOT/'optional/experimental-dreams'
VERSION='0.1.0-beta'
ALLOWED={'.json','.ini','.lofont','.txt','.md','.py','.yml','.csv','.gitignore'}
SECRET=re.compile(rb'(?:github_pat_[A-Za-z0-9_]{30,}|gh[pousr]_[A-Za-z0-9]{30,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)')

def require(ok,message):
    if not ok:raise ValueError(message)

def sha(data):return hashlib.sha256(data).hexdigest()

def unique(pairs):
    result={}
    for k,v in pairs:
        require(k not in result,'duplicate JSON key');result[k]=v
    return result

def files(root):return {p.relative_to(root).as_posix():p for p in sorted(root.rglob('*')) if p.is_file()}

def manifest(root):return {k:sha(p.read_bytes()) for k,p in files(root).items()}

def validate():
    require(not (ROOT/'.git/objects/info/alternates').exists(),'external Git object dependency')
    counts={}
    for label,root in [('base',BASE),('experimental_dreams',ADDON)]:
        all_rows=files(root)
        require(all(k.startswith('mods/ru/') or label=='experimental_dreams' and k=='README.md' for k in all_rows),'unexpected package file')
        rows={k:p for k,p in all_rows.items() if k.startswith('mods/ru/')};keys=0;resources=0;fonts=0
        for name,p in rows.items():
            require(not p.is_symlink(),'symlink in package')
            require(name.startswith('mods/ru/'),'unexpected installation root')
            b=p.read_bytes();require(not SECRET.search(b),'credential-shaped content')
            require(not re.search(rb'C:[\\/]Users[\\/]',b),'private local path')
            if p.suffix=='.lofont':
                require(name.startswith('mods/ru/fonts/'),'font outside fonts')
                require(len(b)>=32,'short font')
                magic,header,n,w,h,zero=struct.unpack_from('<12sIIIII',b)
                require(magic==b'LOFONT1\r\n\0\0\0' and header==32 and zero==0,'font header')
                require(0<n<=1024 and 0<w<=4096 and 0<h<=4096 and len(b)==32+n*12+w*h*4,'font bounds')
                cps=set();rgba=b[32+n*12:]
                for i in range(n):
                    cp,x,y,gw,gh=struct.unpack_from('<IHHHH',b,32+12*i)
                    require(cp not in cps and 0<gw and 0<gh and x+gw<=w and y+gh<=h,'font glyph')
                    require(any(rgba[((y+dy)*w+x+dx)*4+3] for dy in range(gh) for dx in range(gw)),'invisible glyph')
                    cps.add(cp)
                require(any(0x0400<=c<=0x04ff for c in cps),'no Cyrillic glyphs');fonts+=1
            else:
                require(p.suffix in ('.json','.ini','.md','.txt'),'unapproved payload file')
                s=b.decode('utf-8');require('\0' not in s,'NUL in text')
                require(not any(0xd800<=ord(c)<=0xdfff for c in s),'invalid Unicode surrogate')
                if '/text/' in name:
                    require(p.suffix=='.json','non-JSON text override')
                    obj=json.loads(s,object_pairs_hook=unique)
                    require(isinstance(obj,dict) and obj and all(isinstance(k,str) and isinstance(v,str) for k,v in obj.items()),'text mapping')
                    keys+=len(obj);resources+=1
                    for value in obj.values():
                        # Tokens are four-digit native units, optionally with a four-digit parameter.
                        require(not re.search(r'\{[0-9A-Fa-f]{1,3}\}|\{[0-9A-Fa-f]{5,}\}',value),'malformed native token')
            require(p.suffix not in ('.exe','.dll','.fpd','.fpi','.xex','.bin','.png','.dds','.lotex2','.zip'),'prohibited asset')
        counts[label]=dict(keys=keys,text_resources=resources,lofonts=fonts,files=len(rows))
    ini=dict(line.split('=',1) for line in (BASE/'mods/ru/language.ini').read_text(encoding='utf-8').splitlines() if line and not line.startswith(('#',';')))
    require(ini==dict(id='ru',name='Русский',base='int'),'language pack manifest')
    require(counts['base']['keys']==27951 and counts['base']['text_resources']==536 and counts['base']['lofonts']==11,'base counts')
    require(counts['experimental_dreams']['keys']==7802 and counts['experimental_dreams']['text_resources']==34,'Dream counts')
    require(all('/event/1000/int/dr_' not in name for name in files(BASE)),'Dream overrides in default package')
    require((BASE/'mods/ru/licenses/NotoSans-OFL.txt').is_file(),'missing OFL')
    expected=ROOT/'PUBLIC_FILE_MANIFEST.csv'
    if expected.exists():
        with expected.open(encoding='utf-8',newline='') as f:
            for row in csv.DictReader(f):
                p=ROOT/row['path'];require(p.is_file() and p.stat().st_size==int(row['bytes']) and sha(p.read_bytes())==row['sha256'],'manifest mismatch: '+row['path'])
    return counts

def package_entries(addon=False):
    root=ADDON if addon else BASE
    entries={name:p.read_bytes() for name,p in files(root).items() if name.startswith('mods/ru/')}
    for p in sorted((ROOT/'docs').glob('*')):
        if p.is_file():entries['mods/ru/docs/'+p.name]=p.read_bytes()
    for name in ('README.md','README.ru.md','README.en.md','LICENSE.md','THIRD_PARTY_NOTICES.md','RELEASE_NOTES.md'):
        # Installation documents are frozen separately from the GitHub screenshot page.
        entries['mods/ru/'+name]=(ROOT/'release-docs'/name).read_bytes()
    if addon:entries['mods/ru/EXPERIMENTAL_DREAMS.md']=(ROOT/'optional/experimental-dreams/README.md').read_bytes()
    sums='mods/ru/SHA256SUMS-'+('dreams' if addon else 'base')+'.txt'
    entries[sums]=(''.join(sha(b)+'  '+name+'\n' for name,b in sorted(entries.items()))).encode('utf-8')
    return entries

def write_zip(destination,entries):
    with zipfile.ZipFile(destination,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for name,data in sorted(entries.items()):
            require(not name.startswith('/') and '..' not in pathlib.PurePosixPath(name).parts,'unsafe ZIP path')
            info=zipfile.ZipInfo(name,date_time=(2026,10,18,0,0,0));info.create_system=3;info.external_attr=0o100644<<16
            info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,data,compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
    with zipfile.ZipFile(destination) as z:
        require(z.testzip() is None,'ZIP CRC failure')
        require(set(z.namelist())==set(entries),'ZIP member mismatch')
        require(all(z.read(n)==v for n,v in entries.items()),'ZIP payload mismatch')

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('command',choices=['validate','package']);parser.add_argument('--output',type=pathlib.Path)
    args=parser.parse_args();counts=validate()
    if args.command=='package':
        require(args.output is not None,'--output required');args.output.mkdir(parents=True,exist_ok=True)
        for addon,name in [(False,'LostOdyssey-Russian-Language-Pack-v'+VERSION+'.zip'),(True,'LostOdyssey-Russian-Dreams-v'+VERSION+'-EXPERIMENTAL.zip')]:
            target=args.output/name;require(not target.exists(),'output already exists');write_zip(target,package_entries(addon))
            print(name,sha(target.read_bytes()),target.stat().st_size)
    print(json.dumps(dict(status='PASS',counts=counts),indent=2))
if __name__=='__main__':main()
