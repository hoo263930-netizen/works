// 配布物のダウンロード回数を見る（/haifu/count）。2026年10月21日
export async function onRequest({ env }) {
  const headers = { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" };
  if (!env.DL) return new Response(JSON.stringify({ note: "KV（DL）がまだつながっていません" }), { headers });
  const out = {};
  for (const k of (await env.DL.list()).keys) out[k.name] = Number(await env.DL.get(k.name));
  return new Response(JSON.stringify(out, null, 1), { headers });
}
