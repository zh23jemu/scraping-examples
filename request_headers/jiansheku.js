const CryptoJS = require('crypto-js');

f = (new Date).getTime()

// data = {
//     'eid': '',
//     'achievementQueryType': 'and',
//     'achievementQueryDto': [],
//     'personnelQueryDto': {
//         'queryType': 'and',
//     },
//     'aptitudeQueryDto': {
//         'queryType': 'and',
//         'nameStr': '',
//         'aptitudeQueryType': 'and',
//         'businessScopeQueryType': 'or',
//         'filePlaceType': '1',
//         'aptitudeDtoList': [
//             {
//                 'codeStr': '',
//                 'queryType': 'and',
//                 'aptitudeType': 'qualification',
//             },
//         ],
//         'aptitudeSource': 'new',
//     },
//     'page': {
//         'page': 1,
//         'limit': 20,
//         'field': '',
//         'order': '',
//     },
// }

gd = function (e) {
    var t = new Array
        , n = 0;
    for (var i in e)
        t[n] = i,
            n++;
    return t.sort()
}

_d = function e(t) {
    var n;
    if (Array.isArray(t)) {
        for (var r in n = new Array,
            t) {
            var o = t[r];
            for (var i in o)
                null == o[i] ? delete t[r][i] : Array.isArray(t[r][i]) && e(t[r][i])
        }
        return n = t,
            JSON.stringify(n).replace(/^(\s|")+|(\s|")+$/g, "")
    }
    return n = t && t.constructor === Object ? JSON.stringify(t) : t
}

md = function (e) {
    var t = gd(e)
        , n = "";
    for (var i in t) {
        var r = _d(e[t[i]]);
        null != r && "" != r.toString() && (n += t[i] + "=" + r + "&")
    }
    return n
}

pd = function (e, t, time) {
    var n = t + e + time;
    return n = CryptoJS.MD5(n).toString();
}

function getSign(data, f) {
    sign = (param = data,
        time = f,
        t = md(param),
        pd("ghaepVf6IhcHmgnk4NCTXLApxQkBcvh1",
            pd("mwMlWOdyM7OXbjzQPulT1ndRZIAjShDB",
                pd("ZuSj0gwgsKXP4fTEz55oAG2q2p1SVGKK", t, time), time), time))

    return sign
}

console.log(getSign(data, f));
