// 伴走のダウンロード（2026年10月21日）→ 2026年10月24日、伴走は今のHP（地域の道具）へ移した
// 前の住所から来たダウンロードも、今のHPの /dougu/banso/dl（回数を数えてから zip へ送る）へ送る
export async function onRequest() {
  return Response.redirect("https://asoberu-otera.pages.dev/dougu/banso/dl", 302);
}
