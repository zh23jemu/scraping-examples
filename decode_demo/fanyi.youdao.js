const crypto = require('crypto');
const {Buffer} = require('buffer');

d = "fanyideskweb"
u = "webfanyi"

// e是从另一个请求获得, 但好像是个固定值
// https://dict.youdao.com/webtranslate/key?keyid=webfanyi-key-getter&sign=a0f7514bec04b363bcdbe921d5ed22d8&client=fanyideskweb&product=webfanyi&appVersion=1.0.0&vendor=web&pointParam=client,mysticTime,product&mysticTime=1738990548447&keyfrom=fanyi.web&mid=1&screen=1&model=1&network=wifi&abtest=0&yduuid=abcdefg
e = "Vy4EQ1uwPkUoqvcP1nIu6WiAjxFeA3Y9"

function S(e, t) {
    return _(`client=${d}&mysticTime=${e}&product=${u}&key=${t}`)
}

function _(e) {
    return md5(e.toString());
}

function md5(e) {
    return crypto.createHash('md5').update(e).digest('hex');
}

function getParams() {
    params = {}

    a = (new Date).getTime()
    params.mysticTime = a
    params.sign = S(a, e)

    return params
}

console.log(getParams())

o = "Z21kD9ZK1ke6ugku2ccWu4n6eLnvoDT0YgGi0y3g-v0B9sYqg8L9D6UERNozYOHqoQzNRUCyI06c5-fXHEG36QL8otVzFy9yH2bX0qRjbBJpLVuhShQ1gW2_ibzi_ZCov8kB9YPV40qhWUW6UZjEgztaeTrgclA9HMQRe8jH_dIiX429nANGhMRtXGkwVsVx8WwuH1xZpEOtb-sNI_c962nsPfhvyt6w7rAd4IVPv2ue4_1DykKKPi4muiSsWWwPBKI7hmO9MrVBnj2RAwk2A0OgL_FLa_vgLMutRioYbU0LG8TvuqiJb9yMHrNNg-ibYzWHokVYUdZ7pfKY8ory-kwXa1RI-Vl_9Z1-zQfxgfTAl8kkMztxGicK2akHcHI2xOkBKP8ZUa4unNKRueBrOWM8vbQxLTZoqpBF3y7MdwmrA3G2JkWmSpmRSWBU9jC8HUeObnX5vC7RiJ1tGOKRg2ltxCCzrGbJD-49M7CLe-B6Q4ndpsqGz6276HOiwp8unL4rUQf-vbp_8CrE6aTENWariAAoupAsNXP4fgly6v0zdoO8xWFkthrrRjScI8RyS21_Z4nyngLjKfadc11JGGtNb65BzWiK8qFQTt1Zl3hYnQfKFzgrUYe0CJmNg9umBjKaEa6yt8XVNHJPuJffFAyTgwgU0m06mfU8kx_Ka7SG4emtM4PryQEtQlP3R0gTGun495UORo9KZk19utHnrfrSLsqeX-JglRDs6_75Yv4cnHne06oPRYhFjh_Q35Kps-BVhaXfKAeGLc2WnS0Ij3Tq24sU2taVojTdAQSB4tpPFA3vcHdu7p2CLCRkZc25ArFM6oTsjffagAK8rqRs-Y34p_tohegFf5O1wv3LDFUqlRi3tgWmjxyRz0y9JyYefjBi-5_tWhgLmC-wc-AzoOyYNZ5J7ke9Cphlp3FLDBsAgW24fOhsBdV7DS3kpE6kS4AZy-z3Tv3fD_1bso5w1MZYdRHSUxr2SGjvkyKSd_RXox_tZGXgkRhLJllE626cqITks5jNPwF_0t90P-wkxv3cdL_h2G4OgxXTTr16VLIrLp5M6HC5GySz2DgNz56t0twoXmC1OxGLauSh0y2TWPGyB0Rx5N1rH0B4Q3sdlxYtuu9RO4I407dlAgdFpbxfl0WK3XBj1erfc3w5oKY99ERCjCe7QdJZ-K8OAK0vjQWlGSrLoAxwjYAcSkVbBaDEmKaOM6eGzDRdpbHjn-s8rA=="

// 这两个可能也是固定值
decodeKey = "ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl"
decodeIv = "ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4"

function T(e) {
    return crypto.createHash("md5").update(e).digest()
}

function decode(e) {
    if (!e)
        return null;
    const o = Buffer.alloc(16, T(decodeKey))
        , n = Buffer.alloc(16, T(decodeIv))
        , r = crypto.createDecipheriv("aes-128-cbc", o, n);
    let s = r.update(e, "base64", "utf-8");
    return s += r.final("utf-8"),
        s
}

console.log(decode(o))






