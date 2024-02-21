export interface Product {
  id: number;
  name: string;
  price: number;
  description: string;
}

export const products = [
  {
    id: 1,
    name: 'Книга Остин Дж.: Гордость и предубеждение',
    price: 1109,
    description: '«Гордость и предубеждение» – самый популярный женский роман в мире, провозглашенный интернет-пользователями Великобритании одной из лучших книг всех времен и народов.',
    rating: 5.0,
    img: 'https://resources.cdn-kaspi.kz/img/m/p/he9/h9b/63925229420574.jpg?format=gallery-medium',
    link: 'https://kaspi.kz/shop/p/ostin-dzh-gordost-i-predubezhdenie-100326806/?c=750000000'
  },
  // 
  {
    id: 2,
    name: 'Книга Сильвера А.: В конце они оба умрут',
    price: 3209,
    description: 'Однажды ночью сотрудники «Отдела Смерти» звонят Матео Торресу и Руфусу Эметерио, чтобы сообщить им плохие новости: сегодня они умрут. Матео и Руфус не знакомы, но оба по разным причинам ищут себе друга, с которым проведут Последний День. К счастью, специально для этого есть приложение «Последний друг», которое помогает им встретиться и вместе прожить целую жизнь за один день.',
    rating: 5.0,
    img: 'https://resources.cdn-kaspi.kz/img/m/p/had/h09/64123503837214.jpg?format=gallery-medium',
    link: 'https://kaspi.kz/shop/p/sil-vera-a-v-kontse-oni-oba-umrut-101280241/?c=750000000'
  },
  // 
  {
    id: 3,
    name: 'Книга Лондон Д.: Мартин Иден',
    price: 974,
    description: '"Мартин Иден" - самый известный роман Джека Лондона, впервые напечатанный в 1908-1909 гг. Во многом автобиографическая книга о человеке, который "сделал себя сам", выбравшись из самых низов, добился признания. ',
    rating: 5.0,
    img: 'https://resources.cdn-kaspi.kz/img/m/p/h47/h4b/64225442988062.jpg?format=gallery-medium',
    link: 'https://kaspi.kz/shop/p/london-d-martin-iden-101137240/?c=750000000'
  },
  // 
  {
    id: 4,
    name: 'Книга Ремарк Э. М.: Триумфальная арка',
    price: 1745,
    description: '«Триумфальная арка» – пронзительная история любви всему наперекор, любви, приносящей боль, но и дарующей бесконечную радость.',
    rating: 5.0,
    img: 'https://resources.cdn-kaspi.kz/img/m/p/hd0/h7d/63803844821022.jpg?format=gallery-medium',
    link: 'https://kaspi.kz/shop/p/remark-e-m-triumfal-naja-arka-26025852/?c=750000000'
  },
  // 
  {
    id: 5,
    name: 'Книга Ремарк Э. М.: Три товарища',
    price: 1597,
    description: 'Самый красивый в двадцатом столетии роман о любви…Самый увлекательный в двадцатом столетии роман о дружбе…Самый трагический и пронзительный роман о человеческих отношениях за всю историю двадцатого столетия.',
    rating: 5.0,
    img: 'https://resources.cdn-kaspi.kz/img/m/p/h67/h40/63826306072606.jpg?format=gallery-medium',
    link: 'https://kaspi.kz/shop/p/remark-e-m-tri-tovarischa-100010730/?c=750000000'
  },
  // 
  {
    id: 6,
    name: 'Книга Сент-Экзюпери А. де: Маленький принц',
    price: 970,
    description: '"Маленький принц"-Эта печальная, мудрая, человечная сказка предназначена скорее взрослым, чем детям.',
    rating: 5.0,
    img: 'https://resources.cdn-kaspi.kz/img/m/p/h78/h0f/63893360279582.jpg?format=gallery-medium',
    link: 'https://kaspi.kz/shop/p/sent-ekzjuperi-a-de-malen-kii-prints-100313989/?c=750000000'
  }, 
  // 
  {
    id: 7,
    name: 'Книга Нұршайықов Ә.: Махаббат, қызық мол жылдар',
    price: 2599,
    description: 'Әңгіме сүйіспеншілік жайына ауысты. Қазіргі әдебиетте махаббат туралы қалай жазу керектігі сөз болды.',
    rating: 5.0,
    img: 'https://resources.cdn-kaspi.kz/img/m/p/h73/h7e/63989134917662.jpg?format=gallery-medium',
    link: 'https://kaspi.kz/shop/p/n-rshaiy-ov-mahabbat-yzy-mol-zhyldar-100389616/?c=750000000'
  }, 
  // 
  {
    id: 8,
    name: 'Книга Ли Х.: Убить пересмешника',
    price: 1427,
    description: 'История маленького сонного городка на юге Америки, поведанная маленькой девочкой.',
    rating: 4.5,
    img: 'https://resources.cdn-kaspi.kz/img/m/p/h49/h9a/63813500239902.jpg?format=gallery-medium',
    link: 'https://kaspi.kz/shop/p/li-h-ubit-peresmeshnika-26003932/?c=750000000'
  }, 
  // 
  {
    id: 9,
    name: 'Книга Гоголь Н. В.: Мертвые души',
    price: 599,
    description: 'Никому до Гоголя и после него не удавалось так ярко и остро описать пороки и слабости русского человека, так живо и правдиво отразить важнейшие для России проблемы. ',
    rating: 5.0,
    img: 'https://resources.cdn-kaspi.kz/img/m/p/hb0/hef/63896194121758.jpg?format=gallery-medium',
    link: 'https://kaspi.kz/shop/p/gogol-n-v-mertvye-dushi-100299059/?c=750000000'
  },
  // 
  {
    id: 10,
    name: 'Книга Соқпақбаев Б.: Балалық шаққа саяхат',
    price: 1996,
    description: '«Балалық шаққа саяхат» повесі- көркемделмей-ақ, қаз қалпында түскен дүние, тек жазушының шебер қаламы арқылы жүйеленіп, артық жері алынып, керек жері тазаланып берілген. Құтты жерден табылған саф алтын секілді, ешбір өңдеуден өтпей-ақ жарқырап тұрған.',
    rating: 4.5,
    img: 'https://resources.cdn-kaspi.kz/img/m/p/h7a/he6/64125585489950.jpg?format=gallery-medium',
    link: 'https://kaspi.kz/shop/p/so-pa-baev-b-balaly-sha-a-sajahat-100994720/?c=750000000'
  }
];

// Mio
/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/