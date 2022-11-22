import { writable } from 'svelte/store'
import currencies from '$lib/data/currency.json'

let listingCache: Record<string, string>
let mapDataCache: Record<string, string>
let cachedCurrency: string

export const currentCurrency = writable(currencies[0])
let _currentCurrency: { name: string; code: string }
currentCurrency.subscribe(async (value) => {
  _currentCurrency = value
  await getListing()
  await getMapListing()
})

async function getListing() {
  if (cachedCurrency !== _currentCurrency.code) {
    listingCache = (await import(`$lib/data/stats/${_currentCurrency.code}/StatsBar.json`)).default
    mapDataCache = (await import(`$lib/data/map/${_currentCurrency.code}/Map.json`)).default
    cachedCurrency = _currentCurrency.code
  }
  return listingCache
}

async function getMapListing() {
  if (cachedCurrency !== _currentCurrency.code) {
    mapDataCache = (await import(`$lib/data/map/${_currentCurrency.code}/Map.json`)).default
  }
  return mapDataCache
}

export const currentMapData = writable()
export const currentListing = writable()

async function init() {
  const listingCache = await getListing()
  const mapCache = await getMapListing()
  currentListing.set(await listingCache)
  currentMapData.set(await mapCache)
}

init()

export async function setCurrency(languageCode: string) {
  currencies.forEach((value) => {
    if (value.code === languageCode) {
      currentCurrency.set(value)
    }
  })
  currentListing.set(await getListing())
  currentMapData.set(await getMapListing())
}

export const currentLang = writable('en')
