Исходники картинок превью ссылок (Open Graph), 1200×630.

Пересъёмка после смены H1 или подписи:

    C="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    "$C" --headless=new --hide-scrollbars --window-size=1200,630 --virtual-time-budget=3000 \
      --screenshot="$PWD/static/og/default-ru.png" "file://$PWD/og-src/og-ru.html"
    "$C" --headless=new --hide-scrollbars --window-size=1200,630 --virtual-time-budget=3000 \
      --screenshot="$PWD/static/og/default.png" "file://$PWD/og-src/og-en.html"
