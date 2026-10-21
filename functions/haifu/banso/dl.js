// 伴走のダウンロード：回数を1つ足してから、zipへ送る（2026年10月21日）
// 回数は Cloudflare の KV（名前 DL）に入れる。KV をつなぐまでは数えずに、そのまま zip へ送る
// 版を上げたら FILE と KEY を直す（_build.py の BANSO_ZIP も）
const FILE = "/haifu/banso/banso-0.9.zip";
const KEY = "banso-0.9";

export async function onRequest({ env, request }) {
  if (env.DL) {
    try {
      const n = parseInt((await env.DL.get(KEY)) || "0", 10) + 1;
      await env.DL.put(KEY, String(n));
    } catch (e) {
      // 数えられなくても、ダウンロードは止めない
    }
  }
  return Response.redirect(new URL(FILE, request.url).toString(), 302);
}
