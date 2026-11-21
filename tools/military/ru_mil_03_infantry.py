SECTION = dict(
    id="infantry", title="Пехота", en="Infantry", icon="directions_walk",
    blurb="Infantry organisation from squad to division, battle formations, actions, positions and trenches, individual skills and urban fighting.",
    groups=[
        ("Организация", "Organisation", """
отделе'ние | squad, section
звено' | fire team, element | a part of a squad
взвод | platoon
ро'та | company
батальо'н | battalion
полк | regiment
брига'да | brigade
диви'зия | division
ко'рпус | corps
часть | unit | вое'нная часть: a military unit
соедине'ние | formation (brigade or division level)
объедине'ние | combined-arms command (army level)
подразделе'ние | subunit (squad to battalion)
батаре'я | battery
эскадро'н | squadron (cavalry, recon)
экипа'ж | crew
расчёт | gun or weapon crew
боево'й расчёт | combat crew
гру'ппа | group, team
штурмова'я гру'ппа | assault group
гру'ппа прикры'тия | cover group
гру'ппа захва'та | capture team
огнева'я гру'ппа | fire group
резе'рв | reserve
передово'й отря'д | advance detachment
ба'тальонная такти'ческая гру'ппа | battalion tactical group | БТГр
мотострелко'вая брига'да | motorised rifle brigade
мотострелко'вый полк | motorised rifle regiment
гварде'йский | Guards (an honorific for elite units)
отде'льный | separate, independent (of a unit)
"""),
        ("Боевые порядки и фронт", "Formations and the front", """
боево'й поря'док | battle formation
похо'дный поря'док | march formation
предбое'вой поря'док | pre-battle formation
цепь | skirmish line
коло'нна | column
шере'нга | rank, line
клин | wedge
усту'п | echelon (staggered formation)
фронт | front
фланг | flank
пра'вый фланг | right flank
ле'вый фланг | left flank
стык | junction between units
тыл | rear
пере'дний край | forward edge
пере'дний край оборо'ны | forward edge of the defence
ли'ния соприкоснове'ния | line of contact
ли'ния фро'нта | front line
глубина' | depth
уча'сток | sector
направле'ние | axis, direction
полоса' наступле'ния | zone of advance
полоса' оборо'ны | defensive zone
райо'н | area
райо'н сосредото'чения | assembly area
исхо'дное положе'ние | start line, jump-off position
рубе'ж | line, phase line
рубе'ж развёртывания | deployment line
рубе'ж ата'ки | line of departure
рубе'ж откры'тия огня' | fire-opening line
ключева'я высота' | key height
госпо'дствующая высота' | commanding height
диста'нция | distance, range
интерва'л | interval
"""),
        ("Боевые действия", "Actions", """
бой | battle, engagement, fight
боево'е столкнове'ние | clash, engagement
встре'чный бой | meeting engagement
ата'ка | attack, assault
штурм | storming, assault
контрата'ка | counter-attack
наступле'ние | offensive, advance
оборо'на | defence
оборони'тельный бой | defensive battle
отхо'д | withdrawal
отступле'ние | retreat
контрнаступле'ние | counter-offensive
обхо'д | bypass, turning movement
охва'т | envelopment
окруже'ние | encirclement
проры'в | breakthrough
заса'да | ambush
налёт | raid
рейд | raid
вы'лазка | sortie
пресле'дование | pursuit
задержа'ние | delaying action; detention
ско'вывание | pinning down
отвлека'ющий уда'р | diversionary strike
гла'вный уда'р | main effort, main blow
фланго'вый уда'р | flank attack
огнево'й бой | firefight
бли'жний бой | close combat
рукопа'шный бой | hand-to-hand combat
штыково'й бой | bayonet fight
ночно'й бой | night fighting
бой в гора'х | mountain warfare
бой в пусты'не | desert warfare
бой в зи'мних усло'виях | winter warfare
закрепи'ться | to dig in, to consolidate
удержа'ть | to hold
захвати'ть | to seize, to capture
овладе'ть | to take possession of
подави'ть | to suppress
уничто'жить | to destroy
разгроми'ть | to rout, to defeat
отби'ть ата'ку | to repel an attack
поте'ри | losses, casualties
безвозвра'тные поте'ри | irrecoverable losses (killed, captured, missing)
санита'рные поте'ри | wounded casualties
пле'нный | prisoner of war
плен | captivity
взять в плен | to take prisoner
сдава'ться | to surrender
капитуля'ция | capitulation
"""),
        ("Позиции и укрепления", "Positions and field fortifications", """
пози'ция | position
огнева'я пози'ция | firing position
огнева'я то'чка | firing point
опо'рный пункт | strongpoint
око'п | trench, foxhole
стрелко'вый око'п | rifleman's trench
транше'я | trench
ход сообще'ния | communication trench
блинда'ж | dugout, bunker
укры'тие | shelter, cover
убе'жище | shelter (bomb shelter)
щель | slit trench
яче'йка | fighting position, foxhole
стрелко'вая яче'йка | rifleman's foxhole
пулемётное гнездо' | machine-gun nest
дзот | wood-and-earth firing point (pillbox)
дот | permanent firing point (pillbox)
бру'ствер | parapet
бойни'ца | loophole, embrasure
на'кат | log roofing (of a dugout)
перекры'тая щель | covered slit trench
загражде'ние | obstacle
прово'лочное загражде'ние | wire entanglement
колю'чая про'волока | barbed wire
ёж | hedgehog (anti-tank obstacle)
противота'нковый ров | anti-tank ditch
надо'лбы | dragon's teeth, concrete pyramids
эска'рп | scarp
контрэска'рп | counterscarp
у'зел оборо'ны | defensive node
"""),
        ("Движение и действия бойца", "Movement and individual skills", """
перебе'жка | dash, bound
по'лзти | to crawl
ползко'м | crawling
по-пласту'нски | in the prone crawl
бросо'к | rush, dash
марш | march
марш-бросо'к | forced march
выдвиже'ние | moving up, deployment
рассредото'чение | dispersal
сосредото'чение | concentration, massing
развёртывание | deployment
перегруппиро'вка | regrouping
мане'вр | manoeuvre
мане'вр огнём | manoeuvre by fire
ого'нь и движе'ние | fire and movement
прикры'тие | cover
прикрыва'ть | to cover
маскиро'вка | camouflage
маскиро'вочная сеть | camouflage net
камуфля'ж | camouflage (pattern)
маскиро'вочный костю'м | camouflage suit, ghillie suit
скры'тность | concealment, stealth
ли'ния огня' | line of fire
мёртвая зо'на | dead ground, dead zone
се'ктор обстре'ла | sector of fire
се'ктор наблюде'ния | observation sector
наблюде'ние | observation
наблюда'тель | observer
наблюда'тельный пункт | observation post | НП
дозо'р | patrol, picket
карау'л | guard
часово'й | sentry
сторожево'е охране'ние | outpost security
боево'е охране'ние | combat security
секре'т | listening post, ambush outpost
пост | post
дежу'рство | duty
дежу'рить | to be on duty
обхо'д постов | checking the posts, rounds
"""),
        ("Городской бой", "Urban combat", """
городско'й бой | urban combat
зачи'стка | clearing, sweep
зачи'стка зда'ния | building clearance
гру'ппа обеспе'чения | support team
гру'ппа огнево'й подде'ржки | fire-support team
гру'ппа разгражде'ния | breaching team
кварта'л | city block
перекрёсток | crossroads
подва'л | basement
черда'к | attic
эта'ж | floor
ле'стничная кле'тка | stairwell
ле'стничный пролёт | flight of stairs
око'нный проём | window opening
дверно'й проём | doorway
проём | opening
проло'м | breach, hole
проби'ть сте'ну | to breach a wall
стена' | wall
кры'ша | roof
подъе'зд | entrance (of a block of flats)
двор | yard
у'лица | street
переу'лок | alley
жило'й дом | apartment block
многоэта'жный дом | multi-storey building
промы'шленная зо'на | industrial zone
заво'д | factory
мост | bridge
"""),
    ])
