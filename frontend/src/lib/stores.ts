import { writable } from 'svelte/store'
import locations from '$lib/data/locations.json'
import type { Locations } from '$lib/types'

let listingCache: Record<string, string>
let cachedLocation: string

export const currentLocation = writable(locations[0])
let _currentLocation: Locations
currentLocation.subscribe(async (value) => {
  _currentLocation = value
  await getListing()
})

async function getListing() {
  if (cachedLocation !== _currentLocation.code) {
    listingCache = (await import(`./data/${_currentLocation.code}/listing.json`)).default
    cachedLocation = _currentLocation.code
  }
  return listingCache
}

export const currentListing = writable()

async function init() {
  currentListing.set(await getListing())
}

init()

export async function setLocation(languageCode: string) {
  locations.forEach((value) => {
    if (value.code === languageCode) {
      currentLocation.set(value)
    }
  })
  currentListing.set(await getListing())
}
