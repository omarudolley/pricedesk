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
      'you can send support to any of the following accounts: Paypal: humblepleaser@icloud.com; MTN Mobile Money: 0886295272'
  },
  {
    question: 'Who can I contact for more information?',
    answer:
      'For more information contact Siaka Joe Sirleaf. Email: humblepleaser@icloud.com; Whatsapp: +8615857983179'
  }
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
