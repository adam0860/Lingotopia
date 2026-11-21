SECTION = dict(
    id="radio", title="Радиообмен: слова и фразы", en="Radio procedure: words and phrases", icon="record_voice_over",
    blurb="What is actually said on the radio: calling and answering, readability reports, procedure words, corrections, spelling and numbers, reports and requests.",
    groups=[
        ("Вызов и ответ", "Calling and answering", """
Я «Заря», вызываю «Гром» | This is Zarya, calling Grom | the pattern: Я + own callsign, then вызываю + the other callsign
«Гром», я «Заря» | Grom, this is Zarya
«Гром», ответьте «Заре» | Grom, answer Zarya
«Гром», «Гром», я «Заря», как слышите? | Grom, Grom, this is Zarya, how do you read me?
Я «Гром», слушаю вас | This is Grom, I hear you (go ahead)
Я «Гром», на приёме | This is Grom, receiving
«Заря», я «Гром», приём | Zarya, this is Grom, over
Вызываю | I am calling
Отвечаю | I am answering
Слушаю | Go ahead, I am listening
Слушаю вас | Go ahead, I am listening to you
Жду | I am waiting
Жду ответа | I am waiting for an answer
Работаю на передачу | I am transmitting
Перехожу на приём | I am switching to receive
Перехожу на передачу | I am switching to transmit
Приём | Over
Конец связи | Out, end of transmission
Конец | Out
Связь окончена | Communication is finished
Выхожу из связи | I am leaving the net
Ухожу со связи | I am going off the air
Вышел на связь | I have made contact
Ваш позывной? | Your callsign?
Мой позывной | My callsign
Позывной не отвечает | The callsign does not answer
Не отвечает | Does not answer
Отзовитесь | Respond (come in)
Откликнитесь | Respond (answer me)
Всем, всем, всем | To all stations
Всем станциям | To all stations
Внимание | Attention
Внимание, всем | Attention, all
Слушайте меня | Listen to me
Слушайте мою команду | Listen for my command
"""),
        ("Качество связи", "Readability and quality", """
Как слышите? | How do you hear me?
Как меня слышите? | How do you hear me?
Слышу вас хорошо | I hear you well
Слышу вас отлично | I hear you excellently
Слышу вас громко и чётко | I hear you loud and clear
Слышу вас удовлетворительно | I hear you satisfactorily
Слышу вас плохо | I hear you poorly
Слышу вас с помехами | I hear you with interference
Слышу вас слабо | I hear you faintly
Слышу вас на пять | I hear you five by five
Слышу вас на три | I hear you three out of five
Слышу вас на один | I hear you one out of five
Слышимость хорошая | Readability is good
Слышимость плохая | Readability is poor
Слышимость нулевая | I cannot hear you
Не слышу | I do not hear
Вас не слышу | I do not hear you
Вас плохо слышно | You are hard to hear
Вас совсем не слышно | I cannot hear you at all
Вас слышно | I can hear you
Говорите громче | Speak louder
Говорите тише | Speak more quietly
Говорите медленнее | Speak slower
Говорите чётче | Speak more clearly
Говорите ближе к микрофону | Speak closer to the microphone
Вас заглушают помехи | Interference is drowning you out
Вас забивает | You are being jammed
Помехи | Interference
Сильные помехи | Heavy interference
Перебои в связи | The link keeps dropping
Связь неустойчивая | The link is unstable
Связь устойчивая | The link is stable
Связь хорошая | The link is good
Связь плохая | The link is bad
Проверка связи | Radio check
Проверяю связь | I am checking communication
Проверка связи, как слышите? | Radio check, how do you read?
Тест | Test
Раз, два, три | One, two, three (voice check)
"""),
        ("Служебные слова", "Procedure words", """
Понял | Understood
Понял вас | I understand you
Вас понял | I understand you
Вас понял, выполняю | Understood, carrying out
Принял | Received
Принято | Received
Не понял | I did not understand
Вас не понял | I did not understand you
Повторите | Repeat
Повторите, не понял | Repeat, I did not understand
Повторите ещё раз | Repeat once more
Повторите медленнее | Repeat more slowly
Повторяю | I repeat
Повторяю для всех | I repeat for all
Прошу повторить | I request a repeat
Прошу подтвердить | I request confirmation
Подтверждаю | I confirm
Подтвердите | Confirm
Подтверждение | Confirmation
Так точно | Yes, sir
Никак нет | No, sir
Да | Yes
Нет | No
Правильно | Correct
Неправильно | Incorrect
Ошибка | Mistake
Ошибся | I made a mistake
Исправляю | I am correcting
Исправлено | Corrected
Поправка | Correction
Ждите | Wait
Ждать | Wait
Одну минуту | One moment
Продолжайте | Continue
Продолжаю | I continue
Диктуйте | Dictate (go ahead with the text)
Диктую | I am dictating
Записываю | I am writing it down
Записал | I have written it down
Записал, прошу повторить | Written down, request a repeat
Прописью | in words
Цифрами | in figures
По буквам | by letters, spelled
Передаю по буквам | I spell
Передаю цифры | I am sending figures
Передаю координаты | I am sending coordinates
Передаю пароль | I am sending the password
Сообщаю | I am informing
Прошу | I request
Запрашиваю | I request
Разрешите | Request permission
Разрешаю | Permission granted
Не разрешаю | Permission denied
Отставить | Cancel that, as you were
Отменяю | I cancel
Отмена | Cancel
Выполняю | Carrying out
Выполнено | Done
Доложите | Report
Докладываю | I report
Доклад | Report
Срочно | Urgent
Весьма срочно | Very urgent
Немедленно | Immediately
"""),
        ("Тишина в эфире", "Radio discipline", """
Тишина в эфире | Radio silence
Радиомолчание | Radio silence
Соблюдать радиомолчание | Observe radio silence
Нарушение радиомолчания | Breach of radio silence
Молчать в эфире | Keep silent on the air
Не занимайте эфир | Do not occupy the net
Освободите эфир | Clear the net
Эфир занят | The net is busy
Канал занят | The channel is busy
Канал свободен | The channel is free
Прекратить передачу | Stop transmitting
Прекратить разговоры | Stop chatter
Короче | Briefly, shorter
Коротко | Briefly
Говорите коротко | Keep it brief
Не болтать | No chatter
Не называть имён | Do not use names
Не называть координат открытым текстом | Do not give coordinates in the clear
Открытым текстом не передавать | Do not transmit in the clear
Говорите по кодовой таблице | Speak using the code table
Перейти на закрытую связь | Switch to secure communication
Перейти на запасную частоту | Switch to the alternate frequency
Перехожу на запасную частоту | I am switching to the alternate frequency
Перейти на частоту | Switch to frequency
Переходите на запасной канал | Switch to the alternate channel
Включить шифрование | Enable encryption
Работаю без шифра | I am working unencrypted
Противник слушает | The enemy is listening
Противник прослушивает | The enemy is monitoring
Противник глушит | The enemy is jamming
Противник пеленгует | The enemy is direction-finding
Выключить рацию | Switch the radio off
Включить рацию | Switch the radio on
"""),
        ("Донесения и запросы", "Reports and requests", """
Нахожусь в квадрате | I am in grid square
Нахожусь в точке | I am at point
Координаты | Coordinates
Квадрат | Grid square
Высота | Height, hill
Ориентир | Reference point
Азимут | Azimuth
Дальность | Range
Движусь | I am moving
Выдвигаюсь | I am moving out
Занял позицию | I have taken up position
Прибыл | I have arrived
Вышел на рубеж | I have reached the line
Нахожусь на месте | I am in place
Задачу выполнил | Task completed
Задача выполнена | Task completed
К выполнению задачи готов | Ready to carry out the task
Готов | Ready
Готовы | We are ready
Обнаружил противника | I have spotted the enemy
Вижу противника | I see the enemy
Вижу цель | I see the target
Цель вижу | I see the target
Вижу движение | I see movement
Контакт | Contact
Контакт с противником | Contact with the enemy
Противник открыл огонь | The enemy has opened fire
Нахожусь под огнём | I am under fire
Веду бой | I am engaged
Веду огонь | I am firing
Веду огонь по противнику | I am firing on the enemy
Прошу огневую поддержку | I request fire support
Прошу огня | I request fire
Прошу поддержки | I request support
Прошу подкрепление | I request reinforcement
Прошу авиацию | I request air support
Вызываю огонь на себя | I am calling fire on my own position
Огонь по квадрату | Fire on the grid square
Прекратить огонь | Cease fire
Пехота противника | Enemy infantry
Танки противника | Enemy tanks
Бронетехника противника | Enemy armour
Снайпер | Sniper
Вижу вертолёт | I see a helicopter
Вижу беспилотник | I see a drone
Беспилотник над нами | A drone is above us
Воздух | Air! (aircraft or drone overhead)
Прошу огонь по цели | I request fire on the target
Левее ноль-пять | Left zero-five
Правее ноль-пять | Right zero-five
Дальше | Further
Ближе | Closer
Недолёт | Short
Перелёт | Over
Накрытие | On target
Дайте поправку | Give me the correction
Поправка принята | Correction accepted
Повторить огонь | Repeat the fire
Цель поражена | Target destroyed
Задача по цели выполнена | The task on this target is complete
"""),
        ("Потери, помощь и тыл", "Casualties, help and supply", """
Ранен | Wounded
Есть раненые | There are wounded
Раненых | Wounded
Тяжелораненый | Seriously wounded
Лёгкораненый | Lightly wounded
Убит | Killed
Погиб | Killed
Двухсотый | killed (slang, from "cargo 200")
Трёхсотый | wounded (slang, from "cargo 300")
Потери | Casualties
Потери нет | No casualties
Потери есть | There are casualties
Нужна эвакуация | Evacuation is needed
Прошу эвакуацию | I request evacuation
Прошу санитарный транспорт | I request a medical vehicle
Нужен санитар | A medic is needed
Нужна медицинская помощь | Medical help is needed
Боеприпасы на исходе | Ammunition is running low
Боеприпасы закончились | Ammunition is out
Прошу боеприпасы | I request ammunition
Нужны патроны | Need ammunition
Нужны гранаты | Need grenades
Нужна вода | Need water
Нужно питание | Need food
Нужно топливо | Need fuel
Нужен ремонт | Repair needed
Нужна помощь | Help is needed
Прошу помощи | I request help
Нужна поддержка | Support is needed
Подвоз | Resupply
Жду подвоза | I am waiting for resupply
Подвоз прибыл | Resupply has arrived
"""),
        ("Время, числа и условные сигналы", "Time, numbers and conditional signals", """
час «Ч» | H-hour, zero hour
день «Д» | D-day
время «Ч» | H-hour
в час «Ч» | at H-hour
в ноль-ноль | at zero-zero hundred hours
время московское | Moscow time
по московскому времени | by Moscow time
местное время | local time
через десять минут | in ten minutes
через час | in an hour
ровно | exactly
примерно | approximately
ноль | zero
один | one
два | two
три | three
четыре | four
пять | five
шесть | six
семь | seven
восемь | eight
девять | nine
десять | ten
сто | one hundred
двести | two hundred
тысяча | one thousand
ноль-ноль | zero-zero
пять-ноль | five-zero (fifty)
один-ноль-ноль | one-zero-zero (one hundred)
два-пять-ноль | two-five-zero (two hundred fifty)
девять-девять | nine-nine
сигнал | signal
условный сигнал | conditional signal
условная фраза | codeword phrase
кодовая фраза | code phrase
кодовый сигнал | code signal
пароль | password
отзыв | countersign
"""),
    ])
