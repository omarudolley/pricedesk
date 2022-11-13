import { writable } from 'svelte/store'
import currencies from '$lib/data/currency.json'

let listingCache: Record<string, string>
let cachedCurrency: string

export const currentCurrency = writable(currencies[0])
let _currentCurrency: { name: string; code: string }
currentCurrency.subscribe(async (value) => {
  _currentCurrency = value
  await getListing()
})

async function getListing() {
  if (cachedCurrency !== _currentCurrency.code) {
    listingCache = (await import(`$lib/data/stats/${_currentCurrency.code}/StatsBar.json`)).default
    cachedCurrency = _currentCurrency.code
  }
  return listingCache
}

export const currentListing = writable()

async function init() {
  currentListing.set(await getListing())
}

init()

export async function setCurrency(languageCode: string) {
  currencies.forEach((value) => {
    if (value.code === languageCode) {
      currentCurrency.set(value)
    }
  })
  currentListing.set(await getListing())
}
