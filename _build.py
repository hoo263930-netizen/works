# ⚠️ 2026年10月24日：works の中身は、今のHP（https://asoberu-otera.pages.dev/）へ移した。
# 各ページは「移りました」のページ（今のHPへ自動で移す）にしたので、この道具は動かさない（動かすと元のページに戻ってしまう）
raise SystemExit("works の中身は今のHPへ移した（2026年10月24日）。_build.py は使わない")

# works のページを組み立てる（ヘッダー・フッターを全ページで共通にするための、ローカル用の小さな道具）
# 使い方：python _build.py  → index.html / service/ / results/ / about/ / contact/ を書き出す
import io, os

HP = "https://hoo263930-netizen.github.io"
LINE_SOUDAN = "https://lin.ee/ZITRIHg"      # 公式LINEで問い合わせる（今のHPのご依頼ページと同じ）
FORM = HP + "/contact/"                      # お問い合わせフォーム（今のHP）
NOTE = "https://note.com/loyal_dill1011"
INSTA = "https://www.instagram.com/asoberu_otera/"
MAIL = "hoo263930@gmail.com"

SITE = "https://asoberu-otera-works.pages.dev/"  # 2026年10月1日、GitHub PagesからCloudflare Pagesへ移した

NAV = [("", "ホーム"), ("service/", "サービス"), ("results/", "実績"), ("about/", "自己紹介")]

def head(title, desc, root, path=""):
    return f"""<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <script>/* 古い住所（github.io/works）で開かれたら、新しい住所の同じページへ移す */if(/\\.github\\.io$/.test(location.hostname)){{location.replace("{SITE}"+location.pathname.replace(/^\\/works\\/?/,"")+location.search+location.hash);}}</script>
  <title>{title}</title>
  <link rel="canonical" href="{SITE}{path}" />
  <meta name="description" content="{desc}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{root}assets/style.css?v=8" />
</head>
<body>
"""

def header(root, current):
    links = []
    for path, label in NAV:
        cur = ' aria-current="page"' if path == current else ""
        cls = ' class="nav-home"' if path == "" else ""
        links.append(f'<a{cls} href="{root}{path}"{cur}>{label}</a>')
    cur = ' aria-current="page"' if current == "contact/" else ""
    links.append(f'<a class="nav-cta" href="{root}contact/"{cur}>お問い合わせ</a>')
    return f"""<header class="site-header">
  <div class="wrap">
    <a class="logo" href="{root}"><b>遊べるお寺プロジェクト</b><small>ご依頼・お問い合わせ</small></a>
    <nav class="nav" aria-label="メニュー">{''.join(links)}</nav>
  </div>
</header>
"""

def cta_band(root):
    return f"""<section class="cta-band">
  <div class="wrap">
    <h2>お問い合わせはこちらから</h2>
    <p>日にちが決まっていなくても大丈夫です。候補の日、場所、人数、ご予算（決まっていれば）を教えていただけると、話が早く進みます。</p>
    <div class="btns">
      <a class="btn primary" href="{LINE_SOUDAN}" target="_blank" rel="noopener">公式LINEで問い合わせる</a>
      <a class="btn ghost" href="{FORM}" target="_blank" rel="noopener">お問い合わせフォーム</a>
    </div>
    <p class="band-sub">Instagramの<a href="{INSTA}" target="_blank" rel="noopener">DM</a>、メール（<a href="mailto:{MAIL}">{MAIL}</a>）でも受け付けています。</p>
  </div>
</section>
"""

def footer(root):
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="cols">
      <div>
        <b style="color:var(--ink)">遊べるお寺プロジェクト</b><br />
        滋賀県高島市
      </div>
      <ul>
        <li><a href="{root}service/">サービス</a></li>
        <li><a href="{root}results/">実績</a></li>
        <li><a href="{root}about/">自己紹介</a></li>
        <li><a href="{root}haifu/">配布物</a></li>
        <li><a href="{root}contact/">お問い合わせ</a></li>
      </ul>
      <ul>
        <li><a href="{HP}/" target="_blank" rel="noopener">催しに参加したい方へ（遊べるお寺プロジェクトのHP）</a></li>
        <li><a href="{NOTE}" target="_blank" rel="noopener">活動報告（note）</a></li>
        <li><a href="https://www.instagram.com/asoberu_otera/" target="_blank" rel="noopener">Instagram</a></li>
      </ul>
    </div>
    <p class="copy">© 遊べるお寺プロジェクト</p>
  </div>
</footer>
</body>
</html>
"""

def page(path, current, title, desc, body):
    root = "../" * path.count("/")
    html = head(title, desc, root, path) + header(root, current) + "<main>\n" + body.replace("{root}", root) + "</main>\n" + cta_band(root) + footer(root)
    out = path + "index.html" if path.endswith("/") or path == "" else path
    if path == "":
        out = "index.html"
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    io.open(out, "w", encoding="utf-8", newline="\n").write(html)
    print("wrote", out)

# ───────── 実績のカード（トップと実績ページで共通） ─────────
WORKS = [
    ("健康麻雀", "2026年7〜9月", "公民館の健康麻雀講座（全5回）",
     "市の広報での募集に、定員8名のところ40名以上の申し込み。12名・3卓に広げて開きました。終わったあとも「続けたい」という声があり、会場を移して、月2回の講座として続けています。",
     NOTE + "/n/n5e70d0323a00"),
    ("健康麻雀", "2026年9月", "月1回の健康麻雀会（高島市今津町）",
     "数人から始めて、2026年9月には1回で24人。会場に置ける5卓（20人分）を超えました。",
     None),
    ("座禅", "2025年8月", "学童での座禅",
     "約90人の子どもを、20人弱ずつ5つの組に分けて行いました。",
     NOTE + "/n/nba5500e91aa4"),
    ("謎解き", "2026年2月", "市と共催の、子ども向け謎解き脱出ゲーム",
     "定員30名に29名。中学生のボランティア8名と一緒に運営しました。",
     NOTE + "/n/n4468e913ce5d"),
    ("講座", "2026年7月", "ChatGPTとCanvaのチラシ作り講座",
     "定員6名がすぐに埋まり、同じ内容で2回目を開きました。",
     NOTE + "/n/nf34be5c42627"),
]

def work_card(cat, date, title, text, url):
    inner = f'<span class="cat">{cat}</span><span class="date">{date}</span><h3>{title}</h3><p>{text}</p>'
    if url:
        return f'<a class="work" href="{url}" target="_blank" rel="noopener">{inner}<span class="go">活動報告を読む →</span></a>'
    return f'<div class="work">{inner}</div>'

# ───────── トップ ─────────
TOP = f"""
<section class="hero">
  <div class="wrap">
    <p class="eyebrow"><span class="nb">遊べるお寺プロジェクト｜</span><span class="nb">ご依頼・お問い合わせ</span></p>
    <h1><span class="nb">地域の「人が集まる場」を、</span><span class="nb">ひらいて、</span><span class="nb">続く形にします</span></h1>
    <p class="lead">健康麻雀・座禅・ボードゲームで場をひらく、滋賀・高島のお坊さん</p>
    <p class="body">公民館、サロン、学童、施設へ出張します。一回の催しで終わらせず、担い手の方が一人でも回せる形まで、一緒に考えます。</p>
    <div class="btns">
      <a class="btn primary" href="{{root}}contact/">問い合わせる</a>
      <a class="btn ghost" href="{{root}}service/">サービスを見る</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head"><span class="en">CONCERNS</span><h2>こんなとき、お問い合わせください</h2></div>
    <ul class="worries">
      <li>講座や行事を開いても、人が集まらない</li>
      <li>毎年同じ企画で、ネタが尽きてきた</li>
      <li>担い手がいなくて、続かない</li>
      <li>講座が終わると、集まりも終わってしまう</li>
      <li>子どもが楽しめる遊びの作り方が分からない</li>
    </ul>
    <p class="after">出張して場をひらくところから、自分たちで続けられる形にするところまで、お手伝いします。</p>
  </div>
</section>

<section class="section soft">
  <div class="wrap">
    <div class="sec-head"><span class="en">SERVICE</span><h2>できること</h2></div>
    <div class="cards">
      <div class="card has-img"><img class="card-img" src="{{root}}images/mahjong-play.jpg" alt="健康麻雀の会の様子" loading="lazy"><div class="card-body"><span class="num">01</span><h3>出張して、場をひらく</h3><p>健康麻雀、座禅・写経、子どもの遊び、謎解き。麻雀卓や座蒲（座禅用の座布団）など、道具を持って伺います。</p></div></div>
      <div class="card has-img"><img class="card-img" src="{{root}}images/seminar-lecture.jpg" alt="講座の様子" loading="lazy"><div class="card-body"><span class="num">02</span><h3>続く形にする</h3><p>研修・講座・講演。担い手の方が、一人でも回せる大きさで続けるための話をします。チラシや公式LINEなど、告知の道具の使い方も扱います。</p></div></div>
      <div class="card has-img"><img class="card-img" src="{{root}}images/zazen-hall.jpg" alt="お寺の本堂" loading="lazy"><div class="card-body"><span class="num">03</span><h3>相談にのる</h3><p>始めたい。人が集まらない。続けるのがしんどい。何をやるかを決める手前から、一緒に考えます。</p></div></div>
    </div>
    <a class="minor biz" href="{{root}}tsukuru/"><b>お店・事業者の方へ｜公式LINE・ホームページ制作</b>　会って、聞いて、その場で作ります。自分で直せる形でお渡しします。<span class="go">くわしく見る →</span></a>
    <p class="more"><a href="{{root}}service/">サービスの詳細を見る →</a></p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head"><span class="en">RESULTS</span><h2>これまでの場</h2></div>
    <div class="works-list">
      {''.join(work_card(*w) for w in WORKS[:4])}
    </div>
    <p class="more"><a href="{{root}}results/">実績をもっと見る →</a></p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head"><span class="en">VOICES</span><h2>受講した方の声</h2></div>
    <div class="voices">
      <figure class="voice"><blockquote>初めてAIでチラシを作る事ができて、本当に感動しました！また機会があれば是非参加したいです！</blockquote><figcaption>チラシ作り講座（2026年7月）受講者アンケートより</figcaption></figure>
      <figure class="voice"><blockquote>プロンプトは自身で考えるものだと思っていたので、プロンプトをAIに作成してもらうという事を知れたのが収穫でした。</blockquote><figcaption>チラシ作り講座 ステップアップ編（2026年9月）受講者アンケートより</figcaption></figure>
      <figure class="voice"><blockquote>AIを音声で使いこなすことが、意外とスムーズにできたのが嬉しかったです。</blockquote><figcaption>はじめてのAIセミナー（2026年9月）受講者アンケートより</figcaption></figure>
    </div>
  </div>
</section>

<section class="section soft">
  <div class="wrap">
    <div class="sec-head"><span class="en">PROFILE</span><h2>やっている人</h2></div>
    <div class="profile">
      <div class="name"><b>こーせん</b><small>久我 光聖</small><small>住職・社会福祉士・保育士</small><small>滋賀県高島市</small></div>
      <div>
        <p>永平寺で4年半の修行。児童養護施設と、社会福祉協議会で働きました。</p>
        <p>2025年4月に「遊べるお寺プロジェクト」を始め、月1回の健康麻雀会から、ボードゲーム会、写経会、講座へと広げてきました。</p>
        <p class="more" style="text-align:left;margin-top:16px"><a href="{{root}}about/">自己紹介を見る →</a></p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head"><span class="en">FLOW</span><h2>ご依頼の流れ</h2></div>
    <ol class="flow">
      <li><h3>ご連絡</h3><p>公式LINEかフォームから。「こういうことはできますか」の段階で大丈夫です。</p></li>
      <li><h3>うかがう</h3><p>日時・場所・人数・目的をうかがい、できる形と費用をお伝えします。</p></li>
      <li><h3>当日</h3><p>道具を持って伺い、進行まで引き受けます。公式LINE・ホームページは、会って、聞いて、その場で作ります。</p></li>
    </ol>
  </div>
</section>

<section class="section soft">
  <div class="wrap">
    <div class="sec-head"><span class="en">FAQ</span><h2>よくある質問</h2></div>
    <div class="faq">
      <details><summary>まだ内容が決まっていなくても、問い合わせできますか？</summary><p>できます。目的、対象の方、会場、時期をうかがって、お受けできる形と費用をお伝えします。お問い合わせは無料です。何をどうすればいいかを一緒に考える時間は、<a href="{{root}}service/#soudan">「相談にのる」</a>（オンライン1時間3,000円）としてお受けしています。</p></details>
      <details><summary>予算が限られています。</summary><p>時間を短くする、今ある内容を使う、準備物をそちらでご用意いただくなど、条件に合わせて組み直します。</p></details>
      <details><summary>会場で用意するものはありますか？</summary><p>机・椅子・電源・駐車場は、主催者側でご用意いただく形が基本です。麻雀卓など、運べるものはこちらで持って行きます。必要なものは事前にお伝えします。</p></details>
    </div>
  </div>
</section>
"""

# ───────── サービス ─────────
PRICE_NOTE = '<div class="note-box">料金は、内容をうかがってからお伝えします。料金の目安は、準備ができしだい、このページに載せます。</div>'
# 公式LINE・ホームページ制作の料金（2026年9月30日に決定。04_決定事項 9/30）
TSUKURU_PRICE = """<table class="price">
  <tr><th>公式LINE</th><td><b>30,000円</b><span class="p-sub">開設・基本設定（2026年12月までのお申し込み）</span></td></tr>
  <tr><th>＋リッチメニュー</th><td><b>5,000円</b><span class="p-sub">トーク画面の下のボタン</span></td></tr>
  <tr><th>＋アイコン</th><td><b>5,000円</b></td></tr>
  <tr><th>ホームページ</th><td><b>80,000円から</b><span class="p-sub">1ページ</span></td></tr>
</table>
<ul class="price-notes">
  <li>作る日にお店で一緒に作る時間（2時間まで）は、料金に含みます。2時間を超えた分は、1時間3,000円です。</li>
  <li>作るかどうかを決める前の相談で伺う場合は、1回5,000円です。</li>
  <li>ホームページはCanvaで作ります。あとからご自身で直せます。公開は無料のアドレス（〇〇.my.canva.site）です。お店独自のアドレスにする場合は、Canvaの有料プランとドメイン代（年1,000〜3,000円ほど）が、お店側でかかります。</li>
  <li>ホームページの直しは1回まで。文章と写真は、お店側でご用意ください。</li>
</ul>"""
# 03 相談にのる（団体）の料金。今のHPの個別相談と同じ（2026年10月20日に決定・10月24日に団体もそろえた）
SOUDAN_PRICE = """<table class="price">
  <tr><th>オンライン</th><td><b>1時間 3,000円</b></td></tr>
  <tr><th>こちらから伺う場合</th><td><b>1時間 5,000円</b><span class="p-sub">高島市内</span></td></tr>
</table>
<ul class="price-notes">
  <li>1時間をこえる場合は、1時間ごとに同じ料金です。</li>
</ul>"""
SERVICE = f"""
<section class="page-head"><div class="wrap"><span class="en">SERVICE</span><h1>サービス</h1><p>中心は「場をひらく」と「続く形にする」の2つです。公式LINE・ホームページの制作もお受けしています。</p></div></section>
<div class="page-body"><div class="wrap">

<div class="block" id="hiraku">
  <h2>01　出張して、場をひらく</h2>
  <div class="photo-row">
    <figure><img src="../images/mahjong-play.jpg" alt="健康麻雀の会" loading="lazy"><figcaption>健康麻雀</figcaption></figure>
    <figure><img src="../images/zazen-kids.jpg" alt="子どもたちへの座禅" loading="lazy"><figcaption>座禅</figcaption></figure>
    <figure><img src="../images/kids-boardgame.jpg" alt="子どものボードゲーム" loading="lazy"><figcaption>子どもの遊び</figcaption></figure>
  </div>
  <h3>健康麻雀</h3>
  <p>会を開く／大会の企画・運営（組み合わせ、点数表、進行まで）／初めての方への講座。卓と牌を持って伺うので、会場に道具がなくても開けます。麻雀を知らない方も遊べる「4枚麻雀」の体験もできます。</p>
  <h3>座禅・写経・仏教カフェ</h3>
  <p>住職が伺います。座蒲や鐘など、お寺の道具を持って行きます。お寺に来ていただく形もできます。</p>
  <h3>子どもの遊び</h3>
  <p>ボードゲーム会、謎解き・脱出ゲーム、学童・児童館への出張あそび。学年の幅が広くても、組を分けてから合流させる形で、一緒に遊べるように組みます。</p>
  <h3>向いている依頼の例</h3>
  <ul class="tag-list"><li>公民館の講座</li><li>高齢者サロン・地域の集まり</li><li>学童・子ども会・子ども食堂の行事</li><li>お祭り・フェスタのブース</li><li>市や団体の交流イベント</li></ul>
  <h3>料金</h3>
  <p>内容・準備の量・人数・移動の距離で変わります。交通費・印刷物・材料費が要るときは、事前にお伝えします。謎解きを新しく作る場合は、別にお見積もりをお出しします。</p>
  {PRICE_NOTE}
</div>

<div class="block" id="tsuzuku">
  <h2>02　続く形にする（研修・講座・講演）</h2>
  <div class="photo-row one"><figure><img src="../images/seminar-lecture.jpg" alt="講座の様子" loading="lazy"><figcaption>講座の様子</figcaption></figure></div>
  <p>担い手の方が、自分たちで続けられるようにするための研修・講座です。</p>
  <ul>
    <li><b>地域活動のはじめ方</b>：大きく始めず、一人でも回せる大きさで始めて、続ける話</li>
    <li><b>チラシ作り</b>：ChatGPTとCanvaで、告知の紙を自分で作れるようにする回</li>
    <li><b>公式LINEの使い方</b>：お知らせを届ける道具としての、基本の使い方</li>
  </ul>
  <p>内容・時間・対象に合わせて組み立てます。パソコンやスマホに自信がない方に向けた回もできます。1回2時間で組むことが多いです。</p>
  <h3>向いている依頼の例</h3>
  <ul class="tag-list"><li>担い手・ボランティア向けの研修</li><li>市民活動団体・サロンの世話役の勉強会</li><li>事業者向けの告知の道具の講座</li><li>地域づくりの講演</li></ul>
  <h3>料金</h3>
  <p>行政・学校・団体で講師料の規定がある場合は、その規定に合わせて内容を調整します。</p>
  {PRICE_NOTE}
</div>

<div class="block" id="soudan">
  <h2>03　相談にのる</h2>
  <p>これから始めたい。人が集まらない。続けるのがしんどい。そうした段階のご相談をお受けします。場所（箱）・関わる人（ひと）・道具や連絡手段（もの）の順に、何が足りていて、何が止まっているかを一緒に整理します。</p>
  <h3>向いている依頼の例</h3>
  <ul class="tag-list"><li>新しい集まりを始めたい団体・自治会</li><li>行事を少ない人数で回せる形にしたい</li><li>チラシ・公式LINE・ホームページの使い方が分からない</li></ul>
  <p>団体の方は、お会いして、またはオンラインで。個人の方は、<a href="{HP}/consult/#online" target="_blank" rel="noopener">相談のページの個別相談（オンライン1時間3,000円）</a>からお申し込みください。</p>
  <h3>料金</h3>
  {SOUDAN_PRICE}
</div>

<div class="block" id="tsukuru">
  <h2>04　つくる（公式LINE・ホームページ）</h2>
  <ul>
    <li><b>公式LINE</b>：開設から、リッチメニュー（トーク画面の下に出るボタン）まで</li>
    <li><b>ホームページ</b>：1ページのホームページ</li>
  </ul>
  <h3>作り方</h3>
  <ul>
    <li>会って、聞いて、その場で作ります</li>
    <li>お店・団体のアカウントで作ります。こちらの手を離れても、そちらのものとして残ります</li>
    <li>画像は、編集できるデータごとお渡しします</li>
    <li>直し方を、その場で一度一緒にやります</li>
  </ul>
  <h3>料金</h3>
  {TSUKURU_PRICE}
  <p><a href="../tsukuru/">お店・事業者の方へのご案内（流れ・当日までにご用意いただくもの）→</a></p>
</div>

</div></div>
"""


# ───────── つくる（お店・事業者の方へ） ─────────
TSUKURU = f"""
<section class="page-head"><div class="wrap"><span class="en">FOR BUSINESS</span><h1><span class="nb">公式LINE・ホームページ、</span><span class="nb">会って、</span><span class="nb">その場で作ります</span></h1><p>高島のお店・教室・小さな事業者のための、公式LINEとホームページづくりです。</p></div></section>
<div class="page-body"><div class="wrap">

<div class="block">
  <h2>こんなこと、ありませんか</h2>
  <ul class="worries">
    <li>公式LINE、作りたいけど時間がない</li>
    <li>ホームページ、頼むと高そう</li>
    <li>作ったあと、自分で直せるか不安</li>
  </ul>
</div>

<div class="block">
  <h2>3つの特長</h2>
  <div class="cards">
    <div class="card"><span class="num">01</span><h3>その日に、できあがる</h3><p>お店に伺い、お話を聞きながら、その場で作ってお渡しします（公式LINEは目安2時間。ホームページは1〜2回伺います）。</p></div>
    <div class="card"><span class="num">02</span><h3>自分で直せる形で渡す</h3><p>データごとお渡しし、直し方も一度いっしょにやります。あとから誰かに頼まなくてすみます。</p></div>
    <div class="card"><span class="num">03</span><h3><span class="nb">「まだ決めていない」でも</span><span class="nb">問い合わせできる</span></h3><p>作るかどうか迷っている段階でも大丈夫です。お問い合わせは無料です。</p></div>
  </div>
</div>

<div class="block">
  <h2>作れるもの</h2>
  <ul>
    <li><b>公式LINE</b>：開設から、リッチメニュー（トーク画面の下に出るボタン）まで</li>
    <li><b>ホームページ</b>：1ページのホームページ</li>
  </ul>
  <p>お店・団体のアカウントで作ります。こちらの手を離れても、そちらのものとして残ります。</p>
  <div class="note-box">2026年9月、地域のお店の公式LINEを、開設からメニューまで、その日のうちに作りました。<a href="{NOTE}/n/n7ce9939c689e" target="_blank" rel="noopener">そのときの様子（note）</a></div>
</div>

<div class="block">
  <h2>流れ</h2>
  <ol class="flow flow5">
    <li><h3>ご連絡</h3><p>公式LINE・InstagramのDM・メールから。</p></li>
    <li><h3>日程を決める</h3><p>作りたいものと、お店に伺う日を決めます。</p></li>
    <li><h3>お店でお会いする</h3><p>お話を聞きながら、中身を決めます。</p></li>
    <li><h3>その場で作る</h3><p>目の前で作っていきます。</p></li>
    <li><h3>直し方を覚えて完成</h3><p>一度いっしょに直してみて、お渡しします。</p></li>
  </ol>
</div>

<div class="block">
  <h2>当日までにご用意いただくもの</h2>
  <p>ここがそろっていないと、当日は相談だけで終わることがあります。</p>
  <ul>
    <li>使うメールアドレスと、そのパスワードが分かる状態</li>
    <li>SMS（ショートメール）が受け取れる携帯電話</li>
    <li>お店のロゴ・写真（あれば）</li>
    <li>メニュー・値段・営業時間の一覧（紙でもメモでも）</li>
    <li>当日、一緒に見られるパソコンかタブレット（なければこちらで用意します）</li>
  </ul>
</div>

<div class="block">
  <h2>料金</h2>
  {TSUKURU_PRICE}
</div>

</div></div>
"""
# ───────── 実績 ─────────
MORE_WORKS = [
    ("健康麻雀", "2026年8月", "健康麻雀大会", "初めての大会の企画・運営。12名・3卓。", NOTE + "/n/n868f7aded76b"),
    ("健康麻雀", "2025年11月", "フェスタのブース", "麻雀を知らない方も遊べる「4人で4枚麻雀」。", NOTE + "/n/nff7a4b1624c0"),
    ("座禅", "2025年10月", "多文化共生の団体からのご依頼", "未就学児を中心に、親子で約20名。", NOTE + "/n/n64e0cf92b93e"),
    ("子どもの遊び", "2026年7月", "子ども向け事業の遊びの時間（県内）", "小学生約20人を、低学年と高学年に分けてから合流させる形で。", NOTE + "/n/n1e4b9bcd5b6c"),
    ("謎解き", "2026年6月", "市の事業の、婚活謎解きイベント（ホテル会場）", "委託を受けた団体から、企画・実施を担当。", NOTE + "/n/nee20e873fe28"),
    ("つくる", "2026年9月", "地域のお店の公式LINE", "開設からメニューまで、その日のうちに。", NOTE + "/n/n7ce9939c689e"),
]
def cat_section(name, items):
    return f'<h2 class="cat-title">■ {name}</h2><div class="works-list">' + "".join(work_card(*w) for w in items) + "</div>"
allw = WORKS + MORE_WORKS
cats = ["健康麻雀", "座禅", "謎解き", "子どもの遊び", "講座", "つくる"]
RESULTS = """
<section class="page-head"><div class="wrap"><span class="en">RESULTS</span><h1>実績</h1><p>開いてきた場と、お受けした依頼です。くわしい様子は、活動報告（note）に書いています。</p></div></section>
<div class="page-body"><div class="wrap">
""" + "".join(cat_section(c, [w for w in allw if w[0] == c]) for c in cats if any(w[0] == c for w in allw)) + """
</div></div>
"""

# ───────── 自己紹介 ─────────
ABOUT = f"""
<section class="page-head"><div class="wrap"><span class="en">PROFILE</span><h1>自己紹介</h1><p>お寺を、法事や儀式のときだけでなく、人が集まって、遊んで、話せる場所にしたい。そう考えて「遊べるお寺プロジェクト」を始めました。いまは、お寺の外にも出て、地域の場をひらいています。</p></div></section>
<div class="page-body"><div class="wrap">
<div class="block">
  <div class="profile">
    <div class="name"><b>こーせん</b><small>久我 光聖</small><small>遊べるお寺プロジェクト</small><small>住職・社会福祉士・保育士</small><small>滋賀県高島市</small></div>
    <div>
      <h3 style="margin-top:0">経歴</h3>
      <ul>
        <li>曹洞宗の僧侶</li>
        <li>永平寺で4年半、修行</li>
        <li>保育士として、児童養護施設で4年</li>
        <li>社会福祉士として、社会福祉協議会で勤務</li>
        <li>高島市・長善寺の住職</li>
        <li>2025年4月から「遊べるお寺プロジェクト」</li>
      </ul>
    </div>
  </div>
</div>
<div class="block">
  <h2>大事にしていること</h2>
  <ul class="tag-list"><li>続ける前提で始めない</li><li>一人で回せる仕組みをつくる</li></ul>
  <p>大きく始めて、続けるために無理をするより、一人でも回せる大きさで始める。そのほうが続く、と考えています。頼まれて作るものも、相手の方が自分で回せる形でお渡しします。</p>
</div>
<div class="block">
  <h2>いま高島市で開いている会</h2>
  <ul class="tag-list"><li>健康麻雀会（月1回）</li><li>健康麻雀講座（月2回）</li><li>ボードゲーム会</li><li>写経会</li><li>講座（チラシ作り・公式LINE・AI）</li></ul>
  <p>参加したい方は、<a href="{HP}/" target="_blank" rel="noopener">遊べるお寺プロジェクトのホームページ</a>へ。</p>
</div>
</div></div>
"""

# ───────── お問い合わせ ─────────
CONTACT = f"""
<section class="page-head"><div class="wrap"><span class="en">CONTACT</span><h1>お問い合わせ</h1><p>「こういうことはできますか」の段階で大丈夫です。</p></div></section>
<div class="page-body"><div class="wrap">
<div class="block">
  <h2>教えていただけると早いこと</h2>
  <ul>
    <li>開催の希望日（候補で大丈夫です）</li>
    <li>場所（市町名と会場名）</li>
    <li>参加予定の人数と年齢層</li>
    <li>ご予算（決まっていれば）</li>
  </ul>
</div>
<div class="block">
  <h2>窓口</h2>
  <div class="btns">
    <a class="btn primary" href="{LINE_SOUDAN}" target="_blank" rel="noopener">公式LINEで問い合わせる</a>
    <a class="btn ghost" href="{FORM}" target="_blank" rel="noopener">お問い合わせフォーム</a>
  </div>
  <ul>
    <li>Instagramの<a href="{INSTA}" target="_blank" rel="noopener">DM</a>でも受け付けています</li>
    <li>メール：<a href="mailto:{MAIL}">{MAIL}</a></li>
  </ul>
  <p class="note-box">個人の方の個別相談は、<a href="{HP}/consult/#online" target="_blank" rel="noopener">相談のページ</a>からお申し込みください。</p>
</div>
</div></div>
"""

# ───────── Substack（名簿）の登録欄（redesign のたかしまーじゃんの段と同じもの） ─────────
SUBSTACK = "https://kosen3.substack.com"

SUBSCRIBE_HOWTO = f"""<div class="howto">
    <b>登録のしかた</b>
    <ol>
      <li>下の欄にメールアドレスを入れて、オレンジのボタン（Subscribe）を押す</li>
      <li>英語の画面がいくつか出ます。いちばん下の灰色の文字（Skip for now／Maybe later）を押して進めてください</li>
      <li>「Please confirm your subscription」という英語のメールが届きます。オレンジのボタン（Confirm subscription）を押すと、登録が終わります</li>
    </ol>
    <p>うまくいかないときは、公式LINEかメールでお知らせください。</p>
  </div>
  <div class="substack-embed"><iframe src="{SUBSTACK}/embed" title="メールアドレスの登録" width="480" height="320" frameborder="0" scrolling="no"></iframe></div>"""

# ───────── 配布物（2026年10月21日・本人「ワークスみたいにね、私のやっぱところに集約していく」） ─────────
# ダウンロードは誰でも（登録なし）。新しい版のお知らせは Substack（名簿）。伴走のzipは scratchpad の make_banso_zip.py で作る
FORMSPREE = "https://formspree.io/f/mrbybkoe"   # 今のHPのお問い合わせフォームと同じ受け口（届くのは同じメール）
BANSO_ZIP = "banso-0.9.zip"                      # 版を上げたら、functions/haifu/banso/dl.js の FILE も直す

HAIFU = f"""
<section class="page-head"><div class="wrap"><span class="en">FREE DOWNLOADS</span><h1>配布物</h1><p><span class="nb">無料で使える、</span><span class="nb">資料と道具です。</span></p></div></section>
<div class="page-body"><div class="wrap">

<div class="block">
  <div class="works-list">
    <a class="work" href="{{root}}haifu/banso/"><span class="cat">AIの相棒</span><span class="date">試作版・2026年10月</span><h3>伴走｜イベントができて、続いていくまで</h3><p>地域の会・教室・イベントを開く人のための、AIの手引き。始める・チラシ・記録・相談の4つの場面で付き合います。Claude Code と ChatGPT で使えます。</p><span class="go">くわしく見る →</span></a>
    <a class="work" href="{HP}/takashimahjong/" target="_blank" rel="noopener"><span class="cat">遊びのルール</span><span class="date">2026年10月</span><h3>たかしまーじゃん ルール資料</h3><p>牌だけあれば遊べる、いちばんやさしい麻雀。初級・中級・上級のルールの紙と、麻雀牌の読み方表（A4・印刷用）。登録なしでダウンロードできます。</p><span class="go">くわしく見る（遊べるお寺プロジェクトのHP）→</span></a>
  </div>
</div>

<div class="block">
  <h2>新しい版のお知らせ</h2>
  <p>配布物を直したときや、新しいものを出したときは、メール（Substack）でお知らせします。地域活動の話も、ときどき書いています。</p>
  <div class="btns"><a class="btn primary" href="{SUBSTACK}/subscribe" target="_blank" rel="noopener">お知らせをメールで受け取る</a></div>
</div>

</div></div>
"""

BANSO = f"""
<section class="page-head"><div class="wrap"><span class="en">FREE TRIAL</span><h1>伴走</h1><p><span class="nb">イベント・教室・地域の会を開く人のための、</span><span class="nb">AIの相棒です。</span><span class="nb">始めるところから、チラシ、記録、</span><span class="nb">次の回まで付き合います。</span><span class="nb">試作版を、無料で配っています。</span></p></div></section>
<div class="page-body"><div class="wrap">

<div class="block">
  <h2>こんなときに</h2>
  <ul class="worries">
    <li>新しく会を始めたいけれど、何から手をつければいいか分からない</li>
    <li>場所が見つからない。誰と一緒にやればいいか分からない</li>
    <li>AIにチラシを頼んだら、ごちゃごちゃしたものが返ってきた</li>
    <li>会が終わったあと、何を残して、次にどう生かせばいいか分からない</li>
  </ul>
  <p>活動は、場所（箱）・関わる人（ひと）・道具や連絡手段（もの）の3つがそろったとき、はじめて回り出します。伴走は、その土台の点検から、チラシ、記録、次の回の見直しまでを、AIと一緒にやるための手引きです。</p>
</div>

<div class="block">
  <h2>伴走でできること</h2>
  <p>話しかける言葉によって、4つの場面で付き合います。質問はいつも一覧でまとめて出るので、音声入力で一気に答えられます。</p>
  <div class="works-list">
    <div class="work"><span class="cat">始める</span><h3>「新しい回を始めたい」</h3><p>箱・ひと・ものを並べて、足りないところを見える化します。場所の候補をためておく台帳や、場所を借りるときの打診の叩き台も作ります。</p></div>
    <div class="work"><span class="cat">チラシ</span><h3>「チラシを作りたい」</h3><p>19の質問に答えると、構成案（3案＋おすすめ）と、画像を作るAIに渡す指示文ができます。日時や金額は画像に描き込ませず、あとから入れる作りです。</p></div>
    <div class="work"><span class="cat">記録</span><h3>「回が終わったから記録したい」</h3><p>誰が来たか、想定と違ったことを1枚に残します。箱・ひと・もの・マーケの4つで見て、次の一手を3案で出します。</p></div>
    <div class="work"><span class="cat">相談</span><h3>「相談したい」</h3><p>人が集まらない、なんだかうまくいかない。過去の記録を読んでから、一緒に考えます。</p></div>
  </div>
  <p>デザインの画像そのものは作りません。画像は、ChatGPT・Canva など、お使いのもので作ります。</p>
</div>

<div class="block" id="dl">
  <h2>ダウンロード（無料）</h2>
  <p>zipファイル（26KB）です。中に、使い方の説明（README）が入っています。</p>
  <div class="btns"><a class="btn primary" href="{{root}}haifu/banso/dl" download="{BANSO_ZIP}">無料でダウンロード（試作版 0.9）</a></div>
  <div class="note-box"><b>試作版です。</b>使ってみた感想を、下のフォームから聞かせてください。次の版づくりに使います。<br />作ったチラシや記録は、お仕事を含めて自由に使えます。ほかの方に紹介するときは、ファイルではなく、このページのリンクを伝えてください（新しい版が届くように）。</div>
</div>

<div class="block">
  <h2>使い方</h2>
  <p>くわしくは、zipの中の README にあります。</p>
  <h3>Claude Code で使う</h3>
  <ol>
    <li>zipを開いて、<code>banso</code> フォルダを <code>.claude/skills</code> の中へ、フォルダごと入れる</li>
    <li>新しいチャットを開く</li>
    <li>「新しい回を始めたい」「チラシを作りたい」などと話しかける</li>
  </ol>
  <h3>ChatGPT で使う</h3>
  <ol>
    <li>「プロジェクト」を新しく作る</li>
    <li>プロジェクトの「ファイル」に <code>chatgpt/伴走.md</code> を入れる</li>
    <li>「指示」の欄に、READMEにある1行を貼る</li>
    <li>そのプロジェクトの中で、同じように話しかける</li>
  </ol>
  <p class="note-box">使うには、Claude Code（Anthropic の有料プラン）か、ChatGPT の「プロジェクト」の機能が要ります。ChatGPTでは、記録や場所の台帳は会話の中に表で出てきます。手元のメモなどに保存しておき、次に相談するときに貼ってください。</p>
</div>

<div class="block" id="kansou">
  <h2>感想を聞かせてください</h2>
  <p>ひとことでも助かります。お名前はいりません。</p>
  <form class="fb-form" action="{FORMSPREE}" method="POST">
    <fieldset>
      <legend>使ったもの</legend>
      <div class="choices">
        <label><input type="radio" name="使ったもの" value="Claude Code" /> Claude Code</label>
        <label><input type="radio" name="使ったもの" value="ChatGPT" /> ChatGPT</label>
        <label><input type="radio" name="使ったもの" value="そのほか" /> そのほか</label>
      </div>
    </fieldset>
    <div><label for="fb-made">何に使いましたか</label><input type="text" id="fb-made" name="何に使ったか" placeholder="例：教室のチラシ、新しい会の準備、回の記録" /></div>
    <div><label for="fb-good">よかったところ</label><textarea id="fb-good" name="よかったところ"></textarea></div>
    <div><label for="fb-bad">困ったところ・分かりにくかったところ</label><textarea id="fb-bad" name="困ったところ"></textarea></div>
    <div><label for="fb-mail">メールアドレス<span class="opt">返事がほしい方だけ</span></label><input type="email" id="fb-mail" name="email" /></div>
    <input type="hidden" name="_subject" value="伴走 試作版の感想" />
    <input type="text" name="_gotcha" class="hp" tabindex="-1" autocomplete="off" />
    <button type="submit">送る</button>
    <p class="done" hidden>ありがとうございました。届きました。</p>
  </form>
</div>

<div class="block">
  <h2>新しい版のお知らせ</h2>
  <p>新しい版ができたら、メール（Substack）でお知らせします。たかしまーじゃんなど、ほかの配布物のお知らせも同じメールで届きます。いつでも、メールの下のリンクから解除できます。</p>
  {SUBSCRIBE_HOWTO}
</div>

<div class="block">
  <h2>質問・お問い合わせ</h2>
  <p>使い方の質問を受ける窓口（公式LINE）を準備しています。それまでは、上のフォームか、メール（<a href="mailto:{MAIL}">{MAIL}</a>）でどうぞ。</p>
  <p>チラシづくりのやり方のご相談は、<a href="{HP}/consult/#online" target="_blank" rel="noopener">個別相談（オンライン1時間3,000円）</a>でお受けしています。</p>
</div>

<p class="note-box">作った人：遊べるお寺プロジェクト　こーせん（久我光聖）。滋賀県高島市で、健康麻雀・写経会・チラシ作り講座などをやっているお坊さんです。自分の会を開いて、チラシを作り、記録をつけて、次の回を直す中で、この手引きができました。→ <a href="{{root}}about/">自己紹介</a></p>

</div></div>
<script>
/* 感想フォーム：送ったあと、ページを移らずにお礼を出す（JSが動かないときは、ふつうに送られる） */
document.querySelectorAll(".fb-form").forEach(function(f){{
  f.addEventListener("submit", function(e){{
    e.preventDefault();
    var b = f.querySelector("button"); b.disabled = true; b.textContent = "送っています…";
    fetch(f.action, {{method:"POST", body:new FormData(f), headers:{{"Accept":"application/json"}}}})
      .then(function(r){{ if(!r.ok) throw r; f.reset(); b.hidden = true; f.querySelector(".done").hidden = false; }})
      .catch(function(){{ b.disabled = false; b.textContent = "送る"; alert("うまく送れませんでした。時間をおいて、もう一度お試しください。"); }});
  }});
}});
</script>
"""

page("", "", "遊べるお寺プロジェクト｜ご依頼・お問い合わせ", "地域の「人が集まる場」を、ひらいて、続く形にします。健康麻雀・座禅・ボードゲームで場をひらく、滋賀・高島のお坊さん。", TOP)
page("service/", "service/", "サービス｜遊べるお寺プロジェクト ご依頼・お問い合わせ", "出張して場をひらく／続く形にする（研修・講座・講演）／相談にのる／つくる（公式LINE・ホームページ）", SERVICE)
page("results/", "results/", "実績｜遊べるお寺プロジェクト ご依頼・お問い合わせ", "健康麻雀・座禅・謎解き・講座など、これまでに開いた場とお受けした依頼。", RESULTS)
page("about/", "about/", "自己紹介｜遊べるお寺プロジェクト ご依頼・お問い合わせ", "こーせん（久我光聖）。住職・社会福祉士・保育士。滋賀県高島市。", ABOUT)
page("tsukuru/", "tsukuru/", "公式LINE・ホームページ制作｜遊べるお寺プロジェクト ご依頼・お問い合わせ", "高島のお店・教室・小さな事業者のための、公式LINEとホームページづくり。会って、その場で作ります。", TSUKURU)
page("contact/", "contact/", "お問い合わせ｜遊べるお寺プロジェクト ご依頼・お問い合わせ", "公式LINEかお問い合わせフォームから。", CONTACT)
page("haifu/", "haifu/", "配布物｜遊べるお寺プロジェクト", "無料で使える資料と道具。イベントの始め方からチラシ・記録まで付き合うAIの手引き「伴走」、いちばんやさしい麻雀「たかしまーじゃん」のルール資料。", HAIFU)
page("haifu/banso/", "haifu/banso/", "伴走｜イベントができて、続いていくまで（試作版・無料）｜遊べるお寺プロジェクト", "イベント・教室・地域の会を開く人のための、AIの相棒。始める・チラシ・記録・相談の4つの場面で付き合います。Claude Code と ChatGPT で使えます。試作版を無料で配っています。", BANSO)
