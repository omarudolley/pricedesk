import type { FAQ } from '$lib/types'

export const faqs: { en: FAQ[]; fr: FAQ[] } = {
  en: [
    {
      question: 'What is Liberia Market Index?',
      answer: `Market Index provides accurate and up-to-date information about commodities on the Liberian market.`
    },
    {
      question: 'When is data updated?',
      answer: 'Data is updated every Monday morning'
    },

    {
      question: 'Where does the data come from?',
      answer: 'Data are collected in real time by our agents in the market'
    },

    {
      question: 'Who manages the app?',
      answer: "The app is managed by <a href='https://www.facebook.com/Az40tt/'>Shine Liberia</a>"
    },
    {
      question: 'I have a feature request , where can i submit it?',
      answer:
        'Proposals for additional features are welcome on our Github - ' +
        '<a href="https://github.com/omarudolley/pricedesk/issues">https://github.com/omarudolley/pricedesk/issues</a>'
    },
    {
      question: 'Where can I support the application?',
      answer:
        'you can send support to any of the following accounts: ' +
        'Orange Mobile Money <a href="tel:+231-777-298-772">+231777298772</a>  MTN Mobile Money:  <a href="tel:+231886295272">+231886295272</a>'
    },
    {
      question: 'Who can I contact for more information?',
      answer:
        'For more information contact us at' +
        ' <a href="mailto:admin@smartchance.org">admin@smartchance.org</a>'
    }
  ],
  fr: [
    {
      question: "Qu'est-ce que Market Index ?",
      answer: `Market Index fournit des informations précises et à jour sur les produits de base sur le marché Libérien.`
    },
    {
      question: 'Quand les données sont-elles mises à jour ?',
      answer: 'Les données sont mises à jour tous les lundis matin'
    },

    {
      question: "D'où viennent les données ?",
      answer: 'Les données sont collectées en temps réel par nos agents sur le marché'
    },

    {
      question: "Qui gère l'application ?",
      answer:
        "L'application est gérée par <a href='https://www.facebook.com/Az40tt/'>Smartchance</a>"
    },
    {
      question: "J'ai une demande de fonctionnalité, où puis-je la soumettre ?",
      answer:
        'Les propositions de fonctionnalités supplémentaires sont les bienvenues sur notre Github -  ' +
        '<a href="https://github.com/omarudolley/pricedesk/issues">https://github.com/omarudolley/pricedesk/issues</a>'
    },
    {
      question: "Où puis-je soutenir l'application ?",
      answer:
        "vous pouvez envoyer une assistance à l'un des comptes suivants :  " +
        'Orange Mobile Money <a href="tel:+231777298772">+231777298772</a>  MTN Mobile Money:  <a href="tel:+231886295272">+231886295272</a>'
    },
    {
      question: "Qui puis-je contacter pour plus d'informations ?",
      answer:
        "Pour plus d'informations, Contactez-nous à " +
        'Email: <a href="mailto:admin@smartchance.org">admin@smartchance.org</a>'
    }
  ]
}
export const commodities: {
  en: string
  fr: string
}[] = [
  { en: 'Rice (25kg)', fr: 'Riz (25kg)' },
  { en: 'Rice (50kg)', fr: 'Riz (50kg)' },
  { en: 'Water bottle (500ml)', fr: "Bouteille d'eau(500ml)" },
  { en: 'Water bottle (1.5L)', fr: "Bouteille d'eau (1.5L)" },
  { en: 'Loaf of bread (Fula)', fr: 'Miche de pain (Fula)' },
  { en: 'Loaf of bread (Round)', fr: 'Miche de pain (Ronde)' },
  { en: 'Charcoal (bag)', fr: 'Charbon (sac)' },
  { en: 'Onions(bag)', fr: 'Oignons (sac)' },
  { en: 'Diesel (gallon)', fr: 'Diesel (gallon)' },
  { en: 'Beef(Ibs)', fr: 'Boeuf (Ibs)' },
  { en: 'Gasoline (gallon)', fr: 'Gasoline (gallon)' },
  { en: 'Eggs(cart)', fr: 'Oeufs(caisse)' },
  { en: 'Garri (bag)', fr: 'Garri (sac)' },
  { en: 'Garri (cup)', fr: 'Garri (coupe)' },
  { en: 'Milk (carton)', fr: 'Lait (carton)' },
  { en: 'Palm oil (1.5L)', fr: 'Huile de palme (1.5L)' },
  { en: 'Palm oil (gallon)', fr: 'Huile de palme (gallon)' },
  { en: 'Vegetable oil (1.5L)', fr: 'Huile végétale (1.5L)' },
  { en: 'Vegetable oil (gallon)', fr: 'Huile végétale (gallon)' },
  { en: 'Cement (bag)', fr: 'Ciment (sac)' },
  { en: 'Cement (bag)', fr: 'Ciment (sac)' },
  { en: 'Cube Magi(pk)', fr: 'Cube Magi(pk)' },
  { en: 'Corned Beef (1 can)', fr: 'Corned Beef (1 boîte)' },
  { en: 'Corned Beef (carton)', fr: 'Corned Beef (carton)' },

  { en: 'Sugar (bag)', fr: 'Sucre (1 sac)' },

  { en: 'Water (sack)', fr: "Sachet d'eau" },
  { en: 'Flour(bag)', fr: 'Farine (sac)' },

  { en: 'Brick (4-inch)', fr: 'Brique (4 pouces)' },
  { en: 'Brick (6-inch)', fr: 'Brique (6 pouces)' },
  { en: 'Brick (8-inch)', fr: 'Brique (8 pouces)' },

  { en: 'Roofing nail (box)', fr: 'Clou à toiture (boîte' },
  { en: 'Plank (2" by 2")', fr: 'Planche (2" par 2")' },
  { en: 'Plank (2" by 4")', fr: 'Planche (2" par 4")' },

  { en: 'Round pole (single)', fr: 'Poteau rond (simple)' }
]

export const commodityGrid: { [key: string]: { en: string; fr: string }[] } = {

  Food: [
    { en: 'Rice (25kg)', fr: 'Riz (25kg)' },
    { en: 'Rice (50kg)', fr: 'Riz (50kg)' },

    { en: 'Loaf of bread (Fula)', fr: 'Miche de pain (Fula)' },
    { en: 'Loaf of bread (Round)', fr: 'Miche de pain (Ronde)' },

    { en: 'Onions(bag)', fr: 'Oignons (sac)' },
    { en: 'Beef(Ibs)', fr: 'Boeuf (Ibs)' },
    { en: 'Eggs(cart)', fr: 'Oeufs(caisse)' },
    { en: 'Garri (bag)', fr: 'Garri (sac)' },
    { en: 'Milk (carton)', fr: 'Lait (carton)' },
    { en: 'Palm oil (1.5L)', fr: 'Huile de palme (1.5L)' },
    { en: 'Palm oil (gallon)', fr: 'Huile de palme (gallon)' },
    { en: 'Vegetable oil (1.5L)', fr: 'Huile végétale (1.5L)' },
    { en: 'Vegetable oil (gallon)', fr: 'Huile végétale (gallon)' },
    { en: 'Flour(bag)', fr: 'Farine (sac)' },

    { en: 'Cube Magi(pk)', fr: 'Cube Magi(pk)' },
    { en: 'Corned Beef (1 can)', fr: 'Corned Beef (1 boîte)' },
    { en: 'Corned Beef (carton)', fr: 'Corned Beef (carton)' },

    { en: 'Sugar (bag)', fr: 'Sucre (1 sac)' }
  ],

  Beverages: [
    { en: 'Water (sack)', fr: "Sachet d'eau" },
    { en: 'Water bottle (500ml)', fr: "Bouteille d'eau(500ml)" },
    { en: 'Water bottle (1.5L)', fr: "Bouteille d'eau (1.5L)" }
  ],

  Fuel: [
    { en: 'Diesel (gallon)', fr: 'Diesel (gallon)' },
    { en: 'Charcoal (bag)', fr: 'Charbon (sac)' },
    { en: 'Gasoline (gallon)', fr: 'Gasoline (gallon)' }
  ],

 
  Construction: [
    { en: 'Cement (bag)', fr: 'Ciment (sac)' },
    { en: 'Brick (4-inch)', fr: 'Brique (4 pouces)' },
    { en: 'Brick (6-inch)', fr: 'Brique (6 pouces)' },
    { en: 'Brick (8-inch)', fr: 'Brique (8 pouces)' },

    { en: 'Roofing nail (box)', fr: 'Clou à toiture (boîte' },
    { en: 'Plank (2" by 2")', fr: 'Planche (2" par 2")' },
    { en: 'Plank (2" by 4")', fr: 'Planche (2" par 4")' },

    { en: 'Round pole (single)', fr: 'Poteau rond (simple)' }
  ]
}

export const rates: {
  en: string
  fr: string
}[] = [
  { en: 'USD buying rate', fr: "USD taux d'achat" },
  { en: 'USD selling rate', fr: 'USD taux de vente' }
]

export const websiteContent: {
  [item: string]: {
    en: string
    fr: string
  }
} = {
  footer: {
    en: 'Proposals for additional features are welcome on our Github',
    fr: 'Les propositions de fonctionnalités supplémentaires sont les bienvenues sur notre Github'
  },
  intro: {
    en: 'Follow the Liberian market easily in one place. Select item to view detail',
    fr: "Suivez facilement le marché Libérien en un seul endroit. sélectionnez l'élément pour afficher le détail"
  },
  less: {
    en: 'show less',
    fr: 'moins'
  },
  more: {
    en: 'show more',
    fr: 'plus'
  },
  update: {
    en: 'last update',
    fr: 'dernière mise à jour'
  },
  lineChartYaxis: {
    en: 'price in',
    fr: 'prix en'
  },
  lineChartTitle: {
    en: 'over time',
    fr: 'sur une période de temps'
  },
  select: {
    en: 'Select item',
    fr: 'Choisissez'
  },
  lastRecordedPrice: {
    en: 'last week price',
    fr: 'semaine dernière prix'
  },
  lastRecordedRate: {
    en: 'last week rate',
    fr: 'semaine dernière taux'
  },
  inflationRate: {
    en: 'Inflation rate',
    fr: "taux d'inflation"
  },
  rate: {
    en: 'Rate',
    fr: 'Taux'
  },
  seeDetail:{
    en: 'View detail',
    fr: 'Voir les détails'
  }
}

export const locations = [
  'Gbapolu',
  'Bong',
  'Grand Bassa',
  'Grand Cape Mount',
  'Lofa',
  'Montserrado',
  'Margibi',
  'Nimba',
  'Rivercess',
  'Grand Gedeh',
  'Sinoe',
  'River Gee',
  'Grand Kru',
  'Maryland',
  'Bomi'
]
