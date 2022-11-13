export function getLastElement(listings: unknown) {
  return listings && Object.values(listings).pop()
}
