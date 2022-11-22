import type { FAQ } from '$lib/types'

export const faqs: { en: FAQ[]; fr: FAQ[] } = {
  en: [
    {
      question: 'What is Liberia Market Index?',
      answer: `Market Index provides accurate and up-to-date information about commodities on the Liberian market.`
    },
    {
      question: 'When is data updated?',
      answer: 'Data is update twice a week (Mondays and Thursdays)'
    },

    {
      question: 'Where does the data come from?',
      answer: 'Data are collected in real time by our agents in the market'
    },

    {
      question: 'Who manages the app?',
      answer: 'The app is managed by TarjahTech'
    },
    {
      question: 'I have a feature request , where can i submit it?',
      answer:
        'Proposals for additional features are welcome on our Github - https://github.com/omarudolley/pricedesk/issues'
    },
    {
      question: 'Where can I support the application?',
      answer:
        'you can send support to any of the following accounts: Paypal: humblepleaser@icloud.com; MTN Mobile Money: +231886295272'
    },
    {
      question: 'Who can I contact for more information?',
      answer: 'For more information contact Siaka Joe Sirleaf. Email: tarjahtech@gmail.com'
    }
  ],
  fr: [
    {
      question: "Qu'est-ce que Market Index ?",
      answer: `Market Index fournit des informations précises et à jour sur les produits de base sur le marché libérien.`
    },
    {
      question: 'Quand les données sont-elles mises à jour ?',
      answer: 'Les données sont mises à jour deux fois par semaine (Lundi et Jeudi)'
    },

    {
      question: "D'où viennent les données ?",
      answer: 'Les données sont collectées en temps réel par nos agents sur le marché'
    },

    {
      question: "Qui gère l'application ?",
      answer: "L'application est gérée par TarjahTech"
    },
    {
      question: "J'ai une demande de fonctionnalité, où puis-je la soumettre ?",
      answer:
        'Les propositions de fonctionnalités supplémentaires sont les bienvenues sur notre Github - https://github.com/omarudolley/pricedesk/issues'
    },
    {
      question: "Où puis-je soutenir l'application ?",
      answer:
        "vous pouvez envoyer une assistance à l'un des comptes suivants : Paypal : humblepleaser@icloud.com ; Argent mobile MTN : +231886295272"
    },
    {
      question: "Qui puis-je contacter pour plus d'informations ?",
      answer: "Pour plus d'informations, contactez Siaka Joe Sirleaf. Email: tarjahtech@gmail.com; "
    }
  ]
}
export const commodities: {
  en: string
  fr: string
}[] = [
  { en: 'Corn Beef (1 can)', fr: 'Corned Beef (1 can)' },
  { en: 'Corn Beef (carton)', fr: 'Corned Beef (carton)' },
  { en: 'Loaf of bread (Fula)', fr: 'Miche de pain (Fula)' },
  { en: 'Loaf of bread (Round)', fr: 'Miche de pain (Ronde)' },
  { en: 'Cement (bag)', fr: 'Ciment (sac)' },
  { en: 'Cement (bag)', fr: 'Ciment (sac)' },
  { en: 'Charcoal (bag)', fr: 'Charbone (sac)' },
  { en: 'Diesel (gallon)', fr: 'Diesel (gallon)' },
  { en: 'Gasoline (gallon)', fr: 'Gasoline (gallon)' },
  { en: 'Eggs(cart)', fr: 'Oeufs(cart)' },
  { en: 'Garri (bag)', fr: 'Garri (sac)' },
  { en: 'Fresh Milk (carton)', fr: 'Lait (carton)' },
  { en: 'Palm oil (1.5L)', fr: 'Huile de palm (1.5L)' },
  { en: 'Palm oil (gallon)', fr: 'Huile de palm (gallon)' },
  { en: 'Vegetable oil (1.5L)', fr: 'Huile végétale (1.5L)' },
  { en: 'Vegetable oil (gallon)', fr: 'Huile végétale (gallon)' },
  { en: 'Rice (25kg)', fr: 'Riz (25kg)' },
  { en: 'Rice (50kg)', fr: 'Riz (50kg)' },
  { en: 'Sugar (bag)', fr: 'Sucre (1 sac)' },
  { en: 'Water bottle (500ml)', fr: "Bouteille d'eau(500ml)" },
  { en: 'Water bottle (1.5L)', fr: "Bouteille d'eau (1.5L)" },
  { en: 'Water (sack)', fr: "Sachet d'eau" },
  { en: 'Zinc (sheet)', fr: 'Toit en Zinc (feuille)' },
  { en: 'Oil Paint (bucket)', fr: 'Peinture à huile (seau)' },
  { en: 'Water Paint (bucket)', fr: 'Peinture à eau (seau)' }
]

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
    en: 'Follow the Liberian market easily in one place.',
    fr: 'Suivez facilement le marché Libérien en un seul endroit.'
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
    fr: 'Choisir item'
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
