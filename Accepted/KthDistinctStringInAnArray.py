class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:

        letterDict = {}
        counter = 0
        uCounter = 0


        for letter in arr:
            if letter not in letterDict:
                letterDict[letter] = 1
            else:
                letterDict[letter] += 1
        


        #basecase
        for key in letterDict:
            if letterDict[key] == 1:
                uCounter +=1
        if uCounter < k:
            return ""

        
        for letter in arr:
            if letterDict[letter] == 1 and counter == k-1:
                return letter
            elif letterDict[letter] == 1:
                counter +=1
        
        

                







arr = ["joy","pt","yoe","ibria","suvc","d","gua","izen","slt","oe","i","ajcc","gyz","vkx","xy","ktc","i","pgjr","y","qub","wdnu","l","xiu","yv","bdo","gzh","ud","ak","gkz","bsm","w","bgq","zwg","voecw","h","jxjwl","cn","l","uvv","hqy","l","ygpla","gyf","jndji","nm","pabi","wmi","n","c","u","wyy","sze","lgjce","l","eq","hjh","lww","nw","mgf","r","rju","ohcfj","iuo","y","okmx","k","r","rlj","ptw","grniz","youwc","tuox","ib","fqpsi","hteuo","nwgps","dpa","fiksn","dx","zkxvx","wraa","ang","c","fs","kbog","fju","b","guel","alpez","ugahf","uqt","wi","bgvl","sasdu","tbhmj","rnh","litf","tjlp","m","zbtla","tqz","hohg","rad","sba","v","ro","pxj","qf","pv","olku","yhw","ch","vl","iix","nyddk","gh","whpog","lbq","iaz","l","e","mrtv","amru","wu","pcdvm","e","ncal","bvsgi","twl","vysw","bb","pgv","ux","rl","ejt","x","ky","kjdhv","rwit","ko","p","tnvm","tzxar","sfl","y","a","qgdlj","tt","kswr","loos","wg","vzuv","et","pgl","nn","mmwz","qykk","agc","b","wqoc","f","xxp","s","jbew","uggel","gpgc","gmpp","lqcsc","xoym","joni","mfj","p","xhcp","ecxlb","h","y","plt","qm","wvao","qpui","eye","my","q","iwu","shwo","r","pykh","qvia","z","vla","nna","lxzq","frktm","i","tu","eikj","uyfxj","vos","gp","nqm","t","os","asou","qjp","hkwah","rsvxh","a","ywka","lvrq","l","jcgy","snyxu","nuaot","dwjir","bkzgc","nr","o","tclx","g","kx","clog","zbvcs","xmau","upqzf","tngrn","oy","rinwh","mpg","w","kywaj","xge","brg","we","fs","cjby","pyfk","nubf","nautu","h","i","ar","m","a","upbbm","zlmtm","lz","yjia","wze","cjqh","ut","onws","zdlv","wx","vma","ol","cfl","j","htmn","w","f","mdaub","ut","gyqdc","od","yi","tn","xwxh","w","ny","dxis","alhj","dyjq","xrk","kt","xu","ud","ah","am","mcvw","j","bn","jvvk","fc","crc","ubmes","ixf","vzx","rbu","bx","cvif","yif","nb","rb","p","e","wko","pqw","rb","kw","dohos","oxbu","x","swto","yhhz","ci","kvmr","wa","jf","igi","b","rfvik","fs","oz","y","xba","ytobn","ff","drrut","t","p","uij","i","f","boap","oaag","qril","sxor","abwtp","wknu","ix","nmdt","mwran","w","y","owgp","oa","isy","fqran","v","h","lbbbv","fh","bazq","cdqg","iz","yjlyl","sgxj","wjytc","p","mfhn","pdaa","hflf","gg","te","spjp","w","yfgnx","p","lznn","crdvl","mwibr","ggq","i","wunt","nzqp","dd","qpio","ewyy","uqskd","awble","vijg","m","v","ry","irg","yw","rdyk","vdmu","vu","t","c","ac","s","jtse","v","rvfu","e","gna","z","c","swzsy","p","pc","rek","gji","l","ge","bfbux","eh","nks","opq","jso","rmc","opjf","rpyfp","gpvj","jjry","z","yn","gr","et","mftd","m","xrouc","do","yt","geunr","gvitv","szil","f","xttfy","b","ovwbj","h","jix","zg","zs","nnxev","eq","xra","hrby","ylp","czl","fx","ygo","hvzu","nf","vleo","xq","fgua","mhmaj","ysdx","i","xn","gbvbt","kcqi","fccz","jka","eei","nopb","qv","pvorb","g","sgjb","ffwjl","d","ldsd","qmsh","wd","zz","t","qhre","r","ghbs","r","jilcp","tfz","kd","kvog","wi","ybdu","ceo","qeue","be","t","sekeh","ph","yj","swt","vexey","udb","v","x","wy","pf","seuz","ebse","g","rlhbz","p","nfej","rpv","kbje","bbxk","uvnh","nwy","x","ripe","u","tvfml","nql","i","xbtm","w","i","jq","bgjd","osc","tzut","f","xfer","vhusd","dz","mikxe","e","bj","iu","jfjwe","jmv","av","qb","zh","v","lo","lttw","cey","lob","jrlr","hxx","umog","yh","hrdsb","ihax","mfde","kxyu","kc","ssbk","tn","xmz","hpib","am","dvmd","l","lzug","kewq","mfz","gta","ac","m","ds","undj","ynwt","qbr","a","bg","opeti","cbfe","wgoi","gv","iipuo","s","d","cwefs","re","wn","oylg","ehiyg","wwtf","lceat","ialm","xmrxk","qhnh","mouw","peeb","fhu","ralu","k","iouzo","qp","uznab","puyku","uoqe","ych","sc","tlwon","acb","xf","ca","wnqa","um","sbwb","sf","tx","x","dmuj","tc","iby","elj","cuib","tfz","hn","joj","iiqm","ox","dpa","bkrtq","isfc","radjn","wrfuf","kyz","kv","ct","v","axjxb","yt","ohti","io","lewot","wfy","vxb","ijnkw","sluzh","akn","olw","pmf","zca","cv","iitz","xv","o","uii","otcf","zkly","qy","u","rpd","bqlzy","kqz","gept","wurp","gpgx","nj","rz","kyavq","ago","pn","sy","wwpl","k","x","jnr","hnpuv","d","fw","m","qldrq","ntzs","eubps","beuw","rh","t","rwtyp","aivvc","guuuw","fii","qmww","icb","uoa","elwzv","woqij","qtuo","ibsah","ne","trc","jai","v","y","tgpy","huhjx","lu","pvd","irm","iut","mx","aoj","rymh","z","p","mygan","x","xr","bwgu","gnvz","cvol","utnuw","wl","liajp","oadnh","b","y","epv","qczgn","cbi","wtxwb","tg","djjy","nray","sfe","zl","ubk","tzlqt","td","nqqp","kejk","ld","ligej","erih","aj","lcgw","d","lwx","teedd","wrwlh","q","tqzkt","bf","bkj","okgac","f","df","kbimx","jf","s","hkopr","kb","hhud","awxk","xgyc","jso","cotyr","vhoya","x","x","b","yot","tozra","hj","dgq","seexd","d","nlo","o","odbt","cgdhl","nbk","ngfm","s","qbbld","xov","sw","fqc","vfwrb","gba","owrf","enrfi","ipr","ntteh","iu","wzrx","youv","acqq","hchhp","cggns","xs","vilr","lnc","obnr","p","fkkeq","thvih","ol","jq","w","ido","onn","zzao","yzsq","bvhjh","pqae","q","ni","vf","dztl","um","obq","dib","l","d","ksi","lja","qzdp","v","bam","bfulk","e","avks","wawx","z","en","yygo","otmj","b","pyrc","rh","xo","osf","drg","cg","zr","irdkf","cw","a","goqlq","kz","ci","i","hqi","uqhu","x","gw","mlczv","pf","m","qc","r","jtjg","ph","pnwq","tng","b","bct","qwi","kwreq","hk","gxf","yh","xajwe","nirc","dgwz","tq","d","coda","yw","eqows","cxk","pqs","lwxvs","xc","oanm","kf","f","jwaq","dtlw","z","sd","z","ibtb","icqqk","ai","neq","ajjb","uk","fwvi","qws","pnmt","r","rr","ot","btuph","t","uzd","y","qzi","mr","bhnub","c","njapp","h","uavu","jitl","a","vu","m","ar","jaab","doqbt","j","si","wnwfr","ikjs","vtqxj","rh","dp","le","tuyaa","xvoh","tfvfy","rept","k","xgb","bgh","rfse","ev","fzsyv","s","pmj","lgji","m","dhzeg","hr","cwg","jzbts","x","hscu","l","v","qsviy","cbwmw","sus","qx","cd","lzswf","yrebo","kxiji","yzttg","rw","dcutm","q","zc","ls","ypyyx","j","uby","cxi","giz","c","k","mmtsa","rwljp","p","cqyd","gjn","x","z","vxk","da","ewyo","wldqn","x","j","nmth","rcmp","eifm","efakn","hm","k","c","m","bqd","cvz","ob","mbw","zlh","bygh","pobp","bppz","gvbxr","wc","v","wqm","ku","tipun","xlyd","gygp","zg"]
k = 766
s = Solution()
print(s.kthDistinct(arr,k))