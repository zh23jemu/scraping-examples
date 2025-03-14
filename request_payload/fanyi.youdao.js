const crypto = require('crypto');
const {Buffer} = require('buffer');

d = "fanyideskweb"
u = "webfanyi"

function S(e, t) {
    return _(`client=${d}&mysticTime=${e}&product=${u}&key=${t}`)
}

function _(e) {
    return md5(e.toString());
}

function md5(e) {
    return crypto.createHash('md5').update(e).digest('hex');
}

function getParams(key) {
    params = {}

    a = (new Date).getTime()
    params.mysticTime = a
    params.sign = S(a, key)

    return params
}

console.log(getParams('Vy4EQ1uwPkUoqvcP1nIu6WiAjxFeA3Y2'))

// 加密的翻译结果, 搜索的是hello
o = 'Z21kD9ZK1ke6ugku2ccWu-MeDWh3z252xRTQv-wZ6jddVo3tJLe7gIXz4PyxGl73nSfLAADyElSjjvrYdCvEP4pfohVVEX1DxoI0yhm36ytQNvu-WLU94qULZQ72aml6MdaC9LzSO4qdlPmtuyg_YvDQQMdLTVnTMYtInG0ZBrNPOPNzjjiq-jHBIXclo3bdhEzfuCQJrHD9t_lAkSsXJJMWMnE2HZm_g86NPlGORn2w21mrfqMP_Mc96pue4l-upHy_Dlw8NKfIiqjkfVSG6kxyE3oj-56 b5O7rjrKZ1ddUeivB627dvhzgf1Q5iugT-mU2NUPmcPsbp6iVXQ24ol07NwF1jJZmICT4Jc4qv4dt5oxft01Fv6RKqUSspdQjl1ePM9YiH_1iKjo-LN5UnVOp3wvbZSKvNIBKC-Th1NLSPkSEYMTl3AfBb7TKDSw3HDpsfZSAs-I78hplaQdsUjfG9YiyYER_pWstmNdsnMzzUV7GSp6vp5Jh8BkYA6hjQr93DYTafwAeXml0PoFr3hM1GKC2HSoN-k40A06hKJ0P6I-dFnKyvn0MyEcoUh2ggzQLyd4FukFaKxQzQfaA5Z7ZByF-7 jA5HCbwQeeJgUV4IY9iGyZ5xkYG_AlegcuXVGroLs21GWfY-SBaom7DUzkBTC38fotkVCfzd5gPsZofTr_ZmWmM_CIa4WLulYT5xsvKVUFpguspyPrcEXs6koZhny5ZCzbrIxhMJX7uyEF9rxwnIoYfoH4KTiZIUoSUju7N8Vo-APiKOoBkeCrSwfyDXNRKxDEN4Yg8afiW-QMP5LhdOWtLPgZZJDXpgU7jXV5wLLk8UA_eTKifbRI3OzxinwsV3l3xGZnnbS6NGZKfJrLGkdGjZVB9LZhECOMKD8OM-bnJRKKpI6-5 juw1lDeTLyxewCx8aAF9BAW9JqZIVtMLw7wMKwVip27BbLmCUKT0oaWDK8DTos-_gIwkF5tCzphT8FQL2ysIO-Q92IZ8oRPYQzm9QlUNN_6vC-Y-HQN0-S8WPAHVri2tdmTy8_uZm5bzZ-oLQXNSZWItt6-f3NpKQvPOidJTTq8ody2eBXJa8ImoF1I4ZeX0quLMme7T4SsuMMI0pKCXETNU5ae30Vm818QSbt2yqZAZe7_OLE-gUgBtX0KgwTxMlaswrRkq4q76NvXY3Pz0uwzW24aTx_iH3gcXu6Nywdl5Jk20jDDYlozu74RyrJZYj3Xol1roY3LD8HqyqZUqbssKYHeFI7VNqi8dQ9SboWSC43J_Uv0exurLIXtEYFWuKp-TgKdXdYn1lPXIINwsPx2Ohpc='

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






