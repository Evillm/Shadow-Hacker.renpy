# Определение персонажей
define a = Character("Али", color="#c8a2c8")
define l = Character("Лейла", color="#a2c8c8")
define y = Character("Ясер", color="#c8c8a2")
define m = Character("Менеджер", color="#a2a2c8")

# Определение изображений и фонов
image bg office = "bg_office.jpg"  # Фон офиса
image bg cafe = "bg_cafe.jpg"  # Фон кафе
image bg home = "bg_home.jpg"  # Фон дома
image bg prison = "bg_prison.jpg"  # Фон тюрьмы
image bg new_life = "bg_new_life.jpg"  # Фон новой жизни

image ali_neutral = "ali_neutral.png"  # Изображение Али (нейтральное)
image ali_shocked = "ali_shocked.png"  # Изображение Али (шокированный)
image ali_determined = "ali_determined.png"  # Изображение Али (решительный)

image leila = "leila.png"  # Изображение Лейлы
image yasser = "yasser.png"  # Изображение Ясера





# Начало игры
label start:

    # Сцена 1: Начало
    scene bg office:
        fit "fill"  
    show ali_neutral at left:
        zoom 0.9  
    m "Али, у нас новое задание. Компания 'Техно Форс' хочет, чтобы мы проверили безопасность их систем. Это рутинная работа, но нам нужно твое лучшее."
    a "Хорошо, я начну сразу."

    scene bg home:
        fit "fill"  
    show ali_shocked at left:
        zoom 0.9  
    a "Что это? 'Оприон'... Похоже, это секретный проект. Почему нам не сказали?"

    # Сцена 2: Открытие
    scene bg home:
        fit "fill"  
    show ali_shocked at left:
        zoom 0.9  
    show leila at right:
        zoom 0.9  
    a "Лейла, ты не поверишь, что я нашел. 'Оприон' — это не просто программа, это оружие."
    l "Что ты имеешь в виду?"
    a "Они могут использовать его для слежки за каждым гражданином страны. Это очень опасно."
    l "Ты уверен? Это может поставить нашу жизнь под угрозу, если они узнают, что мы знаем."
    a "Я должен что-то сделать. Но я не знаю, кому можно доверять."

    # Сцена 3: Противостояние
    scene bg cafe:
        fit "fill"  
    show ali_determined at left:
        zoom 0.9  
    show yasser at right:
        zoom 0.9  
    y "Ты понимаешь, что это может стоить нам жизни, верно?"
    a "Я знаю, но если мы ничего не сделаем, наши свободы будут уничтожены."
    y "Хорошо, я начну писать статью. Но будь осторожен, эти люди не шутят."

    scene bg home:
        fit "fill"  
    show ali_shocked at left:
        zoom 0.9  
    "Али возвращается домой и находит угрозу на своем устройстве."
    "Сообщение: 'Мы знаем, что ты делаешь. Остановись сейчас, или пожалеешь.'"

    menu:
        "Что ты будешь делать?"

        "Продолжить раскрывать заговор с Ясером.":
            jump expose_conspiracy

        "Остановиться и исчезнуть, чтобы сохранить свою безопасность.":
            jump disappear

        "Противостоять коррумпированным в одиночку.":
            jump confront_alone

# Концовка 1: Раскрытие заговора и спасение страны
label expose_conspiracy:
    scene bg home:
        fit "fill"  
    show ali_determined at left:
        zoom 0.9  
    a "Мы сделали это. Мы спасли страну."
    "Но Али знает, что его жизнь больше не будет прежней, он теперь в постоянной опасности."
    return

# Концовка 2: Неудача в доказательстве вины
label fail_to_prove:
    scene bg prison:
        fit "fill"  
    show ali_shocked at left:
        zoom 0.9  
    a "Я пытался, но сила была сильнее меня."
    return

# Концовка 3: Исчезновение и начало новой жизни
label disappear:
    scene bg new_life:
        fit "fill"  
    show ali_neutral at left:
        zoom 0.9  
    a "Может, я и трус, но по крайней мере я все еще жив."
    return

# Концовка 4: Противостояние коррумпированным в одиночку
label confront_alone:
    scene bg home:
        fit "fill"  
    show ali_determined at left:
        zoom 0.9  
    a "Я противостою им в одиночку. Я не могу позволить им победить."
    "Али пытается собрать доказательства, но коррумпированные обнаруживают его, и его арестовывают."
    jump fail_to_prove