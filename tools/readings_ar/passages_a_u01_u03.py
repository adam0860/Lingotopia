"""Units 1 to 3: the script, greetings and introductions, places and weather.
Levels 1 and 2. `mode` says which test a passage is written for."""

PASSAGES = [
    dict(
        id='ar_r001', pair='ar_14', level=1, kind='text', mode='read',
        title='Signs in the city', ar_title='لَافِتَات فِي الْمَدِينَة',
        lines=[
            (None, 'مَطْعَم', 'Restaurant'),
            (None, 'فُنْدُق', 'Hotel'),
            (None, 'بَنْك', 'Bank'),
            (None, 'مَدْخَل', 'Entrance'),
            (None, 'مَخْرَج', 'Exit'),
            (None, 'صَيْدَلِيَّة', 'Pharmacy'),
        ],
        questions=[
            ('You want to leave the building. Which sign do you follow?', ['Entrance', 'Exit', 'Bank', 'Hotel'], 1, '“مَخْرَج” means exit.'),
            ('Where can you buy medicine?', ['At the restaurant', 'At the bank', 'At the pharmacy', 'At the hotel'], 2, '“صَيْدَلِيَّة” is a pharmacy.'),
            ('Where can you sleep on a trip?', ['Hotel', 'Bank', 'Pharmacy', 'Exit'], 0, '“فُنْدُق” is a hotel.'),
        ],
    ),
    dict(
        id='ar_r002', pair='ar_15', level=1, kind='text', mode='listen',
        title='Counting aloud', ar_title='الْعَدّ بِصَوْت عَالٍ',
        lines=[
            (None, 'وَاحِد، اِثْنَان، ثَلَاثَة.', 'One, two, three.'),
            (None, 'أَرْبَعَة، خَمْسَة، سِتَّة.', 'Four, five, six.'),
            (None, 'سَبْعَة، ثَمَانِيَة، تِسْعَة، عَشَرَة.', 'Seven, eight, nine, ten.'),
        ],
        questions=[
            ('Which number comes right after four?', ['Three', 'Five', 'Six', 'Seven'], 1, 'The second line goes “أَرْبَعَة، خَمْسَة”.'),
            ('Which number is said last?', ['Six', 'Eight', 'Nine', 'Ten'], 3, 'The last word is “عَشَرَة”, ten.'),
            ('Which number comes between six and eight?', ['Five', 'Seven', 'Nine', 'Ten'], 1, '“سِتَّة، سَبْعَة، ثَمَانِيَة”.'),
        ],
    ),
    dict(
        id='ar_r003', pair='ar_18', level=1, kind='text', mode='read',
        title='A name card', ar_title='بِطَاقَة الِاسْم',
        names=['أَحْمَد', 'الْقَاهِرَة'],
        lines=[
            (None, 'اِسْمِي أَحْمَد.', 'My name is Ahmad.'),
            (None, 'أَنَا مُهَنْدِس.', 'I am an engineer.'),
            (None, 'أَنَا مِنْ مِصْر.', 'I am from Egypt.'),
            (None, 'أَنَا فِي الْقَاهِرَة.', 'I am in Cairo.'),
        ],
        questions=[
            ('What is his name?', ['Khalid', 'Maher', 'Ahmad', 'Omar'], 2, '“اِسْمِي أَحْمَد.”'),
            ('What is his job?', ['Doctor', 'Engineer', 'Teacher', 'Driver'], 1, '“أَنَا مُهَنْدِس.”'),
            ('Where is he from?', ['Jordan', 'Morocco', 'Iraq', 'Egypt'], 3, '“أَنَا مِنْ مِصْر.”'),
        ],
    ),
    dict(
        id='ar_r004', pair='ar_17', level=1, kind='dialogue', mode='listen',
        title='Good morning, Sara', ar_title='صَبَاح الْخَيْر يَا سَارَة',
        names=['سَارَة', 'أَحْمَد'],
        lines=[
            ('سَارَة', 'صَبَاح الْخَيْر يَا أَحْمَد.', 'Good morning, Ahmad.'),
            ('أَحْمَد', 'صَبَاح النُّور يَا سَارَة. كَيْفَ حَالُك؟', 'Good morning, Sara. How are you?'),
            ('سَارَة', 'أَنَا بِخَيْر، الْحَمْدُ لِلَّه. وَأَنْتَ؟', 'I am fine, praise God. And you?'),
            ('أَحْمَد', 'أَنَا بِخَيْر، شُكْرًا.', 'I am fine, thank you.'),
        ],
        questions=[
            ('What time of day is it?', ['Morning', 'Afternoon', 'Evening', 'Night'], 0, '“صَبَاح الْخَيْر” is good morning.'),
            ('How is Sara?', ['Tired', 'Fine', 'Ill', 'Sad'], 1, '“أَنَا بِخَيْر.”'),
            ('What does Ahmad say at the end?', ['Hello', 'Goodbye', 'Thank you', 'Welcome'], 2, '“شُكْرًا.”'),
        ],
    ),
    dict(
        id='ar_r005', pair='ar_31', level=1, kind='text', mode='read',
        title='Meeting Layla', ar_title='لِقَاء لَيْلَى',
        names=['لَيْلَى', 'سَارَة'],
        lines=[
            (None, 'مَرْحَبًا، اِسْمِي سَارَة.', 'Hello, my name is Sara.'),
            (None, 'أَنَا طَالِبَة فِي الْجَامِعَة.', 'I am a student at the university.'),
            (None, 'صَدِيقَتِي لَيْلَى مُدَرِّسَة.', 'My friend Layla is a teacher.'),
            (None, 'هِيَ مِنْ سُورِيَا، وَأَنَا مِنَ الْأُرْدُنّ.', 'She is from Syria, and I am from Jordan.'),
        ],
        questions=[
            ('What does Sara do?', ['She is a teacher', 'She is a student', 'She is a doctor', 'She is a driver'], 1, '“أَنَا طَالِبَة فِي الْجَامِعَة.”'),
            ('What is Layla’s job?', ['Teacher', 'Engineer', 'Student', 'Pharmacist'], 0, '“لَيْلَى مُدَرِّسَة.”'),
            ('Where is Sara from?', ['Syria', 'Egypt', 'Jordan', 'Iraq'], 2, '“أَنَا مِنَ الْأُرْدُنّ.”'),
        ],
    ),
    dict(
        id='ar_r006', pair='ar_25', level=1, kind='dialogue', mode='listen',
        title='Where are you from?', ar_title='مِنْ أَيْنَ أَنْتَ؟',
        names=['مَاهِر', 'خَالِد'],
        lines=[
            ('مَاهِر', 'أَهْلًا وَسَهْلًا. أَنَا مَاهِر.', 'Welcome. I am Maher.'),
            ('خَالِد', 'تَشَرَّفْنَا. أَنَا خَالِد.', 'Pleased to meet you. I am Khalid.'),
            ('مَاهِر', 'مِنْ أَيْنَ أَنْتَ يَا خَالِد؟', 'Where are you from, Khalid?'),
            ('خَالِد', 'أَنَا مِنَ الْمَغْرِب. وَأَنْتَ؟', 'I am from Morocco. And you?'),
            ('مَاهِر', 'أَنَا مِنَ الْعِرَاق.', 'I am from Iraq.'),
        ],
        questions=[
            ('Who speaks first?', ['Khalid', 'Maher', 'Sara', 'Ahmad'], 1, '“أَنَا مَاهِر.”'),
            ('Where is Khalid from?', ['Iraq', 'Morocco', 'Egypt', 'Jordan'], 1, '“أَنَا مِنَ الْمَغْرِب.”'),
            ('Where is Maher from?', ['Iraq', 'Syria', 'Lebanon', 'Yemen'], 0, '“أَنَا مِنَ الْعِرَاق.”'),
        ],
    ),
]
