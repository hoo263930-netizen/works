# works のページを組み立てる（ヘッダー・フッターを全ページで共通にするための、ローカル用の小さな道具）
# 使い方：python _build.py  → index.html / service/ / results/ / about/ / contact/ を書き出す
import io, os

HP = "https://hoo263930-netizen.github.io"
LINE_SOUDAN = "https://lin.ee/ZITRIHg"      # 公式LINEで相談する（今のHPのご依頼ページと同じ）
FORM = HP + "/contact/"                      # お問い合わせフォーム（今のHP）
NOTE = "https://note.com/loyal_dill1011"

NAV = [("", "ホーム"), ("service/", "サービス"), ("results/", "実績"), ("about/", "自己紹介")]

def head(title, desc, root):
    return f"""<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="robots" content="noindex, nofollow" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{root}assets/style.css?v=2" />
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
    <a class="logo" href="{root}"><b>遊べるお寺プロジェクト</b><small>ご依頼・ご相談</small></a>
    <nav class="nav" aria-label="メニュー">{''.join(links)}</nav>
  </div>
</header>
"""

def cta_band(root):
    return f"""<section class="cta-band">
  <div class="wrap">
    <h2>ご相談はこちらから</h2>
    <p>日にちが決まっていなくても大丈夫です。候補の日、場所、人数、ご予算（決まっていれば）を教えていただけると、話が早く進みます。</p>
    <div class="btns">
      <a class="btn primary" href="{LINE_SOUDAN}" target="_blank" rel="noopener">公式LINEで相談する</a>
      <a class="btn ghost" href="{FORM}" target="_blank" rel="noopener">お問い合わせフォーム</a>
    </div>
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
    html = head(title, desc, root) + header(root, current) + "<main>\n" + body.replace("{root}", root) + "</main>\n" + cta_band(root) + footer(root)
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
    <p class="eyebrow">遊べるお寺プロジェクト｜ご依頼・ご相談</p>
    <h1><span class="nb">地域の「人が集まる場」を、</span><span class="nb">ひらいて、</span><span class="nb">続く形にします</span></h1>
    <p class="lead">健康麻雀・座禅・ボードゲームで場をひらく、滋賀・高島のお坊さん</p>
    <p class="body">公民館、サロン、学童、施設へ出張します。一回の催しで終わらせず、担い手の方が一人でも回せる形まで、一緒に考えます。</p>
    <div class="btns">
      <a class="btn primary" href="{{root}}contact/">相談する</a>
      <a class="btn ghost" href="{{root}}service/">サービスを見る</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head"><span class="en">CONCERNS</span><h2>こんなとき、ご相談ください</h2></div>
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
      <div class="card"><span class="num">01</span><h3>出張して、場をひらく</h3><p>健康麻雀、座禅・写経、子どもの遊び、謎解き。麻雀卓や座蒲（座禅用の座布団）など、道具を持って伺います。</p></div>
      <div class="card"><span class="num">02</span><h3>続く形にする</h3><p>研修・講座・講演。担い手の方が、一人でも回せる大きさで続けるための話をします。チラシや公式LINEなど、告知の道具の使い方も扱います。</p></div>
      <div class="card"><span class="num">03</span><h3>相談にのる</h3><p>始めたい。人が集まらない。続けるのがしんどい。何をやるかを決める手前から、一緒に考えます。</p></div>
    </div>
    <div class="minor"><b>つくる（公式LINE・ホームページ）</b>　会って、聞いて、その場で作ります。自分で直せる形でお渡しします。</div>
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
      <details><summary>まだ内容が決まっていなくても、相談できますか？</summary><p>できます。目的、対象の方、会場、時期をうかがいながら、できる形を一緒に考えます。</p></details>
      <details><summary>予算が限られています。</summary><p>時間を短くする、今ある内容を使う、準備物をそちらでご用意いただくなど、条件に合わせて組み直します。</p></details>
      <details><summary>会場で用意するものはありますか？</summary><p>机・椅子・電源・駐車場は、主催者側でご用意いただく形が基本です。麻雀卓など、運べるものはこちらで持って行きます。必要なものは事前にお伝えします。</p></details>
    </div>
  </div>
</section>
"""

# ───────── サービス ─────────
PRICE_NOTE = '<div class="note-box">料金は、内容をうかがってからお伝えします。料金の目安は、準備ができしだい、このページに載せます。</div>'
SERVICE = f"""
<section class="page-head"><div class="wrap"><span class="en">SERVICE</span><h1>サービス</h1><p>中心は「場をひらく」と「続く形にする」の2つです。公式LINE・ホームページの制作もお受けしています。</p></div></section>
<div class="page-body"><div class="wrap">

<div class="block" id="hiraku">
  <h2>01　出張して、場をひらく</h2>
  <h3>健康麻雀</h3>
  <p>会を開く／大会の企画・運営（組み合わせ、点数表、進行まで）／初めての方への講座。卓と牌を持って伺うので、会場に道具がなくても開けます。麻雀を知らない方も遊べる「4枚麻雀」の体験もできます。</p>
  <h3>座禅・写経・仏教カフェ</h3>
  <p>住職が伺います。座蒲や鐘など、お寺の道具を持って行きます。お寺に来ていただく形もできます。</p>
  <h3>子どもの遊び</h3>
  <p>ボードゲーム会、謎解き・脱出ゲーム、学童・児童館への出張あそび。学年の幅が広くても、組を分けてから合流させる形で、一緒に遊べるように組みます。</p>
  <h3>向いている依頼の例</h3>
  <ul class="tag-list"><li>公民館の講座</li><li>高齢者サロン・地域の集まり</li><li>学童・子ども会・子ども食堂の行事</li><li>お祭り・フェスタのブース</li><li>市や団体の交流イベント</li></ul>
  <h3>料金</h3>
  <p>内容・準備の量・人数・移動の距離で変わります。交通費・印刷物・材料費が要るときは、事前にお伝えします。謎解きを新しく作る場合は、別にご相談します。</p>
  {PRICE_NOTE}
</div>

<div class="block" id="tsuzuku">
  <h2>02　続く形にする（研修・講座・講演）</h2>
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
  <p>団体の方は、お会いして、またはオンラインで。個人の方は、<a href="{HP}/consult/" target="_blank" rel="noopener">オンラインの個別相談（30分）</a>もあります。</p>
  {PRICE_NOTE}
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
  {PRICE_NOTE}
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
    <a class="btn primary" href="{LINE_SOUDAN}" target="_blank" rel="noopener">公式LINEで相談する</a>
    <a class="btn ghost" href="{FORM}" target="_blank" rel="noopener">お問い合わせフォーム</a>
  </div>
  <p class="note-box">個人の方の個別相談は、<a href="{HP}/consult/" target="_blank" rel="noopener">相談のページ</a>からお申し込みください。</p>
</div>
</div></div>
"""

page("", "", "遊べるお寺プロジェクト｜ご依頼・ご相談", "地域の「人が集まる場」を、ひらいて、続く形にします。健康麻雀・座禅・ボードゲームで場をひらく、滋賀・高島のお坊さん。", TOP)
page("service/", "service/", "サービス｜遊べるお寺プロジェクト ご依頼・ご相談", "出張して場をひらく／続く形にする（研修・講座・講演）／相談にのる／つくる（公式LINE・ホームページ）", SERVICE)
page("results/", "results/", "実績｜遊べるお寺プロジェクト ご依頼・ご相談", "健康麻雀・座禅・謎解き・講座など、これまでに開いた場とお受けした依頼。", RESULTS)
page("about/", "about/", "自己紹介｜遊べるお寺プロジェクト ご依頼・ご相談", "こーせん（久我光聖）。住職・社会福祉士・保育士。滋賀県高島市。", ABOUT)
page("contact/", "contact/", "お問い合わせ｜遊べるお寺プロジェクト ご依頼・ご相談", "公式LINEかお問い合わせフォームから。", CONTACT)
