eT = function (eo) {
    function eu(eo, eu) {
        return eo << eu | eo >>> 32 - eu
    }

    function ep(eo, eu) {
        var ep, em, ey, e_, ew;
        return ey = 2147483648 & eo, e_ = 2147483648 & eu, ep = 1073741824 & eo, em = 1073741824 & eu, ew = (1073741823 & eo) + (1073741823 & eu), ep & em ? 2147483648 ^ ew ^ ey ^ e_ : ep | em ? 1073741824 & ew ? 3221225472 ^ ew ^ ey ^ e_ : 1073741824 ^ ew ^ ey ^ e_ : ew ^ ey ^ e_
    }

    function em(eo, eu, ep) {
        return eo & eu | ~eo & ep
    }

    function ey(eo, eu, ep) {
        return eo & ep | eu & ~ep
    }

    function e_(eo, eu, ep) {
        return eo ^ eu ^ ep
    }

    function ew(eo, eu, ep) {
        return eu ^ (eo | ~ep)
    }

    function eS(eo, ey, e_, ew, eS, eT, eE) {
        return eo = ep(eo, ep(ep(em(ey, e_, ew), eS), eE)), ep(eu(eo, eT), ey)
    }

    function eT(eo, em, e_, ew, eS, eT, eE) {
        return eo = ep(eo, ep(ep(ey(em, e_, ew), eS), eE)), ep(eu(eo, eT), em)
    }

    function eE(eo, em, ey, ew, eS, eT, eE) {
        return eo = ep(eo, ep(ep(e_(em, ey, ew), eS), eE)), ep(eu(eo, eT), em)
    }

    function eM(eo, em, ey, e_, eS, eT, eE) {
        return eo = ep(eo, ep(ep(ew(em, ey, e_), eS), eE)), ep(eu(eo, eT), em)
    }

    function eC(eo) {
        var eu, ep = "", em = "";
        for (eu = 0; 3 >= eu; eu++) ep += (em = "0" + (eo >>> 8 * eu & 255).toString(16)).substr(em.length - 2, 2);
        return ep
    }

    var eL, eA, eD, eP, eI, eO, eN, eR, eF, eY = [], eB = 7, eH = 12, eW = 17, ez = 22, eU = 5, eV = 9, eQ = 14,
        eK = 20, eZ = 4, eG = 11, eJ = 16, eX = 23, e$ = 6, e0 = 10, e2 = 15, e5 = 21;
    for (eY = function (eo) {
        for (var eu, ep = eo.length, em = ep + 8, ey = (em - em % 64) / 64, e_ = 16 * (ey + 1), ew = Array(e_ - 1), eS = 0, eT = 0; ep > eT;) eu = (eT - eT % 4) / 4, eS = eT % 4 * 8, ew[eu] = ew[eu] | eo.charCodeAt(eT) << eS, eT++;
        return eu = (eT - eT % 4) / 4, eS = eT % 4 * 8, ew[eu] = ew[eu] | 128 << eS, ew[e_ - 2] = ep << 3, ew[e_ - 1] = ep >>> 29, ew
    }(eo = function (eo) {
        eo = eo.replace(/\r\n/g, "\n");
        for (var eu = "", ep = 0; ep < eo.length; ep++) {
            var em = eo.charCodeAt(ep);
            128 > em ? eu += String.fromCharCode(em) : em > 127 && 2048 > em ? eu += String.fromCharCode(em >> 6 | 192) + String.fromCharCode(63 & em | 128) : eu += String.fromCharCode(em >> 12 | 224) + String.fromCharCode(em >> 6 & 63 | 128) + String.fromCharCode(63 & em | 128)
        }
        return eu
    }(eo)), eO = 1732584193, eN = 4023233417, eR = 2562383102, eF = 271733878, eL = 0; eL < eY.length; eL += 16) eA = eO, eD = eN, eP = eR, eI = eF, eO = eS(eO, eN, eR, eF, eY[eL + 0], eB, 3614090360), eF = eS(eF, eO, eN, eR, eY[eL + 1], eH, 3905402710), eR = eS(eR, eF, eO, eN, eY[eL + 2], eW, 606105819), eN = eS(eN, eR, eF, eO, eY[eL + 3], ez, 3250441966), eO = eS(eO, eN, eR, eF, eY[eL + 4], eB, 4118548399), eF = eS(eF, eO, eN, eR, eY[eL + 5], eH, 1200080426), eR = eS(eR, eF, eO, eN, eY[eL + 6], eW, 2821735955), eN = eS(eN, eR, eF, eO, eY[eL + 7], ez, 4249261313), eO = eS(eO, eN, eR, eF, eY[eL + 8], eB, 1770035416), eF = eS(eF, eO, eN, eR, eY[eL + 9], eH, 2336552879), eR = eS(eR, eF, eO, eN, eY[eL + 10], eW, 4294925233), eN = eS(eN, eR, eF, eO, eY[eL + 11], ez, 2304563134), eO = eS(eO, eN, eR, eF, eY[eL + 12], eB, 1804603682), eF = eS(eF, eO, eN, eR, eY[eL + 13], eH, 4254626195), eR = eS(eR, eF, eO, eN, eY[eL + 14], eW, 2792965006), eN = eS(eN, eR, eF, eO, eY[eL + 15], ez, 1236535329), eO = eT(eO, eN, eR, eF, eY[eL + 1], eU, 4129170786), eF = eT(eF, eO, eN, eR, eY[eL + 6], eV, 3225465664), eR = eT(eR, eF, eO, eN, eY[eL + 11], eQ, 643717713), eN = eT(eN, eR, eF, eO, eY[eL + 0], eK, 3921069994), eO = eT(eO, eN, eR, eF, eY[eL + 5], eU, 3593408605), eF = eT(eF, eO, eN, eR, eY[eL + 10], eV, 38016083), eR = eT(eR, eF, eO, eN, eY[eL + 15], eQ, 3634488961), eN = eT(eN, eR, eF, eO, eY[eL + 4], eK, 3889429448), eO = eT(eO, eN, eR, eF, eY[eL + 9], eU, 568446438), eF = eT(eF, eO, eN, eR, eY[eL + 14], eV, 3275163606), eR = eT(eR, eF, eO, eN, eY[eL + 3], eQ, 4107603335), eN = eT(eN, eR, eF, eO, eY[eL + 8], eK, 1163531501), eO = eT(eO, eN, eR, eF, eY[eL + 13], eU, 2850285829), eF = eT(eF, eO, eN, eR, eY[eL + 2], eV, 4243563512), eR = eT(eR, eF, eO, eN, eY[eL + 7], eQ, 1735328473), eN = eT(eN, eR, eF, eO, eY[eL + 12], eK, 2368359562), eO = eE(eO, eN, eR, eF, eY[eL + 5], eZ, 4294588738), eF = eE(eF, eO, eN, eR, eY[eL + 8], eG, 2272392833), eR = eE(eR, eF, eO, eN, eY[eL + 11], eJ, 1839030562), eN = eE(eN, eR, eF, eO, eY[eL + 14], eX, 4259657740), eO = eE(eO, eN, eR, eF, eY[eL + 1], eZ, 2763975236), eF = eE(eF, eO, eN, eR, eY[eL + 4], eG, 1272893353), eR = eE(eR, eF, eO, eN, eY[eL + 7], eJ, 4139469664), eN = eE(eN, eR, eF, eO, eY[eL + 10], eX, 3200236656), eO = eE(eO, eN, eR, eF, eY[eL + 13], eZ, 681279174), eF = eE(eF, eO, eN, eR, eY[eL + 0], eG, 3936430074), eR = eE(eR, eF, eO, eN, eY[eL + 3], eJ, 3572445317), eN = eE(eN, eR, eF, eO, eY[eL + 6], eX, 76029189), eO = eE(eO, eN, eR, eF, eY[eL + 9], eZ, 3654602809), eF = eE(eF, eO, eN, eR, eY[eL + 12], eG, 3873151461), eR = eE(eR, eF, eO, eN, eY[eL + 15], eJ, 530742520), eN = eE(eN, eR, eF, eO, eY[eL + 2], eX, 3299628645), eO = eM(eO, eN, eR, eF, eY[eL + 0], e$, 4096336452), eF = eM(eF, eO, eN, eR, eY[eL + 7], e0, 1126891415), eR = eM(eR, eF, eO, eN, eY[eL + 14], e2, 2878612391), eN = eM(eN, eR, eF, eO, eY[eL + 5], e5, 4237533241), eO = eM(eO, eN, eR, eF, eY[eL + 12], e$, 1700485571), eF = eM(eF, eO, eN, eR, eY[eL + 3], e0, 2399980690), eR = eM(eR, eF, eO, eN, eY[eL + 10], e2, 4293915773), eN = eM(eN, eR, eF, eO, eY[eL + 1], e5, 2240044497), eO = eM(eO, eN, eR, eF, eY[eL + 8], e$, 1873313359), eF = eM(eF, eO, eN, eR, eY[eL + 15], e0, 4264355552), eR = eM(eR, eF, eO, eN, eY[eL + 6], e2, 2734768916), eN = eM(eN, eR, eF, eO, eY[eL + 13], e5, 1309151649), eO = eM(eO, eN, eR, eF, eY[eL + 4], e$, 4149444226), eF = eM(eF, eO, eN, eR, eY[eL + 11], e0, 3174756917), eR = eM(eR, eF, eO, eN, eY[eL + 2], e2, 718787259), eN = eM(eN, eR, eF, eO, eY[eL + 9], e5, 3951481745), eO = ep(eO, eA), eN = ep(eN, eD), eR = ep(eR, eP), eF = ep(eF, eI);
    return (eC(eO) + eC(eN) + eC(eR) + eC(eF)).toLowerCase()
}

data = '{"appId":"34385","params":"{\\"device\\":\\"HMA-AL00\\",\\"isBeta\\":\\"false\\",\\"grayHair\\":\\"false\\",\\"from\\":\\"nt_history\\",\\"brand\\":\\"HUAWEI\\",\\"info\\":\\"wifi\\",\\"index\\":\\"4\\",\\"rainbow\\":\\"\\",\\"schemaType\\":\\"auction\\",\\"elderHome\\":\\"false\\",\\"isEnterSrpSearch\\":\\"true\\",\\"newSearch\\":\\"false\\",\\"network\\":\\"wifi\\",\\"subtype\\":\\"\\",\\"hasPreposeFilter\\":\\"false\\",\\"prepositionVersion\\":\\"v2\\",\\"client_os\\":\\"Android\\",\\"gpsEnabled\\":\\"false\\",\\"searchDoorFrom\\":\\"srp\\",\\"debug_rerankNewOpenCard\\":\\"false\\",\\"homePageVersion\\":\\"v7\\",\\"searchElderHomeOpen\\":\\"false\\",\\"search_action\\":\\"initiative\\",\\"sugg\\":\\"_4_1\\",\\"sversion\\":\\"13.6\\",\\"style\\":\\"list\\",\\"ttid\\":\\"600000@taobao_pc_10.7.0\\",\\"needTabs\\":\\"true\\",\\"areaCode\\":\\"CN\\",\\"vm\\":\\"nw\\",\\"countryNum\\":\\"156\\",\\"m\\":\\"pc\\",\\"page\\":1,\\"n\\":48,\\"q\\":\\"%E6%97%A0%E7%BA%BF%E7%BD%91%E5%8D%A1\\",\\"qSource\\":\\"url\\",\\"pageSource\\":\\"a21bo.jianhua/a.201856.d13\\",\\"tab\\":\\"all\\",\\"pageSize\\":48,\\"totalPage\\":100,\\"totalResults\\":4800,\\"sourceS\\":\\"0\\",\\"sort\\":\\"_coefp\\",\\"bcoffset\\":\\"\\",\\"ntoffset\\":\\"\\",\\"filterTag\\":\\"\\",\\"service\\":\\"\\",\\"prop\\":\\"\\",\\"loc\\":\\"\\",\\"start_price\\":null,\\"end_price\\":null,\\"startPrice\\":null,\\"endPrice\\":null,\\"itemIds\\":null,\\"p4pIds\\":null,\\"p4pS\\":null,\\"categoryp\\":\\"\\",\\"ha3Kvpairs\\":null,\\"myCNA\\":\\"PbabH1o0HjsCAXBRDezmK1tA\\"}"}'

function getParams(data) {
    params = {}
    params['t'] = (new Date).getTime()

    // 第一个值是cookie中_m_h5_tk的前半部分, 会随着时间变化
    params['sign'] = eT("84e0a209e1907d03d9fc49b2fed58df4" + "&" + params['t'] + "&" + "12574478" + "&" + data)

    return params

}

console.log(getParams(data))