---
title: "Избранные работы"
layout: "work"
seoTitle: "Избранные работы · AnKo Software Labs"
description: "Flutter-приложения Антона Козырева: Zhabby, перенос Android-приложения с Java на Flutter, Mealhub и GreenFeed, Q-Working и Jobline."
kicker: "Работы"
lead: "Мобильные приложения, которые Антон сделал или делал в команде как Flutter-разработчик — в командах заказчиков и работодателей, до и параллельно со студией. Роли указаны как есть, названия заказчиков под NDA не раскрываются."
honesty: "Эти проекты сделаны в роли разработчика в командах других компаний, а не от имени AnKo Software Labs. Страницы в магазинах и на сайтах принадлежат их владельцам."
labels:
  task: "Задача"
  did: "Что сделал"
  stack: "Стек"
  result: "Результат"
  role: "Роль"
  all: "Все работы"
  nda: "Название заказчика не раскрывается (NDA)"
cases:
  - id: "zhabby"
    name: "Zhabby"
    client: "Проектная работа"
    period: "2025"
    role: "Второй Flutter-разработчик, проектная работа"
    mock: "feed"
    summary: "Социальная сеть коротких видео с вознаграждением за активность: персональная лента, загрузка видео, баллы за просмотры, лайки и комментарии, обмен баллов на награды."
    did:
      - "Сверстал все экраны приложения по макетам Figma."
      - "В ряде разделов подключал запросы к API и управление состоянием."
      - "Работал по задачам ведущего разработчика в общей кодовой базе."
    stack: ["Flutter", "Dart", "Dio", "REST API", "Figma"]
    result: "Опубликовано в App Store и Google Play."
    links:
      - { label: "App Store", url: "https://apps.apple.com/us/app/zhabby-%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE-%D0%B8-%D0%BD%D0%B0%D0%B3%D1%80%D0%B0%D0%B4%D1%8B/id6758106499" }
      - { label: "zhabby.info", url: "https://zhabby.info/" }
  - id: "migration"
    name: "Android (Java) → Flutter"
    client: ""
    nda: true
    period: "В работе"
    role: "Единственный мобильный разработчик в продуктовой команде"
    mock: "chat"
    summary: "Приложение исполнителя для платформы подбора персонала. До переноса существовала только нативная Android-версия на Java."
    did:
      - "Перенёс приложение на Flutter без потери функциональности и с обновлённым дизайном."
      - "Выпустил его на iOS и Android из одной кодовой базы."
      - "Развиваю и поддерживаю, перевожу архитектуру на Riverpod."
    stack: ["Flutter", "Dart", "Riverpod", "GoRouter", "Dio", "Firebase"]
    result: "Одна кросс-платформенная кодовая база вместо приложения только под Android; регулярные релизы."
    links: []
  - id: "greenway"
    name: "Mealhub и GreenFeed"
    client: "Гринвэй"
    period: "2022–2023"
    role: "Второй Flutter-разработчик, договор"
    mock: "map"
    summary: "Mealhub — рестораны на карте, бронирование столов и заказ еды. GreenFeed — каталог кормов и расчёт рациона для фермеров."
    did:
      - "Вёрстка экранов по макетам Figma, адаптивная вёрстка под разные устройства."
      - "Работа с картами (Google Maps API) и состоянием приложения."
      - "Интеграция с REST API, исправление ошибок, поддержка и доработки, код-ревью у ведущего разработчика."
    stack: ["Flutter", "Dart", "Dio", "REST API", "Google Maps", "Figma"]
    result: "Оба приложения опубликованы в App Store."
    links:
      - { label: "Mealhub", url: "https://apps.apple.com/ru/app/mealhub/id1640713837" }
      - { label: "GreenFeed", url: "https://apps.apple.com/ru/app/greenfeed/id6453763960" }
  - id: "jobline"
    name: "Q-Working и Jobline"
    client: "Телепорт"
    period: "2023–2024"
    role: "Flutter-разработчик, частичная занятость"
    mock: "list"
    summary: "Две платформы для работы с внешними исполнителями: поиск заказов, сделки, документы и чеки, выплаты."
    did:
      - "С нуля сделал приложение исполнителя Q-Working: регистрация, профиль и услуги, заказы и вознаграждения."
      - "С нуля сделал мобильное приложение Jobline: регистрация исполнителей, документы и чеки по сделкам, выплаты."
    stack: ["Flutter", "Dart", "Dio", "REST API", "Google Maps", "FCM", "WebView"]
    result: "Оба приложения написаны с первого коммита; кейсы опубликованы на сайте Телепорта."
    links:
      - { label: "Кейс Q-Working", url: "https://teleport.run/projects/q-working" }
      - { label: "Кейс Jobline", url: "https://teleport.run/projects/jobline" }
      - { label: "jobline.one", url: "https://jobline.one/" }
cta:
  title: "Нужно что-то похожее?"
  text: "Опишите продукт или задачу в нескольких строках. Ответит инженер, который будет это делать."
---
