# -*- coding: utf-8 -*-
"""Regenerate repo pages with iOS 4-6 style: blue nav bar, icons with
rounded corners + thin shadow. Nav title: index='主頁', depictions=package
name. Back button on depictions reads '主頁' and links to repo root."""
import os

BASE = os.path.expanduser("~/workspace/cydia-repo")

CSS = """<style>
/* iOS 4-6 style nav bar + icons (overrides cytyle where needed) */
/* cytyle hardcodes body{width:320px} and fieldset{max-width:302px}, which leaves
   a pinstripe gap on wider screens - override so pages fill the screen like
   iOS 4 Settings (full-width nav bar + grouped tables). */
html,body{overflow-x:hidden;}
body{margin:0 auto !important;width:auto !important;max-width:568px !important;}
panel>fieldset{max-width:none !important;}
img{max-width:100%;}
.navbar{position:relative;height:44px;background-image:url({REL}icons/navbar-bg@2x.png);background-repeat:repeat-x;background-size:1px 44px;border-bottom:1px solid #2e4a6b;-webkit-box-shadow:0 1px 3px rgba(0,0,0,0.35);box-shadow:0 1px 3px rgba(0,0,0,0.35);text-align:center;}
.navtitle{display:block;margin:0 60px;color:#fff;font-size:18px;font-weight:bold;line-height:44px;text-shadow:0 -1px 0 rgba(0,0,0,0.45);font-family:Helvetica,Arial,sans-serif;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;text-align:center;}
.backbtn{position:absolute;left:8px;top:7px;height:30px;line-height:30px;padding:0 10px 0 18px;color:#fff;font-size:14px;font-weight:bold;text-decoration:none;text-shadow:0 -1px 0 rgba(0,0,0,0.45);font-family:Helvetica,Arial,sans-serif;background-image:url({REL}icons/backbtn@2x.png);background-repeat:no-repeat;background-size:100% 100%;}
/* app icons: iOS rounded rect + thin shadow. Icon files are solid full-bleed
   squares now (no transparent/white corners), CSS only rounds the corners. */
.appicon{-webkit-border-radius:10px;border-radius:10px;-webkit-box-shadow:0 1px 3px rgba(0,0,0,0.45);box-shadow:0 1px 3px rgba(0,0,0,0.45);}
.pkgicon{float:left;width:59px;height:59px;margin:1px 10px 1px 0;}
.depicon{float:left;width:64px;height:64px;margin:1px 12px 1px 0;}
.deprow{min-height:64px;}
.pkgtext{overflow:hidden;word-wrap:break-word;}
.addicon{vertical-align:middle;width:40px;height:40px;margin-right:10px;-webkit-transform:scale(1.12);transform:scale(1.12);}
.repoicon{float:left;width:64px;height:64px;margin:1px 12px 1px 0;}
.reporow{min-height:64px;}
.urlwrap{word-break:break-all;}
</style>"""

CYTYPE = """<style>
@import url(https://cydia.saurik.com/cytyle/style-3163da6b7950852a03d31ea77735f4e1d2ba6699.css);
@import url(http://cydia.saurik.com/cytyle/style-3163da6b7950852a03d31ea77735f4e1d2ba6699.css);
</style>"""

def page(title, nav, body, rel="", extra_head=""):
    return ("<!DOCTYPE html>\n<html><head>\n"
            "    <meta http-equiv=\"content-type\" content=\"text/html; charset=UTF-8\">\n"
            "    <meta charset=\"UTF-8\">\n"
            "    <title>%s</title>\n%s\n%s\n%s\n"
            "    <meta name=\"viewport\" content=\"initial-scale=1.0,width=device-width\">\n"
            "</head>\n<body class=\"pinstripe\">\n%s\n%s\n</body></html>\n"
            % (title, CYTYPE, CSS.replace("{REL}", rel), extra_head, nav, body))

def nav_index():
    return '    <div class="navbar"><span class="navtitle">主頁</span></div>'

def nav_dep(name):
    return ('    <div class="navbar"><a class="backbtn" href="../../">主頁</a>'
            '<span class="navtitle">%s</span></div>' % name)

# ---------------- index ----------------
index_body = """    <panel>
        <fieldset>
            <div>
                <div>
                    <img class="appicon repoicon" src="CydiaIcon.png" width="64" height="64">
                    <div class="pkgtext reporow">
                        <strong>ky's cydia repo</strong><br>
                        <span class="urlwrap" style="font-size: small">https://kyej04u.github.io/repo/</span>
                    </div>
                </div>
            </div>
        </fieldset>
        <fieldset>
            <a href="cydia://url/https://cydia.saurik.com/api/share#?source=https://kyej04u.github.io/repo/">
                <div>
                    <div>
                        <img class="appicon addicon" src="icons/cydia.png" width="40" height="40">Add to Cydia
                    </div>
                </div>
            </a>
        </fieldset>
        <label>套件列表</label>
        <fieldset>
            <a href="depictions/com.kyej04u.pushalertsuppression/">
                <div>
                    <div>
                        <img class="appicon pkgicon" src="icons/tweak.png" width="59" height="59">
                        <div class="pkgtext">
                            PushAlertSuppression<br>
                            <span style="font-size: small">1.0.0 &middot; iOS 4&ndash;6</span><br>
                            隱藏 iPhone 未正確啟用造成的「連接 iTunes 以使用推播通知」提示。
                        </div>
                    </div>
                </div>
            </a>
            <a href="depictions/com.kyej04u.nosimalert/">
                <div>
                    <div>
                        <img class="appicon pkgicon" src="icons/tweak.png" width="59" height="59">
                        <div class="pkgtext">
                            NoSIMAlert<br>
                            <span style="font-size: small">1.0.0 &middot; iOS 3&ndash;6</span><br>
                            隱藏每次重啟都會跳出來的「尚未安裝 SIM 卡」提示。
                        </div>
                    </div>
                </div>
            </a>
            <a href="depictions/com.kyej04u.timeperiodstatusbar/">
                <div>
                    <div>
                        <img class="appicon pkgicon" src="icons/tweak.png" width="59" height="59">
                        <div class="pkgtext">
                            TimePeriodStatusBar<br>
                            <span style="font-size: small">1.0.6 &middot; iOS 6.0&ndash;6.1.x</span><br>
                            在 iOS 6 狀態列顯示更細的時段，像 iPadOS 16+ 一樣。只在 12 小時制、中文語系時啟用。
                        </div>
                    </div>
                </div>
            </a>
            <a href="depictions/com.kyej04u.appinstaller/">
                <div>
                    <div>
                        <img class="appicon pkgicon" src="icons/appinstaller.png" width="59" height="59">
                        <div class="pkgtext">
                            APP Installer<br>
                            <span style="font-size: small">1.0.6 &middot; iOS 3&ndash;6</span><br>
                            在 iPhone 上直接安裝 IPA 檔案，點一下就能裝。內建檔案瀏覽器，也可以從 iFile 用「打開方式」開啟 IPA。
                        </div>
                    </div>
                </div>
            </a>
            <a href="depictions/com.kyej04u.lumixposure/">
                <div>
                    <div>
                        <img class="appicon pkgicon" src="icons/lumixposure.png" width="59" height="59">
                        <div class="pkgtext">
                            LumiXposure (beta)<br>
                            <span style="font-size: small">1.1b1 &middot; iOS 5&ndash;6</span><br>
                            iOS 5-6 內建相機底片模擬插件。
                        </div>
                    </div>
                </div>
            </a>
            <a href="depictions/com.kyej04u.ntpsyncd/">
                <div>
                    <div>
                        <img class="appicon pkgicon" src="icons/tweak.png" width="59" height="59">
                        <div class="pkgtext">
                            NTPSync Daemon<br>
                            <span style="font-size: small">1.0.4 &middot; iOS 3&ndash;5</span><br>
                            修復iOS 3-5內建時間無法從網路伺服器自動同步，每小時從time.apple.com等四個伺服器自動同步時間一次。
                        </div>
                    </div>
                </div>
            </a>
            <a href="depictions/com.kyej04u.ntpsync/">
                <div>
                    <div>
                        <img class="appicon pkgicon" src="icons/tweak.png" width="59" height="59">
                        <div class="pkgtext">
                            NTPSync<br>
                            <span style="font-size: small">1.0 &middot; iOS 3&ndash;5</span><br>
                            修復iOS 3-5內建時間無法從網路伺服器自動同步，透過此app可以手動查詢並更新時間。
                        </div>
                    </div>
                </div>
            </a>
        </fieldset>
    </panel>"""

# ---------------- depictions ----------------
def dep_header(name, meta, icon):
    return """        <fieldset class="dephead">
            <div>
                <div>
                    <img class="appicon depicon" src="../../icons/%s" width="64" height="64">
                    <div class="pkgtext deprow">
                        <strong>%s</strong><br>
                        <span style="font-size: small">%s</span>
                    </div>
                </div>
            </div>
        </fieldset>""" % (icon, name, meta)

# Cydia detection: when a depiction is opened inside Cydia, Cydia already
# provides its own navigation chrome and package header, so the page's own
# nav bar + icon row would just duplicate them. When the same page is opened
# in a phone browser (Safari), there is no Cydia chrome, so the page shows
# its own nav bar + header. Cydia's web view sends a User-Agent containing
# "Cydia"; the script runs in <head> (before body renders) so there is no
# flash of the nav bar inside Cydia.
CYDIA_DETECT = """<script>if(/Cydia/i.test(navigator.userAgent))document.documentElement.className+=' cydia';</script>
<style>.cydia .navbar{display:none!important}.cydia .dephead{display:none!important}</style>"""

def dep_page(name, meta, icon, sections):
    # Depiction pages always render the nav bar + icon/header row in the HTML,
    # but CYDIA_DETECT hides both when the page is viewed inside Cydia. In a
    # regular phone browser they stay visible.
    body = "    <panel>\n"
    body += dep_header(name, meta, icon) + "\n"
    for label, rows in sections:
        if label:
            body += "        <label>%s</label>\n" % label
        body += "        <fieldset>\n"
        for r in rows:
            body += "            <div>\n                <div>\n                    %s\n                </div>\n            </div>\n" % r
        body += "        </fieldset>\n"
    body += "    </panel>"
    return page(name, nav_dep(name), body, rel="../../", extra_head=CYDIA_DETECT)

pages = {}

pages["index.html"] = page("ky's cydia repo", nav_index(), index_body)

pages["depictions/com.kyej04u.pushalertsuppression/index.html"] = dep_page(
    "PushAlertSuppression", "Version 1.0.0 &middot; iOS 4&ndash;6 &middot; Tweaks", "tweak.png",
    [("說明", ["隱藏 iPhone 未正確啟用造成的「連接iTunes以接收\"推播通知\"」提示，支援 iOS 4-6。",
                "此插件只隱藏這個提示，不會修復推播通知本身。"])])

pages["depictions/com.kyej04u.nosimalert/index.html"] = dep_page(
    "NoSIMAlert", "Version 1.0.0 &middot; iOS 3&ndash;6 &middot; Tweaks", "tweak.png",
    [("說明", ["隱藏每次重啟都會跳出來的「尚未安裝 SIM 卡」提示，支援 iOS 3&ndash;6。",
                "只擋「沒有 SIM 卡」這個提示，SIM PIN / PUK 輸入提示不會被擋掉，照常顯示。"])])

time_rows = ["0:00&ndash;0:59　午夜", "1:00&ndash;4:59　凌晨", "5:00&ndash;7:59　清晨",
             "8:00&ndash;10:59　上午", "11:00&ndash;12:59　中午", "13:00&ndash;16:59　下午",
             "17:00&ndash;18:59　傍晚", "19:00&ndash;23:59　晚上"]
pages["depictions/com.kyej04u.timeperiodstatusbar/index.html"] = dep_page(
    "TimePeriodStatusBar", "Version 1.0.6 &middot; iOS 6.0&ndash;6.1.x &middot; Tweaks", "tweak.png",
    [("說明", ["在 iOS 6 狀態列顯示更細的時段，像 iPadOS 16+ 一樣：午夜 / 凌晨 / 清晨 / 上午 / 中午 / 下午 / 傍晚 / 晚上，例如「上午 3:07」→「凌晨 3:07」。只在 12 小時制、中文語系時啟用；英文 AM/PM 不動。在 App 裡面也一樣會顯示。"]),
     ("時段對照", time_rows)])

pages["depictions/com.kyej04u.appinstaller/index.html"] = dep_page(
    "APP Installer", "Version 1.0.6 &middot; iOS 3&ndash;6 &middot; Utilities", "appinstaller.png",
    [("說明", ["在 iPhone 上直接安裝 IPA 檔案，點一下就能裝。支援 iOS 3&ndash;6，內建檔案瀏覽器，也可以從 iFile 用「打開方式」開啟 IPA（需要 iOS 4 以上；在 iOS 3.1.3 上請用內建檔案瀏覽器）。",
                "安裝未簽名的 IPA 需要先裝對應版本的 AppSync；這個 App 本身不會跳過簽名驗證。"])])

pages["depictions/com.kyej04u.lumixposure/index.html"] = dep_page(
    "LumiXposure (beta)", "Version 1.1b1 &middot; iOS 5&ndash;6 &middot; Tweaks", "lumixposure.png",
    [("說明", ["iOS 5-6 內建相機底片模擬插件，目前只在 iPhone 4, 4s, 5，iOS 5.1.1, 6.1.3 上做過測試，請謹慎使用。",
                "Film simulation plugin for the built-in Camera app on iOS 5-6. Currently tested only on iPhone 4, 4s, 5, iOS 5.1.1, 6.1.3. Please use with caution."]),
     ("限制", ["只支援 iPhone / iPod touch，iPad 不能安裝；只支援 iOS 5-6，其他版本不能安裝。",
                "iPhone / iPod touch only - iPad is not supported. iOS 5-6 only - other versions cannot install."]),
     ("版本紀錄", ["1.1b1：新增設定頁面，用戶可以自行選擇底片濃度、顆粒設定，A5以上設備改為採用CoreImage渲染以提升出圖速度。",
                "1.0.55b1：初始發佈版本。"])])

pages["depictions/com.kyej04u.ntpsyncd/index.html"] = dep_page(
    "NTPSync Daemon", "Version 1.0.4 &middot; iOS 3&ndash;5 &middot; Utilities", "tweak.png",
    [("說明", ["修復iOS 3-5內建時間無法從網路伺服器自動同步，每小時從time.apple.com等四個伺服器自動同步時間一次"])])

pages["depictions/com.kyej04u.ntpsync/index.html"] = dep_page(
    "NTPSync", "Version 1.0 &middot; iOS 3&ndash;5 &middot; Utilities", "tweak.png",
    [("說明", ["修復iOS 3-5內建時間無法從網路伺服器自動同步，透過此app可以手動查詢並更新時間"])])

for rel, html in pages.items():
    p = os.path.join(BASE, rel)
    with open(p, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", rel, len(html), "bytes")
