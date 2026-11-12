import sys, pathlib
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).parent
FS = (ROOT / "node_modules/@fontsource").as_uri()
PHOTO = pathlib.Path("/home/claude/nick-pham-profile/img/nick-pham.jpg").as_uri()

T = {
 "en": dict(
  role="English Teacher · Examiner · Item Writer · Curriculum Designer",
  contact="Contact", phone="Zalo / Phone", loc="Location", locv="Đồng Nai, Vietnam",
  scores="Scores", ielts="Overall band", toeic="Listening & Reading", tkt="Top band, 3 modules",
  quals="Qualifications",
  q=[("MA in Applied Linguistics","Curtin University, Australia · 2023"),
     ("IELTS 8.0","British Council Vietnam"),
     ("TOEIC 990","IIG Vietnam"),
     ("TKT Band 4/4, 3 modules","Teaching Knowledge Test · British Council"),
     ("VSTEP Speaking & Writing Examiner","Certificate · Levels 3–5"),
     ("VSTEP Item Writer","Certificate · Levels 3–5")],
  profile="Profile",
  summary="English teacher with eight years in the classroom, a certified examiner for Cambridge and VSTEP speaking and writing tests, and a certified VSTEP item writer. I design TOEIC and IELTS courses and build the learning platform my students use every day.",
  roles="Current roles",
  r=[("Current","Co-founder & Academic Director, Duc Thinh Academy","English centre in Đồng Nai. Leads curriculum for IELTS, TOEIC and foundation programmes, teaches, and develops the centre's learning platform."),
     ("Since 2023","Cambridge Speaking Examiner","Starters · Movers · Flyers · KET · PET"),
     ("Since 2023","VSTEP Speaking & Writing Examiner","Levels 3–5 (B1–C1)"),
     ("Certified","VSTEP Item Writer","Writes test items for levels 3–5 (B1–C1)")],
  work="Areas of work",
  w=[("Teaching","English from foundation to advanced levels: general English and IELTS/TOEIC preparation, in class, online and in hybrid classes."),
     ("Assessment","Rating speaking and writing in standardised tests (VSTEP levels 3–5, Cambridge Starters to PET) and writing VSTEP test items."),
     ("Curriculum","Building syllabuses and coursebooks for TOEIC and IELTS preparation courses."),
     ("EdTech","Built an LMS where students follow their class schedule and complete assigned tasks at home, with an online test builder.")],
  how="Teaching approach",
  h=["Teach what actually blocks learners, such as the meaning of question wording that recurs across exams.",
     "Practise in the real exam format; parallel test forms of equal difficulty.",
     "Original reading and listening texts written for each course.",
     "Grammatical accuracy, with Vietnamese explanations where they help.",
     "Technology that serves the lesson: LMS homework and hybrid classes."],
 ),
 "vi": dict(
  role="Giáo viên tiếng Anh · Giám khảo · Người viết đề · Xây dựng chương trình",
  contact="Liên hệ", phone="Zalo / Điện thoại", loc="Địa điểm", locv="Đồng Nai, Việt Nam",
  scores="Điểm thi", ielts="Điểm tổng", toeic="Nghe & Đọc", tkt="Band cao nhất, 3 module",
  quals="Bằng cấp & chứng chỉ",
  q=[("Thạc sĩ Ngôn ngữ học Ứng dụng","Curtin University, Úc · 2023"),
     ("IELTS 8.0","British Council Việt Nam"),
     ("TOEIC 990","IIG Việt Nam"),
     ("TKT Band 4/4, 3 module","Teaching Knowledge Test · British Council"),
     ("Chứng chỉ cán bộ chấm thi Nói – Viết VSTEP","Bậc 3–5"),
     ("Chứng chỉ cán bộ viết tiểu mục đề thi VSTEP","Bậc 3–5")],
  profile="Giới thiệu",
  summary="Giáo viên tiếng Anh với 8 năm đứng lớp, giám khảo được cấp chứng chỉ chấm thi Nói – Viết VSTEP và chấm thi Nói Cambridge, đồng thời là cán bộ viết tiểu mục đề thi VSTEP. Tôi xây dựng chương trình luyện thi TOEIC, IELTS và tự phát triển hệ thống học tập trực tuyến mà học viên sử dụng hằng ngày.",
  roles="Vai trò hiện tại",
  r=[("Hiện tại","Đồng sáng lập & Giám đốc Học thuật, Duc Thinh Academy","Trung tâm Anh ngữ tại Đồng Nai. Phụ trách chương trình IELTS, TOEIC và tiếng Anh nền tảng, trực tiếp giảng dạy và phát triển hệ thống học tập của trung tâm."),
     ("Từ 2023","Giám khảo chấm thi Nói Cambridge","Starters · Movers · Flyers · KET · PET"),
     ("Từ 2023","Cán bộ chấm thi Nói – Viết VSTEP","Bậc 3–5 (B1–C1)"),
     ("Có chứng chỉ","Cán bộ viết tiểu mục đề thi VSTEP","Viết tiểu mục đề thi bậc 3–5 (B1–C1)")],
  work="Lĩnh vực công việc",
  w=[("Giảng dạy","Tiếng Anh từ cơ bản đến nâng cao: tiếng Anh tổng quát và luyện thi IELTS, TOEIC, dạy trực tiếp, trực tuyến và lớp hybrid."),
     ("Khảo thí","Chấm thi Nói và Viết các kỳ thi chuẩn hoá (VSTEP bậc 3–5, Cambridge từ Starters đến PET) và viết tiểu mục đề thi VSTEP."),
     ("Chương trình","Xây dựng chương trình học và giáo trình cho các khoá luyện thi TOEIC, IELTS."),
     ("Công nghệ giáo dục","Tự xây dựng LMS cho phép học viên theo dõi lịch học và làm nhiệm vụ được giao tại nhà, kèm công cụ tạo đề trực tuyến.")],
  how="Phong cách giảng dạy",
  h=["Dạy đúng chỗ học viên bị vướng, chẳng hạn nghĩa của những cách hỏi lặp lại trong đề thi.",
     "Luyện tập đúng định dạng đề thật; đề song song có độ khó tương đương.",
     "Bài đọc, bài nghe được viết mới cho từng khoá học.",
     "Chú trọng độ chính xác ngữ pháp, giải thích bằng tiếng Việt khi cần.",
     "Công nghệ phục vụ bài học: bài tập trên LMS và lớp hybrid."],
 ),
}

def html(lang):
    t = T[lang]
    quals = "".join(f"<li><b>{a}</b><span>{b}</span></li>" for a,b in t["q"])
    roles = "".join(f'<div class="role"><span class="when">{w}</span><div><b>{a}</b><p>{b}</p></div></div>' for w,a,b in t["r"])
    work = "".join(f'<div class="wk"><b>{a}</b><p>{b}</p></div>' for a,b in t["w"])
    how = "".join(f"<li>{x}</li>" for x in t["h"])
    return f"""<!DOCTYPE html><html lang="{lang}"><head><meta charset="utf-8"><title>Phạm Anh Đức (Nick Pham) CV</title>
<link rel="stylesheet" href="{FS}/be-vietnam-pro/400.css"><link rel="stylesheet" href="{FS}/be-vietnam-pro/500.css">
<link rel="stylesheet" href="{FS}/be-vietnam-pro/600.css"><link rel="stylesheet" href="{FS}/newsreader/600.css">
<link rel="stylesheet" href="{FS}/newsreader/700.css"><link rel="stylesheet" href="{FS}/newsreader/400-italic.css">
<link rel="stylesheet" href="{FS}/ibm-plex-mono/500.css">
<style>
@page{{size:A4; margin:0}}
*{{box-sizing:border-box}}
html,body{{margin:0; -webkit-print-color-adjust:exact; print-color-adjust:exact}}
body{{font-family:"Be Vietnam Pro",sans-serif; font-size:9.4pt; line-height:1.45; color:#14213D; width:210mm; height:297mm; display:grid; grid-template-columns:68mm 1fr}}
.side{{background:#14213D; color:#F3F5F9; padding:12mm 8mm 10mm 10mm; position:relative}}
.ph{{display:block; width:34mm; height:42.5mm; object-fit:cover; border:1.6mm solid #fff; border-radius:2.5mm; margin:0 0 6mm}}
.side::before{{content:""; position:absolute; left:5mm; top:0; bottom:0; width:.6pt; background:rgba(210,59,59,.7)}}
.mono{{font-family:"IBM Plex Mono",monospace; font-size:7pt; letter-spacing:.12em; text-transform:uppercase; font-weight:500}}
.mono.h{{color:#FFD54A; display:block; margin:0 0 2.5mm; padding-bottom:1.5mm; border-bottom:.6pt solid rgba(255,255,255,.2)}}
.mono.m{{color:#D23B3B; display:block; margin:0 0 3mm; padding-bottom:1.5mm; border-bottom:.8pt solid #14213D}}
.mono-box{{margin-bottom:5.5mm}}
.mono-box p{{margin:0 0 2mm}}
.mono-box small{{display:block; opacity:.65; font-size:7pt}}
.score{{display:grid; grid-template-columns:auto 1fr; gap:0 3mm; align-items:center; margin-bottom:2.6mm}}
.score b{{font-family:"Newsreader",serif; font-weight:700; font-size:20pt; line-height:1; color:#FFD54A; min-width:16mm}}
.score span{{font-size:8pt; line-height:1.3}}
.score span i{{display:block; font-style:normal; opacity:.65; font-size:7pt}}
.side ul{{list-style:none; margin:0; padding:0}}
.side li{{margin-bottom:2.6mm}}
.side li b{{display:block; font-weight:600; font-size:8.6pt; line-height:1.3}}
.side li span{{opacity:.68; font-size:7.6pt}}
.main{{padding:15mm 13mm 12mm 11mm}}
h1{{font-family:"Newsreader",serif; font-weight:700; font-size:30pt; line-height:1; margin:0}}
.aka{{font-family:"Newsreader",serif; font-style:italic; font-size:13pt; color:#5A6477; margin-top:1mm}}
.role-line{{display:inline-block; margin:3.5mm 0 6mm; font-weight:600; font-size:8.6pt; background:linear-gradient(transparent 55%, #FFD54A 55%); padding:0 1mm}}
section{{margin-bottom:5.5mm}}
.summary{{margin:0; color:#2c3754}}
.role{{display:grid; grid-template-columns:19mm 1fr; gap:3mm; padding:1.8mm 0; border-bottom:.5pt solid #DCE1EA}}
.role:last-child{{border-bottom:0}}
.when{{font-family:"IBM Plex Mono",monospace; font-size:7pt; color:#2F6FDE; font-weight:500; text-transform:uppercase; letter-spacing:.06em; padding-top:.6mm}}
.role b, .wk b{{font-weight:600; font-size:9.4pt}}
.role p, .wk p{{margin:.3mm 0 0; color:#5A6477; font-size:8.6pt}}
.work{{display:grid; grid-template-columns:1fr 1fr; gap:3mm 5mm}}
.wk{{border-left:2pt solid var(--c); padding-left:2.6mm}}
.how{{margin:0; padding-left:4.5mm}}
.how li{{margin-bottom:1.2mm; color:#2c3754}}
.how li::marker{{color:#D23B3B; font-weight:600}}
</style></head><body>
<aside class="side">
  <img class="ph" src="{PHOTO}" alt="">
  <div class="mono-box"><span class="mono h">{t['contact']}</span>
    <p><small>{t['phone']}</small>0962 285 135</p>
    <p><small>Email</small>anhducpham.ftu2@gmail.com</p>
    <p><small>{t['loc']}</small>{t['locv']}</p></div>
  <div class="mono-box"><span class="mono h">{t['scores']}</span>
    <div class="score"><b>8.0</b><span>IELTS<i>{t['ielts']}</i></span></div>
    <div class="score"><b>990</b><span>TOEIC<i>{t['toeic']}</i></span></div>
    <div class="score"><b>4/4</b><span>TKT<i>{t['tkt']}</i></span></div></div>
  <div><span class="mono h">{t['quals']}</span><ul>{quals}</ul></div>
</aside>
<main class="main">
  <h1>Phạm Anh Đức</h1><div class="aka">Nick Pham</div>
  <span class="role-line">{t['role']}</span>
  <section><span class="mono m">{t['profile']}</span><p class="summary">{t['summary']}</p></section>
  <section><span class="mono m">{t['roles']}</span>{roles}</section>
  <section><span class="mono m">{t['work']}</span><div class="work">
    {work.replace('<div class="wk">','<div class="wk" style="--c:#2F6FDE">',1).replace('<div class="wk">','<div class="wk" style="--c:#D23B3B">',1).replace('<div class="wk">','<div class="wk" style="--c:#17977A">',1).replace('<div class="wk">','<div class="wk" style="--c:#D99A00">',1)}
  </div></section>
  <section><span class="mono m">{t['how']}</span><ol class="how">{how}</ol></section>
</main></body></html>"""

out = ROOT / "out"; out.mkdir(exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
    for lang in ("en","vi"):
        f = ROOT / f"cv-{lang}.html"; f.write_text(html(lang), encoding="utf-8")
        pg = b.new_page()
        pg.goto(f.as_uri()); pg.wait_for_timeout(800)
        h = pg.evaluate("document.body.scrollHeight")
        pg.pdf(path=str(out / f"Pham-Anh-Duc-CV-{lang.upper()}.pdf"), format="A4", print_background=True, prefer_css_page_size=True)
        pg.set_viewport_size({"width":794,"height":1123})
        pg.screenshot(path=str(out / f"cv-{lang}.png"), full_page=True)
        print(lang, "height", h)
    b.close()
