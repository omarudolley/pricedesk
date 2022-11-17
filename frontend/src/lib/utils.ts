export function getCurrentLang(url: string) {
  return url === '/' ? 'en' : url.split('/').slice(-1) || 'en'
}
