"""Unit 36: foreign affairs (textbook Chapter 36): world organizations, diplomacy and treaties, trade vocabulary, relations between regions, si-clauses, ser/estar/haber in the past. All texts are original."""
from dsl_es import *

# ---------------------------------------------------------------------------- 758
L758 = lesson(
    "World organizations: ONU, OMS, UNESCO and CEPAL",
    "La ONU trabaja por la paz y la seguridad del mundo.",
    requires=["organización", "mundial", "salud", "educación", "ciencia", "cultura", "paz", "seguridad", "país", "miembro", "sede", "reunir"],
    cards=[
        card("Four organizations you hear about in the news",
             "These organizations appear often in news about international affairs. The descriptions are short summaries, not complete definitions.",
             tables=[table(["Sigla", "English", "Ejemplo"],
                           [["la ONU", "the United Nations", "La ONU trabaja por la paz y la seguridad del mundo; su sede está en Nueva York."],
                            ["la OMS", "the World Health Organization", "La OMS se ocupa de la salud en todo el mundo; su sede está en Ginebra."],
                            ["la UNESCO", "the UN organization for education, science and culture", "La UNESCO apoya la educación, la ciencia y la cultura; su sede está en París."],
                            ["la CEPAL", "the UN commission for Latin America and the Caribbean", "La CEPAL estudia la economía de América Latina y el Caribe; su sede está en Santiago de Chile."]],
                           say=[2])]),
        card("Useful phrases",
             "Use tener su sede en to say where an organization has its headquarters, and ser miembro de to say that a country belongs to it.",
             examples=[
                 ex("Chile es miembro de la ONU.", "Chile is a member of the UN.", "miembro"),
                 ex("Los países miembros se reúnen en Nueva York.", "The member countries meet in New York.", "miembros"),
                 ex("La OMS tiene su sede en Ginebra.", "The WHO has its headquarters in Geneva.", "sede"),
             ]),
    ],
    exercises=[
        M("What does the OMS work on?", "Health", ["Oil prices", "Policing", "Bank loans"], "OMS = Organización Mundial de la Salud."),
        M("Which organization supports education, science and culture?", "UNESCO", ["OMS", "CEPAL", "A football federation"], "UNESCO."),
        M("Where is the headquarters of the ONU?", "New York", ["Geneva", "Paris", "Santiago de Chile"], "La sede de la ONU está en Nueva York."),
        F("La OMS tiene su ___ en Ginebra.", "sede", ["paz", "salud", "ciencia"], "Sede = headquarters.", tr="The WHO has its headquarters in Geneva."),
        F("La ___ estudia la economía de América Latina y el Caribe.", "CEPAL", ["OMS", "UNESCO", "OTAN"], "CEPAL studies the regional economy.", tr="CEPAL studies the economy of Latin America and the Caribbean."),
        F("Chile es ___ de la ONU.", "miembro", ["sede", "paz", "ciencia"], "Ser miembro de.", tr="Chile is a member of the UN."),
        F("La OMS se ocupa de la ___ en todo el mundo.", "salud", ["cultura", "policía", "guerra"], "Health.", tr="The WHO takes care of health all over the world."),
        F("La UNESCO apoya la educación, la ___ y la cultura.", "ciencia", ["policía", "deuda", "guerra"], "Education, science and culture.", tr="UNESCO supports education, science and culture."),
        F("Los países ___ de la ONU se reúnen en Nueva York.", "miembros", ["sedes", "paces", "ciencias"], "Member countries.", tr="The member countries of the UN meet in New York."),
    ],
)

# ---------------------------------------------------------------------------- 759
L759 = lesson(
    "More organizations: Banco Mundial, INTERPOL, OPEP and OTAN",
    "INTERPOL ayuda a las policías de muchos países a compartir información.",
    requires=["banco", "policía", "petróleo", "alianza", "ayudar", "préstamo", "pobreza", "país", "ejército", "seguridad", "compartir", "prestar"],
    cards=[
        card("Four more names",
             "These four organizations have very different jobs. Notice the verbs in the examples: ayudar, prestar, compartir, exportar.",
             tables=[table(["Sigla", "English", "Ejemplo"],
                           [["el Banco Mundial", "the World Bank", "El Banco Mundial presta dinero y da apoyo a países en desarrollo; su sede está en Washington."],
                            ["INTERPOL", "the international police cooperation organization", "INTERPOL ayuda a las policías de muchos países a compartir información; su sede está en Lyon."],
                            ["la OPEP", "OPEC", "La OPEP reúne a países que exportan petróleo; su sede está en Viena."],
                            ["la OTAN", "NATO", "La OTAN es una alianza militar de defensa colectiva; su sede está en Bruselas."]],
                           say=[2])]),
        card("What each one does not do",
             "Do not mix up their jobs. INTERPOL is not an army: it helps police forces share information. The OTAN is a military alliance, but the Banco Mundial is a bank for development. According to the treaty of the OTAN, an attack on one member is treated as an attack on all, and each member agrees to help, taking the action it considers necessary.",
             examples=[
                 ex("Los miembros de la OTAN se comprometen a ayudarse si uno de ellos sufre un ataque.", "The members of NATO commit to helping one another if one of them is attacked.", "ayudarse"),
                 ex("Los países de la OPEP exportan petróleo.", "The countries of OPEC export oil.", "petróleo"),
             ]),
    ],
    exercises=[
        M("Which organization is a bank for development?", "El Banco Mundial", ["INTERPOL", "La OPEP", "La OTAN"], "Banco = bank."),
        M("What do the OPEP countries have in common?", "They export oil", ["They share one army", "They are all in Europe", "They run a police school"], "OPEP = exporting countries of petroleum."),
        M("Which one is a military alliance?", "La OTAN", ["El Banco Mundial", "INTERPOL", "La UNESCO"], "OTAN."),
        F("El Banco Mundial ___ dinero a países en desarrollo.", "presta", ["prestan", "prestamos", "prestar"], "Singular subject.", tr="The World Bank lends money to developing countries.", lemma="prestar:él"),
        F("INTERPOL ayuda a las ___ de muchos países a compartir información.", "policías", ["monedas", "escuelas", "fábricas"], "Police forces.", tr="INTERPOL helps the police forces of many countries share information."),
        F("La ___ reúne a países que exportan petróleo.", "OPEP", ["OMS", "UNESCO", "CEPAL"], "OPEP.", tr="OPEC brings together countries that export oil."),
        F("La OTAN es una ___ militar de defensa colectiva.", "alianza", ["pobreza", "sede", "salud"], "Alliance.", tr="NATO is a military alliance of collective defense."),
        F("Los países de la OPEP ___ petróleo.", "exportan", ["exporta", "exportamos", "exportar"], "Plural subject.", tr="The countries of OPEC export oil.", lemma="exportar:ellos"),
        F("INTERPOL tiene su sede en Lyon; el Banco Mundial, en ___.", "Washington", ["Viena", "Bruselas", "Ginebra"], "Banco Mundial → Washington.", tr="INTERPOL has its headquarters in Lyon; the World Bank, in Washington."),
    ],
)

# ---------------------------------------------------------------------------- 760
L760 = lesson(
    "Diplomacy: embajador, canciller, cumbre, tratado",
    "El canciller y el embajador hablan con otros gobiernos sobre un tratado.",
    requires=["embajador", "canciller", "cumbre", "tratado", "acuerdo", "convenio", "pacto", "alianza", "gobierno", "ministro", "presidente", "firmar"],
    cards=[
        card("People and documents",
             "El canciller is the foreign minister in many Latin American countries. El embajador represents a country in another country. "
             "A tratado, an acuerdo, a convenio and a pacto are all agreements, but tratado sounds the most formal.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["el canciller", "foreign minister", "El canciller viaja a la cumbre."],
                            ["el embajador", "ambassador", "La embajadora habla con el ministro del país vecino."],
                            ["la cumbre", "summit", "En la cumbre, los presidentes hablan de comercio."],
                            ["el tratado", "treaty", "Los dos países firman un tratado."],
                            ["el acuerdo", "agreement", "Los dos gobiernos llegan a un acuerdo."],
                            ["el convenio", "agreement, convention", "Ese convenio protege a los trabajadores migrantes."],
                            ["el pacto", "pact", "El pacto dura diez años."],
                            ["la alianza", "alliance", "Estos países tienen una alianza económica."]],
                           say=[2])]),
        card("Gender of the nouns",
             "El canciller and el embajador change for women: la canciller and la embajadora. The nouns tratado, acuerdo, convenio and pacto are masculine; la cumbre and la alianza are feminine.",
             examples=[
                 ex("La embajadora firmó el convenio.", "The ambassador (f.) signed the agreement.", "embajadora"),
                 ex("El canciller llegó a la cumbre ayer.", "The foreign minister arrived at the summit yesterday.", "llegó"),
             ]),
    ],
    exercises=[
        M("Who represents a country in another country?", "El embajador", ["El canciller", "El fiscal", "El electorado"], "Embajador = ambassador."),
        M("What is “una cumbre”?", "A meeting of leaders (a summit)", ["A kind of tax", "A police report", "A mountain village"], "Cumbre here = summit."),
        M("Which of these four words is the most formal for an agreement between countries?", "tratado", ["trato", "arreglo", "plan"], "Tratado."),
        F("Los presidentes hablan de comercio en la ___.", "cumbre", ["alianza", "sede", "frontera"], "Summit.", tr="The presidents talk about trade at the summit."),
        F("Los dos gobiernos ___ un tratado de comercio.", "firman", ["firma", "firmamos", "firmar"], "Plural subject.", tr="The two governments sign a trade treaty.", lemma="firmar:ellos"),
        F("La ___ habló con el ministro del país vecino.", "embajadora", ["embajador", "cumbre", "alianza"], "A woman: embajadora.", tr="The ambassador (f.) spoke with the minister of the neighboring country."),
        F("El ___ viaja a la cumbre para hablar en nombre de su país.", "canciller", ["pacto", "convenio", "tratado"], "A person is needed.", tr="The foreign minister travels to the summit to speak on behalf of his country."),
        F("Los dos países tienen una ___ económica.", "alianza", ["cumbre", "embajadora", "sede"], "Economic alliance.", tr="The two countries have an economic alliance."),
        F("Ayer el canciller ___ al aeropuerto con su equipo.", "llegó", ["llegan", "llegaré", "llegar"], "Yesterday → preterite, singular.", tr="Yesterday the foreign minister arrived at the airport with his team.", lemma="llegar:él:pret"),
    ],
)

# ---------------------------------------------------------------------------- 761
L761 = lesson(
    "Verbs of treaties: ratificar, estipular, entrar en vigor",
    "El tratado entra en vigor cuando el Congreso lo ratifica.",
    requires=["firmar", "acordar", "imponer", "ampliar", "enfrentar", "reaccionar", "tratado", "acuerdo", "plazo", "gobierno", "presidente", "sanción"],
    cards=[
        card("From signing to taking effect",
             "First, two governments negociar (negotiate) and acordar (agree on) something. Then they firmar the treaty. In many countries the congress must ratificar it. "
             "The text estipula (stipulates) the rules, and the treaty entra en vigor (takes effect) on a certain date.",
             tables=[table(["Verbo", "English", "Ejemplo"],
                           [["acordar (ue)", "to agree on", "Los gobiernos acuerdan un plazo de cinco años."],
                            ["firmar", "to sign", "Los presidentes firman el tratado."],
                            ["ratificar", "to ratify", "El Congreso ratifica el tratado."],
                            ["estipular", "to stipulate", "El texto estipula las reglas del comercio."],
                            ["entrar en vigor", "to take effect", "El tratado entra en vigor en enero."],
                            ["imponer", "to impose", "Un país impone una sanción a otro."],
                            ["ampliar", "to expand", "Los dos países amplían el acuerdo."]],
                           say=[2])]),
        card("The present tense of acordar and imponer",
             "Acordar changes o → ue (acuerdo, acuerdas, acuerda, acordamos, acordáis, acuerdan). Imponer has an irregular yo form (impongo) and is otherwise regular (impones, impone, imponemos, imponéis, imponen).",
             tables=[table(["Persona", "acordar", "imponer"],
                           [["yo", "acuerdo", "impongo"], ["tú", "acuerdas", "impones"], ["él / ella / usted", "acuerda", "impone"],
                            ["nosotros", "acordamos", "imponemos"], ["vosotros", "acordáis", "imponéis"], ["ellos / ustedes", "acuerdan", "imponen"]],
                           say=[1, 2])]),
    ],
    exercises=[
        M("What does “ratificar” mean?", "To approve officially", ["To cancel", "To sign a check", "To sell"], "Ratificar."),
        M("What does “entrar en vigor” mean?", "To take effect", ["To enter a building", "To be cancelled", "To be rewritten"], "Entrar en vigor."),
        M("Which verb means “to impose”?", "imponer", ["imponerse", "importar", "impedir"], "Imponer."),
        F("Los gobiernos ___ un plazo de cinco años.", "acuerdan", ["acordamos", "acuerda", "acordar"], "Plural subject; o → ue.", tr="The governments agree on a period of five years.", lemma="acordar:ellos"),
        F("Yo ___ las reglas del juego a mis hijos.", "impongo", ["impone", "imponemos", "impones"], "Yo form.", tr="I impose the rules of the game on my children.", lemma="imponer:yo"),
        F("El Congreso ___ el tratado antes de enero del año próximo.", "ratificará", ["ratificaba", "ratificó", "ratificar"], "Del año próximo (future) → future.", tr="Congress will ratify the treaty before January of next year.", lemma="ratificar:él:fut"),
        F("El texto ___ las reglas del comercio entre los dos países.", "estipula", ["estipulan", "estipulamos", "estipular"], "Singular subject.", tr="The text stipulates the rules of trade between the two countries.", lemma="estipular:él"),
        F("El tratado entra en ___ en enero.", "vigor", ["firma", "plazo", "cumbre"], "Entrar en vigor.", tr="The treaty takes effect in January."),
        F("Nosotros ___ el acuerdo con otros temas.", "ampliamos", ["amplía", "amplían", "ampliar"], "Nosotros form.", tr="We expand the agreement with other topics.", lemma="ampliar:nosotros"),
    ],
    verify=(vp("acordar", "acuerdo", "acuerdas", "acuerda", "acordamos", "acordáis", "acuerdan")
            + vp("imponer", "impongo", "impones", "impone", "imponemos", "imponéis", "imponen")),
)

# ---------------------------------------------------------------------------- 762
L762 = lesson(
    "Trade and economy words: arancel, insumo, tasa, plazo",
    "Un arancel es un impuesto sobre los productos que llegan de otro país.",
    requires=["tasa", "plazo", "deuda", "bienestar", "oferta", "demanda", "promedio", "socio", "comercio", "mercado", "inversión", "tesoro"],
    cards=[
        card("Words for talking about trade",
             "These words appear in news about trade agreements and foreign debt.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["el arancel", "tariff", "Un arancel es un impuesto sobre los productos que llegan de otro país."],
                            ["los bienes", "goods", "El comercio de bienes es muy importante."],
                            ["el insumo", "raw material, input", "La fábrica compra insumos en el extranjero."],
                            ["la tasa", "rate", "La tasa de interés del préstamo es alta."],
                            ["el plazo", "period, deadline", "El plazo para pagar es de tres meses."],
                            ["la deuda externa", "foreign debt", "Algunos países tienen una deuda externa grande."],
                            ["el bienestar", "well-being", "El gobierno quiere mejorar el bienestar de la gente."],
                            ["la oferta y la demanda", "supply and demand", "La oferta y la demanda influyen en los precios."],
                            ["el promedio", "average", "El promedio de ingresos subió este año."],
                            ["el socio", "partner", "Brasil es un socio comercial de muchos países."]],
                           say=[2])]),
        card("Hedging in economic news",
             "Reports about the economy often use words like según (according to), algunos, otros and creen que because experts do not always agree. In the examples below, notice how they avoid saying that something is certain.",
             examples=[
                 ex("Según algunos economistas, los aranceles suben los precios.", "According to some economists, tariffs raise prices.", "Según"),
                 ex("Otros expertos creen que protegen la industria nacional.", "Other experts believe that they protect national industry.", "protegen"),
             ]),
    ],
    exercises=[
        M("What is “un arancel”?", "A tax on imported products", ["A bank loan", "A kind of treaty", "A meeting of presidents"], "Arancel = tariff."),
        M("What does “el promedio” mean?", "The average", ["The deadline", "The profit", "The debt"], "Promedio."),
        M("What does “la oferta y la demanda” refer to?", "Supply and demand", ["Borders and visas", "Debt and taxes", "Strikes and protests"], "Oferta = supply; demanda = demand."),
        F("Un ___ es un impuesto sobre los productos que llegan de otro país.", "arancel", ["promedio", "plazo", "socio"], "Tariff.", tr="A tariff is a tax on products that come from another country."),
        F("El ___ para pagar el préstamo es de tres meses.", "plazo", ["arancel", "socio", "bienestar"], "Period.", tr="The period to pay the loan is three months."),
        F("La ___ de interés del préstamo es alta.", "tasa", ["oferta", "deuda", "inversión"], "Rate.", tr="The interest rate on the loan is high."),
        F("La ___ y la demanda influyen en los precios.", "oferta", ["deuda", "tasa", "cumbre"], "Supply.", tr="Supply and demand influence prices."),
        F("Brasil es un ___ comercial de muchos países.", "socio", ["plazo", "arancel", "insumo"], "Partner.", tr="Brazil is a trading partner of many countries."),
        F("El gobierno quiere mejorar el ___ de la gente.", "bienestar", ["arancel", "promedio", "plazo"], "Well-being.", tr="The government wants to improve people’s well-being."),
    ],
)

# ---------------------------------------------------------------------------- 763
L763 = lesson(
    "Regional organizations and trade agreements",
    "Argentina, Brasil, Paraguay y Uruguay fundaron el Mercosur.",
    requires=["libre", "comercio", "acuerdo", "región", "país", "tratado", "firmar", "empleo", "economía", "fundar", "proteger", "trabajador"],
    cards=[
        card("Five regional names",
             "Latin American and Caribbean countries have created several regional organizations. These are only a few of them.",
             tables=[table(["Nombre", "English", "Ejemplo"],
                           [["el Mercosur", "Southern Common Market", "Argentina, Brasil, Paraguay y Uruguay fundaron el Mercosur."],
                            ["la Alianza del Pacífico", "Pacific Alliance", "Chile, Colombia, México y Perú crearon la Alianza del Pacífico."],
                            ["el T-MEC", "the Mexico–United States–Canada trade agreement", "El T-MEC sustituyó a un tratado anterior entre México, Estados Unidos y Canadá."],
                            ["la CARICOM", "the Caribbean Community", "La CARICOM reúne a países y territorios del Caribe."],
                            ["la OEA", "Organization of American States", "La OEA reúne a países de América y tiene su sede en Washington."]],
                           say=[2])]),
        card("What is a free-trade agreement?",
             "A tratado de libre comercio (TLC) lowers or removes tariffs between the countries that sign it. Its defenders say that it increases trade and creates jobs. "
             "Its critics say that it can hurt some workers or industries. Economists do not always agree about the results.",
             examples=[
                 ex("Los defensores dicen que un TLC puede crear empleos.", "Defenders say that a free-trade agreement can create jobs.", "empleos"),
                 ex("Los críticos dicen que puede perjudicar a algunos trabajadores.", "Critics say that it can hurt some workers.", "perjudicar"),
             ]),
    ],
    exercises=[
        M("Which bloc was created by Chile, Colombia, Mexico and Peru?", "La Alianza del Pacífico", ["El Mercosur", "La CARICOM", "La OEA"], "Alianza del Pacífico."),
        M("What does a free-trade agreement (TLC) do?", "It lowers or removes tariffs between the countries that sign it", ["It creates a common army", "It makes all citizens pay the same tax", "It closes all borders"], "Libre comercio."),
        M("Which organization has its headquarters in Washington?", "La OEA", ["La CARICOM", "El Mercosur", "La OPEP"], "OEA → Washington."),
        F("Argentina, Brasil, Paraguay y Uruguay ___ el Mercosur.", "fundaron", ["fundó", "fundamos", "fundar"], "Plural subject, past.", tr="Argentina, Brazil, Paraguay and Uruguay founded Mercosur.", lemma="fundar:ellos:pret"),
        F("Chile, Colombia, México y Perú ___ la Alianza del Pacífico.", "crearon", ["creó", "creamos", "crear"], "Plural subject, past.", tr="Chile, Colombia, Mexico and Peru created the Pacific Alliance.", lemma="crear:ellos:pret"),
        F("Un tratado de ___ comercio baja o elimina aranceles.", "libre", ["libres", "libertad", "liberar"], "Tratado de libre comercio.", tr="A free-trade agreement lowers or removes tariffs."),
        F("Los defensores de un TLC dicen que puede crear ___.", "empleos", ["sanciones", "embajadas", "cumbres"], "Jobs.", tr="Defenders of a free-trade agreement say that it can create jobs."),
        F("Los críticos dicen que un TLC puede ___ a algunos trabajadores.", "perjudicar", ["fundar", "firmar", "votar"], "Hurt.", tr="Critics say that a free-trade agreement can hurt some workers."),
        F("El T-MEC ___ a un tratado anterior.", "sustituyó", ["sustituyen", "sustituimos", "sustituir"], "Singular subject, past.", tr="The T-MEC replaced an earlier treaty.", lemma="sustituir:él:pret"),
    ],
)

# ---------------------------------------------------------------------------- 764
L764 = lesson(
    "Reading: the Senate approves a trade agreement (invented news)",
    "El Senado aprobó ayer un convenio comercial con dos países vecinos.",
    requires=["aprobar", "votar", "voto", "senado", "senador", "presidente", "empleo", "precio", "entrar", "poder", "decir", "traer"],
    cards=[
        card("A short news report (invented)",
             "This news report is invented for practice. It shows how news reports talk about agreements. Notice who says what: the report attributes opinions to the president, to some senators and to experts.",
             examples=[
                 ex("El Senado aprobó ayer un convenio comercial con dos países vecinos.", "Yesterday the Senate approved a trade agreement with two neighboring countries.", "aprobó"),
                 ex("El resultado de la votación fue de ochenta votos a favor y veinte en contra.", "The result of the vote was eighty votes in favor and twenty against.", "votos"),
                 ex("El presidente dijo que el convenio traerá empleos y mejores precios.", "The president said that the agreement will bring jobs and better prices.", "traerá"),
                 ex("Algunos senadores dijeron que el convenio podría perjudicar a los pequeños productores.", "Some senators said that the agreement could hurt small producers.", "podría"),
                 ex("El convenio entrará en vigor el año próximo, si los otros países también lo ratifican.", "The agreement will take effect next year, if the other countries also ratify it.", "entrará"),
                 ex("Los expertos creen que sus efectos todavía están por verse.", "Experts believe that its effects remain to be seen.", "verse"),
             ]),
    ],
    exercises=[
        M("What did the Senate do?", "It approved a trade agreement", ["It rejected a treaty", "It elected a president", "It sanctioned a country"], "Aprobó un convenio."),
        M("What was the vote?", "Eighty in favor, twenty against", ["Twenty in favor, eighty against", "Fifty-fifty", "Unanimous"], "Ochenta votos a favor y veinte en contra."),
        M("What does “están por verse” suggest about the effects?", "Nobody knows yet", ["They are already clear", "They are hidden on purpose", "They were bad"], "Estar por verse = remains to be seen."),
        F("El Senado ___ ayer un convenio comercial.", "aprobó", ["aprueba", "aprobará", "aprobar"], "Yesterday → preterite.", tr="Yesterday the Senate approved a trade agreement.", lemma="aprobar:él:pret"),
        F("El presidente dijo que el convenio ___ empleos y mejores precios.", "traerá", ["trajo", "traen", "traer"], "Reported future.", tr="The president said the agreement will bring jobs and better prices.", lemma="traer:él:fut"),
        F("Algunos senadores ___ que el convenio podría perjudicar a los pequeños productores.", "dijeron", ["dijo", "dijimos", "decir"], "Plural subject, past.", tr="Some senators said that the agreement could hurt small producers.", lemma="decir:ellos:pret"),
        F("El convenio ___ en vigor el año próximo.", "entrará", ["entró", "entraba", "entrar"], "Next year → future.", tr="The agreement will take effect next year.", lemma="entrar:él:fut"),
        F("El resultado de la ___ fue de ochenta votos a favor y veinte en contra.", "votación", ["firma", "cumbre", "sede"], "Vote (the act of voting).", tr="The result of the vote was eighty votes in favor and twenty against."),
        F("Los expertos creen que sus efectos todavía están por ___.", "verse", ["viendo", "visto", "vean"], "Estar por verse.", tr="Experts believe that its effects remain to be seen."),
    ],
)

# ---------------------------------------------------------------------------- 765
L765 = lesson(
    "Sanctions and sovereignty: two points of view",
    "Algunos gobiernos imponen sanciones; otros dicen que violan su soberanía.",
    requires=["sanción", "imponer", "presionar", "población", "derecho", "criticar", "defender", "daño", "gobierno", "política", "levantar", "experto"],
    cards=[
        card("Words for a debate",
             "A sanción is a measure that one government or group of governments imposes on another to put pressure on it. Sanctions are controversial. "
             "Notice the words that mark different opinions: según (according to), algunos, otros, dicen que.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["sancionar", "to sanction", "Un gobierno puede sancionar a empresas o a personas."],
                            ["perjudicar", "to harm", "Algunos dicen que las sanciones perjudican a la población."],
                            ["socavar", "to undermine", "Un gobierno puede decir que otro socava su soberanía."],
                            ["la soberanía", "sovereignty", "La soberanía es el poder de un país para decidir sobre su territorio."],
                            ["la injerencia", "interference", "Una injerencia es entrar en los asuntos de otro país."],
                            ["el alcance", "reach, scope", "Los expertos discuten el alcance de las sanciones."]],
                           say=[2])]),
        card("Both sides",
             "Governments that impose sanctions usually say that they want to press another government to change its policy. Governments that receive sanctions often say that sanctions are illegal or unfair. "
             "Experts disagree about how well sanctions work and whom they affect most.",
             examples=[
                 ex("Según algunos expertos, las sanciones presionan al gobierno.", "According to some experts, sanctions put pressure on the government.", "presionan"),
                 ex("Según otros, también perjudican a la población.", "According to others, they also harm the population.", "perjudican"),
             ]),
    ],
    exercises=[
        M("What is “una sanción” in international news?", "A measure that puts pressure on another government", ["A prize for good behavior", "A kind of summit", "A loan"], "Sanción."),
        M("What is “la injerencia”?", "Interference in another country’s affairs", ["A treaty", "A tax", "A bank loan"], "Injerencia."),
        M("The text says that experts…", "disagree about the effects of sanctions", ["all say sanctions always work", "all say sanctions never work", "have never studied sanctions"], "Both sides."),
        F("Algunos gobiernos ___ sanciones para presionar a otros.", "imponen", ["impone", "imponemos", "imponer"], "Plural subject.", tr="Some governments impose sanctions to put pressure on others.", lemma="imponer:ellos"),
        F("Según algunos expertos, las sanciones ___ al gobierno.", "presionan", ["presiona", "presionamos", "presionar"], "Plural subject.", tr="According to some experts, sanctions put pressure on the government.", lemma="presionar:ellos"),
        F("Otros dicen que también ___ a la población.", "perjudican", ["perjudica", "perjudicamos", "perjudicar"], "Plural subject.", tr="Others say that they also harm the population.", lemma="perjudicar:ellos"),
        F("La ___ es el poder de un país para decidir sobre su territorio.", "soberanía", ["sanción", "cumbre", "deuda"], "Sovereignty.", tr="Sovereignty is the power of a country to decide about its territory."),
        F("Una ___ es entrar en los asuntos de otro país.", "injerencia", ["soberanía", "sanción", "alianza"], "Interference.", tr="Interference is getting involved in another country’s affairs."),
        F("Algunos gobiernos piden que se ___ las sanciones.", "levanten", ["levantan", "levantamos", "levantar"], "Subjunctive after pedir que.", tr="Some governments ask that the sanctions be lifted.", lemma="levantar:ellos:subj"),
    ],
)

# ---------------------------------------------------------------------------- 766
L766 = lesson(
    "China and Russia in Latin America: trade and influence",
    "En las últimas décadas, el comercio entre China y América Latina creció mucho.",
    requires=["socio", "comercio", "inversión", "energía", "infraestructura", "crecimiento", "región", "economía", "analista", "influencia", "presencia", "experto"],
    cards=[
        card("Reporting on a debated topic",
             "News reports on this topic usually describe trade first and then add the opinions of analysts. The sentences below summarize ideas that experts often mention. Opinions differ.",
             examples=[
                 ex("En las últimas décadas, el comercio entre China y América Latina creció mucho.", "In recent decades, trade between China and Latin America grew a lot.", "creció"),
                 ex("China es hoy uno de los principales socios comerciales de varios países sudamericanos.", "China is today one of the main trading partners of several South American countries.", "socios"),
                 ex("En su comercio con China, la región vende sobre todo materias primas y compra productos manufacturados.", "In its trade with China, the region mostly sells raw materials and buys manufactured products.", "materias primas"),
                 ex("China también invierte en energía y en infraestructura.", "China also invests in energy and infrastructure.", "invierte"),
                 ex("Algunos expertos dicen que la relación ofrece oportunidades.", "Some experts say that the relationship offers opportunities.", "oportunidades"),
                 ex("Otros advierten que es desigual, porque la región depende de vender materias primas.", "Others warn that it is unequal, because the region depends on selling raw materials.", "desigual"),
                 ex("El comercio de Rusia con la región es mucho menor.", "Russia’s trade with the region is much smaller.", "menor"),
                 ex("Según varios analistas, Rusia busca ampliar su influencia y diversificar sus socios.", "According to several analysts, Russia seeks to increase its influence and diversify its partners.", "busca"),
             ]),
    ],
    exercises=[
        M("What does the text say about trade between China and Latin America?", "It grew a lot in recent decades", ["It disappeared", "It stayed exactly the same", "It is smaller than Russia’s"], "Creció mucho."),
        M("What does the region sell mostly, according to the text?", "Raw materials", ["Computers", "Tourist visas", "Weapons"], "Materias primas."),
        M("How does the text describe Russia’s trade with the region?", "Much smaller", ["Much larger than China’s", "The same as China’s", "Not mentioned"], "Mucho menor."),
        F("En las últimas décadas, el comercio ___ mucho.", "creció", ["crece", "crecerá", "crecer"], "Past decades → preterite.", tr="In recent decades, trade grew a lot.", lemma="crecer:él:pret"),
        F("China ___ en energía y en infraestructura.", "invierte", ["invierten", "invertimos", "invertir"], "Singular subject.", tr="China invests in energy and infrastructure.", lemma="invertir:él"),
        F("Algunos expertos dicen que la relación ___ oportunidades.", "ofrece", ["ofrecen", "ofrecemos", "ofrecer"], "Singular subject.", tr="Some experts say that the relationship offers opportunities.", lemma="ofrecer:él"),
        F("Otros ___ que es una relación desigual.", "advierten", ["advierte", "advertimos", "advertir"], "Plural subject.", tr="Others warn that it is an unequal relationship.", lemma="advertir:ellos"),
        F("Según varios analistas, Rusia ___ ampliar su influencia.", "busca", ["buscan", "buscamos", "buscar"], "Singular subject.", tr="According to several analysts, Russia seeks to increase its influence.", lemma="buscar:él"),
        F("La región depende de ___ materias primas.", "vender", ["vende", "vendes", "vendido"], "Preposition + infinitive.", tr="The region depends on selling raw materials."),
    ],
)

# ---------------------------------------------------------------------------- 767
L767 = lesson(
    "The United States and Latin America: a long and complex relationship",
    "La relación entre Estados Unidos y América Latina ha tenido épocas de cooperación y épocas de tensión.",
    requires=["relación", "vecino", "histórico", "complejo", "migración", "cooperación", "seguridad", "comercio", "influencia", "amistad", "confianza", "política"],
    cards=[
        card("A relationship with many themes",
             "Experts often mention trade, migration, security and economic cooperation as frequent themes. Many Latin Americans have mixed opinions: some see the United States as a partner, others criticize its influence, and many hold both views at the same time.",
             examples=[
                 ex("La relación entre Estados Unidos y América Latina ha tenido épocas de cooperación y épocas de tensión.", "The relationship between the United States and Latin America has had periods of cooperation and periods of tension.", "ha tenido"),
                 ex("Entre los temas frecuentes están el comercio, la migración y la seguridad.", "Frequent topics include trade, migration and security.", "frecuentes"),
                 ex("Algunos latinoamericanos ven a Estados Unidos como un socio importante.", "Some Latin Americans see the United States as an important partner.", "ven"),
                 ex("Otros critican su influencia en la política de la región.", "Others criticize its influence on the region’s politics.", "critican"),
             ]),
        card("“Nuestra América”",
             "In the nineteenth century, the Cuban writer José Martí published an essay titled “Nuestra América”. In it, he wrote about the identity of the region and about the need for countries to know and respect each other. "
             "Today people still use the phrase when they talk about regional identity, and different writers read it in different ways.",
             examples=[
                 ex("José Martí escribió un ensayo sobre la identidad de la región.", "José Martí wrote an essay about the region’s identity.", "ensayo"),
             ]),
    ],
    exercises=[
        M("Which topics does the text list as frequent in the relationship?", "Trade, migration and security", ["Football, music and food", "Only military topics", "Only tourism"], "Comercio, migración y seguridad."),
        M("What does the text say about Latin American opinions?", "They are mixed", ["Everybody agrees", "Nobody has an opinion", "Only experts have opinions"], "Opiniones mixtas."),
        M("What is “Nuestra América”?", "An essay by José Martí", ["A trade agreement", "A summit of presidents", "A bank"], "Ensayo."),
        F("La relación ha tenido épocas de cooperación y épocas de ___.", "tensión", ["sede", "deuda", "tasa"], "Periods of tension.", tr="The relationship has had periods of cooperation and periods of tension."),
        F("Entre los temas frecuentes están el comercio, la ___ y la seguridad.", "migración", ["sanción", "cumbre", "alianza"], "Migration.", tr="Frequent topics include trade, migration and security."),
        F("Algunos latinoamericanos ___ a Estados Unidos como un socio importante.", "ven", ["ve", "vemos", "ver"], "Plural subject.", tr="Some Latin Americans see the United States as an important partner.", lemma="ver:ellos"),
        F("Otros ___ su influencia en la política de la región.", "critican", ["critica", "criticamos", "criticar"], "Plural subject.", tr="Others criticize its influence on the region’s politics.", lemma="criticar:ellos"),
        F("José Martí ___ un ensayo sobre la identidad de la región.", "escribió", ["escribe", "escribirá", "escribir"], "Historical past.", tr="José Martí wrote an essay about the identity of the region.", lemma="escribir:él:pret"),
        F("Muchas personas tienen opiniones ___ sobre esta relación.", "mixtas", ["mixto", "sede", "mixtos"], "Feminine plural.", tr="Many people have mixed opinions about this relationship."),
    ],
)

# ---------------------------------------------------------------------------- 768
L768 = lesson(
    "Describing relations between countries: adjectives",
    "Las relaciones entre los dos países fueron tormentosas, pero ahora son más confiables.",
    requires=["relación", "futuro", "situación", "estable", "fuerte", "débil", "amistad", "confianza", "paz", "acuerdo", "país", "económico"],
    cards=[
        card("Adjectives from the news",
             "Reports about foreign affairs use these adjectives often. Adjectives ending in -o change for gender and number (duradero, duradera, duraderos, duraderas); most adjectives ending in -e, -l or -z only change for number (confiable, confiables; bilateral, bilaterales; feliz, felices). Adjectives of nationality that end in a consonant, and those ending in -or, add -a for the feminine (español, española; trabajador, trabajadora).",
             tables=[table(["Adjetivo", "English", "Ejemplo"],
                           [["bilateral", "between two countries", "Las relaciones bilaterales son entre dos países."],
                            ["duradero", "lasting", "Los dos países quieren una paz duradera."],
                            ["confiable", "reliable", "Un socio confiable cumple sus promesas."],
                            ["incierto", "uncertain", "El futuro del acuerdo es incierto."],
                            ["precario", "precarious", "La situación económica es precaria."],
                            ["provechoso", "beneficial", "El acuerdo fue provechoso para los dos países."],
                            ["tormentoso", "stormy, conflictive", "Las relaciones fueron tormentosas durante años."],
                            ["vigente", "in force, current", "El tratado vigente protege a los trabajadores."],
                            ["pragmático", "pragmatic", "Un gobierno pragmático busca resultados prácticos."],
                            ["hegemónico", "dominant", "Una potencia hegemónica tiene más poder que otras."],
                            ["geoestratégico", "geostrategic", "Es una zona geoestratégica por su ubicación."],
                            ["inmutable", "unchangeable", "Ninguna política exterior es inmutable."]],
                           say=[2])]),
    ],
    exercises=[
        M("Which adjective means “reliable”?", "confiable", ["duradero", "vigente", "incierto"], "Fiable."),
        M("What does “vigente” mean?", "In force, current", ["Broken", "Secret", "Very old"], "Vigente."),
        M("What does “tormentoso” suggest about relations?", "They were stormy, with many conflicts", ["They were very calm", "They were new", "They were secret"], "Tormentoso."),
        F("Las relaciones entre los dos países fueron ___ durante años.", "tormentosas", ["tormentoso", "tormentosa", "tormentosos"], "Feminine plural.", tr="Relations between the two countries were stormy for years."),
        F("Un socio ___ cumple sus promesas.", "confiable", ["confiables", "inciertos", "precaria"], "Singular, reliable.", tr="A reliable partner keeps his promises."),
        F("El futuro del acuerdo es ___, y nadie sabe qué pasará.", "incierto", ["duradero", "vigente", "provechoso"], "Uncertain.", tr="The future of the agreement is uncertain, and nobody knows what will happen."),
        F("El acuerdo fue ___ para los dos países; los dos ganaron.", "provechoso", ["precario", "tormentoso", "hegemónico"], "Beneficial.", tr="The agreement was beneficial for both countries; both gained."),
        F("Los dos países quieren una paz ___.", "duradera", ["duradero", "duraderas", "duraderos"], "Feminine singular.", tr="Both countries want a lasting peace."),
        F("El tratado ___ protege los derechos de los trabajadores.", "vigente", ["vigentes", "confiable", "precaria"], "Singular, in force.", tr="The treaty in force protects workers’ rights."),
    ],
)

# ---------------------------------------------------------------------------- 769
L769 = lesson(
    "Verbs that change meaning with se",
    "Los gobiernos acordaron un plazo, pero yo no me acuerdo de la fecha.",
    requires=["acordar", "recordar", "alumno", "equipo", "plan", "decisión", "seguridad", "país", "cuadro", "problema", "cumplir", "tratado"],
    cards=[
        card("The same verb, a different meaning",
             "Adding se (me, te, nos…) can change a verb’s meaning a little or a lot. You do not need to memorize every pair now; learn to notice the pronoun and let the context help you.",
             tables=[table(["Verbo", "English", "Ejemplo"],
                           [["acordar", "to agree on", "Los gobiernos acordaron un plazo."],
                            ["acordarse de", "to remember", "Yo no me acuerdo de la fecha."],
                            ["callar a alguien", "to silence someone", "La maestra hizo callar a los alumnos que hablaban."],
                            ["callarse", "to stop talking, to be quiet", "Los alumnos se callan cuando entra la maestra."],
                            ["comprometer", "to endanger, to compromise", "Esa decisión puede comprometer la seguridad del país."],
                            ["comprometerse a", "to commit to", "Los países se comprometen a cumplir el tratado."],
                            ["disputar", "to dispute, to contest", "Dos vecinos disputan el límite de un terreno."],
                            ["disputarse", "to compete for", "Dos equipos se disputan el primer lugar."],
                            ["enmarcar", "to frame", "Ella enmarca el cuadro con un marco de madera."],
                            ["enmarcarse en", "to fit within", "El acuerdo se enmarca en un plan regional."]],
                           say=[2])]),
        card("Present tense with the pronoun",
             "Acordarse is reflexive and has o → ue: me acuerdo, te acuerdas, se acuerda, nos acordamos, os acordáis, se acuerdan.",
             examples=[
                 ex("Nos acordamos de la reunión.", "We remember the meeting.", "acordamos"),
                 ex("¿Te acuerdas de mi nombre?", "Do you remember my name?", "acuerdas"),
             ]),
    ],
    exercises=[
        M("What does “acordarse de” mean?", "To remember", ["To agree on", "To cancel", "To sign"], "Acordarse de = recordar."),
        M("What does “comprometerse a” mean?", "To commit to", ["To endanger", "To argue about", "To forget"], "Comprometerse a."),
        M("What does “enmarcarse en” mean?", "To fit within", ["To put in a picture frame only", "To start", "To leave"], "Enmarcarse."),
        F("Los países ___ a cumplir el tratado.", "se comprometen", ["me comprometo", "te comprometes", "nos comprometemos"], "Third person plural.", tr="The countries commit to complying with the treaty."),
        F("Yo no ___ de la fecha de la cumbre.", "me acuerdo", ["se acuerdan", "te acuerdas", "nos acordamos"], "Yo → me.", tr="I do not remember the date of the summit."),
        F("Los alumnos ___ cuando entra la maestra.", "se callan", ["me callo", "te callas", "nos callamos"], "Third person plural.", tr="The students stop talking when the teacher comes in."),
        F("Dos equipos ___ el primer lugar.", "se disputan", ["me disputo", "te disputas", "nos disputamos"], "Third person plural.", tr="Two teams compete for first place."),
        F("Ese acuerdo ___ en un plan regional.", "se enmarca", ["me enmarco", "te enmarcas", "nos enmarcamos"], "Third person singular.", tr="That agreement fits within a regional plan."),
        F("Los gobiernos ___ un plazo de dos meses.", "acordaron", ["acordamos", "acordó", "acordar"], "Plural subject, past.", tr="The governments agreed on a period of two months.", lemma="acordar:ellos:pret"),
    ],
)

# ---------------------------------------------------------------------------- 770
L770 = lesson(
    "Crime and justice across borders",
    "Si la policía detiene a un prófugo en otro país, ese país puede extraditarlo.",
    requires=["delito", "delincuente", "fiscal", "tribunal", "juzgar", "condena", "culpable", "inocente", "policía", "detener", "justicia", "investigar"],
    cards=[
        card("Words for a legal process",
             "These words appear in reports about crime. The example situation is general; it does not describe a real case.",
             tables=[table(["Español", "English", "Ejemplo"],
                           [["el delito", "crime, offense", "Robar es un delito."],
                            ["el delincuente", "criminal", "La policía busca a un delincuente."],
                            ["el fiscal", "prosecutor", "El fiscal presenta el caso en el tribunal."],
                            ["el tribunal", "court", "El tribunal decide si una persona es culpable."],
                            ["juzgar", "to try, to judge", "El tribunal juzga a los acusados."],
                            ["imputar", "to charge (with a crime)", "El fiscal imputa un delito a una persona."],
                            ["el prófugo", "fugitive", "Un prófugo huye de la justicia."],
                            ["el paradero", "whereabouts", "Se desconoce el paradero del prófugo."],
                            ["la condena", "sentence", "La condena fue de cinco años."],
                            ["cumplir una condena", "to serve a sentence", "Debe cumplir su condena en su país."],
                            ["dar parte a la policía", "to report to the police", "Los testigos dan parte a la policía."],
                            ["extraditar", "to extradite", "Un país puede extraditar a un prófugo."]],
                           say=[2])]),
        card("From arrest to trial",
             "If the police arrest a fugitive in another country, that country may extradite him, that is, send him to the country where he must be tried. Each case follows the laws and treaties of the countries involved. "
             "In many legal systems, a person is considered inocente until a court decides otherwise.",
             examples=[
                 ex("Una persona es inocente hasta que un tribunal decide lo contrario.", "A person is innocent until a court decides otherwise.", "inocente"),
             ]),
    ],
    exercises=[
        M("What is “un prófugo”?", "A person who is running away from justice", ["A judge", "A witness", "A police chief"], "Prófugo."),
        M("What does “cumplir una condena” mean?", "To serve a sentence", ["To announce a verdict", "To pay a tax", "To sign a treaty"], "Cumplir una condena."),
        M("What does “extraditar” mean?", "To send a suspect to the country that wants to try him", ["To free a prisoner", "To fine a driver", "To open a court"], "Extraditar."),
        F("El ___ presenta el caso en el tribunal.", "fiscal", ["paradero", "delito", "prófugo"], "Prosecutor.", tr="The prosecutor presents the case in court."),
        F("El tribunal ___ a los acusados.", "juzga", ["juzgan", "juzgamos", "juzgar"], "Singular subject.", tr="The court tries the accused.", lemma="juzgar:él"),
        F("La policía ___ a un prófugo en otro país.", "detiene", ["detienen", "detenemos", "detener"], "Singular subject.", tr="The police arrest a fugitive in another country.", lemma="detener:él"),
        F("Se desconoce el ___ del prófugo.", "paradero", ["fiscal", "tribunal", "delito"], "Whereabouts.", tr="The whereabouts of the fugitive are unknown."),
        F("Robar es un ___.", "delito", ["paradero", "tribunal", "fiscal"], "Crime.", tr="Stealing is a crime."),
        F("Una persona es ___ hasta que un tribunal decide lo contrario.", "inocente", ["culpable", "prófuga", "condenada"], "Innocent until a court decides.", tr="A person is innocent until a court decides otherwise."),
    ],
)

# ---------------------------------------------------------------------------- 771
L771 = lesson(
    "Set expressions from the news",
    "El ministro hizo hincapié en la importancia del tratado.",
    requires=["cuenta", "tomar", "frente", "salir", "bien", "mal", "decisión", "acuerdo", "importante", "problema", "plan", "anunciar"],
    cards=[
        card("Fixed phrases",
             "These phrases are used all the time in news and speeches. Learn them as whole units.",
             tables=[table(["Expresión", "English", "Ejemplo"],
                           [["hacer hincapié en", "to stress, to emphasize", "El ministro hizo hincapié en la seguridad."],
                            ["darse cuenta de que", "to realize", "Nos dimos cuenta de que el plazo era corto."],
                            ["dar por sentado", "to take for granted", "No debemos dar por sentado que todos están de acuerdo."],
                            ["tener en cuenta", "to keep in mind", "Hay que tener en cuenta los costos."],
                            ["ponerse de acuerdo", "to reach an agreement", "Los dos países se ponen de acuerdo."],
                            ["estrechar relaciones", "to strengthen relations", "Los gobiernos quieren estrechar relaciones."],
                            ["hacer frente a", "to face, to confront", "El país debe hacer frente a la crisis."],
                            ["salir bien / salir mal", "to turn out well / badly", "Si el plan sale mal, buscaremos otra solución."],
                            ["estar por verse", "to remain to be seen", "El resultado está por verse."],
                            ["dar a conocer", "to announce, to make public", "El gobierno dio a conocer su plan."],
                            ["tomar una decisión", "to make a decision", "El presidente tomará una decisión mañana."],
                            ["de aquí en adelante", "from now on", "De aquí en adelante, habrá más controles."]],
                           say=[2])]),
        card("Prepositions to remember",
             "Notice the prepositions: hacer hincapié EN, darse cuenta DE (que), ponerse DE acuerdo, hacer frente A, tener EN cuenta. Say darse cuenta de que, not darse cuenta que, in careful speech and writing.",
             examples=[
                 ex("Me di cuenta de que el plan era difícil.", "I realized that the plan was difficult.", "de que"),
             ]),
    ],
    exercises=[
        M("What does “hacer hincapié en” mean?", "To stress or emphasize", ["To make a mistake", "To sign a form", "To forget"], "Hacer hincapié en."),
        M("What does “estar por verse” mean?", "To remain to be seen", ["To be on TV", "To be hidden", "To be finished"], "Estar por verse."),
        M("What does “dar a conocer” mean?", "To announce", ["To meet someone", "To hide", "To forget"], "Dar a conocer."),
        F("El ministro hizo hincapié ___ la importancia del tratado.", "en", ["de", "a", "con"], "Hacer hincapié en.", tr="The minister stressed the importance of the treaty."),
        F("Nos dimos cuenta ___ que el plazo era corto.", "de", ["en", "a", "por"], "Darse cuenta de que.", tr="We realized that the deadline was short."),
        F("Los dos países se ponen ___ acuerdo.", "de", ["en", "con", "por"], "Ponerse de acuerdo.", tr="The two countries come to an agreement."),
        F("Hay que tener ___ cuenta los costos del plan.", "en", ["de", "a", "con"], "Tener en cuenta.", tr="One has to keep the costs of the plan in mind."),
        F("Todavía no sabemos si el plan saldrá bien; el resultado ___ por verse.", "está", ["es", "hay", "tiene"], "Estar por verse.", tr="We still do not know whether the plan will turn out well; the result remains to be seen.", lemma="estar:él"),
        F("No debemos dar por ___ que todos están de acuerdo.", "sentado", ["sentada", "sentido", "sentir"], "Dar por sentado.", tr="We must not take it for granted that everybody agrees."),
    ],
)

# ---------------------------------------------------------------------------- 772
L772 = lesson(
    "Verbs of policy and conflict, part 1",
    "El presidente aborda el tema de la deuda en la cumbre.",
    requires=["ampliar", "aguantar", "enfrentar", "crisis", "deuda", "pobreza", "precio", "protesta", "economía", "ministerio", "gobierno", "presión"],
    cards=[
        card("Ten verbs for reading the news",
             "These verbs are common in newspapers. Most of them are regular. Ejercer changes c → z in the yo form (shown in the table below), and ampliar puts an accent on the í in some present forms (amplío, amplías, amplía, amplían).",
             tables=[table(["Verbo", "English", "Ejemplo"],
                           [["abordar", "to address, to tackle", "El presidente aborda el tema de la deuda en la cumbre."],
                            ["aguantar", "to put up with", "Muchas familias no pueden aguantar precios tan altos."],
                            ["blindar", "to shield", "El país quiere blindar su economía contra las crisis."],
                            ["contrarrestar", "to counteract", "Un gobierno puede contrarrestar la pobreza con programas sociales."],
                            ["desatar", "to unleash", "La noticia desató una discusión larga."],
                            ["detonar", "to trigger", "La subida de precios detonó protestas."],
                            ["ejercer", "to exert, to practice", "Algunos países ejercen presión económica sobre otros."],
                            ["emitir", "to issue", "El ministerio emite un comunicado."],
                            ["enfrentar", "to face, to confront", "Los gobiernos deben enfrentar la crisis."],
                            ["ampliar", "to expand", "La empresa quiere ampliar su mercado."]],
                           say=[2])]),
        card("The present tense of ejercer",
             "Ejercer changes c → z in the yo form, like vencer: ejerzo. The other forms follow the pattern of -er verbs.",
             tables=[table(["Persona", "ejercer"],
                           [["yo", "ejerzo"], ["tú", "ejerces"], ["él / ella / usted", "ejerce"],
                            ["nosotros", "ejercemos"], ["vosotros", "ejercéis"], ["ellos / ustedes", "ejercen"]],
                           say=[1])]),
    ],
    exercises=[
        M("What does “abordar” mean in the news?", "To address or tackle a topic", ["To get on a boat only", "To ignore", "To close"], "Abordar un tema."),
        M("What does “detonar” mean here?", "To trigger", ["To repair", "To announce", "To delay"], "Detonar."),
        M("What does “contrarrestar” mean?", "To counteract", ["To count again", "To ratify", "To reward"], "Contrarrestar."),
        F("Yo ___ mi profesión de maestra desde hace años.", "ejerzo", ["ejerce", "ejercemos", "ejerces"], "Yo form.", tr="I have practiced my profession as a teacher for years.", lemma="ejercer:yo"),
        F("Algunos países ___ presión económica sobre otros.", "ejercen", ["ejerce", "ejercemos", "ejerzo"], "Plural subject.", tr="Some countries exert economic pressure on others.", lemma="ejercer:ellos"),
        F("El ministerio ___ un comunicado todas las semanas.", "emite", ["emiten", "emitimos", "emitir"], "Singular subject.", tr="The ministry issues a statement every week.", lemma="emitir:él"),
        F("Nosotros ___ el tema de la deuda en la cumbre.", "abordamos", ["aborda", "abordan", "abordar"], "Nosotros form.", tr="We address the topic of the debt at the summit.", lemma="abordar:nosotros"),
        F("La semana pasada, la subida de precios ___ protestas en varias ciudades.", "detonó", ["detona", "detonamos", "detonar"], "Past event.", tr="The rise in prices triggered protests in several cities.", lemma="detonar:él:pret"),
        F("Los gobiernos deben ___ la crisis con medidas claras.", "enfrentar", ["enfrenta", "enfrentan", "enfrentado"], "Infinitive after deber.", tr="Governments must face the crisis with clear measures."),
    ],
    verify=vp("ejercer", "ejerzo", "ejerces", "ejerce", "ejercemos", "ejercéis", "ejercen"),
)

# ---------------------------------------------------------------------------- 773
L773 = lesson(
    "Verbs of policy and conflict, part 2",
    "Varios países respaldan el plan; otros reiteran sus dudas.",
    requires=["plan", "país", "esfuerzo", "daño", "inversión", "crecimiento", "tradición", "siglo", "violencia", "solución", "museo", "ministro"],
    cards=[
        card("Twelve more verbs",
             "These verbs often appear in reports about politics and the economy.",
             tables=[table(["Verbo", "English", "Ejemplo"],
                           [["provenir de", "to come from", "El café proviene de varias regiones del país."],
                            ["remontarse a", "to go back to", "Esta tradición se remonta al siglo dieciocho."],
                            ["repudiar", "to condemn, to reject", "El gobierno repudia la violencia."],
                            ["resguardar", "to protect, to keep safe", "El museo resguarda objetos antiguos."],
                            ["respaldar", "to support", "Varios países respaldan el plan."],
                            ["revertir", "to reverse", "Es difícil revertir el daño ambiental."],
                            ["robustecer", "to strengthen", "Los programas sociales pueden robustecer la economía familiar."],
                            ["socavar", "to undermine", "La corrupción puede socavar la confianza."],
                            ["redoblar", "to redouble", "Los equipos redoblan sus esfuerzos."],
                            ["reiterar", "to repeat, to reaffirm", "El canciller reitera su posición."],
                            ["plantear", "to raise, to propose", "El ministro plantea una solución nueva."],
                            ["potenciar", "to boost", "La inversión puede potenciar el crecimiento."]],
                           say=[2])]),
        card("Three irregular present tenses",
             "Provenir is conjugated like venir: provengo, provienes, proviene, provenimos, provenís, provienen. Robustecer adds z before c in the yo form: robustezco. Revertir has e → ie: revierto, reviertes, revierte, revertimos, revertís, revierten.",
             tables=[table(["Persona", "provenir", "robustecer", "revertir"],
                           [["yo", "provengo", "robustezco", "revierto"], ["tú", "provienes", "robusteces", "reviertes"],
                            ["él / ella / usted", "proviene", "robustece", "revierte"], ["nosotros", "provenimos", "robustecemos", "revertimos"],
                            ["vosotros", "provenís", "robustecéis", "revertís"], ["ellos / ustedes", "provienen", "robustecen", "revierten"]],
                           say=[1, 2, 3])]),
    ],
    exercises=[
        M("What does “respaldar” mean?", "To support", ["To reject", "To ignore", "To delay"], "Respaldar."),
        M("What does “remontarse a” mean?", "To go back in time to", ["To climb a mountain", "To expand", "To cancel"], "Remontarse a."),
        M("What does “socavar” mean?", "To undermine", ["To strengthen", "To announce", "To find"], "Socavar."),
        F("El café ___ de varias regiones del país.", "proviene", ["provienen", "provenimos", "provengo"], "Singular subject.", tr="The coffee comes from several regions of the country.", lemma="provenir:él"),
        F("Varios países ___ el plan.", "respaldan", ["respalda", "respaldamos", "respaldo"], "Plural subject.", tr="Several countries support the plan.", lemma="respaldar:ellos"),
        F("El canciller ___ su posición ante la prensa.", "reitera", ["reiteran", "reiteramos", "reitero"], "Singular subject.", tr="The foreign minister reaffirms his position before the press.", lemma="reiterar:él"),
        F("Los equipos ___ sus esfuerzos para terminar el proyecto.", "redoblan", ["redobla", "redoblamos", "redoblo"], "Plural subject.", tr="The teams redouble their efforts to finish the project.", lemma="redoblar:ellos"),
        F("Ayer el ministro ___ una solución nueva.", "planteó", ["plantea", "plantean", "plantear"], "Yesterday → preterite.", tr="Yesterday the minister proposed a new solution.", lemma="plantear:él:pret"),
        F("Yo ___ mis esfuerzos para reforzar el equipo.", "redoblo", ["redobla", "redoblas", "redoblan"], "Yo form.", tr="I redouble my efforts to reinforce the team.", lemma="redoblar:yo"),
    ],
    verify=(vp("provenir", "provengo", "provienes", "proviene", "provenimos", "provenís", "provienen")
            + vp("robustecer", "robustezco", "robusteces", "robustece", "robustecemos", "robustecéis", "robustecen")
            + vp("revertir", "revierto", "reviertes", "revierte", "revertimos", "revertís", "revierten")),
)

# ---------------------------------------------------------------------------- 774
L774 = lesson(
    "Si-clauses: likely, imaginary, general truths",
    "Si firma el tratado, el comercio aumentará. Si firmara el tratado, el comercio aumentaría.",
    requires=["firmar", "aumentar", "comercio", "tratado", "crisis", "precio", "subir", "embajador", "ministro", "preocupado", "canciller", "gobierno"],
    cards=[
        card("Which tense after si?",
             "The tense of the si-clause depends on what you want to say. Use the present indicative for something likely or for a general truth, and the imperfect subjunctive for something imaginary or unlikely. "
             "Never use the present subjunctive or the conditional right after si in these patterns.",
             tables=[table(["Qué quieres decir", "Ejemplo"],
                           [["Likely future: si + present → future", "Si el gobierno firma el tratado, el comercio aumentará."],
                            ["Imaginary or unlikely: si + imperfect subjunctive → conditional", "Si el gobierno firmara el tratado, el comercio aumentaría."],
                            ["General truth: si + present → present", "Si hay una crisis, los precios suben."],
                            ["Request: si + present → command", "Si ves al embajador, dile que lo espero."],
                            ["Explanation: si + present → es porque…", "Si el ministro reacciona así, es porque está preocupado."]],
                           say=[1])]),
    ],
    exercises=[
        M("Which sentence describes a likely future event?", "Si el gobierno firma el tratado, el comercio aumentará.", ["Si el gobierno firmara el tratado, el comercio aumentaría.", "Si el gobierno firmó el tratado, el comercio aumentaría.", "Si el gobierno firme el tratado, el comercio aumentará."], "Si + present, future."),
        M("Which form is never correct right after si in a condition about the present or future?", "The present subjunctive", ["The present indicative", "The imperfect subjunctive", "The present perfect indicative"], "No present subjunctive after si."),
        M("Which sentence is NOT correct Spanish?", "Si el gobierno firme el tratado, el comercio aumentará.", ["Si el gobierno firma el tratado, el comercio aumentará.", "Si el gobierno firmara el tratado, el comercio aumentaría.", "Si hay una crisis, los precios suben."], "No present subjunctive after si."),
        F("Si el gobierno ___ el tratado, el comercio aumentará.", "firma", ["firme", "firmará", "firmaría"], "Likely future → si + present.", tr="If the government signs the treaty, trade will increase.", lemma="firmar:él"),
        F("Si el gobierno firmara el tratado, el comercio ___.", "aumentaría", ["aumenta", "aumentará", "aumentó"], "Imaginary → conditional.", tr="If the government signed the treaty, trade would increase.", lemma="aumentar:él:cond"),
        F("Si hay una crisis, los precios ___ casi siempre.", "suben", ["subirán", "suban", "subirían"], "General truth → present.", tr="If there is a crisis, prices almost always go up.", lemma="subir:ellos"),
        F("Si ves al embajador, ___ que lo espero.", "dile", ["dijiste", "dirías", "dijera"], "Request → command.", tr="If you see the ambassador, tell him that I am waiting for him."),
        F("Si el ministro reacciona así, ___ porque está preocupado.", "es", ["sea", "fuera", "ser"], "Explanation: es porque.", tr="If the minister reacts that way, it is because he is worried.", lemma="ser:él"),
        F("Si yo ___ canciller, firmaría el tratado hoy.", "fuera", ["soy", "seré", "sería"], "Imaginary → imperfect subjunctive.", tr="If I were foreign minister, I would sign the treaty today.", lemma="ser:yo:isubj"),
    ],
)

# ---------------------------------------------------------------------------- 775
L775 = lesson(
    "Si + present: real possibilities and what will happen",
    "Si el Congreso ratifica el tratado, el presidente lo firmará.",
    requires=["aprobar", "pagar", "ganar", "salir", "subir", "llegar", "cumplir", "ayudar", "tratado", "plazo", "deuda", "economía"],
    cards=[
        card("Real conditions",
             "When the condition is real or likely, use si + present indicative. The result can be a future, a present, or a command. "
             "The order of the clauses does not change the meaning: Si llueve, no salgo. = No salgo si llueve.",
             tables=[table(["Si + presente", "Resultado"],
                           [["Si el Congreso ratifica el tratado,", "el presidente lo firmará."],
                            ["Si el país paga la deuda a tiempo,", "tendrá más crédito."],
                            ["Si la economía crece,", "habrá más empleos."],
                            ["Si llegas temprano,", "ayúdame con los documentos."],
                            ["Si no cumplen el plazo,", "pagan una multa."]],
                           say=[0, 1])],
             examples=[
                 ex("Habrá más empleos si la economía crece.", "There will be more jobs if the economy grows.", "crece"),
             ]),
    ],
    exercises=[
        M("Which sentence is a real possibility?", "Si el país paga la deuda a tiempo, tendrá más crédito.", ["Si el país pagara la deuda a tiempo, tendría más crédito.", "Si el país pagó la deuda a tiempo, tendría más crédito.", "Si el país pague la deuda a tiempo, tendrá más crédito."], "Si + present, future."),
        M("Which sentence puts the condition second?", "Habrá más empleos si la economía crece.", ["Si la economía crece, habrá más empleos.", "Si hay empleos, la economía crece.", "Si no hay empleos, la economía no crece."], "Condition at the end."),
        M("What can follow a si + present clause?", "A future, a present or a command", ["Only the conditional", "Only the past", "Only the subjunctive"], "Three results."),
        F("Mañana, si el Congreso ___ el tratado, el presidente lo firmará.", "ratifica", ["ratifique", "ratificara", "ratificaría"], "Real condition → present.", tr="Tomorrow, if Congress ratifies the treaty, the president will sign it.", lemma="ratificar:él"),
        F("Si el país paga la deuda a tiempo, ___ más crédito.", "tendrá", ["tenga", "tuviera", "tuvo"], "Result → future.", tr="If the country pays its debt on time, it will have more credit.", lemma="tener:él:fut"),
        F("Si la economía crece, ___ más empleos.", "habrá", ["hubo", "había", "haya"], "Result → future.", tr="If the economy grows, there will be more jobs.", lemma="haber:él:fut"),
        F("Si llegas temprano, ___ con los documentos.", "ayúdame", ["ayudaría", "ayudaste", "ayudabas"], "Request → command.", tr="If you arrive early, help me with the documents."),
        F("Si los precios ___ mucho, la gente compra menos.", "suben", ["suban", "subieran", "subirían"], "General truth → present.", tr="If prices rise a lot, people buy less.", lemma="subir:ellos"),
        F("Si ellos no cumplen el plazo, ___ una multa.", "pagan", ["pague", "pagaron", "pagaban"], "Real rule → present.", tr="If they do not meet the deadline, they pay a fine.", lemma="pagar:ellos"),
    ],
    verify=vpf("tener", "tendré", "tendrás", "tendrá", "tendremos", "tendréis", "tendrán"),
)

# ---------------------------------------------------------------------------- 776
L776 = lesson(
    "Si + imperfect subjunctive: imaginary or unlikely situations",
    "Si el gobierno bajara los aranceles, los productos serían más baratos.",
    requires=["bajar", "ser", "tener", "poder", "querer", "vivir", "haber", "impuesto", "barato", "gobierno", "viajar", "país"],
    cards=[
        card("Imaginary conditions",
             "For situations that are imaginary, contrary to fact, or very unlikely, use si + imperfect subjunctive, and then the conditional. Many speakers also use this pattern to be polite or cautious.",
             tables=[table(["Si + imperfecto de subjuntivo", "Condicional"],
                           [["Si el gobierno bajara los aranceles,", "los productos serían más baratos."],
                            ["Si yo tuviera más tiempo,", "viajaría a otros países."],
                            ["Si pudiéramos elegir,", "viviríamos cerca del mar."],
                            ["Si tú fueras embajador,", "¿qué harías?"],
                            ["Si hubiera menos deuda,", "habría más dinero para escuelas."]],
                           say=[0, 1])],
             examples=[
                 ex("¿Qué dirías si fueras canciller?", "What would you say if you were foreign minister?", "fueras"),
             ]),
    ],
    exercises=[
        M("Which sentence describes an imaginary situation?", "Si el gobierno bajara los aranceles, los productos serían más baratos.", ["Si el gobierno baja los aranceles, los productos serán más baratos.", "Si el gobierno bajó los aranceles, los productos eran más baratos.", "Cuando el gobierno baja los aranceles, los productos son más baratos."], "Imperfect subjunctive + conditional."),
        M("Which form follows si in an imaginary situation?", "The imperfect subjunctive", ["The conditional", "The future", "The present subjunctive"], "Si + imperfect subjunctive."),
        M("Which is the correct main verb for “Si yo tuviera más tiempo, ___ a otros países.”?", "viajaría", ["viajo", "viajé", "viajaré"], "Conditional."),
        F("Si el gobierno ___ los aranceles, los productos serían más baratos.", "bajara", ["baja", "bajaría", "bajará"], "Imaginary → imperfect subjunctive.", tr="If the government lowered tariffs, products would be cheaper.", lemma="bajar:él:isubj"),
        F("Si yo ___ más tiempo, viajaría a otros países.", "tuviera", ["tengo", "tendría", "tuve"], "Imaginary → imperfect subjunctive.", tr="If I had more time, I would travel to other countries.", lemma="tener:yo:isubj"),
        F("Si nosotros ___ elegir, viviríamos cerca del mar.", "pudiéramos", ["podemos", "podríamos", "pudimos"], "Imaginary → imperfect subjunctive.", tr="If we could choose, we would live near the sea.", lemma="poder:nosotros:isubj"),
        F("Si tú ___ embajador, ¿qué harías?", "fueras", ["eres", "serías", "fuiste"], "Imaginary → imperfect subjunctive.", tr="If you were an ambassador, what would you do?", lemma="ser:tú:isubj"),
        F("Si hubiera menos deuda, ___ más dinero para escuelas.", "habría", ["hay", "habrá", "había"], "Result → conditional.", tr="If there were less debt, there would be more money for schools.", lemma="haber:él:cond"),
        F("Si ellos ___ comprar más, las fábricas producirían más.", "quisieran", ["quieren", "querrían", "quisieron"], "Imaginary → imperfect subjunctive.", tr="If they wanted to buy more, the factories would produce more.", lemma="querer:ellos:isubj"),
    ],
    verify=(vpq("tener", "tuviera", "tuvieras", "tuviera", "tuviéramos", "tuvierais", "tuvieran")
            + vpq("querer", "quisiera", "quisieras", "quisiera", "quisiéramos", "quisierais", "quisieran")),
)

# ---------------------------------------------------------------------------- 777
L777 = lesson(
    "More uses of si: whether, habits, and ¿sí o no?",
    "No sé si el ministro viaja mañana. Si llovía, nos quedábamos en casa.",
    requires=["saber", "preguntar", "viajar", "llover", "quedar", "salir", "llegar", "reunión", "tarde", "casa", "vez", "siempre"],
    cards=[
        card("Si has other jobs",
             "Si can mean “whether” in an indirect question: No sé si viene. It can introduce a habit in the past with the imperfect: Si llovía, nos quedábamos en casa. "
             "Do not confuse si (if, whether) with sí (yes), which has an accent.",
             tables=[table(["Uso", "Ejemplo"],
                           [["whether", "No sé si el ministro viaja mañana."],
                            ["whether", "Me pregunto si el plan funcionará."],
                            ["past habit (every time)", "Si llovía, nos quedábamos en casa."],
                            ["past habit (every time)", "Si llegaba tarde, mi jefe no decía nada."],
                            ["yes", "—¿Vienes? —Sí, voy."]],
                           say=[1])]),
        card("A preview",
             "There is one more pattern with si, for things that did not happen in the past: si + pluperfect subjunctive (Si hubiera llegado antes, …). You will study it later.",
             examples=[
                 ex("Le pregunté si venía a la reunión.", "I asked her whether she was coming to the meeting.", "si"),
             ]),
    ],
    exercises=[
        M("What does “si” mean in “No sé si viene”?", "Whether", ["If only", "Yes", "So"], "Indirect question."),
        M("Which word means “yes”?", "sí", ["si", "se", "su"], "The accent marks “yes”."),
        M("Which sentence describes a habit in the past?", "Si llovía, nos quedábamos en casa.", ["Si llueve, nos quedaremos en casa.", "Si lloviera, nos quedaríamos en casa.", "Si llueva, nos quedamos en casa."], "Imperfect + imperfect."),
        F("No sé ___ el ministro viaja mañana.", "si", ["sí", "se", "sé"], "Whether: no accent.", tr="I do not know whether the minister is traveling tomorrow."),
        F("—¿Vienes a la reunión? —___, voy.", "Sí", ["Si", "Se", "Sé"], "Yes: accent.", tr="—Are you coming to the meeting? —Yes, I am."),
        F("Cuando era niño, si llovía, nos ___ en casa.", "quedábamos", ["quedaremos", "quedamos", "quedemos"], "Past habit → imperfect.", tr="When I was a child, if it rained, we stayed at home.", lemma="quedar:nosotros:impf"),
        F("Si mi jefe ___ tarde, no decía nada.", "llegaba", ["llegó", "llegue", "llegará"], "Past habit → imperfect.", tr="If my boss arrived late, he did not say anything.", lemma="llegar:él:impf"),
        F("Me pregunto si el plan ___.", "funcionará", ["funcionó", "funcione", "funcionaba"], "Future uncertainty.", tr="I wonder whether the plan will work.", lemma="funcionar:él:fut"),
        F("Le pregunté si ___ a la reunión.", "venía", ["vendrá", "venga", "vino"], "Reported question in the past.", tr="I asked her whether she was coming to the meeting.", lemma="venir:él:impf"),
    ],
    verify=vpi("llegar", "llegaba", "llegabas", "llegaba", "llegábamos", "llegabais", "llegaban"),
)

# ---------------------------------------------------------------------------- 778
L778 = lesson(
    "Estar in the past: imperfect or preterite?",
    "Raúl estaba en la sala. Raúl estuvo dos horas en la sala.",
    requires=["estar", "triste", "enfermo", "sala", "hora", "ayer", "noche", "estudiar", "semana", "reunión", "teléfono", "sonar"],
    cards=[
        card("Estar in the past",
             "Most of the time estar in the past is imperfect: it describes where someone was, how someone felt, or what was going on. "
             "Use the preterite when you give a bounded period of time (dos horas, varios días) or a specific moment.",
             tables=[table(["Imperfecto: estaba", "Pretérito: estuvo"],
                           [["Raúl estaba en la sala.", "Raúl estuvo dos horas en la sala."],
                            ["Dora estaba triste.", "Dora estuvo triste por varios días."],
                            ["Mi trabajo estaba cerca del centro.", "Ayer estuvimos en la oficina."],
                            ["La sopa estaba caliente.", "Anoche Raúl estuvo en la biblioteca de las ocho a las diez."]],
                           say=[0, 1]),
                    table(["Persona", "Imperfecto", "Pretérito"],
                          [["yo", "estaba", "estuve"], ["tú", "estabas", "estuviste"], ["él / ella / usted", "estaba", "estuvo"],
                           ["nosotros", "estábamos", "estuvimos"], ["vosotros", "estabais", "estuvisteis"], ["ellos / ustedes", "estaban", "estuvieron"]],
                          say=[1, 2])]),
    ],
    exercises=[
        M("Which tense is usual for location or a state of being in the past?", "The imperfect", ["The preterite", "The future", "The present subjunctive"], "Estaba."),
        M("Which tense is usual when you give a period of time, like “two hours”?", "The preterite", ["The imperfect", "The conditional", "The future"], "Estuvo + period of time."),
        M("Which sentence tells how long Dora was sad?", "Dora estuvo triste por varios días.", ["Dora estaba triste.", "Dora está triste.", "Dora estará triste."], "Period of time → preterite."),
        F("El embajador ___ dos horas en la cumbre.", "estuvo", ["estaba", "estará", "esté"], "Period of time → preterite.", tr="The ambassador was at the summit for two hours.", lemma="estar:él:pret"),
        F("Cuando llegué, el embajador ___ en la sala.", "estaba", ["estuvo", "estará", "estuviera"], "Background → imperfect.", tr="When I arrived, the ambassador was in the room.", lemma="estar:él:impf"),
        F("Cuando era joven, mi trabajo ___ cerca del centro.", "estaba", ["estuvo", "estaré", "estén"], "Description → imperfect.", tr="When I was young, my job was near downtown.", lemma="estar:él:impf"),
        F("El año pasado, Dora ___ triste por varios días.", "estuvo", ["estaba", "estará", "esté"], "Period of time → preterite.", tr="Last year Dora was sad for several days.", lemma="estar:él:pret"),
        F("Cuando el teléfono sonó, yo ___ en la reunión.", "estaba", ["estuve", "estaré", "esté"], "Background → imperfect.", tr="When the phone rang, I was in the meeting.", lemma="estar:yo:impf"),
        F("Anoche, Raúl y Dora ___ en la biblioteca de las ocho a las diez.", "estuvieron", ["estaban", "estarán", "estén"], "Specific time span → preterite.", tr="Last night Raúl and Dora were in the library from eight to ten.", lemma="estar:ellos:pret"),
    ],
    verify=(vpp("estar", "estuve", "estuviste", "estuvo", "estuvimos", "estuvisteis", "estuvieron")
            + vpi("estar", "estaba", "estabas", "estaba", "estábamos", "estabais", "estaban")),
)

# ---------------------------------------------------------------------------- 779
L779 = lesson(
    "Ser in the past: imperfect or preterite?",
    "Mi abuelo era generoso. Fue alcalde durante diez años.",
    requires=["ser", "abuelo", "alcalde", "generoso", "mesa", "madera", "edificio", "banco", "capital", "año", "ciudad", "presidente"],
    cards=[
        card("Ser in the past",
             "Use the imperfect to describe people, places and things as they used to be, to say what they were made of or whose they were, and to identify something in the past. "
             "Use the preterite when you give a bounded period of time, a specific time, or a short biographical statement.",
             tables=[table(["Imperfecto: era", "Pretérito: fue"],
                           [["Mi abuelo era muy generoso.", "Mi abuelo fue alcalde durante diez años."],
                            ["Las mesas eran de madera.", "Esa ciudad fue la capital durante veinte años."],
                            ["Ese edificio era un banco.", "Ella fue maestra y después presidenta."],
                            ["Nosotros éramos vecinos.", "El descubrimiento fue histórico."]],
                           say=[0, 1]),
                    table(["Persona", "Imperfecto", "Pretérito"],
                          [["yo", "era", "fui"], ["tú", "eras", "fuiste"], ["él / ella / usted", "era", "fue"],
                           ["nosotros", "éramos", "fuimos"], ["vosotros", "erais", "fuisteis"], ["ellos / ustedes", "eran", "fueron"]],
                          say=[1, 2])]),
    ],
    exercises=[
        M("Which tense do you use for a period of time, like “for ten years”?", "The preterite", ["The imperfect", "The future", "The conditional"], "Fue + period of time."),
        M("Which tense describes what something was made of?", "The imperfect", ["The preterite", "The future", "The present subjunctive"], "Eran de madera."),
        M("Which sentence gives a short biography?", "Ella fue maestra y después presidenta.", ["Ella era maestra.", "Ella es presidenta.", "Ella será maestra."], "Biographical → preterite."),
        F("Cuando yo era niña, mi abuelo ___ muy generoso.", "era", ["fueron", "fui", "será"], "Description in the past.", tr="When I was a girl, my grandfather was very generous.", lemma="ser:él:impf"),
        F("Mi abuelo ___ alcalde durante diez años.", "fue", ["eran", "fueron", "será"], "Period of time → preterite.", tr="My grandfather was mayor for ten years.", lemma="ser:él:pret"),
        F("Las mesas ___ de madera.", "eran", ["era", "serán", "sean"], "Material → imperfect.", tr="The tables were made of wood.", lemma="ser:ellos:impf"),
        F("Esa ciudad ___ la capital durante veinte años.", "fue", ["fueron", "será", "sea"], "Period of time → preterite.", tr="That city was the capital for twenty years.", lemma="ser:él:pret"),
        F("De niños, nosotros ___ vecinos.", "éramos", ["eran", "seremos", "somos"], "Description in the past.", tr="As children, we were neighbors.", lemma="ser:nosotros:impf"),
        F("El descubrimiento ___ histórico para el país.", "fue", ["fueron", "será", "sea"], "Evaluation of a completed event.", tr="The discovery was historic for the country.", lemma="ser:él:pret"),
    ],
    verify=(vpp("ser", "fui", "fuiste", "fue", "fuimos", "fuisteis", "fueron")
            + vpi("ser", "era", "eras", "era", "éramos", "erais", "eran")),
)

# ---------------------------------------------------------------------------- 780
L780 = lesson(
    "Reading: a trade story with ser, estar and haber (invented)",
    "Hace cien años, el comercio entre los dos países era mínimo porque los puertos estaban cerrados.",
    requires=["comercio", "puerto", "cerrado", "mercado", "crisis", "año", "gobierno", "acuerdo", "importante", "preocupado", "precio", "alto"],
    cards=[
        card("An invented story",
             "This short history is invented for practice. It does not describe real countries. Notice how ser, estar and haber change between the imperfect (background) and the preterite (events, periods, specific moments). "
             "For haber, había = there was or there were (background), hubo = there was or there were (an event).",
             examples=[
                 ex("Hace cien años, el comercio entre los dos países era mínimo porque los puertos estaban cerrados.", "A hundred years ago, trade between the two countries was minimal because the ports were closed.", "era"),
                 ex("Había pocos productos en los mercados.", "There were few products in the markets.", "Había"),
                 ex("Después hubo una crisis económica que duró varios años.", "Afterward there was an economic crisis that lasted several years.", "hubo"),
                 ex("Entonces la gente estaba preocupada y los precios estaban muy altos.", "At that time people were worried and prices were very high.", "estaba"),
                 ex("En mil novecientos cincuenta, los dos gobiernos firmaron un acuerdo.", "In nineteen fifty, the two governments signed an agreement.", "firmaron"),
                 ex("Ese acuerdo fue importante para los dos países.", "That agreement was important for both countries.", "fue"),
                 ex("Durante veinte años, el puerto principal estuvo abierto.", "For twenty years, the main port was open.", "estuvo"),
             ]),
        card("Haber in the past",
             "Haber has these two forms for “there was / there were”: había (imperfect) and hubo (preterite). Both stay singular: Había muchos productos. Hubo dos crisis.",
             tables=[table(["Imperfecto", "Pretérito"], [["Había pocos productos.", "Hubo una crisis."]], say=[0, 1])]),
    ],
    exercises=[
        M("What does the story say about the ports a hundred years ago?", "They were closed", ["They were open every day", "They were new", "They were destroyed"], "Los puertos estaban cerrados."),
        M("Which sentence gives background?", "Había pocos productos en los mercados.", ["Hubo una crisis económica.", "Los gobiernos firmaron un acuerdo.", "Ese acuerdo fue importante."], "Había = background."),
        M("Which sentence tells an event that happened once?", "Hubo una crisis económica.", ["Había pocos productos.", "Los precios estaban altos.", "El comercio era mínimo."], "Hubo = event."),
        F("Hace cien años, el comercio ___ mínimo.", "era", ["sea", "fueron", "será"], "Background description.", tr="A hundred years ago, trade was minimal.", lemma="ser:él:impf"),
        F("Los puertos ___ cerrados.", "estaban", ["estuvo", "estaba", "estarán"], "Background state, plural.", tr="The ports were closed.", lemma="estar:ellos:impf"),
        F("Después ___ una crisis económica que duró varios años.", "hubo", ["había", "haya", "hay"], "Event → preterite.", tr="Afterward there was an economic crisis that lasted several years.", lemma="haber:él:pret"),
        F("Entonces los precios ___ muy altos.", "estaban", ["estuvo", "estaba", "estarán"], "Background state, plural.", tr="At that time prices were very high.", lemma="estar:ellos:impf"),
        F("Ese acuerdo ___ importante para los dos países.", "fue", ["estaba", "fueron", "sea"], "Evaluation of an event.", tr="That agreement was important for both countries.", lemma="ser:él:pret"),
        F("Durante veinte años, el puerto principal ___ abierto.", "estuvo", ["estaban", "estuvieron", "estará"], "Period of time.", tr="For twenty years, the main port was open.", lemma="estar:él:pret"),
    ],
)
UNIT = unit("Asuntos exteriores y relaciones internacionales", [L758, L759, L760, L761, L762, L763, L764, L765, L766, L767, L768, L769, L770, L771, L772, L773, L774, L775, L776, L777, L778, L779, L780])
