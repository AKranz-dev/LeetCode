#The only way to make this solution run faster is to implement threading. It is otherwise fully optimized. Passing 46/54 test cases.


import cProfile
import operator

class Solution:
    

    
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        
        xList = s.getXList(points)
        differenceDict = s.evaluateDiffrences(xList)        
        result = s.evaluateContainingPoints(differenceDict,xList)
        return result
        

    #Get a list of all X coordinates
    def getXList(self,points):
        xList = []
        for pair in points:
            xList.append(pair[0])   
        return xList         
    
    #Get a list of differences in x coordinates
    def evaluateDiffrences(self,xList):
        differenceDict = {}
        for num in xList:
            for item in xList:
                if (num,item) not in differenceDict and (item,num) not in differenceDict: 
                        difference = abs(num-item)
                        differenceDict[num,item] = difference
        return differenceDict
    
    
    #Iterate through the pairs of coordinates (starting with the pair that has the biggest difference in x coordinates, and moving smaller from there. This ensures the widest area is found.) checking if there are any points that have an x value between the pair of coordinate's x values
    def evaluateContainingPoints(self,differenceDict,xList):
        
        sortedDict = dict(sorted(differenceDict.items(), key=operator.itemgetter(1),reverse=True))

        for boundary in sortedDict:
            boundary=list(boundary)
            boundary.sort()

            
            #print("New pair of x coordinate boundaries is {},{} for a difference of {}".format(boundary[0],boundary[1],boundary[1]-boundary[0]))
            fail = 0
            for x in xList:
                if x > boundary[0] and x < boundary[1]: 
                    fail=1
                    break
            if fail == 0:
                return boundary[1]-boundary[0]

                
s = Solution()

points = [[9917470,721890],[7389502,7955520],[6346692,593558],[8387532,2477482],[4989565,352895],[7826578,4865917],[4075019,4183067],[1807726,9847751],[8220349,7255002],[320174,2753074],[2871445,18845],[9318480,1317365],[6033174,8531771],[1328938,5676493],[6290217,6745485],[31234,2296487],[525333,6193292],[3513688,5989979],[5379437,2615353],[95818,4468328],[6962010,6645406],[3455977,2597842],[796391,5944530],[5070998,6316206],[6463935,2923372],[6373398,4758593],[7598124,4107672],[7777433,5621042],[6778180,1178510],[5794036,1983694],[1246546,9921436],[6094146,6437958],[7222792,8343301],[8670022,2014624],[2614810,1701952],[3213038,5953808],[9892856,8469110],[5618242,9966807],[9923987,7090724],[4611217,9259418],[1180376,9134540],[9133232,760283],[8453634,8067877],[7004952,4216208],[4003141,6483782],[1525734,4569808],[5573822,5673442],[5587939,2981684],[1488995,1878407],[7269360,660773],[7626237,5487527],[141604,7073062],[4389875,2222999],[1979662,4269695],[52633,2368711],[1183021,7360112],[9662092,9680508],[2296150,5768401],[3863020,2298583],[4365224,9384830],[1105363,5925253],[9336499,7895675],[2852853,1666884],[3482067,9434526],[9901866,9658527],[9321666,1130861],[4164380,7969262],[7288597,9267148],[9679612,5103604],[7779243,2457311],[6228368,7129547],[7651186,8476116],[986852,2763674],[2752834,3306462],[3488572,7393447],[6123835,7403150],[66482,9233846],[2546201,9350049],[6156594,8468155],[5103191,2556923],[1923891,7566821],[7882491,122852],[9454719,7814885],[5974562,6903999],[9352797,3985867],[2547243,6325584],[8469780,2654123],[1551614,7900968],[8311432,9450914],[5671270,9357867],[4509832,7710585],[8357103,9597102],[9071131,9234307],[6371398,2548870],[6319038,6158392],[4638937,3020294],[2944892,7304205],[7075974,7970008],[7870309,623867],[310682,6452426],[7379226,725486],[9449641,5978741],[4931131,5218228],[1375423,1040600],[3688958,3239388],[2858308,6135511],[6731643,8926241],[9865189,5869475],[9792516,322709],[1107872,131957],[9559209,1268415],[7999308,1205914],[2698891,108172],[6455442,6968663],[8141057,9897882],[4662390,4228149],[6593028,7391355],[3603127,9668061],[3315369,6494909],[8743475,1482720],[4619383,6736349],[1284723,8652223],[2878922,5897845],[494398,7046407],[5320774,8374084],[6615356,2407861],[1712841,544307],[791674,5367389],[8933400,9228307],[7847725,2745795],[5715894,6047210],[4472892,4617876],[9448526,2835871],[2917097,327439],[1290281,927336],[330984,5713804],[3085473,7519397],[1058013,6159416],[52493,4397890],[2225291,9486755],[6298638,4785346],[3960552,8264548],[8224422,7565964],[1057104,8779210],[1048395,712003],[3554976,1398109],[5413185,3245412],[5224819,9904312],[274428,2110880],[7089219,2208483],[8712688,5565336],[1153925,8746713],[5362546,6844422],[8142444,8012294],[1619053,707359],[1266048,6739335],[5080900,8756239],[5836495,4022921],[8174023,1020193],[3661118,4878244],[7762726,6712707],[6364426,8224379],[8574682,3310031],[8881978,156230],[6966822,7574938],[6399274,5543908],[4338996,3768120],[604974,8999567],[8025896,4179435],[1498329,2032195],[514491,8208420],[4991662,6473735],[4284991,9564294],[5701128,7070935],[9436720,8971316],[7851672,299846],[1323644,8457343],[1784543,3432517],[4705578,849808],[5354184,1879021],[4456905,7853732],[4038821,9234101],[2229567,6899680],[9251595,5929394],[7670126,7075727],[6547773,2184654],[7544695,3383189],[8806021,8466215],[4015192,9523601],[1482071,1855148],[1973313,7935915],[7580132,3636921],[3025183,5229868],[5624208,3288012],[8071362,6393227],[854210,1480069],[38759,9832896],[8943707,914797],[3791748,9493208],[4879088,7746893],[2534808,486145],[461546,8444860],[2041645,8446464],[3500760,751423],[2720582,8345234],[3599117,6115350],[6205360,2214990],[7986778,668768],[4779021,3150516],[8878432,1106668],[2183562,9045963],[9033077,5248741],[9269708,2562222],[6339576,5835839],[1961325,1249575],[9887633,3664803],[4941662,9166212],[6181404,8731236],[5963610,6935710],[6207793,1614939],[9124655,3929428],[9717868,6962934],[6456746,1501340],[7186541,9373730],[7681543,947107],[4766112,2662981],[3851529,2914394],[9266909,9799562],[8630986,4868079],[7671297,8630586],[7543882,2046830],[5315825,5653734],[7240270,5098206],[1900231,8244858],[3954104,3945278],[5063532,4886572],[931682,4567816],[4653749,9921357],[685747,1215642],[5895588,9628631],[3870999,8840982],[7514710,6190131],[3248860,4405525],[5186542,7839717],[2715771,8903070],[4225351,1330926],[9709660,2845972],[9362226,5638289],[8841286,4193009],[2688229,5224214],[3504534,7840705],[5256730,1727183],[4469675,9479705],[4732167,8450419],[3153217,439038],[757324,7309316],[8695660,4529677],[5693189,3690033],[7761874,7954075],[9260229,7887642],[7186584,770769],[6153273,5739524],[73227,3460139],[5440356,7374024],[27632,5914484],[5837009,8944272],[5570987,9981941],[8550732,6391245],[8726716,4948935],[4726441,8661452],[5946901,9670952],[7588877,5589770],[7788884,8425607],[1627251,6001470],[7796464,7444504],[9234228,7348587],[7702184,7393610],[1148151,9052232],[9186069,1987658],[7222335,8918455],[93384,2480138],[7635449,3830403],[3529184,3847601],[3499372,7238454],[3272004,547126],[9767053,1434103],[8729117,8755238],[309821,6254635],[4652328,6698737],[1713867,3146670],[3941907,3232341],[675651,3105896],[9341806,9304675],[6412430,895618],[3313028,8010133],[5013796,776721],[1847347,2925651],[959497,776495],[9934634,1250361],[6807871,9495904],[2739667,6064962],[3352513,1114041],[7536140,945213],[4714393,7231179],[3622280,4648637],[2040760,5455983],[1629897,5663823],[44006,8485146],[3689920,4111434],[1080163,2934176],[1552459,2702675],[3110868,8401208],[1508966,4777331],[568313,4594752],[9523127,4159157],[2172254,4275240],[2217363,1320257],[2838509,6206256],[8762783,3516320],[3602954,3584323],[4238413,4317045],[9347372,5756452],[3392222,9449034],[1629934,9200979],[7599070,8426124],[2207893,3874549],[5382241,3278107],[8714509,9736076],[2850970,2875605],[9061247,6540402],[2192522,7230987],[6044432,2713585],[7950266,3511409],[8916965,5884171],[3422916,2133420],[132886,7622325],[4583687,2867249],[3440136,31026],[9658975,1148001],[6254830,9683951],[6867933,1842051],[4219785,1773977],[977616,1215368],[3857681,9699431],[2073321,9348471],[634177,4699866],[7244205,3363575],[6033467,8269520],[127790,8135528],[6620981,2516659],[7701079,4818152],[3023499,1129200],[7488682,7831519],[1412029,4582543],[8899607,3928593],[1957289,8890392],[1243317,572699],[2469349,3659462],[3678439,1509718],[5254594,5765615],[4502964,4412701],[6773371,5156317],[6007429,3839485],[1196670,7984341],[8147767,9891728],[9340405,5065114],[5085038,3276945],[1302743,9531677],[6755255,3952125],[7867867,9912914],[1613370,4130055],[6025923,8675787],[4427807,3909149],[7090456,3159808],[1487007,1971178],[3883301,4228802],[7958212,3770892],[3232513,9560312],[5907979,7796599],[8584754,8947953],[3893470,4812320],[9637383,406547],[7853375,6040789],[3711827,9499247],[3916087,8086256],[9159253,2018229],[828755,9374058],[4807997,4880642],[7487291,642986],[6041060,8124776],[3006614,1917417],[9121834,5026224],[168852,1173536],[6454138,7719760],[8935736,8508546],[5589617,8196960],[4454813,946367],[1187044,3386301],[9635463,4757001],[4354395,2271034],[8818474,2011983],[585868,4657763],[4228233,6952138],[5979958,1646243],[4096993,8868220],[1656919,538297],[3502257,3048406],[4898968,1156129],[3878557,4196000],[9413414,4365810],[9914566,8708052],[3255019,8474028],[5068131,919093],[3743798,1742367],[2194575,9276214],[3046242,9501785],[4373584,7523907],[8899249,2023261],[8177946,4756499],[8920541,9010794],[2910098,4445216],[6807801,8509759],[9035179,1073900],[8575170,187291],[4985621,4797328],[3433627,8545504],[7253739,460533],[5065263,7297244],[7642933,346636],[7315855,4818496],[7825622,7751704],[6882083,4474325],[912879,6904049],[8835126,3737563],[4246806,246971],[6094092,4630383],[6491334,9930951],[9128168,4882003],[875476,6056475],[3811217,5248988],[318226,2255637],[6368766,9188282],[6607044,2054176],[340989,575997],[6089297,9579500],[6592737,7674983],[8469385,1914691],[6554326,1084028],[8587757,7303820],[4160880,7628087],[6542590,234919],[1588954,1054310],[4054279,808515],[2593162,8721395],[2699858,7015589],[3276893,9671535],[6332050,4930968],[4156939,6084823],[3189349,9174994],[5066012,5137841],[5414303,7368147],[7094908,3243414],[8428766,3057741],[7841195,5454118],[8104461,1211884],[8409765,9877786],[4024076,5005551],[4737948,3144706],[3244442,4455468],[6784538,9803649],[7195011,9115996],[7575683,1438112],[1116682,2117516],[4271687,8535754],[4547328,7018950],[357223,9800728],[9729781,1588631],[7489171,3697817],[6014775,8239133],[3561851,194608],[9436059,7849490],[3470346,1779834],[2671359,4899677],[2173901,1419617],[8815395,7402469],[5581917,932833],[6718120,3358488],[6931531,2015463],[7314457,5722631],[3964610,62520],[9617225,675589],[7244804,7334469],[405747,3426790],[2693462,954051],[4641159,5245770],[9496122,6620042],[4442588,1551347],[3023074,4639528],[717910,8100539],[9876615,3452759],[1151871,3887635],[22041,8715280],[1216096,9273998],[15768,147881],[237991,1943416],[8947422,341097],[3954621,4985578],[4002655,5303884],[1446488,2012526],[7834344,2671003],[5915454,1940110],[6793015,4206922],[612533,3574317],[7816488,5404491],[6956230,1366174],[7968229,4107824],[9038870,260725],[7341168,2046297],[6311202,916755],[3873679,7013424],[5797385,531242],[129275,7097157],[5820239,3204517],[5372285,8733877],[4476996,9884880],[7976882,8453082],[6059530,7756468],[605535,6340632],[6738220,8759889],[9158450,6122060],[7463235,4966883],[6121588,4560373],[7175073,4088333],[6262192,3754728],[1093642,233643],[4881012,773083],[4819060,1168231],[7467094,2008897],[9213366,3741063],[1919617,5930331],[4702586,2656570],[7570632,1078612],[6244099,3034544],[2914522,366757],[3814668,6801766],[6235173,8980690],[5033985,7617149],[6407607,5546904],[8135485,1137955],[8662738,256450],[5469335,7848088],[3345998,2880463],[7984228,8065088],[7194678,7203915],[1616160,4169730],[6869582,8317505],[9191773,6636502],[1750055,2999362],[4004795,3850616],[344509,5253681],[6225281,8857203],[2989980,4196532],[5918044,604754],[5647493,8619959],[7619383,5176674],[6746578,833313],[9853504,9943442],[3744757,4515485],[416371,1907495],[4455998,2395033],[7469161,7045632],[2407421,5995786],[5229637,9794028],[7532750,9645857],[2499904,1640162],[7688364,5452622],[7061917,9314952],[3484696,3741965],[2537187,4495968],[8876710,2802006],[738655,5487333],[8320771,7324199],[6695170,3293416],[8954096,4026654],[6411954,9973513],[8518457,8658810],[8654558,3714892],[1613766,1439073],[8870848,1693764],[9377286,7938362],[8307860,1565342],[9108544,4721622],[140876,5711392],[2892140,7783104],[6750817,3884653],[6956327,8830237],[4622402,556894],[5217451,4638991],[4312158,2386349],[9352721,2072114],[4602268,7672640],[3884830,3964384],[8071627,7883189],[904945,1808561],[670548,8433329],[5867766,9572714],[6020471,7674788],[9345092,8053058],[827099,2782660],[1598633,2452649],[6252334,9321029],[7417387,7403198],[2263347,5794515],[1906290,7613471],[2025722,1678053],[3251118,9721927],[9504749,3546043],[6487045,7137351],[257179,6350702],[1453493,301241],[3483935,2361730],[1708357,1876982],[1269336,8951783],[8885604,3835912],[7120607,9471199],[4290947,3562229],[4870814,8047896],[1966784,9216357],[7196565,6002779],[2639099,2158841],[314210,521602],[9587761,757532],[7919738,3298408],[9387810,5093105],[2632771,8323257],[2678545,5220340],[5148153,6702455],[3773237,3498257],[1049364,1960532],[51937,3998478],[9426888,6955332],[3130056,6722802],[4179113,3788357],[3897004,7433460],[6195499,1292032],[9925234,1230630],[4481301,4999856],[5743929,3314724],[2472524,2597429],[9324623,7251549],[3797135,628577],[1428721,2378767],[2790044,302042],[7439299,6280463],[8593533,3538811],[3754942,2695593],[5386775,3306012],[4096993,2531185],[58486,215539],[2692987,6895193],[4409267,4946106],[491661,7963257],[8103193,5527062],[6133285,9636831],[1792140,7547332],[3753927,6941847],[8213291,4354441],[2674067,2146350],[2291697,6319004],[4015163,2653205],[2317056,9295112],[161360,6692517],[3065966,3687627],[4259109,5362166],[1824080,5134852],[921800,3129824],[1969505,3672190],[9433439,6613172],[1811014,9101552],[6305482,2275601],[9782488,9241451],[7336161,2010531],[4254586,3075946],[4042144,3569309],[8997945,8988017],[1313507,8072958],[4892695,41214],[747886,4265370],[1717224,7946841],[5190680,1630837],[6530234,5315305],[9734475,4578066],[1795727,7247799],[9182917,4824183],[690064,974167],[2970432,4805434],[2953848,2692994],[664367,8629300],[7582609,5022703],[5282041,1488602],[3720016,8370295],[4691338,9527128],[198432,1729466],[1755006,6329998],[9249630,422440],[3192752,1266595],[8223040,6165500],[7376480,5472002],[9088167,4651564],[8169015,2099190],[9936860,7731814],[9759956,4157843],[7128592,9250078],[5174069,8905602],[9761933,612085],[6551482,510253],[3339656,4929793],[7269114,8246069],[3735370,3019708],[6033866,436852],[5850132,8610019],[7556588,1057830],[1248084,8104636],[7183939,1032036],[8288013,4042657],[4817081,5638489],[9373492,3866555],[886099,2141367],[6212182,8923345],[4149655,587361],[6803766,7948501],[6752919,4923633],[3935229,7226998],[5640664,8129679],[2754660,2168042],[4444604,1536369],[1050647,9858010],[4487771,8476267],[8519224,8702299],[4132126,9514298],[1954774,5313617],[8489776,8914436],[2198381,6983685],[3350254,1891880],[8729817,5118740],[8760636,5213582],[8819535,5944262],[7473395,4229724],[4516367,4805425],[3810117,2023178],[2797358,5194487],[1024203,171199],[1150736,5706714],[5457618,5428433],[3576232,9348826],[8727793,3287562],[3950208,7903065],[7123167,2145827],[3495112,2618953],[3526200,4654601],[5822085,8261871],[1233164,2265194],[1077464,3712163],[919992,2099448],[9762922,2102051],[5760985,4963885],[8687680,3970918],[8850930,7807345],[7672852,6275948],[2913967,4899225],[2697682,7211595],[6681719,7029609],[6927406,1435620],[8728543,6009486],[8652451,3750358],[916853,5807],[3066942,1194956],[9524140,6339954],[5661277,7744208],[6309672,7157855],[406074,5338808],[6276199,3205418],[467030,513028],[2917573,6356182],[9562797,572951],[8539449,3857883],[1024643,1782251],[2719918,8958859],[6922311,3642200],[6095809,2399967],[8514779,2492867],[2292359,4934140],[2450895,7810774],[3439695,2003191],[6695482,9071932],[2304555,9999492],[6642560,4091257],[6395657,2085401],[3953427,5618435],[4922656,7404513],[5094803,1000870],[5882008,3090070],[2026805,4895244],[4243349,7461708],[105644,8750626],[4806227,5919158],[8902006,9915761],[306620,8563614],[6325240,437548],[2360785,1104364],[1764179,1081268],[1662586,1264337],[3564832,4076416],[3230878,6047009],[8160511,251108],[9062600,7987297],[7425406,6010682],[9936585,1572971],[8348483,7671479],[6200735,1163636],[9812348,6828899],[693379,1223283],[77071,1573544],[4295425,3806428],[7872902,2323861],[1030502,7503593],[5760358,2436834],[2714246,2033670],[3738024,2657056],[4593375,1515342],[9853198,5424816],[9137074,8914612],[9087964,8052675],[757828,7994213],[89734,6782151],[1226441,6022955],[959701,8038124],[6296768,7096046],[1391011,4822959],[1447589,1723656],[5374721,3023648],[5975996,8715330],[6048295,5883344],[7163170,5335917],[7099203,1934559],[9519614,2987337],[1798807,6116183],[1049244,8651356],[424555,542724],[7130393,1731790],[5837703,1551594],[3407884,7676767],[2161994,4112255],[9383204,7184706],[6368740,9426627],[637475,6143698],[8420471,3897564],[1294325,236163],[1270932,8599657],[4072733,3830605],[4804055,4124648],[5893203,5809952],[5327779,8265684],[9600324,7381421],[2309197,167551],[3467524,5116193],[6769343,6264307],[5381629,1209012],[9640788,3927604],[3193860,9816686],[1920854,3702920],[9352943,3476279],[2557769,1516239],[6371081,7590127],[844215,8331895],[18673,3497407],[9164315,4560396],[3790843,5940774],[6693719,4272425],[7254266,478279],[6762728,1681232],[6171840,1293395],[5910862,164671],[7195284,4782418],[1197473,1437759],[9329943,3315061],[6239560,8179345],[931280,1025553],[2118545,413460],[6213508,7724370],[289669,1026332],[5296501,8149507],[5658351,855643],[6003867,8612672],[1200387,5422448],[6581249,205767],[4527554,4945558],[7502448,8760716],[5782554,8979551],[2627788,7337516],[9048049,9743754],[2686748,625714],[6997158,3666519],[8431625,2619722],[8434899,1259349],[9546364,8530690],[271445,78191],[2263779,8174056],[9336212,9121724],[9301095,1240850],[6240715,9786184],[2191254,6680605],[1661537,6335920],[9373388,9541658],[9093499,7240366],[7038248,4689109],[9991112,6593986],[4784965,9527496],[7056318,6588096],[3315325,8719900],[2419329,1836610],[5770245,9120540],[7883142,9070406],[6385279,8491009],[6604484,8641281],[1672187,6110487],[3499696,9675350],[7397273,9137119],[4559483,6552276],[7573527,2181227],[2942499,9430761],[3283415,8628038],[910470,6806539],[2772051,6952759],[6547117,9327606],[2359123,1621223],[1054499,8866281],[3965313,5445656],[4746777,9031140],[4293503,8820171],[2515294,4593821],[7769577,2901419],[8423204,6035371],[642784,4737856],[7500113,3710607],[9498127,2930442],[9427057,5241643],[9431093,9240882],[2335439,7198102],[6170153,7173490],[8162279,594909],[7303743,1584964],[462023,6063008],[2862487,6510683],[2056589,8946339],[8399879,2476937],[7343787,5473830],[8841611,7234878],[3749185,6388681],[1662196,4228992],[3173023,4167858],[8322383,8004102],[5582643,125557],[9711805,5945187],[5883482,2580689],[489605,4234881],[2196830,8021404],[6964361,5179072],[3901080,9700869],[5410823,4992217],[8823299,8033335],[9374673,1973137],[3147767,1997002],[7585645,778718],[7143906,8169211],[5535726,1485836],[415485,1685699],[3535545,9735381],[8125607,6242607],[4305477,9307537],[1409297,9097405],[4704841,2989264],[9897560,3687568],[5532270,6363807],[8881249,1169324],[6966891,2486869],[1485559,3234768],[1420967,8799693],[6244040,3070754],[8393324,9947647],[8365318,8261318],[1812802,1167648],[7344266,3990301],[9355661,5115730],[1370438,1676498],[423809,6451068],[5535008,7340976],[87566,5749335],[1278406,4588880],[3412011,9009800],[752664,6322919],[393521,3787348],[5021353,3306200],[2573080,8520234],[6683675,4958413],[957725,2994216],[3693623,8987724],[4566640,2059380],[6161941,4908869],[7564892,2912055],[3891934,3235745],[4841530,2883487],[2652471,2417003],[1689940,6052587],[289662,5298212],[8845389,7163730],[991492,1802189],[3423135,3954873],[8207807,3192485],[7238882,4929379],[1041018,5176350],[5084120,8907462],[7912459,2954917],[6267262,5915393],[6700906,8336254],[379524,4881782],[5063221,2959345],[4262084,1846316],[296187,88420],[9862791,4123390],[8672150,4996705],[9839579,5922524],[6031883,2919700],[3037308,887985],[4916506,8308538],[620784,334940],[2722710,5891530],[6376030,5703393],[3274271,7176570],[3320922,4183955],[2311666,6623131],[8458447,8250633],[3650291,1216854],[9913559,162903],[484071,7217160],[6751935,3345572],[1574338,8840697],[4572778,1367805],[7897926,7022650],[1264916,5200754],[4623681,6531850],[3070944,1037475],[7975478,3530344],[1263618,6630835],[2882035,9764828],[8334613,8167576],[9144180,3624453],[3689466,9280061],[8736803,6828663],[3995378,7044870],[9294636,6748666],[9044328,3941799],[8224899,1754107],[8732132,6037810],[1532078,2197821],[2974826,9254098],[1270025,4974424],[8008644,564219],[2631275,5712817],[9457116,7602836],[134846,2499469],[8162432,4522201],[3523252,3047027],[1415672,164185],[5580275,3527447],[2157803,5727025],[426423,1200348],[4498416,2885123],[2753552,9244357],[4951276,4469381],[923384,9637952],[9640153,7814091],[9384596,2966689],[2348287,5171796],[3228423,3948065],[7925121,4996376],[3291550,76083],[4782516,678125],[3509999,553696],[5495738,8461981],[7120298,8957148],[3376178,4547570],[714610,1601099],[6045525,1458489],[8568251,5419785],[5906521,388033],[1372279,4595009],[8858173,4560704],[1331678,8480086],[4317068,4524023],[8608233,1872162],[5930103,9759622],[8265125,5795065],[1911043,3316861],[9325582,8840700],[4140997,9302245],[6479328,2810111],[7592083,6472634],[8233360,6437441],[4718971,8920028],[7155187,5401034],[2920537,7434296],[5681981,4321417],[2004026,3588725],[2182437,5515938],[4869116,245358],[1258441,7485553],[7498683,4146365],[110736,7668165],[6190818,3924300],[6451412,9967603],[7998527,9777329],[1487999,7485687],[6805491,3923744],[3418687,6562233],[8990516,9594052],[310678,1230919],[2644789,3309040],[7408406,9107190],[9446842,783175],[8414041,8924034],[992282,6306586],[8049041,4369635],[1252040,4434449],[7005488,439940],[5444493,6592926],[4831722,4104660],[9614104,4211550],[9231267,4120630],[233368,5925401],[2840367,9675052],[1711944,2428060],[2205958,5540945],[921648,4483628],[3188355,495123],[6799696,2143898],[1594115,5475526],[4475984,1913057],[8329670,5221817],[5572507,4129839],[2486619,6401955],[8739800,8883062],[3634922,6115236],[2723918,6059148],[6404565,2375425],[9555120,342961],[2623429,843934],[3625012,1236230],[7158047,3571609],[7629335,3917448],[7819374,9748327],[1028090,7239067],[236128,2202992],[1843961,9051863],[8882781,3771715],[3045375,1683132],[6234702,2485033],[6966418,5417624],[6836398,5022031],[1381635,4669373],[350443,4474964],[3799151,2137968],[6496085,2018142],[4671505,3331902],[5433777,3526199],[7697304,3238741],[8282191,8136784],[9152987,8188092],[1206320,1862457],[1283633,6934716],[601154,2343156],[9544912,8373724],[5031507,7647747],[275220,4945025],[8957095,8611644],[3487129,5976819],[1016982,4302472],[3738563,6884406],[6468881,8298947],[825648,686344],[7257883,6032533],[3748770,144492],[8841776,4390669],[5566015,3946217],[1958329,5972854],[3317026,1392850],[6642571,2318818],[7088760,2434197],[9855712,554413],[9320300,6689430],[1170012,9788305],[5347827,1972347],[3894356,8547359],[5710972,9842704],[8744256,6819676],[4491678,6221158],[8836727,9076224],[5204960,655667],[3564821,1289026],[8434114,3858671],[3760601,2013652],[1178500,9881836],[8749335,1757403],[9425667,5424153],[8286187,6689033],[6934901,7530563],[4121638,8655690],[5384031,1589094],[4085340,7397621],[5873725,957338],[3952525,261460],[6073281,9655023],[6392194,142017],[2629132,8325807],[8692389,5814701],[9444687,2697159],[2337223,86070],[7692011,2615682],[5367317,5412709],[1282561,9432147],[5368065,5658467],[1015758,1989048],[1766001,1329904],[5296149,4464974],[2608902,5314771],[4139703,6133757],[3154085,8009505],[9483139,5527089],[5255391,4209033],[1220679,1127978],[925407,7391830],[9483359,9089438],[6160880,5197913],[1620996,2374395],[55566,8483137],[7086419,3599343],[2218222,5606161],[4847278,4487841],[5062743,2877218],[7862087,3654372],[6517481,5579792],[1862750,6740142],[8355792,7787297],[4627030,8214382],[7716934,8192296],[9564372,8661333],[8522335,4665960],[2735972,9370749],[6271006,2394782],[2691338,6026269],[6404349,5577502],[2929252,7396920],[2896589,892226],[344985,3488750],[8114340,2173638],[703561,4598090],[9713123,9170613],[9053439,4002590],[4333239,9697556],[5738622,9729880],[6649263,3266953],[2589465,2282291],[5834253,6397106],[8482223,7990020],[3357162,3097166],[3491494,8595478],[5153604,764156],[4123299,7513238],[9178882,7031630],[9415027,3885655],[2246185,7030828],[8274340,3005357],[3876470,2863612],[7629773,4142700],[4656316,9017698],[6995115,302165],[4710380,9952739],[5225241,5196299],[271175,6692304],[7572879,4487503],[8605498,1998046],[7337929,1503244],[1376927,9764828],[2679490,3911069],[6740024,2140849],[7288177,6386576],[5968298,1142175],[3391416,899272],[9547404,8640043],[8847905,45637],[542831,7092540],[3436930,2323855],[244431,3019891],[4239548,8226462],[2047377,9259954],[6828903,8071929],[3471429,2179195],[5629006,3817437],[5979234,4968125],[9498427,6194276],[5190878,6910535],[6433598,9493591],[3080813,6291327],[542416,8292244],[4031904,7064550],[3022368,6514156],[4917141,2229913],[9251626,3963728],[460177,185666],[5370721,2039095],[6264218,1930283],[570445,1411333],[8912861,2355267],[898227,7981991],[5566001,819575],[3098219,7047395],[5238360,8056388],[4329442,5001397],[2727728,1578749],[4812529,8307116],[9993708,7926660],[9191522,2531546],[7822889,7854887],[4738041,1726542],[6277462,4580428],[9199746,9338565],[9065229,1933710],[9454432,8598870],[8458010,9682104],[9102795,5878244],[8733152,2291635],[9872894,9052812],[1476396,262162],[9473580,440331],[5788346,7616705],[8671314,6115826],[2452774,4375321],[7258059,6521407],[6333602,8101764],[7958168,3349469],[6808898,1783992],[3836233,188680],[83299,7889948],[6503097,5147539],[4480379,2440890],[5829721,9794322],[3325270,6225912],[759289,4325301],[5990408,6776944],[2246389,4158507],[9129722,9686011],[2764366,3331407],[6435844,205831],[8560695,1567135],[9646721,7298187],[5374225,9631572],[988216,6721756],[1317304,9224141],[7650170,5008482],[3885827,9239684],[9954662,5922387],[3655156,2102979],[525124,9682634],[1318360,9374588],[4106547,600054],[4639719,4435606],[6892844,5296354],[3747462,6833221],[3575295,6547143],[6912809,4445571],[1809572,3553421],[2898486,8979472],[5028933,8962097],[5599314,8745333],[6224518,486636],[1489827,4413576],[3037846,9256213],[3212175,4622261],[4055475,4846757],[1316329,6123888],[8182642,8348693],[1369262,2988239],[2681125,1837940],[4751758,6359163],[6270590,8519070],[6307709,587779],[3971705,4974809],[5649890,6096594],[523739,3282208],[1299569,3876510],[5548229,8580761],[752297,8726133],[8020575,2795685],[1641214,8417644],[7935720,1298233],[6492897,3532055],[5593762,1139969],[464347,7325341],[4015346,3531628],[3846671,1751421],[2974880,3666807],[4089938,5867890],[2491613,868134],[1177356,8366816],[4877312,9467531],[8420036,5070460],[3353374,7980032],[4803940,8333197],[3490652,8058005],[6707160,9395231],[7764486,3898530],[9294600,7101670],[2059568,6592048],[1211196,3921251],[4587184,1378414],[131148,4236648],[9871994,6184509],[2360277,9899684],[170106,1646342],[5283174,4873018],[6032646,8192604],[1622576,9621466],[6392065,4858531],[8160925,4438648],[8785850,6506],[8586243,4663393],[5035176,9918084],[9406413,3831278],[3609935,7019736],[9902727,3032745],[4224825,3318276],[3508334,4786164],[1637823,679861],[1589779,308187],[6359701,7675250],[4428343,5461766],[4466977,9654496],[3035246,2302096],[9929087,7376541],[9196147,8443788],[715805,8683998],[6355815,4208496],[3418986,7442758],[3127321,4494035],[3037328,4028945],[1073455,398940],[6377785,7343492],[2452643,9229902],[575089,7733057],[2819905,9611711],[7497500,8355190],[9748973,4230275],[8027601,8718615],[7758535,4473512],[7109694,7060797],[5695192,6726751],[1751363,2037308],[9764759,2439746],[4317108,4842692],[6635472,6729739],[9053877,6236901],[1521003,8053116],[2703826,1621315],[6656359,6827017],[1946812,4859478],[9691332,2006105],[6462412,6162241],[1458621,1204548],[4093312,3166986],[3788713,2426177],[7679086,6878121],[8504669,3503685],[8844041,1046327],[3752922,5148007],[9114613,2807481],[2030011,8661544],[4311849,3054814],[3568068,9625203],[483420,9108232],[2844348,706280],[1224660,6392326],[6353994,604976],[3837563,1251007],[7367622,4268344],[5701624,3369219],[4545673,8418181],[9420344,7463727],[2836186,2267214],[9675710,764282],[205796,67670],[1745019,5704167],[2861082,6911480],[3894738,4214210],[2338635,2714115],[3391472,2425738],[9354470,8203573],[4366010,1860964],[6975927,5457778],[3042800,5842918],[8750714,9823095],[134463,1620305],[9004387,2040923],[9211429,3886311],[5718236,7055044],[5516855,5988482],[3034878,5792904],[4380398,45832],[554826,6900877],[9741238,4177362],[2630050,9265553],[7023813,7068467],[65596,5505775],[3394792,7378318],[6578498,6870247],[3824813,5160100],[9301634,3997087],[8807683,9897740],[7653268,3132083],[738540,8267964],[2504065,7653458],[7051860,1626365],[8826865,5826498],[4450242,557668],[8568695,1284532],[8976993,7786842],[3113375,9483481],[2475093,4777203],[7671014,3436095],[7292756,4193256],[3127026,5053576],[7974129,3416047],[5427781,3212039],[5892814,4251885],[3866553,9356591],[1295673,9184251],[8077268,392159],[6452494,8260539],[1773993,504428],[6110060,5519283],[4955981,2940929],[970293,8172454],[4033034,807531],[1985174,5447919],[1354149,9391069],[38990,5313471],[8195386,3897808],[7266622,7743257],[4267974,6462766],[8643482,1693869],[5342448,1910017],[1387284,2294071],[8159733,3946777],[1868809,4115038],[4757724,8894147],[4529411,7621090],[4826781,9079553],[2912968,3917889],[1673054,6501984],[7781500,803136],[4018799,1018523],[4382673,5405221],[6313396,4784473],[223987,9158084],[8987209,8879816],[8592426,6980998],[7583745,9336477],[4844679,1781537],[759942,8601237]]

#print(s.maxWidthOfVerticalArea(points))

#Shows which functions take the longest to process. You can split the data that the functions are evaluating into two pieces and apply concurrency to make it faster.
cProfile.run('s.maxWidthOfVerticalArea(points)')